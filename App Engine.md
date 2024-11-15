# App Engine

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
