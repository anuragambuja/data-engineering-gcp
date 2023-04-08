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
  - [Google Kubernetes Engine (GKE)](#google-kubernetes-engine-gke)
  - [App Engine](#app-engine)

- [Storage](#storage)
  - [Overview](#overview-3) 
  - [Cloud Storage](#cloud-storage)
  - [Memory Store](#memory-store)
  - [Which storage to use when ?](#which-storage-to-use-when-)

- [Database](#database)
  - [Overview](#overview-4) 
  - [Cloud SQL](https://github.com/anuragambuja/data-engineering-gcp/blob/main/Cloud%20SQL.md)
  - [Cloud Spanner](https://github.com/anuragambuja/data-engineering-gcp/blob/main/Cloud%20Spanner.md)
  - [Memory Store](https://github.com/anuragambuja/data-engineering-gcp/blob/main/Memory%20Store.md)
  - [Bigtable](https://github.com/anuragambuja/data-engineering-gcp/blob/main/Bigtable.md)
  - [Datastore and Firestore](https://github.com/anuragambuja/data-engineering-gcp/blob/main/Datastore%20and%20Firestore.md)
  - [Bigquery](https://github.com/anuragambuja/data-engineering-gcp/blob/main/BigQuery.md)    
  - [Comparison of different Database services](#comparison-of-different-database-services)

- [Processing](#processing)
  - [Overview](#overview-5) 
  - [Cloud Function](#cloud-function)
  - [Data Fusion](https://github.com/anuragambuja/data-engineering-gcp/blob/main/Data%20Fusion.md)
  - [PubSub](https://github.com/anuragambuja/data-engineering-gcp/blob/main/PubSub.md)
  - [Dataflow](https://github.com/anuragambuja/data-engineering-gcp/blob/main/Dataflow.md)
  - [Dataproc](https://github.com/anuragambuja/data-engineering-gcp/blob/main/Dataproc.md)
  - [Cloud Composer](https://github.com/anuragambuja/data-engineering-gcp/blob/main/Cloud%20Composer.md)

- [Data Governance](#data-governance)
  - [Overview](#overview-6) 
  - [Data Catalog](#data-catalog)
  - [Data Loss Prevention](#data-loss-prevention)

- [Logging & Monitoring](#logging--monitoring)
  - [Cloud Monitor](#cloud-monitor)
  - [Cloud Logging](#cloud-logging)

- [Machine Learning](https://github.com/anuragambuja/data-engineering-gcp/blob/main/Machine%20Learning.md)

- [Codes](#codes)
  - [gcloud](#gcloud)
  - [Codelines](https://github.com/anuragambuja/data-engineering-gcp/tree/main/codelines)

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

- roles associated with the account: `gcloud projects get-iam-policy $PROJECT --format='table(bindings.role)' --flatten="bindings[].members" --filter="bindings.members:$USER_EMAIL"`
 
- Add the Dataflow Admin role to the user account: `gcloud projects add-iam-policy-binding $PROJECT --member=user:$USER_EMAIL --role=roles/dataflow.admin`

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

> ### Google Compute Engine (GCE)
- IAAS – Full Control, more flexibility, more responsibility
- Important parameter : Zone, Service Account, Machine family – CPU, RAM, Boot Disk, Storage, Virtual Private Cloud
- The more sphisticated load balancing need to be done, the higher you need to go in OSI stack.
- Projects can have upto 5 VPC(virtual private netword). Each GCE instance belongs in one VPC. Instances within VPC communicate on LAN. Instances across VPC communicate on internet.
- Every VM instance comes with a small root persistent disk containing the OS. 
- When you stop an VM instance, External IP address is lost. Static IP can be switched to another VM instance in same project. You are billed for an Static IP when you are NOT using it!. Static IP remains attached even if you stop the instance. You have to
manually detach it.
- You cannot change the zone of the machine once instanciated.
- Different Machine Families for Different Workloads:
  - General Purpose (E2, N2, N2D, N1) : Best price-performance ratio
      - Web and application servers, Small-medium databases, Dev environments
  - Memory Optimized (M2, M1): Ultra high memory workloads
    - Large in-memory databases and In-memory analytics
  - Compute Optimized (C2): Compute intensive workloads
    - Gaming applications
- Hands-on : Setting up a HTTP server   
  ```
  #! /bin/bash
  sudo su
  apt update
  apt -y install apache2
  sudo service apache2 start
  sudo update-rc.d apache2 enable
  echo "Hello World" > /var/www/html/index.html
  echo "Hello world from $(hostname) $(hostname -I)" > /var/www/html/index.html
  ```
![image](https://user-images.githubusercontent.com/19702456/230639657-628833a5-e7a7-40e7-b126-dcbf4052a8f0.png)
- Instance Group - Group of VM instances managed as a single entity.
  - Managed: Identical VMs created using a template. Instance template is mandatory
    - Features: Auto scaling, auto healing and managed releases
      - Rolling updates: Release new version step by step (gradually). Update a percentage of instances to the new version at a time.
      - Canary Deployment: Test new version with a group of instances before releasing it across all instances.
  - Unmanaged: Different configuration for VMs in same group:
    - Does NOT offer auto scaling, auto healing & other services
    - NOT Recommended unless you need different kinds of VMs
- Load Balancing
  - Network Layer - Transfer bits and bytes. IP (Internet Protocol): Transfer bytes. Unreliable.
  - Transport Layer - Are the bits and bytes transferred properly ?
    - TCP (Transmission Control): Reliability > Performance
    - TLS (Transport Layer Security): Secure TCP
    - UDP (User Datagram Protocol): Performance > Reliability
  - Application Layer - Make REST API calls and Send Emails
    - HTTP(Hypertext Transfer Protocol): Stateless Request Response Cycle
    - HTTPS: Secure HTTP
    - SMTP: Email Transfer Protocol
  
  ![image](https://user-images.githubusercontent.com/19702456/230649398-063274c7-67c7-4d49-94dd-2bd63954d79d.png)

  ![image](https://user-images.githubusercontent.com/19702456/230650183-c9c0f718-5edb-41ec-945a-c55688528338.png)

- Sustained use discounts (Automatic discounts for running VM instances for significant portion of the billing month) Does NOT apply on certain machine types (example: E2 and A2), or to VMs created by App Engine flexible and Dataflow. Applicable for instances created by Google Kubernetes Engine and Compute Engine.
- Committed use discounts with predictable resource needs. Applicable for instances created by Google Kubernetes Engine and Compute Engine. Does NOT apply to VMs created by App Engine flexible and Dataflow. Commit for 1 year or 3 years. 
- Spot VMs - Latest version of preemtible VMs but does not have a maximumum runtime of 24 hours.
- Managed Services for Compute

  ![image](https://user-images.githubusercontent.com/19702456/230710552-dc31cd82-a9ba-4bac-a72b-c1f5769b4180.png)


> ### Google Kubernetes Engine (GKE)
- Developed by Google , Launched in 2014 – Kubernetes. In 2015, Google Launched cloud version - GKE
- Cloud Agnostics
- Written in Go language
- Google Kubernetes Engine (GKE) provides a managed environment for deploying, managing, and scaling your containerized applications using Google infrastructure. The Kubernetes Engine environment consists of multiple machines (specifically Compute Engine instances) grouped to form a container cluster. Kubernetes (master) instance manages node instances which runs a kubelet agent instance which communicates with kubernetes and manages pod which runs multiple containers inside it. Container disks are ephemeral (data is lost once the container is restarted) so use GCEPersistentDIsk. Network load balancing works with container engine. For HTTP load balancing, need to integrate with Compute Engine load balancing. Managed master runs the kubernetes API server which services REST requests, schedules pod creation & deletion on worker nodes, and synchronizes pod information (such as open ports and location).
- Google Kubernetes Engine (GKE) clusters are powered by the Kubernetes open source cluster management system. Kubernetes provides the mechanisms through which you interact with your container cluster. When you run a GKE cluster, you also gain the benefit of advanced cluster management features that Google Cloud provides. These include:
  -	Load balancing for Compute Engine instances
  -	Node pool is subset of machines within a cluster that all have the same configuration. You can run multiple kubernetes node versions on each node pool in your cluster, update each node pool independently and target different node poola for specific deployments. Node pools to designate subsets of nodes within a cluster for additional flexibility
  -	Automatic scaling of your cluster's node instance count
  -	Automatic upgrades for your cluster's node software
  -	Node auto-repair to maintain node health and availability
  -	Logging and Monitoring with Cloud Monitoring for visibility into your cluster

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
![image](https://user-images.githubusercontent.com/19702456/222907142-7afd4075-0ca9-40a0-a7cf-973eb2ab2672.png)

![image](https://user-images.githubusercontent.com/19702456/222905632-043fd232-cb69-40b4-8e17-f2915877e2ce.png)

![image](https://user-images.githubusercontent.com/19702456/222908272-a6bb9bcf-9fcc-4dcf-9ff3-3476f4b6221d.png)

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
> ### Comparison of different Database services
![image](https://user-images.githubusercontent.com/19702456/222908281-cb761edb-11df-4bc7-b653-d2b2475f53c6.png)
  
> ## Cloud Function
- Server less
- Fully managed
- Build small micro service
- Auto scaling as traffic increase
- Event based trigger
  - Http
  - File upload etc.
  - Message pushed to pub/sub

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

## References
- [Google Cloud Console](https://console.cloud.google.com/)



