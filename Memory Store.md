# Memory Store

   ![image](https://github.com/user-attachments/assets/4f291770-1252-47dd-8de6-0a4e7c2f6359)

- Fully managed Inmemory database. High availability, failover, patching, and monitoring. Highly available with 99.9% SLA
- Sub-millisecond data access
- Instances up to 300 GB
- Network throughput of 12 Gbps
- Only Internal IP
- Import/Export data from Cloud Storage to memory store

- Two engine supported
  - Redis
    - Strings, Lists, Sets, Sorted Sets, Hashes, Bitmaps (based on Strings), HyperLogLogs (based on Strings, approx. number of distinct elements in list)
    - Scale upto 30 GB storage and 12 GPS network throughput
    - Secure with only an internal IP address
      - Available only from within the same VPC
      - Use IAM roles to control access
    - Two Tier:
       - Basic Tier
         - Basic tier has a single instance
         - Cache with no replication
         - No cross zone replication
         - No automatic failover
       - Standard Tier
         - Standard tier deploys a failover replica in another zone.
         - Cache with replication
         - Cross zone replication
         - Automatic failover
         - supports up to five read replicas which are replicated across zones and provide a 99.9% availability SLA

  - Memcached
    - Distributed in-memory key-value store eg. {A_cnt: 10, B_cnt: 20, C_cnt: 24}
    - Useful for large caches, up to 5 TB of memory in an instance
    - High availability clusters
    - Used for : Reference data, Database query caching, Session caching
    - Instance is one cluster. While Configuring provide number of nodes and vCPUs and memory
    - Maximum of 20 nodes. 1 to 32 vCPUs. 1 GB to 256 GB per node
    - Maximum 5 TB in an instance

> ## Differences with Open Source Redis
- Persisting to Disk
  - Available in OS version
    - point in time snapshots (RDB)
    - Logs of write Operations (AOF)
  - Not available in Cloud Memorystore
- Most parameters set and can't be changed in cloud memorystore
- Some Redis commands are blocked
- Standard Tier does not allow reading from replica 





