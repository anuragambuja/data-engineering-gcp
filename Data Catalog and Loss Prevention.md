
# Data Governance

One solution for data governance is the Cloud data catalog and the data loss prevention API.

# Data Catalog

- A fully managed and highly scalable data discovery and metadata management service.
- Single place to discover all data, asset across all project
- Technical Metadata
  - For BigQuery, Pubsub these metadata resides inside individual products
  - Technical meta data being registered by catalog automatically
- Business Metadata
  - Attach Tag to existing data asset
  - Define some Tag template and attach metadata. Using tag templates provides consistent metadata to make searching the catalog more successful

     ![image](https://user-images.githubusercontent.com/19702456/225636350-66717e1e-41f6-4def-a1b6-ac60042fb299.png)


Data Catalog is a fully managed, scalable metadata management service within Dataplex that you can use to tag data assets and search for assets to which you have access. Tags allow you to attach custom metadata fields to specific data assets for easy identification and retrieval (such as tagging certain assets as containing protected or sensitive data); you can also create reusable tag templates to rapidly assign the same tags to different data assets.

# Data Loss Prevention API

- Fully managed service designed to help you discover, classify, and protect your most sensitive data.
  - PII data: Person’s name, Credit Card Number, SSN
- Apply API on Cloud Storage, Big Query Data
- DLP work upon Free form Text, Structured & Unstructured data (image)
- What to do with this Data
  - Discover and classify sensitive data
    - automatic DLP for BigQuery
    - deep inspection for BigQuery and Cloud Storage
    - support for structured and unstructured
    - real-time and at rest 
  - De-identify - to help protect data and reduce compliance risk. including masking, tokenization, bucketing, date-shifting, and more
    - Redacation – remove sensitive data
    - Replacement – replace with some tokens (Like Info_type)
    - Masking – Replace one/more character with some other char
    - Encryption – Encrypt Sensitive Data
  - re-identify (In case want to recover original data)
    - to understand statistical anomalies that can lead to increased privacy risk. 
- Detectors can be customized to classify/redact new data items. E.g., social security numbers in a particular country’s format
  
### Templates

- Configuration which is define for:
  - Identification: Find Sensitive Data
  - De-identification: Remove sensitive Data
- Once Template defined, it can be reused for other Jobs

### InfoTypes
- Pattern detectors to idenity sensitive information. Ex. date of birth, Passwords, US SSN, Authentication Tokens, Indian AADHAR etc
- Inspection Job applies InfoTypes to a dataset. When API matches a pattern, it returns 
  - InfoType
  - Likelihood Score
  - Location

![image](https://user-images.githubusercontent.com/19702456/225634162-0e27eb81-7a2c-4847-a0cd-4310651da660.png)

![image](https://user-images.githubusercontent.com/19702456/225634259-3b386912-8075-4927-a522-582700ffcbd3.png)

[DLP API Demo](https://cloud.google.com/dlp/demo/#!/)


  
