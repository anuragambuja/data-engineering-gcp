# Data Catalog

  ![image](https://github.com/user-attachments/assets/7acf14e3-484e-4d0e-b9f1-3c018763e496)

- Single place to discover all data, asset across all project
- Data Catalog is a fully managed, scalable data discovery and metadata management service within Dataplex that you can use to tag data assets and search for assets to which you have access. Tags allow you to attach custom metadata fields to specific data assets for easy identification and retrieval (such as tagging certain assets as containing protected or sensitive data); you can also create reusable tag templates to rapidly assign the same tags to different data assets.
- Technical Metadata (automatically ingested from data source)
  - For BigQuery, Pubsub these metadata resides inside individual products
  - Technical meta data being registered by catalog automatically
  - eg. Table names, column names, Table descriptions, column descriptions, Date created, date modified
- Business Metadata (user provided / inferred)
  - Attach Tag to existing data asset
  - Define some Tag template and attach metadata. Using tag templates provides consistent metadata to make searching the catalog more successful
  - eg. Table has PII, Data quality owner, ‘Delete by’ date, ‘Retain till’ date, Business logic used for computing a column, Data quality score
- Features:
  - Provides a simple search interface for data discovery
  - Supports UI and API for all metadata operations
  - Supports business metadata through schematized tags
  - Auto-ingests technical metadata from GCP data assets
  - Enforces ACL controls on metadata. Providing column-level security for BigQuery tables
  - Auto-tags PII data through DLP integration
- To catalog metadata from non-Google Cloud systems in your organization, you can use the following:
  - Community-contributed connectors to multiple popular on-premises data sources
  - Manually leverage the Data Catalog APIs for custom entries


## Sensitive Data Protection (renamed from Data Loss Prevention) 

  ![image](https://github.com/user-attachments/assets/7b333994-ebea-4640-8aaa-da456d7ab838)

- Fully managed service designed to help you discover, classify, and protect your most sensitive data.
- DLP uses Pattern Plus Context to identify PII. PIIs like Person’s name, Credit Card Number, SSN. Detectors can be customized to classify/redact new data items. E.g., social security numbers in a particular country’s format
- DLP work upon Free form Text, Structured & Unstructured data (image)
- DLP is a stateless service, which means it’s not storing your sensitive data
- API can also be used with other cloud providers as well as on-premise. Built-in support is provided for BigQuery, Datastore, and Cloud Storage.
- When working with databases, we might not want to do a full table scan, which can be spendy. With DLP we can scan a % of row, select top or random rows, exclude fields and more.
  
- What to do with this Data
  - Discover and classify sensitive data
    - automatic DLP for BigQuery
    - deep inspection for BigQuery and Cloud Storage
    - support for structured and unstructured
    - real-time and at rest 
  - De-identify: to help protect data and reduce compliance risk. including masking, tokenization, bucketing, date-shifting, and more
    - Redacation – remove sensitive data
    - Replacement – replace with some tokens (Like Info_type)
    - Masking – Replace one/more character with some other char
    - Encryption – Encrypt Sensitive Data
  - re-identify (In case want to recover original data)
    - to understand statistical anomalies that can lead to increased privacy risk. 

> ## Templates

- Configuration which is defined for:
  - Identification: Find Sensitive Data
  - De-identification: Remove sensitive Data
- Once Template defined, it can be reused for other Jobs

> ## InfoTypes
- Pattern detectors to idenity sensitive information. Ex. date of birth, Passwords, US SSN, Authentication Tokens, Indian AADHAR etc
- Inspection Job applies InfoTypes to a dataset. When API matches a pattern, it returns 
  - InfoType
  - Likelihood Score
  - Location

      ![image](https://user-images.githubusercontent.com/19702456/225634162-0e27eb81-7a2c-4847-a0cd-4310651da660.png)
      
      ![image](https://user-images.githubusercontent.com/19702456/225634259-3b386912-8075-4927-a522-582700ffcbd3.png)


