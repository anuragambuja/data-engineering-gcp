## PDE Test Sample Questions 

1. Our valued customer, an established Apache Kafka user, is exploring migration options to Google Cloud. They seek guidance on the most efficient and cost-effective approach for transitioning their Kafka infrastructure. What would you recommend as the most cost-effective solution?
    - Spin up a Compute Engine VM and install Apache Pulsar.
    - Spin up a Compute Engine VM and install Apache Kafka.
    - Recommend Pub/Sub.
    - Recommend Pub/Sub Lite. 

Ans: D. Pub/Sub Lite is a high-volume, partitioned messaging service offered by Google Cloud Platform. It's designed for applications that prioritize cost-effectiveness and scalability while dealing with large amounts of data streams.

2. You are looking for a messaging service that prioritizes message order for building a data pipeline. The pipeline needs to: Stream log messages for 5 days continuously. Offer real-time querying to check the current processing status. Integrate with a searchable repository for long-term storage and analysis. How should you set up the input messages?
    - Use Cloud Pub/Sub for input. Add an ordering key to every message in the publisher and enable message ordering on the subscription.
    - Use Apache Kafka on Compute Engine for input. Attach a unique identifier to every message in the publisher.
    - Use Cloud Pub/Sub for input. Attach a unique identifier to every message in the publisher.
    - Use Apache Kafka on Compute Engine for input. Attach a timestamp to every message in the publisher.

Ans: A

3. To deliver accurate results for our ML project, we need to ensure a clean and well-prepared dataset. One team member may need extra guidance due to their limited programming skills. Can we suggest alternative approaches or tools to make data preparation accessible for them?
    - Prepare a data cleaning pipeline in Data Studio. Then deploy the pipeline to a Google Kubernetes Engine cluster to perform the processing.
    - Prepare a data cleaning pipeline in Dataprep. Then deploy the pipeline to Dataproc to perform the processing.
    - Prepare a data cleaning pipeline in Dataprep. Then deploy the pipeline to Dataflow to perform the processing.
    - Prepare a data cleaning pipeline in Data Fusion The deploy the pipeline to Dataflow to perform the processing.

Ans: C. Dataprep looks and feels similar to other GUI programs and has a shorter learning curve than Data Fusion. The cost structure of Dataprep is much more suited to exploratory cleaning of data and is very cost effective to run.

4. Cloud SQL PostgreSQL supports which types of replication? Pick 3.
    - Cross-region read replicas.
    - External read replicas
    - Cloud SQL replicas when replicating from an external server
    - Read replicas
    - Cascading read replicas.

Ans: A,D,E

5. Your containerized application needs a SQL-accessible database (up to 10TB) with 99.95% uptime in us-central. You prioritize a managed service for minimized cost. What storage options should we consider? Which solution would you recommend?
    - Use a Spanner multi-regional regional instance, with a 5 node configuration to accommodate the maximum database size of 10 TB.
    - Use Oracle on a Bare Metal Solution as the application database.
    - Use a CloudSQL instance in us-central1-b with two read replicas in us-central1-c and us-central1-a to ensure availability in the event of any zonal failure in us-central.
    - Use a CloudSQL instance in us-central1-b with a failover replica in us-central1-c to ensure that the availability target is met.

Ans: D. Both (c) and (d) are possible answers. The question does not specifically ask about adding read replicas but those are the only two answers that make sense. The final answer comes down to cost as read replicas must be the same configuration or larger than the primary instance.

6. You are working in the analytics group in a large company, which is storing sales history data in BigQuery. To better predict future sales trends, we want to develop a forecasting model using our BigQuery data. We prioritize a rapid prototype with acceptable accuracy over ultimate perfection, considering potential data quality challenges. You are concerned your sales data has many missing/incorrect values. What should you do first?
    - Use the ML.EVALUATE query to assess the quality of your existing data.
    - Create a notebook in Vertex AI Workbench to begin training your model.
    - Use the SQL CREATE MODEL statement to create a logistical regression model to make predictions, with a specified feature set
    - Run some exploratory queries in BigQuery SQL to assess the quality of the existing sales data, and fix incorrect data where possible.

Ans: D. ML models need clean data. Clean data is data that is free of errors and inconsistencies. It is data that is accurate, complete, and consistent. ML models can only learn from clean data, so it is important to ensure that your data is clean before you train a model.

7. What is NOT a Cloud SQL feature?
    - Read replicas
    - Auto scaling CPU and RAM on read replicas
    - External read replicas
    - Fully managed service

Ans: B. A Cloud SQL read replica is an exact copy of a primary Cloud SQL instance. Data and other changes on the primary instance are updated in almost real time on the read replica. You can manually increase the machine configuration of a Cloud SQL read replica after it is created. However, you cannot decrease the size of the read replica.

8. An Oracle cluster, currently residing in a customer's data center and incapable of virtual machine licensing, necessitates migration to optimize operational costs, specifically targeting expenses related to power and cooling. What Google Cloud service would you recommend?
    - Oracle on Bare Metal
    - Compute Engine with Oracle installed
    - Migrate to Cloud SQL
    - Migrate to Cloud Spanner

Ans: A. Oracle licensing is very clear about which Oracle products can run on virtual machines and which products must run on physical (Bare Metal) servers.

9. A customer is running a MySQL database server on-premise with the storage option set to MyISAM. You will be migrating to Cloud SQL MySQL.
    - MEMORY
    - BLACKHOLE
    - InnoDB
    - MyISAM

Ans: C. As Cloud SQL MySQL exclusively relies on InnoDB for persistence, your on-premise MyISAM storage engine necessitates conversion during migration.

10. A customer is preparing to migrate an on premise SQL Server database to Google Cloud SQL SQL Server. The production transactional environment hosts 40TB of data and requires a VM with 16GB RAM, 8 vCPU and with approximately 12,000 simultaneous user connections at any given time. There are concerns that a managed service such as Cloud SQL SQL Server can not support that many simultaneous connections. How many connections can a Cloud SQL SQL Server support?
    - 100
    - 4,000
    - 32,767
    - 15,000

Ans: C.
