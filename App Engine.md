# App Engine

- Deploy HTTP based application
- Serverless PAAS Solution. No Server management required. Automatic load balancing & Auto scaling. No usage charges - Pay for resources provisioned
- Support many runtime engine: Python, java, Go, Node JS

 > ## App Engine environments
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

> ## Scaling
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

