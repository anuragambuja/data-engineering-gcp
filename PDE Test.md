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

11. Pick three data sources that support SQL pushdowns using EXTERNAL_QUERY() via a BigQuery federated connection?
    - Cloud SQL SQL Server
    - Cloud SQL MySQL
    - Cloud SQL PostgreSQL
    - Firestore
    - Spanner

Ans: A,B,E 

12. What external table types does BigQuery support? Pick three.
    - Federated queries
    - Oracle
    - IBM DB2
    - External data sources
    - BigLake tables

Ans: A,D,E

13. You are building a DataFlow pipeline with time-based windowing and trigger-driven aggregations. What type of trigger is NOT supported in Dataflow?
    - After watermark trigger
    - Element count trigger
    - Processing time trigger
    - Element size trigger

Ans: C.

14. We're seeing an influx of lower-priority queries within the Development project's BigQuery instance. While those are valuable for exploration, they might be impacting the performance of critical business analysis queries in the Production project. To ensure smooth operations for everyone, let's prioritize critical Production queries, perhaps by utilizing query queueing or resource reservations. You currently have on-demand pricing, and you also want to put a ceiling on your costs. How should you proceed?
    - Keep the on-demand pricing. Get an increase in your per-project quota of slots available to BigQuery for the Production project.
    - Remove the BigQuery user role from the developers in IAM.
    - Switch to BigQuery editions pricing. Create a reservation of sufficient slots and assign the reservation to the Production project.
    - Create an organizational policy that will apply a lower priority to BigQuery queries coming from the Development project.

Ans: C. You have a choice of using an on-demand pricing model or a capacity-based pricing model. Both models use slots for data processing. With a capacity-based model, you can pay for dedicated or autoscaled query processing capacity. The capacity-based model gives you explicit control over slots and analytics capacity, whereas the on-demand model does not. Customers on the capacity-based pricing model explicitly choose how many slots to reserve.

15. You are looking for a messaging service that prioritizes message order for building a data pipeline. The pipeline needs to: Stream log messages for 5 days continuously. Offer real-time querying to check the current processing status. Integrate with a searchable repository for long-term storage and analysis. How should you set up the input messages?
    - Use Cloud Pub/Sub for input. Attach a unique identifier to every message in the publisher.
    - Use Apache Kafka on Compute Engine for input. Attach a unique identifier to every message in the publisher.
    - Use Apache Kafka on Compute Engine for input. Attach a timestamp to every message in the publisher.
    - Use Cloud Pub/Sub for input. Add an ordering key to every message in the publisher and enable message ordering on the subscription.

Ans: C,D.

16. How many partitions can a BigQuery table have?
    - 200
    - 25,000
    - 10,000
    - 9,000

Ans: C.

17. A website logs user page visits with session IDs and URLs to Pub/Sub. You are to develop a Dataflow pipeline that calculates total page views per user (session timeout: 30 minutes) and stores results in BigQuery. Which type of Dataflow window should you choose?
    - Fixed-time windows with a duration of 30 minutes.
    - Session-based windows with a gap duration of 30 minutes.
    - A single global window.
    - Sliding-time windows with a duration of 30 minutes and a new window every 5 minutes.

Ans: B.

18. Your system currently relies on a single Hadoop cluster for both data analytics and job processing. While the stored data (using Parquet format) remains accessible 24/7, nightly processing jobs can take up to 6 hours, impacting performance. Phase 1: Prioritize speed and minimize disruption by replicating your entire Hadoop environment, including data and processing logic, to Google Cloud Platform. Phase 2: Focus on modernization by gradually shifting analytics to BigQuery, a serverless data warehouse, and processing to Cloud Dataflow, a flexible streaming and batch service. What should you do?
    - Create a single Cloud Dataproc cluster to support both analytics and data processing, and point it at a Cloud Storage bucket that contains the Parquet files that were previously stored on HDFS.
    - Lift and shift Hadoop/HDFS to Compute Engine.
    - Create separate Cloud Dataproc clusters to support analytics and data processing. Point both at the same Cloud Storage bucket that contains the Parquet files that were previously stored on HDFS.
    - Lift and shift Hadoop/HDFS to Cloud Dataproc.

Ans: C.

19. Build a real-time Dataflow pipeline to efficiently stream Avro time-series data, achieving lowest possible latency while writing to both BigQuery and Cloud Bigtable concurrently. Meeting stringent performance requirements is key.You want to achieve minimal end-to-end latency. What should you do?
    - Create a pipeline and use ParDo transform.
    - Create a pipeline that groups data using a PCollection, and then use Avro I/O transform to write to Cloud Storage. After the data is written, load the data from Cloud Storage into BigQuery and Bigtable.
    - Create a pipeline that groups the data into a PCollection and uses the Combine transform.
    - Create a pipeline that groups data using a PCollection and then uses Bigtable and BigQueryIO transforms.

Ans: D.

20. We are seeking a system to capture and analyze the continuous flow of JSON device status messages (250k devices, 10s updates) for real-time outlier detection through time series analysis. What should you do?
    - Ship data to BigQuery. Develop a custom application that uses the BigQuery API to query the dataset and displays device outlier data based on your business requirements.
    - Ship the data into Cloud Bigtable. Install and use the HBase shell for Cloud Bigtable to query the table for device outlier data based on your business requirements.
    - Ship data to Cloud Bigtable. Use the Cloud Bigtable cbt tool to display device outlier data based on your business requirements.
    - Ship data to BigQuery. Use the BigQuery console to query the dataset and display device outlier data based on your business requirements.

Ans: C.

21. You are building a scalable relational database on Google Cloud. The solution must be a robust data repository that seamlessly adapts to varying demands. Key requirements are: Transactional consistency guaranteed Node count seamlessly adjusts to unpredictable bursts in input traffic. Continuous oversight ensures optimal responsiveness during traffic spikes. What should you do?
    - Use Cloud Spanner for storage. Monitor CPU utilization and increase node count if more than 70% utilized for your time span.
    - Use Cloud Bigtable for storage. Monitor data stored and increase node count if more than 70% utilized.
    - Use Cloud Spanner for storage. Monitor storage usage and increase node count if more than 70% utilized.
    - Use Cloud Bigtable for storage. Monitor CPU utilization and increase node count if more than 70% utilized for your time span.

Ans: A. CPU utilization is the recommended metric for scaling, per Google best practices.

22. BigQuery dynamically segments incoming data into daily partitions. As new data arrives throughout the day, it gets added to the relevant partition for that date. However, no specific field was identified by the data modeler to be used as the basis for this partitioning. What kind of partition is being used?
    - Ingestion time partitioned tables.
    - Clustered tables.
    - Integer range partitioned tables
    - Timestamp partitioned tables.

Ans: A.

23. You have been tasked with developing a BQML classification model. The presence of outliers in the training data poses a risk of overfitting my classification model, requiring careful mitigation strategies. What technique would you use to reduce the impact of those outliers on the model?
    - Gradient descent
    - Backpropagation
    - L2 regularization
    - Large number of epochs

Ans: C. L2 regularization calculates a penalty based on the sum-of-the-squares of the weights. L1 regularization should be used when you want less relevant features to have weights close to zero.

24. An on-prem data warehouse is currently deployed using HBase on Hadoop. You want to migrate the database to Google Cloud Platform. You could continue to run HBase within a Cloud Dataproc cluster. What other option would help ensure consistent performance and support the HBase API?
    - Store the data in Cloud Bigtable.
    - Store the data in Cloud Storage.
    - Store the data in Cloud Dataflow.
    - Store the data in Cloud Datastore.

Ans: A.

25. A formal data security policy hasn't been implemented at our startup. Granting unrestricted access to BigQuery datasets across all teams has fostered a flexible environment, but with potential security risks. Your mission is to enhance data warehouse security by uncovering the current usage landscape. What should you do first?
    - Use Cloud Audit Logs to review data access.
    - Use the Cloud Billing API to see what account the warehouse is being billed to.
    - Use Cloud Monitoring to see the usage of BigQuery query slots.
    - Get the identity and access management (IAM) policy of each table.

Ans: A. This is the best way to get granular access to data showing which users are accessing which data.

26. You're designing cloud-based file storage for a data pipeline that processes JSON files. The JSON schema might evolve over time, and your analyst team needs the flexibility to analyze the data using live-updating ANSI SQL queries. What should you do?
    - Use BigQuery for storage. Select "Automatically detect" in the Schema section.
    - Use BigQuery for storage. Provide format files for data load. Update the format files as needed.
    - Use Cloud Storage for storage. Link data as permanent tables in BigQuery and turn on the "Automatically detect" option in the Schema section of BigQuery.
    - Use Cloud Storage for storage. Link data as temporary tables in BigQuery and turn on the "Automatically detect" option in the Schema section of BigQuery.

Ans: A.

27. As part of a financial services firm, you manage a Cloud Bigtable database containing equity and bond trading information for roughly 950 clients. This database tracks over 10,000 financial instruments and receives over 5,000 data points per minute. What general design pattern would you recommend?
    - One table per customer.
    - One table for equities and one for bonds.
    - Tall and narrow table.
    - Options A and C.

Ans: D. Together A and C, we have a small number of tall and narrow tables split by bonds and equities. https://cloud.google.com/bigtable/docs/schema-design

28. You created a compelling Looker Studio report and want to share it with your team. Which methods allow you to grant others access to view or interact with your report? Select three correct answers.
    - Schedule automatic email deliveries of the report in its current format.
    - Invite collaborators by email, specifying their viewing or editing permissions.
    - Embed the report directly into your team's project management platform.
    - Generate a PDF and email it.
    - Share a public link to the report, adjustable with access restrictions.

Ans: A,B,C

29. A data analyst encountered an error message while running a query on BigQuery. Despite having read access to the relevant dataset, the query failed. They are seeking help to resolve this. What role would you think is missing from the users' assigned roles?
    - roles/BigQuery.jobUser
    - roles/BigQuery.queryRunner
    - roles/BigQuery.metadataViewer
    - roles/BigQuery.admin

Ans: A. .roles/BigQuery.jobUser allows users to run jobs, including queries.

30. As a data warehousing specialist, you're tasked with assisting a large enterprise in constructing a unified customer data repository. This comprehensive data hub will house sales, financial, inventory, and logistical information, with the specific use cases of this data to be determined in later phases. What Google Cloud storage system would you recommend that the enterprise use to store that data?
    - BigQuery
    - Bigtable
    - Spanner
    - Cloud Storage

Ans: D.

31. 
