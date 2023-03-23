# Contents 

- [History and Architecture](#history-and-architecture)

- [Zone & Region](#zone--region)
  - [Overview](#overview)
  - [Why Zones & Regions ?](#why-zones--regions-)
  - [What is RTO & RPO ?](#what-is-rto--rpo-)

- [IAM](#iam)
  - [Overview](#overview-1)
  - [G Suite and Cloud Identity](#g-suite-and-cloud-identity)
  - [Google Group](#google-group)

- [Compute](#compute)
  - [Overview](#overview-2)
  - [Google Compute Engine (GCE)](#google-compute-engine-gce)
  - [Google Kubernetes Engine](#google-kubernetes-engine)
  - [App Engine](#app-engine)

- [Storage](#storage)
  - [Cloud Storage](#cloud-storage)
  - [Memory Store](#memory-store)
  - [Which storage to use when ?](#which-storage-to-use-when-)

- [Database](#database)
  - [Cloud SQL](https://github.com/anuragambuja/data-engineering-gcp/blob/main/Cloud%20SQL.md)
  - [Cloud Spanner](https://github.com/anuragambuja/data-engineering-gcp/blob/main/Cloud%20Spanner.md)
  - [Memory Store](https://github.com/anuragambuja/data-engineering-gcp/blob/main/Memory%20Store.md)
  - [Bigtable](https://github.com/anuragambuja/data-engineering-gcp/blob/main/Bigtable.md)
  - [Datastore and Firestore](https://github.com/anuragambuja/data-engineering-gcp/blob/main/Datastore%20and%20Firestore.md)
  - [Bigquery](https://github.com/anuragambuja/data-engineering-gcp/blob/main/BigQuery.md)    
  - [Comparison of different Database services](#comparison-of-different-database-services)

- [Processing](#processing)
  - [Cloud Function](#cloud-function)
  - [Data Fusion](https://github.com/anuragambuja/data-engineering-gcp/blob/main/Data%20Fusion.md)
  - [PubSub](https://github.com/anuragambuja/data-engineering-gcp/blob/main/PubSub.md)
  - [Dataflow](https://github.com/anuragambuja/data-engineering-gcp/blob/main/Dataflow.md)
  - [Dataproc](https://github.com/anuragambuja/data-engineering-gcp/blob/main/Dataproc.md)
  - [Cloud Composer](https://github.com/anuragambuja/data-engineering-gcp/blob/main/Cloud%20Composer.md)

- [Data Governance](#data-governance)
  - [Data Catalog](#data-catalog)
  - [Data Loss Prevention](#data-loss-prevention)

- [Logging & Monitoring](#logging--monitoring)
  - [Cloud Monitor](#cloud-monitor)
  - [Cloud Logging](#cloud-logging)

- [Machine Learning](https://github.com/anuragambuja/data-engineering-gcp/blob/main/Machine%20Learning.md)

- [Usuable Codes](https://github.com/anuragambuja/data-engineering-gcp/tree/main/codelines)

- [References](#references)
 

## History and Architecture

![image](https://user-images.githubusercontent.com/19702456/222905593-f0e0471b-def3-4df9-9e1a-38394d5e74ec.png)

![image](https://user-images.githubusercontent.com/19702456/222905584-a8066c4c-df25-412b-9854-e9094c29fd5b.png)

![image](https://user-images.githubusercontent.com/19702456/222905595-4d6ad300-4175-440e-b251-ba255316fd56.png)

![image](https://user-images.githubusercontent.com/19702456/222907236-509e4398-71aa-4aae-b5d9-1c5ce4a3a116.png)

## Zone & Region
> ### Overview
- Zones – Independent data Center. Each Zone has one or more discrete clusters.
- Region – Specific geographical location to host your resources
- Multi-region - Geographical Collection
- Global - Anywhere

![image](https://user-images.githubusercontent.com/19702456/222907494-543244ac-2303-470b-8db1-240333a0c5e4.png)

> ### Why Zones & Regions ?
- Low latency
- Adhere to government regulations
- High availability
- Disaster recovery
- Global Footprint

Find the updated zones and regions [here](https://cloud.google.com/about/locations).

> ### What is RTO & RPO ?
- RTO – Recovery Time objective: Maximum time for which system can be down
- RPO - Recovery Point objective: Maximum time for which organization can tolerate Dataloss

![image](https://user-images.githubusercontent.com/19702456/224393217-f29fcfe6-87ea-482d-8dba-acd4808bbdf7.png)

## IAM
> ### Overview
- Roles are collection of permissions. One can assign Role to identity, but Can not assign permission directly. So, permissions are assigned to identities via roles.
- Service Account is identity for Compute engine. Max 10 keys per Service Account and Max 100 Service Account per project.
- Roles are attached to identities; policies are attached to resources.

![image](https://user-images.githubusercontent.com/19702456/222914917-7c47e20e-2520-493c-adb9-4ac360901a94.png)

![image](https://user-images.githubusercontent.com/19702456/222914943-ce2666bf-cd5b-4db0-a075-62d0f2bf081a.png)

A policy is set on a resource and each policy contains a set of roles and role members.  resources inherit policies from parents so a policy can be set on a resource for example a service and another policy can be set on a parent such as a project that contains that service. The final policy is the union of the parent policy and the resource policy. In case of conflict, if the parent policy is less restrictive it overrides a more restrictive resource policy. 

![image](https://user-images.githubusercontent.com/19702456/222905653-00cbff0f-1444-44f9-9eee-9b47bc93f32b.png)

> ### G Suite and Cloud Identity
- G Suite user is a member of an organization's G Suite domain
- Cloud Identity is like G Suite domain but without access to G suite services

> ### Google Group
- Collection of Identities
- Useful for assigning roles to multiple users
- Identities in group acquire roles assigned to the group and loses when removed from group

## Compute
> ### Overview
  - Compute Compute Engine lets you create virtual machines that run different operating systems, including multiple flavors of Linux (Debian, Ubuntu, Suse, Red Hat, CoreOS) and Windows Server, on Google infrastructure. 
  - Resources that live in a zone are referred to as zonal resources. Virtual machine instances and persistent disks live in a zone. If you want to attach a persistent disk to a virtual machine instance, both resources must be in the same zone. Similarly, if you want to assign a static IP address to an instance, the instance must be in the same region as the static IP address.

Compute Engine lets you create virtual machines that run different operating systems, including multiple flavors of Linux (Debian, Ubuntu, Suse, Red Hat, CoreOS) and Windows Server, on Google infrastructure. A region is a specific geographical location where you can run your resources. Each region has one or more zones. For example, the us-central1 region denotes a region in the Central United States that has zones us-central1-a, us-central1-b, us-central1-c, and us-central1-f. Resources that live in a zone are referred to as zonal resources. Virtual machine instances and persistent disks live in a zone. If you want to attach a persistent disk to a virtual machine instance, both resources must be in the same zone. Similarly, if you want to assign a static IP address to an instance, the instance must be in the same region as the static IP address.
1. GCE (Google Compute Engine) - IAAS. The more sphisticated load balancing need to be done, the higher you need to go in OSI stack.Projects can have upto 5 VPC(virtual private netword). Each GCE instance belongs in one VPC. Instances within VPC communicate on LAN. Instances across VPC communicate on internet. Every VM instance comes with a small root persistent disk containing the OS. You cannot change the zone of the machine once instanciated. 

2. Google Container Engine - Kubernetes (GKE): Kubernetes (master) instance manages node instances which runs a kubelet agent instance which communicates with kubernetes and manages pod which runs multiple containers inside it. Container disks are ephemeral (data is lost once the container is restarted) so use GCEPersistentDIsk. Network load balancing works with container engine. For HTTP load balancing, need to integrate with Compute Engine load balancing. Managed master runs the kubernetes API server which services REST requests, schedules pod creation & deletion on worker nodes, and synchronizes pod information (such as open ports and location). Node pool is subset of machines within a cluster that all have the same configuration. You can run multiple kubernetes node versions on each node pool in your cluster, update each node pool independently and target different node poola for specific deployments. Autoscaling is possible using cluster autoscaler. Hybrid apps

3. App Engine: Paas, serverless and ops-free. Standard Environments gives a pre configured container. Fexible environment gives a VM.Instance Classes determine the prices. Write simple, single purpose functions attached to the events emitted from cloud infra and services. Cloud functions are written in javascript and can run in any standard node.js runtime. use cases: Mobile and IoT apps
  
> ### Google Compute Engine (GCE)
- IAAS – Full Control, more flexibility, more responsibility
- Important parameter : Zone, Service Account, Machine family – CPU, RAM, Boot Disk, Storage, Virtual Private Cloud

> ### [Google Kubernetes Engine](https://github.com/anuragambuja/data-engineering-gcp/blob/main/Google%20Kubernetes%20Engine.md)

> ### App Engine
- PAAS Solution
- No Server management
- Deploy HTTP based application
- Support many runtime engine: Python, java, Go, Node JS

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

## Storage

![image](https://user-images.githubusercontent.com/19702456/222907142-7afd4075-0ca9-40a0-a7cf-973eb2ab2672.png)

![image](https://user-images.githubusercontent.com/19702456/222905632-043fd232-cb69-40b4-8e17-f2915877e2ce.png)

![image](https://user-images.githubusercontent.com/19702456/222908272-a6bb9bcf-9fcc-4dcf-9ff3-3476f4b6221d.png)

### [Cloud Storage](https://github.com/anuragambuja/data-engineering-gcp/blob/main/Cloud%20Storage.md)

### [Memory Store](https://github.com/anuragambuja/data-engineering-gcp/blob/main/Memory%20Store.md)

#### **Which storage to use when ?**
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

### **Comparison of different Database services**
![image](https://user-images.githubusercontent.com/19702456/222908281-cb761edb-11df-4bc7-b653-d2b2475f53c6.png)
  
## Cloud Function
- Server less
- Fully managed
- Build small micro service
- Auto scaling as traffic increase
- Event based trigger
  - Http
  - File upload etc.
  - Message pushed to pub/sub

## Data Governance
### [Data Catalog](https://github.com/anuragambuja/data-engineering-gcp/blob/main/Data%20Catalog.md)
### [Data Loss Prevention](https://github.com/anuragambuja/data-engineering-gcp/blob/main/Data%20Loss%20Prevention.md)

## Logging & Monitoring

### Cloud Monitor

- Collect metrices from GCP, AWS and hybrid cloud resources
- Dashboards and Visualizations
- Alerting and Anomaly reporting
- Predefined and custom metrices. For more detailed metrices install monitoring agent. 

### Cloud Logging

- Centralized repository for ingesting logs
- System and application logs
- managed Service
- Uses Google-customized FluentD agent
- Retains logs for 30 days
- Stream logs to pub/sub for 3rd party tools
- Analytics with Bigquery

## References
- 

===============================================================================

One solution for data governance is the Cloud data catalog and the data loss prevention API. The data catalog makes all the metadata about your datasets available to search for your users. You group datasets together with tags, flag certain columns as sensitive et cetera. Often used in conjunction with data catalog is the Cloud Data Loss Prevention API, or DLP API, which helps you better understand and manage sensitive data. It provides fast, scalable classification and reduction for sensitive data elements like credit card numbers, names, social security numbers, US and selected international identifier numbers, phone numbers and Google Cloud credentials.
Google Cloud has a fully-managed version of Airflow called "Cloud Composer." Cloud Composer helps your data engineering team orchestrate all the pieces to the data engineering puzzle. 





