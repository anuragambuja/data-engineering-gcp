
# Cloud Spanner

  ![image](https://github.com/user-attachments/assets/64c840fe-ddc7-4175-adaf-3ea96ad7fc99)

- Distributed, Horizontally Scalable (Petabyte scale) and Fully managed solution for RDBMS in GCP with 99.999% availability 
- Costlier than Cloud SQL. Use when Data volume > 2 TB. Upto 10 TB per node. 
- Regional/ Multi-region level instance can be created.
- Cloud SQL has just Read replicas, where as in cloud spanner horizontal read/write across region.
- Spanner can scale horizontally by adding nodes while still maintaining strongly consistent ACID transactions. Uses atomic clocks attached to the servers that run Spanner
- Data is strongly typed.
  - Must define schema database
  - Datatype for each column of each table must be defined.
- Spanner does not have triggers and stored procs.
- Data export:
  - Cannot export with gcloud
  - Need cloud console or cloud dataflow job

    <img src="https://github.com/user-attachments/assets/a620da07-f364-4f40-81ee-9a0738992f0d" width="600">
  
> ## Scalability takeaways
- High scalability is achieved by partitioning data into splits
  - Splits are created and deleted based on resource usage
  - Splits are moved between servers for load balancing
- Splits are transactionally consistent across replicas
  - Same splits exist in all replicas and form a Paxos group
  - One of the split replicas is the "leader" that handles writes
- Split management is invisible to users: Reads, writes, SQL, DML account for splits behind the scenes

  
> ## Availability takeaways
  - High availability achieved via replication
    - Data replicated via Paxos. Spanner automatically replicates at the byte level. Spanner writes database mutations to files in this file system, and the file system takes care of replicating and recovering the files when a machine or disk fails.

      ![image](https://github.com/user-attachments/assets/cba8e452-6bc3-4963-bb6d-3b4919359ef6)

    - Zones failures handled transparently
  - Regional instances provide 99.99% availability
    - Data replicated to 3 zones. When you buy N nodes, you actually get N x 3 servers per region
    - Can handle single zone failure
    - Each Cloud Spanner node provides up to 10,000 queries per second (QPS) of reads or 2,000 QPS of writes (writing single rows at 1 KB of data/row), and 10 TiB storage
    - Recommend allocating enough nodes to keep high priority CPU utilization under 65% for single-region instances
  - Multi-regional instances provide 99.999% availability
    - Data replicated to 5+ zones
    - Can handle single region failure
    - For optimal write latency, place compute resources for write-heavy workloads within or close to the default leader region.
    - For optimal read performance outside of the default leader region, use staleness of at least 15 seconds
    - Provision enough Cloud Spanner nodes to keep overall CPU utilization under 45% in each region.


> ## Hot Spotting
- Hot spots occur when many read and write operations happen on the same node
- Can happen with sequential primary keys
  - Auto-increment values
  - Timestamps
- Consider using 
  - hash value of primary
  - Bit-reverse sequential values
  - Promote high cardinality attributes in multi-attribute primary key. You can also use inter leaved tables with parent-child relationship (one-to many).

 
> ## Interleaved Tables
- Parent-Child relationship
  - Order to order line 
  - Person to addresses
- Row from parent table stored with rows from child table
- More efficient when retriving data from both


> ## Query Insights
- The Query insights dashboard shows the query load based on the database and time range that you select.

> ## Spanner SQL Studio
- Spanner Studio includes an Explorer pane that integrates with a query editor and a SQL query results table. 

