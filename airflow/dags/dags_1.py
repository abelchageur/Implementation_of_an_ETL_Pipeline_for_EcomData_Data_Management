from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta  
import os  # Import os for executing shell commands
from airflow.utils.dates import days_ago
from kafka import KafkaConsumer
import json

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'retries': 1,
}

# Function to verify MinIO upload
def check_minio_file():
    try:
        # List all files in the MinIO bucket
        result = os.popen("docker exec minio mc ls myminio/ecommerce-data").read()
        print(f"MinIO Bucket Contents:\n{result}")

        # Extract the latest CSV file (assuming it starts with 'orders_')
        csv_files = []
        for line in result.splitlines():
            parts = line.split()
            if len(parts) >= 4 and parts[-1].endswith('.csv') and parts[-1].startswith('orders_'):
                csv_files.append(parts[-1])  # Append the filename

        if not csv_files:
            raise Exception("No CSV files found in MinIO bucket.")
        
        latest_csv = sorted(csv_files)[-1]  # Get the latest file by name
        print(f"Latest CSV file in MinIO: {latest_csv}")
    except Exception as e:
        print(f"Error checking MinIO: {e}")
        raise

# Function to check Kafka for messages
def check_kafka_messages():
    try:
        # Consume one message from the Kafka topic
        result = os.popen("docker exec kafka kafka-console-consumer --bootstrap-server kafka:9092 --topic user-interactions --from-beginning --max-messages 1").read()
        print(f"Kafka Message:\n{result}")

        if not result.strip():
            raise Exception("No messages found in Kafka topic.")
    except Exception as e:
        print(f"Error checking Kafka: {e}")
        raise

# Define the DAG
with DAG(
    dag_id='generate_and_verify_data',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
) as dag:

    # Task 1: Generate Data (using BashOperator)
    generate_data_task = BashOperator(
        task_id='run_generate_script',
        bash_command='cd /opt/airflow/data/ && python3 /opt/airflow/data/generate_script.py && echo "Script executed successfully." || echo "Script failed."'
    )

    # Task 2: Check MinIO
    check_minio_task = PythonOperator(
        task_id='check_minio',
        python_callable=check_minio_file
    )

    # Task 3: Check Kafka for messages
    check_kafka_task = PythonOperator(
        task_id='check_kafka',
        python_callable=check_kafka_messages
    )

    # Set task dependencies
    generate_data_task >> check_minio_task >> check_kafka_task