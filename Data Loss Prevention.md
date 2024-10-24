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


  
