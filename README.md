# Contents 

> ## Terminologies
- Fully Managed: No setup, Automated backups,updates, replication 
- Serverless: No server management, Fully managed security, pay only for usage
  
> ## History

![image](https://user-images.githubusercontent.com/19702456/222905593-f0e0471b-def3-4df9-9e1a-38394d5e74ec.png)

![image](https://github.com/user-attachments/assets/e299837a-7bf3-4eda-9a20-c349eeb014ab)


> ## Comparison of different ETL tools

  ![image](https://github.com/user-attachments/assets/0c78b2a1-fe37-45d9-9aa7-5be06db7be16)

> ## Compare Automation Options

  ![image](https://github.com/user-attachments/assets/c50a43c9-4e7e-4802-9076-7f644656c3e9)

> ## Comparison between Cloud SQL and Cloud Spanner

  ![image](https://github.com/user-attachments/assets/82ba95ab-0c18-4823-99b2-591ac1f8eafb)

> ## Comparison between Storage Options

  ![image](https://user-images.githubusercontent.com/19702456/222908281-cb761edb-11df-4bc7-b653-d2b2475f53c6.png)

> ## Which Storage option to select ?
  ![image](https://github.com/user-attachments/assets/040199d1-16b5-4630-845b-4a115e6ffb51)
  
  ![image](https://user-images.githubusercontent.com/19702456/222905632-043fd232-cb69-40b4-8e17-f2915877e2ce.png)
    
  ![image](https://github.com/user-attachments/assets/933d50a0-63f6-4c82-90e7-4f0d9ccda273)

- Cloud Storage
  - Unstructured data storage
  - Video stream, Image
  - Staging environment
  - Compliance
  - Backup
  - Data lake
- Persistent Disk
  - Attach Disk with VM & Containers
  - Share read-only disk with multiple VM
  - Database storage
- Local Disk
  - Temporary high performance attach Disk
- File Store
  - FUlly managed, High performance filestorage, easy fileshare
  - Network attached storage (NAS) for compute Engine and GKE instances
  - Minimum 1 TB, can scale upto 64 TB
  - Supports both HDD and SSD
  - Costly copared to cloud storage
  - Lift-shift millions of Files





> ## References
- [Google Cloud Console](https://console.cloud.google.com/)




## Data Governance
> ### Overview
- One solution for data governance is the Cloud data catalog and the data loss prevention API.

> ### [Data Catalog](https://github.com/anuragambuja/data-engineering-gcp/blob/main/Data%20Catalog.md)
> ### [Data Loss Prevention](https://github.com/anuragambuja/data-engineering-gcp/blob/main/Data%20Loss%20Prevention.md)

## Logging & Monitoring

> ### Cloud Monitor

- Collect metrices from GCP, AWS and hybrid cloud resources
- Dashboards and Visualizations
- Alerting and Anomaly reporting
- Predefined and custom metrices. For more detailed metrices install monitoring agent. 

> ### Cloud Logging

- Centralized repository for ingesting logs
- System and application logs
- managed Service
- Uses Google-customized FluentD agent
- Retains logs for 30 days
- Stream logs to pub/sub for 3rd party tools
- Analytics with Bigquery

## Codes

> ### gcloud

- gcloud command structure 
  - gcloud GROUP SUBGROUP ACTION ...
    - GROUP - config or compute or container or dataflow or functions or iam or ..
      - Which service group are you playing with?
    - SUBGROUP - instances or images or instance-templates or machine-types or regions or zones
      - Which sub group of the service do you want to play with?
    - ACTION - create or list or start or stop or describe or ...
      - What do you want to do?

- Set environment variable to point to your downloaded GCP keys:
   ```shell
   export GOOGLE_APPLICATION_CREDENTIALS="<path/to/your/service-account-authkeys>.json"
   
   # Refresh token/session, and verify authentication
   gcloud auth application-default login
   
   OR, gcloud auth activate-service-account --key-file $GOOGLE_APPLICATION_CREDENTIALS
   ```
- Get project id: `gcloud info --format='value(config.project)'`
- Enable/Disable service: `gcloud services enable/disable dataflow.googleapis.com --force`
  ```
  gcloud compute instances list
  gcloud compute zones list
  gcloud compute regions list
  gcloud compute machine-types list
  gcloud compute machine-types list --filter="zone:us-central1-b"
  gcloud compute machine-types list --filter="zone:( us-central1-b europe-west1-d )"
  ```

> ### [Codelines](https://github.com/anuragambuja/data-engineering-gcp/tree/main/codelines)



## DataLake 
Two modernization routes: Open fromat datalake or BigQuery based datalake
![image](https://github.com/user-attachments/assets/07ec45e3-7463-450e-a62c-88c35f6c1de1)



