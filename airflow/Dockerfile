FROM apache/airflow:2.7.1

USER root

# Install dependencies: Java (Kafka requires it), curl, and unzip
RUN apt-get update && apt-get install -y \
    default-jdk \
    curl \
    unzip \
    && apt-get clean

# # Set Kafka version
# ENV KAFKA_VERSION=3.7.2
# ENV SCALA_VERSION=2.13
# ENV KAFKA_HOME=/opt/kafka

# # Download and extract Kafka
# RUN curl -sL "https://downloads.apache.org/kafka/${KAFKA_VERSION}/kafka-${KAFKA_VERSION}-src.tgz" | tar -xz -C /opt && \
#     ln -s /opt/kafka_${SCALA_VERSION}-${KAFKA_VERSION} $KAFKA_HOME

# # Add Kafka binaries to PATH
# ENV PATH="${PATH}:${KAFKA_HOME}/bin"
USER airflow

# # Switch back to airflow user
RUN pip install --upgrade pip
RUN pip install kafka
RUN pip install pandas
RUN pip install faker
RUN pip uninstall -y kafka && pip install kafka-python

