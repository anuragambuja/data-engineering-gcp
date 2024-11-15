# Contents 

> ## Terminologies
- Fully Managed: No setup, Automated backups,updates, replication 
- Serverless: No server management, Fully managed security, pay only for usage
  
> ## History

![image](https://user-images.githubusercontent.com/19702456/222905593-f0e0471b-def3-4df9-9e1a-38394d5e74ec.png)

![image](https://github.com/user-attachments/assets/e299837a-7bf3-4eda-9a20-c349eeb014ab)


> ## Compare ETL tools

  ![image](https://github.com/user-attachments/assets/0c78b2a1-fe37-45d9-9aa7-5be06db7be16)

> ## Compare Automation Options

  ![image](https://github.com/user-attachments/assets/c50a43c9-4e7e-4802-9076-7f644656c3e9)

> ## Compare Cloud SQL and Cloud Spanner

  ![image](https://github.com/user-attachments/assets/82ba95ab-0c18-4823-99b2-591ac1f8eafb)

> ## Compare Firestore and Bigtable
  
  ![image](https://github.com/user-attachments/assets/6bab4c08-0868-420d-b831-bf02b9377841)

> ## Comparison between Storage Options

  ![image](https://user-images.githubusercontent.com/19702456/222908281-cb761edb-11df-4bc7-b653-d2b2475f53c6.png)
  
  ![image](https://github.com/user-attachments/assets/040199d1-16b5-4630-845b-4a115e6ffb51)
  
  ![image](https://user-images.githubusercontent.com/19702456/222905632-043fd232-cb69-40b4-8e17-f2915877e2ce.png)
    
  ![image](https://github.com/user-attachments/assets/933d50a0-63f6-4c82-90e7-4f0d9ccda273)


> ## Which Storage to use ?

  ![image](https://github.com/user-attachments/assets/09bc17a1-5615-41af-8d5f-cb0f4258161d)




> ## Commands and SQLs

- ### gcloud commands 
  ```shell
  # Get project id
  gcloud info --format='value(config.project)'
  
  # Refresh token/session, and verify authentication
  gcloud auth application-default login # user authentication
  gcloud auth activate-service-account --key-file <path/to/your/service-account-authkeys.json> # service account authentication
  
  # compute commands
  gcloud compute instances list
  gcloud compute zones list
  gcloud compute regions list
  gcloud compute machine-types list
  gcloud compute machine-types list --filter="zone:us-central1-b"
  gcloud compute machine-types list --filter="zone:( us-central1-b europe-west1-d )"
  
  # Enable/Disable service
  gcloud services enable/disable dataflow.googleapis.com --force
  ```

- ### SQL
> ##### Get number of rows, last modified and creation time of all the tables in a dataset
  ```sql
  SELECT
     project_id
    ,dataset_id
    ,table_id AS table_name
    ,TIMESTAMP_MILLIS(creation_time) AS creation_tm
    ,TIMESTAMP_MILLIS(last_modified_time) AS last_modified_tm
    ,row_count AS record_count
  FROM `project.dataset.__TABLES__`
  ORDER BY 1, 2, 3
  ;
  ```

> ##### Get region details of all datasets in the project 
  ```sql
  SELECT
     catalog_name
    ,schema_name
    ,location
  FROM `project`.INFORMATION_SCHEMA.SCHEMATA
  ORDER BY 1, 2
  ;
  ```

> ##### Get list of all tables in the region
  ```sql
  SELECT
     table_catalog
    ,table_schema
    ,table_name
    ,table_type
  FROM `project.region-REGION`.INFORMATION_SCHEMA.TABLES
  ORDER BY 1, 2, 3
  ;
  ```

- ### gsutil
> ##### Customer supplied Encryption keys
  ```bash
  # generate your key 
  $ openssl rand -base64 32
  =+kkqTwwF+yrL2+WTG2ToHN5ZuT/q8OFOXppM7jUfpbM=
  
  # copy file to bucket
  $ gsutil -o 'GSUtil:encryption_key='=+kkqTwwF+yrL2+WTG2ToHN5ZuT/q8OFOXppM7jUfpbM= cp README.txt gs://proven-audio-376216-testing
  
  # Get the content of file
  $ gsutil -o 'GSUtil:encryption_key='=+kkqTwwF+yrL2+WTG2ToHN5ZuT/q8OFOXppM7jUfpbM= cat gs://proven-audio-376216-testing/README.txt
  ```


> ## References
- [Google Cloud Console](https://console.cloud.google.com/)



