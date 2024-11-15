# Contents 

## Terminologies
- Fully Managed: No setup, Automated backups,updates, replication 
- Serverless: No server management, Fully managed security, pay only for usage
  
## History

![image](https://user-images.githubusercontent.com/19702456/222905593-f0e0471b-def3-4df9-9e1a-38394d5e74ec.png)

![image](https://github.com/user-attachments/assets/e299837a-7bf3-4eda-9a20-c349eeb014ab)


## Comparison of different ETL tools

  ![image](https://github.com/user-attachments/assets/0c78b2a1-fe37-45d9-9aa7-5be06db7be16)

## Compare Automation Options

  ![image](https://github.com/user-attachments/assets/c50a43c9-4e7e-4802-9076-7f644656c3e9)

## Comparison between Cloud SQL and Cloud Spanner

  ![image](https://github.com/user-attachments/assets/82ba95ab-0c18-4823-99b2-591ac1f8eafb)

## Comparison between Storage Options

  ![image](https://user-images.githubusercontent.com/19702456/222908281-cb761edb-11df-4bc7-b653-d2b2475f53c6.png)

## Which Storage option to select ?
  ![image](https://github.com/user-attachments/assets/040199d1-16b5-4630-845b-4a115e6ffb51)
  
  ![image](https://user-images.githubusercontent.com/19702456/222905632-043fd232-cb69-40b4-8e17-f2915877e2ce.png)
    
  ![image](https://github.com/user-attachments/assets/933d50a0-63f6-4c82-90e7-4f0d9ccda273)






## References
- [Google Cloud Console](https://console.cloud.google.com/)

















> ### App Engine
- PAAS Solution. No Server management required. Serverless. 
- Deploy HTTP based application
- Support many runtime engine: Python, java, Go, Node JS
- Automatic load balancing & Auto scaling. No usage charges - Pay for resources provisioned
- App Engine environments
  - Standard: Applications run in language specific sandboxes
    - Complete isolation from OS/Disk/Other Apps
    - V1: Java, Python, PHP, Go (OLD Versions)
      - ONLY for Python and PHP runtimes:
        - Restricted network Access
        - Only white-listed extensions and libraries are allowed
      - No Restrictions for Java and Go runtimes
    - V2: Java, Python, PHP, Node.js, Ruby, Go (NEWER Versions)
      Full Network Access and No restrictions on Language Extensions
  - Flexible - Application instances run within Docker containers
    - Makes use of Compute Engine virtual machines
    - Support ANY runtime (with built-in support for Python, Java, Node.js, Go, Ruby, PHP, or .NET)
    - Provides access to background processes and local disks

- Scaling
  - Automatic - Automatically scale instances based on the load:
    - Recommended for Continuously Running Workloads
      - Auto scale based on:
        - Target CPU Utilization - Configure a CPU usage threshold.
        - Target Throughput Utilization - Configure a throughput threshold
        - Max Concurrent Requests - Configure max concurrent requests an instance can receive
      - Configure Max Instances and Min Instances
  - Basic - Instances are created as and when requests are received:
    - Recommended for Adhoc Workloads
      - Instances are shutdown if ZERO requests
        - Tries to keep costs low
        - High latency is possible
      - NOT supported by App Engine Flexible Environment
      - Configure Max Instances and Idle Timeout
  - Manual - Configure specific number of instances to run:
    - Adjust number of instances manually over time

```bash
# Initialize your SDK
$ gcloud init

# Deploy your code to App Engine 
$ gcloud app deploy

# stream logs of your application
$ gcloud app logs tail -s default

# view your application - will provide URL for the browser
$ gcloud app browse
```

```
cd default-service
gcloud app deploy
gcloud app services list
gcloud app versions list
gcloud app instances list
gcloud app deploy --version=v2
gcloud app versions list
gcloud app browse
gcloud app deploy --version=v3 --no-promote
gcloud app browse --version v3
gcloud app services set-traffic splits=v3=.5,v2=.5
watch curl https://melodic-furnace-304906.uc.r.appspot.com/
gcloud app services set-traffic --splits=v3=.5,v2=.5 --split-by=random
 
cd ../my-first-service/
gcloud app deploy
gcloud app browse --service=my-first-service
 
gcloud app services list
gcloud app regions list
```

## Storage
> ### Overview

> ### [Cloud Storage](https://github.com/anuragambuja/data-engineering-gcp/blob/main/Cloud%20Storage.md)

> ### [Memory Store](https://github.com/anuragambuja/data-engineering-gcp/blob/main/Memory%20Store.md)

> ### Which storage to use when ?
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
  ```
  sudo apt-get -y install nfs-common
  sudo mkdir -p /mnt/new # folder to mount filestore instance
  sudo mount <filestore_ip>:/<fileshare_name> <mount point> # /mnt/new
  sodo chmod go+rw /mnt/new
  ```
  
## Database
> ### Overview

  
> ## Cloud Function
- Server less
- Fully managed
- Build small micro service
- Auto scaling as traffic increase
- Events are triggered from
  - Cloud Storage
  - Cloud Pub/Sub
  - HTTP POST/GET/DELETE/PUT/OPTIONS
  - Firebase
  - Cloud Firestore
  - Stack driver logging
- 2 product versions
  - Cloud Functions (1st gen): First version
  - Cloud Functions (2nd gen): New version built on top of Cloud Run and Eventarc


- Pay only for what you use
  - Number of invocations
  - Compute time of the invocations
  - Memory and CPU provisioned
- Key Enhancements in 2nd gen:
  - Longer Request timeout: Up to 60 minutes for HTTP-triggered functions
  - Larger instance sizes: Up to 16GiB RAM with 4 vCPU (v1: Up to 8GB RAM with 2 vCPU)
  - Concurrency: Upto 1000 concurrent requests per function instance (v1: 1 concurrent request per function instance)
  - Multiple Function Revisions and Traffic splitting supported (v1: NOT supported)
  - Support for 90+ event types - enabled by Eventarc (v1: Only 7)


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



