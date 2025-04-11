# 📦 EcomData - Big Data Pipeline Project

## 🧠 Contexte du Projet

EcomData est une entreprise e-commerce spécialisée dans la vente de produits électroniques.  
Chaque jour, des milliers de commandes sont passées, et les clients interagissent avec la plateforme via :

* Clics
* Consultations de pages
* Achats

Actuellement, les données sont :

* Dispersées dans plusieurs systèmes
* Stockées dans des formats variés (CSV, JSON)
* Non centralisées

---

## ❗ Problématique

L’entreprise rencontre plusieurs défis :

* ❌ Données non centralisées  
* ❌ Manque d’automatisation  
* ❌ Difficulté d’analyse  

---

## 🎯 Objectifs du Projet

* Automatiser l’ingestion des données des **commandes** et des **interactions utilisateur**
* Stocker les données brutes de manière organisée sur **Amazon S3** et **Kafka (Iceberg)**
* Orchestrer le pipeline de données avec **Apache Airflow**

---

## 🛠️ Étapes du Projet

### 1. Génération de données

* Développer un script Python pour générer :
  * Fichiers **CSV** : Commandes
  * Fichiers **JSON** : Logs d'interactions utilisateur
* Stocker les fichiers générés dans le dossier `./Staging`

### 2. Ingestion avec Apache NiFi

Créer deux flux NiFi :

* **Flow 1 :** `GetFile` → `PutS3Object`  
  * Pour envoyer les fichiers **CSV** vers **Amazon S3**
  
* **Flow 2 :** `GetFile` → `PublishKafkaRecord`  
  * Pour publier les fichiers **JSON** vers **Kafka**

### 3. Orchestration avec Apache Airflow

Créer un DAG Airflow qui :

* Exécute le script Python **toutes les heures**
* Déclenche les flux **NiFi**
* Vérifie que les données ont bien été envoyées à **S3** et **Kafka**

---

## 🔐 Conformité RGPD et Gouvernance des Données

* Assurer la **conformité RGPD**, notamment la protection des données personnelles
* Mettre en place des **politiques de gouvernance** pour :
  * Qualité des données
  * Sécurité
  * Intégrité
* Développer un **catalogue de données** pour assurer la traçabilité et la compréhension des sources

---

## 📁 Arborescence Prévisionnelle

