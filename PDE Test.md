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

31. Your team needs to quickly add automatic subject labeling to your blog platform on Google Cloud, but you're facing time constraints and limited AI expertise. What should you do?
    - Build and train a text classification model using TensorFlow. Deploy the model using AI Platform Prediction. Call the model from your application and process the results as labels.
    - Build and train a text classification model using TensorFlow. Deploy the model using a Kubernetes Engine cluster. Call the model from your application and process the results as labels.
    - Call the Cloud Natural Language API from your application. Process the generated Sentiment Analysis as labels.
    - Call the Cloud Natural Language API from your application. Process the generated Entity Analysis as labels.

Ans: D.

32. You are designing a streaming pipeline for ingesting player interaction data for a mobile game. You want the pipeline to handle out-of-order data delayed up to 15 minutes on a per-player basis and exponential growth in global users. What should you do?
    - Design a Dataflow streaming pipeline with a single global window of 15 minutes. Use Pub/Sub as a message bus for ingestion.
    - Design a Dataflow streaming pipeline with a single global window of 15 minutes. Use Apache Kafka as a message bus for ingestion.
    - Design a Dataflow streaming pipeline with session windowing and a minimum gap duration of 15 minutes. Use "individual player" as the key. Use Apache Kafka as a message bus for ingestion.
    - Design a Dataflow streaming pipeline with session windowing and a minimum gap duration of 15 minutes. Use "individual player" as the key. Use Pub/Sub as a message bus for ingestion.

Ans: D. Correct because it provides a managed service and a fully trained model, and the user is pulling the entities, which is the right label.

33. As a data engineer on Google Cloud Platform, you're building a data pipeline for analysts. One challenge is persisting CSV files for efficient storage and querying. Additionally, an I/O-intensive custom Apache Spark transformation is required, adding complexity. Your goal is to design a solution that balances storage efficiency, query performance, and efficient execution of the Spark transformation, while using ANSI SQL for analyst familiarity. How should you transform the input data?
    - Use Cloud Storage for storage. Use Dataflow to run the transformations.
    - Use BigQuery for storage. Use Dataproc Serverless to run the transformations.
    - Use BigQuery for storage. Use Dataflow to run the transformations.
    - Use Cloud Storage for storage. Use Dataproc Serverless to run the transformations.

Ans: B. Is correct because of the requirement to use custom Spark transforms; use Dataproc Serverless. ANSI SQL queries require the use of BigQuery.

34. Facing the need to migrate a collection of legacy Python scripts used for data transformation within an ETL pipeline, a team of data warehouse developers seeks a managed service offering that allows continued use of Python while reducing administrative tasks and operational support requirements. Which Google Cloud Platform service would you recommend?
    - Spanner
    - Dataflow
    - Dataprep
    - Dataproc

Ans: B. Dataflow supports Python and is a serverless platform.

35. Previously executed on your department's Hadoop cluster, several MapReduce, Pig, and PySpark jobs must now be adapted and run within the Google Cloud Platform environment as part of your on-premises to cloud migration. What configuration for running these jobs would you recommend?
    - Create one cluster per job. Keep the cluster running continuously so that you need not start a new cluster for each job.
    - Create one cluster for each job and shut down the cluster when the job completes.
    - Create one persistent cluster for Hadoop jobs, one for Pig jobs and one for PySpark.
    - Create a single cluster and deploy Pig and Spark in the cluster.

Ans: B. Create an ephemeral cluster and delete after the job completes (think efficient, cost effective and low maintenance) – use Dataproc Workflow Templates.

36. Business owners demand complete transparency into data evolution, requiring the data warehouse to capture and store every instance of data modification. Understanding the "when" and "why" behind data changes is critical for the business, the data warehouse needs to evolve to encompass a full historical record of all changes, not just static data slices. What data warehousing pipeline should be used to meet this new requirement?
    - Extraction and Load.
    - ELT
    - Change Data Capture.
    - ETL

Ans: C.

37. Following a recent acquisition of a startup with an on-premises IoT platform, a major enterprise seeks to migrate the platform to Google Cloud Platform, prioritizing the utilization of managed services whenever feasible. What Google Cloud Platform service would you recommend for ingesting data?
    - BigQuery streaming inserts
    - Cloud SQL
    - Cloud Storage
    - Pub/Sub

Ans: D. Pub/Sub: Scalable + Managed messaging Service used for ingesting High Volume streaming data.

38. You're collaborating with genetic researchers on a data analysis project. Together, you're leveraging Cloud Storage to process massive datasets generated by gene sequencers. The analysis entails executing a multi-step pipeline consisting of 6 distinct programs. Each program produces an output that serves as the input for the subsequent step. Ultimately, the entire analysis workflow culminates in loading the final results into BigQuery for in-depth exploration. What tool will you recommend for orchestrating this workflow?
    - Apache Flink
    - Composer
    - Dataproc
    - Dataflow
   
Ans: B. Cloud Composer is designed to support workflow orchestration.

39. To address historical data quality challenges, the data pipeline for the sales data mart integrates a comprehensive set of filtering rules dictated by the project sponsor, ensuring only clean data populates the mart. At what stage of the pipeline would you implement those rules?
    - Storage
    - Ingestion
    - Analysis
    - Transformation

Ans: D. The transformation stage is where business logic and filters are applied.

40. To empower different teams working with IoT data, developers are crafting reusable patterns specifically designed for building streaming data pipelines. This approach aims to facilitate collaboration and reduce development time when constructing these pipelines. What component should they use?
    - Dataproc PySpark jobs
    - Dataproc templates
    - Dataflow Python Scripts
    - Dataflow templates

Ans: D. Use Dataflow templates to specify patterns and use parameters to customize templates.

41. Your company's new real-time data warehouse uses BigQuery's streaming inserts. Duplicate data might sneak in, but each record has a unique ID and timestamp. How can you ensure duplicate-free results when querying interactively? Which query type should you use?
    - Use the LAG window function with PARTITION by unique ID along with WHERE LAG IS NOT NULL.
    - Use the ROW_NUMBER window function with PARTITION by unique ID along with WHERE row equals 1.
    - Include ORDER BY DESC on the timestamp column and LIMIT to 1.
    - Use GROUP BY on the unique ID column and timestamp column and SUM on the values.

Ans: B. Correct because it will just pick a single row for each set of duplicates.

42. A Cloud Spanner regional instance (us-west1) is being provisioned with 20 TB of dedicated storage. What is the minimum number of nodes required?
    - 10
    - 20
    - 40
    - 2

Ans: D. Each node can store up to 10TB of data, hence 2 nodes.

43. A developer has built a BigQuery machine learning (BQML) model to predict the category of news stories. Possible values are politics, business, economics, health, science and local news. The developer has tried several algorithms but the model accuracy is poor even when evaluating on training data. This is an example of what kind of potential problem with ML models?
    - Too much training data.
    - Using tenfold cross validation for evaluation.
    - Overfitting.
    - Underfitting.

Ans: D. Correct since the model performs poorly with multiple algorithms, so training data is low.

44. Six months ago, our ecommerce company launched a product recommendation system powered by historical sales data. While it initially delivered results, its effectiveness has waned in recent weeks despite no changes to the underlying BigQuery machine learning (BQML) model. What could be causing the decrease in effectiveness and how do you recommend fixing it?
    - The model is overfitting - use regularization.
    - Data used to train the model is no longer representative of current sales data, and the model should be retrained with more current data.
    - The model is underfitting - train with more data.
    - The model should be monitored to collect performance metrics to identify the root cause of decreasing effectiveness.

Ans: D.

45. The data modeler is constructing a schema that facilitates spontaneous queries with dynamic filtering and pivoting capabilities. The database design prioritizes flexible data exploration through drill-down functionality and multidimensional analysis possibilities. What data model is the data modeler likely to use?
    - OLAP
    - Normalized
    - OLTP
    - Graph

Ans: A.

46. A new engineer needs assistance defining a managed instance group (MIG), including configuration and scaling parameters. What is the next thing the engineer must do to create the desired MIG?
    - Create an instance template using gcloud compute instance-template command.
    - Create each of the initial members of the instance group using gcloud compute instance create command.
    - Create an instance template using cbt create instance-template command
    - Create each of the initial instance group members using the cloud console.

Ans: A.

47. A data engineer with limited machine learning expertise has created several models using raw data from a data lake. Unfortunately, the models' performance is subpar. Seeking to improve efficiency and accuracy, they have requested assistance in refining the development process. What would you first do with the developer?
    - Explore data for feature engineering purposes.
    - Create visualizations of accuracy, precision, recall and F measures.
    - Tune hyperparameters.
    - Use tenfold cross validation.

Ans: A. Feature preprocessing is one of the most important steps in developing a machine learning model. It consists of the creation of features and the cleaning of the data. Sometimes feature creation is also called "feature engineering".

48. Your Spark application generates Parquet files daily to Cloud Storage, but BigQuery users need access. The application environment: How can we optimize for speed and organization?
    - Use "BigQueryCreateExternalTableOperator" with "schema_object" pointing to a schema JSON in Cloud Storage and "source_format" set to "PARQUET".
    - Use "BashOperator" to call "bq insert".
    - Use "GoogleCloudStorageToBigQueryOperator" with "schema_object" pointing to a schema JSON in Cloud Storage and "source_format" set to "PARQUET".
    - Use "BashOperator" to call "bq cp" with the "--append" flag.

Ans: C. Correct because it loads the data and sets partitioning and clustering.

49. A developer has built a BigQuery machine learning (BQML) model to predict the category of news stories. Possible values are politics, business, economics, health, science and local news. The model works well with training data but does poorly with test data. What would you recommend to fix this?
    - Use L1 or L2 regularization while evaluating.
    - Use L1 or L2 regularization while training.
    - Tune hyperparameters more.
    - Use confusion matrices for evaluation.

Ans: B. The model is overfitting the training data, so adding a penalty with L1 or L2 regularization will reduce the overfitting.

50. A data scientist, specializing in machine learning, is crafting a powerful algorithm to discern fraudulent transactions. This algorithm, called a neural network, is being fine-tuned by testing various configurations of processing units (nodes) and layers of complexity. What data should they use to evaluate the quality of models being developed with each combination of settings?
    - Training data.
    - Validation data.
    - Hyperparameter data.
    - Test data.

Ans: B. Use Validation to assess the quality of data for the models when tuning hyperparameters. The Validation dataset is used during training to track the performance of your model on “unseen” data.

51. Your company runs its business-critical system on Oracle. The system is accessed simultaneously from many locations around the world and supports millions of customers. Your database administration team handles the redundancy and scaling manually. The database server is configured for high availability but with all traffic going to the primary. You want to migrate the database to Google Cloud. You need a solution that will provide global scale and availability and require minimal maintenance. What should you do?
    - Migrate to Cloud Spanner.
    - Migrate to BigQuery.
    - Migrate to a Cloud SQL for PostgreSQL instance.
    - Migrate to bare metal machines in multiple Google Cloud Regional Data Centers with Oracle installed.

Ans: A.

52. Hey team, we have a juicy challenge! Our job is to design a system for tracking all the amazing stuff players can collect in our game. Whether they earn it through quests, buy it in the shop, or trade it with friends, we need to keep tabs on it all. What datastore will you recommend?
    - Wide column database
    - Transactional database
    - Document database
    - Analytics database

Ans: C. The requirement is for a SEMI STRUCTURED schema.

53. For over two years, your data-driven online shopping site thrived thanks to a powerful BigQuery Machine Learning (BQML) model accurately predicting customer behavior. However, several market changes such as high inflation and increased interest rates have affected buying patterns and the model's accuracy has begun to suffer. Now, it's time to revitalize its performance and safeguard against future disruptions. What should you do?
    - Monitor data until usage patterns normalize, and then retrain the model.
    - Retrain the model with all newly collected data.
    - Retrain the model with a mix of newly collected data and older data. Add a step to continuously monitor model input data for changes, and retrain the model as new data arrives.
    - Retrain the model with all newly collected data. After one year, return to the older model.

Ans: C.

54. You have just received a large BigQuery dataset. You have comprehensive documentation on the dataset and ready to start analyzing. You will do some visualization and data filtering, but you also want to be able to run custom Python functions. As a Data Engineer you want to work interactively with the data. What Google Cloud Platform service will you use?
    - BigQuery Notebooks
    - Looker Studio
    - Vertex AI Workbench
    - Cloud Dataproc

Ans: A.

55. Your mission is to migrate a MongoDB database, which stores data in flexible documents, to Cloud Spanner. While Cloud Spanner offers similar functionality, you are aiming to retain specific aspects of the document organization originally created in MongoDB.
    - String
    - Array
    - STRUCT
    - JSON

Ans: C. Use STRUCT to store ordered type fields.

56. An audit of our company's Google Cloud Platform user permissions identified that some employees have more access than their job duties necessitate. Currently, all user accounts leverage predefined roles, which may grant broader permissions than what individual users require. To address this and adhere to audit findings, we're transitioning to custom roles that provide granular access control tailored to each user's specific needs. What permission is needed to create a custom role?
    - iam.custom.roles
    - roles/iam.custom.create
    - iam.roles.create
    - roles/iam.create.custom

Ans: C.

57. Your Cloud Spanner database stores customer order information across the tables customer, order, items and products. The four table joins are constantly being performed using existing primary and foreign keys. The customers table contains in excess of 75 million rows while both the Orders and items tables now contain billions of rows. The current architecture has performance issues. You want to follow Google-recommended practices to improve performance. What should you do?
    - Denormalize the data, and have a row for each customer, order, item and products combination.
    - Create interleaved tables, and store orders under customers.
    - Combine the items into single character fields per row and when required, split the data.
    - Retain the existing architecture, but use short, two-letter codes for the products and orders.

Ans:

58. You are building a BigQuery machine learning (BQML) model to predict the sales price of a house. You have 7 years of historical data including 18 features of the house and their sales price. What type of machine learning algorithm would you use?
    - Reinforcement learning
    - Decision trees
    - Regression
    - Classifier

Ans: C. Sales price is a continuous value so Regression is the right value here.

59. You have been asked to build a BigQuery machine learning (BQML) model that will predict if a news article story is about technology or another topic. Which of the following will you use?
    - Multiple linear regression
    - Simple linear regression
    - K-means clustering
    - Logistic Regression

Ans: A, D

60. Your company recently acquired a smaller firm with 20 reporting analysts. All 20 analysts have excellent SQL skills but are new to using BigQuery. It could be several weeks or months until BigQuery training starts and you are noticing much greater slot usage on various BigQuery datasets. You need to control costs in BigQuery and ensure that there is no budget overrun while you maintain the quality of query results. What should you do?
    - Train the analysts to use the query validator or --dry_run to estimate costs so that the analysts can self-regulate usage.
    - Export the BigQuery daily costs, and visualize the data on Looker on a per-analyst basis so that the analysts can self-regulate usage.
    - Reduce the data in the BigQuery tables so that the analysts query less data, and then archive the remaining data.
    - Set a customized project-level or user-level daily quota to acceptable values.

Ans: D.

61. Currently, IT retrieves data from BigQuery, sends it as CSV files, and finance analyzes it in spreadsheets. Our finance team thrives on spreadsheets, but the current data transfer from BigQuery is manual and time-consuming. Can we improve this process using spreadsheets?
    - Run the query in BigQuery. Give the finance team access to Looker Studio's data visualizations.
    - Run the query in BigQuery, and give the finance team access to the results view, which can be analyzed using Google Sheets.
    - Run the query in BigQuery, and save the results to a Google Sheets shared spreadsheet that can be accessed and analyzed by the finance team.
    - Run the query in BigQuery, export the data to CSV, upload the file to a Cloud Storage bucket, and share the file with the finance team.

Ans: B.

62. Leveraging our extensive customer data, spanning years and containing sensitive information like addresses and credit card details, presents an exciting opportunity to unlock valuable insights through BigQuery Machine Learning (BQML) models. However, both ourselves and our management share a critical concern: data security. Breaches or inadvertent leaks of personally identifiable information (PII) could not only damage our reputation but also violate customer trust and potentially incur legal repercussions. We must prioritize addressing these data security concerns while harnessing the power of BQML responsibly. What should you do?
    - Use libraries like SciPy to build the ML models on your local computer.
    - Identify the rows that contain sensitive data, and apply SQL queries to remove only those rows.
    - Remove any tables that contain sensitive data.
    - Remove sensitive data using the Cloud Data Loss Prevention (DLP) API.

Ans: D. DLP is now Sensitive Data Protection.

63. Our healthcare application's user and device growth has triggered a data deluge overwhelming the current backend system designed for event intake from IoT devices. To guarantee no event losses and ensure efficient processing, a complete overhaul of the data pipeline is necessary. We aim to leverage Google's recommended practices for a robust and scalable solution. What should you do?
    - Use Pub/Sub with pull mode and Dataflow.
    - Use Pub/Sub with push mode and Dataflow.
    - Run Cloud Scheduler at fixed intervals.
    - Use Kafka with pull mode.

Ans: A.

64. Your scooter-sharing fleet generates a continuous stream of data, including location, battery levels, and speed. This data is displayed in real-time dashboards to monitor overall health and activity. To compensate for potential connectivity issues, scooters transmit key information repeatedly within a brief window. However, occasional errors have been detected, including messages with missing values. The data flows through a Pub/Sub messaging system and ultimately lands in BigQuery for long-term storage and analysis. It's crucial to ensure this data pipeline delivers clean, reliable information by eliminating duplicate messages and filtering out any records with incomplete fields. How can you filter out these incomplete records before storing them in BigQuery?
    - Use Dataflow to subscribe to Pub/Sub, apply a custom transformation in the data pipeline, and store the data in BigQuery.
    - Store the data in BigQuery, and run delete queries on erroneous and duplicate data.
    - Create an application on Compute Engine with Managed Instance Groups that can remove duplicates and erroneous data. Then insert the data into BigQuery.
    - Use Kubernetes to create a microservices application that can remove duplicates and erroneous data. Then insert the data into BigQuery.

Ans: A.

65. We're transitioning our data analytics to Google BigQuery while keeping our day-to-day operations on-premises. This migration involves: What should you do?
    - Use a Transfer Appliance to move the existing data to Google Cloud. Set up a Dedicated or Partner Interconnect for daily transfers.
    - As early as possible every day, use Cloud VPN to transfer the existing data over the internet.
    - Use a Transfer Appliance to move the historical data to Google Cloud. Use BigQuery Data Transfer Service for daily appends.
    - Use a Transfer Appliance to move the existing data to Google Cloud.. Use VPC Network Peering to transfer data daily.

Ans: C.

66. Your team leverages Dataproc for workloads where individual worker nodes process tasks in roughly 45 minutes. To reduce costs, you've investigated aggressively shutting down idle nodes. Unfortunately, metrics reveal this approach negatively impacts overall job completion time. You now seek a cost optimization strategy that doesn't compromise timely results. Which approach BEST balances cost optimization with timely results?
    - Implement dynamic scaling to add and remove worker nodes based on real-time resource demands.
    - Increase the number of vCPUs on each worker node so that the processing finishes sooner.
    - Rewrite the processing in Cloud Data Fusion, and run the job automatically.
    - Rewrite the processing in Dataflow, and use stream processing of the same data.

Ans: A.

67. A Bigtable installation has been running for over a year without any performance issues. Recently the company has opened a number of stores which has created a large influx of data and a sizable increase in queries. These changes may be the reason for a degradation in performance. The business needs answers fast and your boss tells you to investigate. What should you do?
    - Use Cloud Trace to identify the performance issue.
    - Add more nodes to the cluster to see if that resolves the performance issue.
    - Use Key Visualizer to analyze performance.
    - Add logging statements into the code to see which inserts cause the delay.

Ans: C. 

68. Your client currently leverages on-premises Hadoop and Spark for data analysis, with central access to primary data residing on hard disks. They seek a smooth, scalable migration to Google Cloud. To minimize migration effort, you aim to propose an architecture requiring minimal code changes and operational adjustments. What should you do?
    - Use Dataproc to run Hadoop and Spark jobs. Move the data to Cloud Storage.
    - Use Dataflow to recreate the jobs in a serverless approach. Retain the data on a Compute Engine VM with an attached persistent disk.
    - Use Dataflow to recreate the jobs in a serverless approach. Move the data to Cloud Storage.
    - Use Dataproc to run Hadoop and Spark jobs. Retain the data on a Compute Engine VM with an attached persistent disk.
   
Ans: A.

69. The challenge: millions of traders are actively using a stock exchange, generating data at breakneck speed. We're building a visualization platform that displays this data in real-time, showing how stock prices behave and markets evolve. What Google Cloud storage solution can ensure rapid data retrieval for this high-performance requirement?
    - Use Firestore.
    - Use Bigtable.
    - Use Memorystore.
    - Use Cloud SQL.

Ans: B.

70. A client's 5 TB SQL Server database, projected to reach 25 TB, supports an internal reporting app used weekly. The goal is to migrate everything to Google Cloud for simplified management and cost optimization (maintaining or reducing current expenses). Which of the following is NOT a benefit of migrating to Google Cloud?
    - Reduced costs.
    - Increased scalability and performance.
    - Increased vendor lock-in.
    - Improved disaster recovery

Ans: C.

71. You need to grant secure access to a Cloud SQL instance with a public IP address to a remote developer. The developer will write code locally on their laptop, which will connect to a MySQL instance on Cloud SQL. The instance has an external (public) IP address. You want to follow Google-recommended practices when you give access to Cloud SQL to the new team member.
    - Provide the developer direct access to the public IP address and root user credentials.
    - Configure a VPN tunnel between the developer's machine and the Google Cloud network.
    - Give instance access permissions in Identity and Access Management (IAM). Have the developer run Cloud SQL Auth proxy to connect to a MySQL instance.
    - Create a Cloud SQL user for the developer with full database administrator privileges.
    - Remove the Cloud SQL external IP address, and replace it with an internal IP address.

Ans: C, E

72. What is the main advantage of using a VPC Service Control perimeter around the Cloud SQL instance?
    - Disable public access to the Cloud SQL instance completely.
    - It automatically scales to accommodate varying workloads on the Cloud SQL instance.
    - It isolates the Cloud SQL instance within a secure virtual network segment, restricting access to authorized services only.
    - It provides built-in data encryption for all communication within the perimeter.

Ans: C.

73. What is the default encoding for BigQuery?
    - UTF-7
    - UTF-8
    - UTF-9
    - UTF-6

Ans: B.

74. During a BigQuery import of CSV files, all records were loaded successfully. Despite this, there's a byte-level difference between the source and imported data. What's the most probable explanation for this behavior?
    - Hidden characters could be affecting byte count unless filtered consistently.
    - BigQuery's guess might be wrong.
    - The CSV data had invalid rows that were skipped on import.
    - The CSV data loaded in BigQuery is not using BigQuery’s default encoding.

Ans: D.

75. CMEK stands for Customer-managed encryption keys. What does it mean to use CMEK?
    - Google manages your encryption keys, but you choose encryption algorithms.
    - You create, manage, and control the encryption keys used to protect your data.
    - Google encrypts your data with special keys for additional security.
    - You can access and decrypt any data stored in Google Cloud services.

Ans: B.

76. When might using CMEK NOT be recommended?
    - When you need to follow strict data residency regulations.
    - When you require the highest level of data security for sensitive information.
    - When you have limited expertise in managing encryption keys.
    - When you prioritize ease of use and minimal management overhead.

Ans: C.

77. Challenge: We're building a data lake on Google Cloud to power a website recommendation engine. We need to ingest diverse, ever-changing unstructured data from various sources and process it through pipelines to generate recommendations. Reprocessing the data might be necessary, so it's crucial to preserve its original structure. Desired Architecture: Design a flexible architecture that addresses these key points: What services should you use?
    - Store the data in a BigQuery table. Design the processing pipelines to retrieve the data from the table.
    - Send the data through the processing pipeline, and then store the processed data in a BigQuery table for reprocessing.
    - Store the data in a Cloud Storage bucket. Design the processing pipelines to retrieve the data from the bucket.
    - Send the data through the processing pipeline, and then store the processed data in a Cloud Storage bucket for reprocessing.

Ans: C.

78. Your project necessitates a layered approach to access control in Google Cloud Platform to uphold two critical compliance requirements:
    - Add the finance team members to the default IAM Owner role. Add the developers to a custom role that allows them to see their own spend only.
    - Add the finance team members to the Billing Administrator role for each of the billing accounts they must manage. Add the developers to the Viewer role for the Project.
    - Add the developers and finance managers to the Viewer role for the Project.
    - Add the finance team to the Viewer role for the Project. Add the developers to the Security Reviewer role for each of the billing accounts.

Ans: B.

79. You decide to use Cloud SQL Proxy and Cloud IAM for access control. What additional security measure is recommended to further protect the Cloud SQL instance?
    - Add a second public IP address to load balance traffic.
    - Enable Cloud SQL Audit Logging to track all database activity.
    - Configure the Cloud SQL Proxy to listen on a non-standard port.
    - Disable public access to the Cloud SQL instance completely.

Ans: B.

80. In Dataflow what is NOT part of a pipeline?
    - PCollections
    - Cloud Storage
    - PTransformation
    - Pipeline Runner

Ans: B.

81. What is NOT a valid reason for modifying the BigQuery dataset number of days for Time Travel?
    - Lower storage costs.
    - Enforcing Data Governance data life.
    - Faster data exports.
    - Faster query performance.

Ans: D

82. GoogleSQL, used by both BigQuery and Spanner, supports what version of ANSI SQL?
    - 2000
    - 2020
    - 2007
    - 2011

Ans: D

83. What is the default trigger type in Dataflow?
    - AfterCount
    - AfterComposite
    - AfterWatermark
    - AfterProcessingTime

Ans: C

84. BigQuery storage supports two dataset storage billing models. What are they? Pick two.
    - Active bytes
    - Logical bytes
    - Physical bytes
    - Inactive bytes

Ans: B,C

85. When choosing a side input pattern in Dataflow, what factors should you consider?
    - The complexity of the DoFn logic is the primary consideration.
    - The programming language used in your pipeline dictates the best pattern.
    - The size and update frequency of side input data is irrelevant.
    - Both the size/update frequency of the side input and the DoFn's processing needs are crucial.

Ans: D

86. What is the difference between BigQuery Slots and BigQuery BI Engine Slots?
    - BigQuery Slots are stateful.
    - No difference.
    - BI Engine Slots are shorter.
    - BI Engine Slots are stateful.

Ans: D.

87. What is NOT a windowing type in Apache Beam?
    - Grouped
    - Session
    - Fixed
    - Sliding

Ans: A

88. You have a Dataflow pipeline analyzing website traffic logs. The main data stream tracks user actions, but you also want to enrich it with information about product categories accessed by each user. This information is stored in a separate, smaller dataset. How can you incorporate this product data into your pipeline?
    - Use the product data to filter the traffic logs.
    - Store the product data in a Cloud Storage bucket and access it within your DoFn using external calls.
    - Directly merge the two datasets as a single PCollection.
    - Utilize a side input to provide product information alongside each user action log.

Ans: D.

89. When creating a custom Dataflow template what language is NOT supported?
    - GO
    - Dataflow SQL
    - Python
    - Java

Ans: B.

90. What is the minimum and maximum number of days for BigQuery Time Travel?
    - 1 and 10
    - 1 and 8
    - 2 and 9
    - 2 and 7

Ans: D

91. When do budget alerts fire?
    - When forecasted cost exceeds budgeted forecasted cost.
    - When actual cost exceeds budgeted actual cost.
    - When actual or forecasted cost exceeds percentage of budget.
    - When an email alert is initiated by a trigger firing.

Ans: C.

92. Which data storage option can you export automated billing information to?
    - Cloud SQL
    - Cloud Storage
    - Cloud Spanner
    - BigQuery

Ans: D.

93. Which of the following controls are considered a hard ceiling cost control? Pick all that apply.
    - Rate Limits
    - Identity and Access Management (IAM)
    - Budgets
    - Quotas

Ans: A, D.

94. What is the purpose of Eventarc?
    - Extend a project's IAM model to externally hosted services.
    - Asynchronously deliver events from Google services, SaaS, and your own apps.
    - Cost control of supported service.
    - Higher SLA for supported services.

Ans: B.

95. Which Cloud Storage buckets support turbo replication?
    - Autoclass
    - Standard
    - Dual-region
    - Multi-region

Ans: C.

96. Which Cloud Storage Autoclass feature is NOT true?
    - When an object's data is read, the object transitions to Standard storage if it's not already stored in Standard storage.
    - You can define which storage classes Autoclass will work with.
    - Moves data that is accessed to Standard storage to optimize future accesses.
    - Moves data that is not accessed to colder storage classes to reduce storage cost.

Ans: B.

97. In a project which BigQuery features are NOT unlimited?
    - Rows
    - Columns
    - Tables
    - Datasets

Ans: B. A table, query result, or view definition can have up to 10,000 columns.

98. Which database does NOT have Query Insights?
    - Cloud SQL MySQL
    - Cloud Spanner
    - Cloud SQL PostgreSQL
    - Cloud SQL SQL Server

Ans: D.

99. What is the maximum size of a Memorystore Redis or Memcached data store?
    - 300GB
    - 750GB
    - 64TB
    - 1TB

Ans: A

100. What are the benefits of Cloud Functions? Pick all that apply.
    - Auto Scalable
    - Serverless
    - HTTP and event driven
    - Integration with Google Cloud databases

Ans: A,B,C,D

101. You are working on optimizing BigQuery for a query that is run repeatedly on a single table. The data queried is about 1 GB, and some rows are expected to change about 10 times every hour. You have optimized the SQL statements as much as possible. You want to further optimize the query's performance. What should you do?
    - Create a materialized view based on the table, and query that view.
    - Enable caching of the queried data so that subsequent queries are faster.
    - Create a scheduled query, and run it a few minutes before the report has to be created.
    - Reserve a larger number of slots in advance so that you have maximum compute power to execute the query.

Ans: Option A is correct because materialized views periodically cache the results of a query for increased performance. Materialized views are suited to small datasets that are frequently queried. When underlying table data changes, the materialized view invalidates the affected portions and re-reads them. Option B is not correct because caching is automatically enabled but is not performant when the underlying data changes. Option C is not correct because scheduled queries let you schedule recurring queries but do not provide specific performance optimizations. Also, running a query too early could use old/stale data. Option D is not correct because reserving more slots guarantees the availability of BigQuery slots but does not improve performance.

102. Several years ago, you built a machine learning model for an ecommerce company. Your model made good predictions. Then a global pandemic occurred, lockdowns were imposed, and many people started working from home. Now the quality of your model has degraded. You want to improve the quality of your model and prevent future performance degradation. What should you do?
    - Retrain the model with data from the first 30 days of the lockdown.
    - Monitor data until usage patterns normalize, and then retrain the model.
    - Retrain the model with data from the last 30 days. After one year, return to the older model.
    - Retrain the model with data from the last 30 days. Add a step to continuously monitor model input data for changes, and retrain the model.
 
Ans: Option A is not correct because retraining based on the data from the first 30 days of the lockdown might only be useful for predictions during similar lockdowns and not for regular periods. Option B is not correct because usage patterns might have changed permanently and might continue to change in the future. Option C is not correct because the older model might not be indicative of user behavior after a year. Option D is correct because the data used to build the original model is no longer relevant. Retraining the model with recent data from the last 30 days will improve the predictions. To keep a watch on future data drifts, monitor the incoming data.

103. A new member of your development team works remotely. The developer will write code locally on their laptop, which will connect to a MySQL instance on Cloud SQL. The instance has an external (public) IP address. You want to follow Google-recommended practices when you give access to Cloud SQL to the new team member. What should you do?
    - Ask the developer for their laptop's IP address, and add it to the authorized networks list.
    - Remove the external IP address, and replace it with an internal IP address. Add only the IP address for the remote developer's laptop to the authorized list.
    - Give instance access permissions in Identity and Access Management (IAM), and have the developer run Cloud SQL Auth proxy to connect to a MySQL instance.
    - Give instance access permissions in Identity and Access Management (IAM), change the access to "private service access" for security, and allow the developer to access Cloud SQL from their laptop.

Ans: Option A is not correct, because although adding an authorized networks list is possible, it is more effort to track it and also less secure.  Option B is not correct, because if you remove the external IP address, access for those who work remotely will be more complicated because they also have to be within private RFC 1918 address space. Option C is correct because the recommended approach is to use Cloud SQL Auth proxy. Permissions can be controlled by IAM. You don't need to track authorization lists for changing user IP addresses. Option D is not correct because private service access will require access from a private RFC 1918 address space, which might not be available to developers who work remotely.

104. Your Cloud Spanner database stores customer address information that is frequently accessed by the marketing team. When a customer enters the country and the state where they live, this information is stored in different tables connected by a foreign key. The current architecture has performance issues. You want to follow Google-recommended practices to improve performance. What should you do?
    - Create interleaved tables, and store states under the countries.
    - Denormalize the data, and have a row for each state with its corresponding country.
    - Retain the existing architecture, but use short, two-letter codes for the countries and states.
    - Combine the countries in a single cell's text, for example "country:state1,state2, …" and when required, split the data.

Ans: Option A is correct because Cloud Spanner supports interleaving that guarantees data being stored in the same split, which is performant when you need a strong data locality relationship. Option B is not correct because denormalizing is not a preferred approach in relational databases. It leads to multiple rows with repeated data. Option C is not correct because reducing the size of the fields to short names will have lower impact because the data access and joins will be a bigger performance issue. Option D is not correct because packing multiple types of data into the same cell is not recommended for relational databases.

105. Your company runs its business-critical system on PostgreSQL. The system is accessed simultaneously from many locations around the world and supports millions of customers. Your database administration team manages the redundancy and scaling manually. You want to migrate the database to Google Cloud. You need a solution that will provide global scale and availability and require minimal maintenance. What should you do?
    - Migrate to BigQuery.
    - Migrate to Cloud Spanner.
    - Migrate to a Cloud SQL for PostgreSQL instance.
    - Migrate to bare metal machines with PostgreSQL installed.

Ans: Option A is not correct because BigQuery doesn’t support global scale. BigQuery also isn’t the best option for migrating a transactional database like PostgreSQL because it is more analytics-focused. Option B is correct because Cloud Spanner provides a global-scale, highly available database that supports relational data. Option C is not correct because Cloud SQL options are regional and have less scalability compared to Cloud Spanner. Option D is not correct because running PostgreSQL on bare metal machines requires a greater maintenance effort.

106. Your company collects data about customers to regularly check their health vitals. You have millions of customers around the world. Data is ingested at an average rate of two events per 10 seconds per user. You need to be able to visualize data in Bigtable on a per user basis. You need to construct the Bigtable key so that the operations are performant. What should you do?
    - Construct the key as user-id#device-id#activity-id#timestamp.
    - Construct the key as timestamp#user-id#device-id#activity-id.
    - Construct the key as timestamp#device-id#activity-id#user-id.
    - Construct the key as user-id#timestamp#device-id#activity-id.

Ans: Option A is correct because the design does not monotonically increase, thus avoiding hotspots. Option B is not correct because it monotonically increases, thus causing hotspots. Option C is not correct because it monotonically increases, thus causing hotspots. Option D is not correct because it monotonically increases, thus causing hotspots.

107. Your company is hiring several business analysts who are new to BigQuery. The analysts will use BigQuery to analyze large quantities of data. You need to control costs in BigQuery and ensure that there is no budget overrun while you maintain  the quality of query results. What should you do?
    - Set a customized project-level or user-level daily quota to acceptable values.
    - Reduce the data in the BigQuery table so that the analysts query less data, and then archive the remaining data.
    - Train the analysts to use the query validator or --dry_run to estimate costs so that the analysts can self-regulate usage.
    - Export the BigQuery daily costs, and visualize the data on Looker on a per-analyst basis so that the analysts can self-regulate usage.

Ans: Option A is correct because if you have multiple BigQuery projects and users, you can manage costs by requesting a custom quota that specifies a limit on the amount of query data processed per day.  Option B is not correct because giving only partial data to the analysts might not produce accurate query results. Option C is not correct because costs could still overrun budgets. This approach assumes that analysts always follow guidelines. Option D is not correct because your costs could still overrun budgets. This approach also assumes that the analysts look at the charts daily and adjust their behavior.

108. Your Bigtable database was recently deployed into production. The scale of data ingested and analyzed has increased significantly, but the performance has degraded. You want to identify the performance issue. What should you do?
    - Use Key Visualizer to analyze performance.
    - Use Cloud Trace to identify the performance issue.
    - Add logging statements into the code to see which inserts cause the delay.
    - Add more nodes to the cluster to see if that resolves the performance issue.

Ans: Option A is correct because Key Visualizer for Bigtable generates visual reports for your tables that detail your usage based on the row keys that you access, show you how Bigtable operates, and can help you troubleshoot performance issues. Option B is not correct because Cloud Trace is used to debug latency in applications. Option C is not correct because adding logging statements won't help you understand the performance issues within Bigtable. Option D is not correct because adding more nodes might improve the performance, but the database could continue to have performance issues if the keys are not designed well.

109. Your company is moving your data analytics to BigQuery. Your other operations will remain on-premises. You need to transfer 800 TB of historic data. You also need to plan for 30 Gbps of daily data transfers that must be appended for analysis the next day. You want to follow Google-recommended practices to transfer your data. What should you do?
    - As early as possible every day, use Cloud VPN to transfer the existing data over the internet.
    - Use a Transfer Appliance to move the existing data to Google Cloud. Use Cloud VPN to transfer data daily.
    - Use a Transfer Appliance to move the existing data to Google Cloud.. Use VPC Network Peering to transfer data daily.
    - Use a Transfer Appliance to move the existing data to Google Cloud. Set up a Dedicated or Partner Interconnect for daily transfers.
 
Ans: Option A is not correct because the internet in general will have less stability and much lower speed. Transferring large amounts of data is not viable.  Option B is not correct because Cloud VPN is useful for data transfers at a rate of a few Gbps (1.5 Gbps to 3 Gbps). Option C is not correct because VPC Network Peering is used for data transfers within Google Cloud Organizations. Option D is correct because using a Transfer Appliance is recommended to transfer hundreds of terabytes of data. For large data transfers that occur regularly, a dedicated, hybrid networking connection is recommended.

110. Your team runs Dataproc workloads where the worker node takes about 45 minutes to process. You have been exploring various options to optimize the system for cost, including shutting down worker nodes aggressively. However, in your metrics you see that the entire job takes even longer. You want to optimize the system for cost without increasing job completion time. What should you do?
    - Set a graceful decommissioning timeout greater than 45 minutes.
    - Rewrite the processing in Cloud Data Fusion, and run the job automatically.
    - Rewrite the processing in Dataflow, and use stream processing of the same data.
    - Increase the number of vCPUs on each worker node so that the processing finishes sooner.

Ans: Option A is correct because graceful decommissioning will finish work in progress on a worker node before it is removed from the Dataproc cluster. Option B is not correct because rebuilding the data pipeline in Cloud Data Fusion will increase effort, cost, and time. Option C is not correct because rewriting the code in Dataflow will increase effort, cost, and time. Option D is not correct because increasing the number of vCPUs will greatly increase the cost.

111. Your customer has a SQL Server database that contains about 5 TB of data in another public cloud. You expect the data to grow to a maximum of 25 TB. The database is the backend of an internal reporting application that is used once a week. You want to migrate the application to Google Cloud to reduce administrative effort while keeping costs the same or reducing them. What should you do?
    - Migrate the database to Bigtable.
    - Migrate the database to Cloud Spanner.
    - Install SQL Server on a Compute Engine VM.
    - Migrate the database to SQL Server in Cloud SQL.
 
Ans: Option A is not correct because Bigtable is a NoSQL database and is not a suitable destination from a SQL Server source. Option B is not correct because Cloud Spanner will be costlier than Cloud SQL. Although Spanner has global availability, it is unnecessary for this application requirement. Option C is not correct because installing a custom SQL Server instance on a Compute Engine VM will require more administrative effort. Option D is correct because Cloud SQL provides managed MySQL, PostgreSQL, and SQL Server databases, which will reduce administrative effort. Twenty-five TB can be accommodated efficiently on Cloud SQL.

112. Your IT team uses BigQuery for storing structured data. Your finance team recently moved to Google Workspace Enterprise edition from a standalone, desktop-based spreadsheet processor. When the finance team needs data insights, the IT team runs a query on BigQuery, exports the data to a CSV file, and sends the file as an email attachment to the finance team members. You want to improve the process while you retain familiar methods of data analysis for the finance team. What should you do?
    - Run the query in BigQuery, and give the finance team access to the results view, which can be analyzed.
    - Run the query in BigQuery, and give the finance team access to the data visualizations in Google Data Studio.
    - Run the query in BigQuery, export the data to CSV, upload the file to a Cloud Storage bucket, and share the file with the finance team.
    - Run the query in BigQuery, and save the results to a Google Sheets shared spreadsheet that can be accessed and analyzed by the finance team.

Ans: Option A is not correct because the finance team will have to be given Google Cloud access and be trained on using BigQuery, which is not a familiar method. Option B is not correct because only giving the visualizations on Data Studio won't let the finance teams analyze the data. Option C is not correct because the finance team will have to be given Google Cloud access and be trained on using Cloud Storage, which is not a familiar method. Option D is correct because Connected Sheets gives you a direct and easy way to share BigQuery data through Google Sheets.

113. Your scooter-sharing company collects information about their scooters, such as location, battery level, and speed. The company visualizes this data in real time. To guard against intermittent connectivity, each scooter sends repeats of certain messages within a short interval. Occasional data errors have been noticed. The messages are received in Pub/Sub and stored in BigQuery. You need to ensure that the data does not contain duplicates and that erroneous data with empty fields is rejected. What should you do?
    - Store the data in BigQuery, and run delete queries on erroneous and duplicate data.
    - Use Dataflow to subscribe to Pub/Sub, process the data, and store the data in BigQuery.
    - Use Kubernetes to create a microservices application that can remove duplicates and erroneous data. Then insert the data into BigQuery.
    - Create an application on Compute Engine with Managed Instance Groups that can remove duplicates and erroneous data. Then insert the data into BigQuery.

Ans: Option A is not correct because directly storing data in BigQuery could cause data to be overwritten, and erroneous data could be present before it is deleted. Workarounds within BigQuery to circumvent these concerns would cost more effort, time, and money. Option B is correct because Dataflow is the recommended data processing product for streaming data. Dataflow can be programmed to remove duplicates, delete empty fields, and perform other custom data processing. Option C is not correct because creating a custom application for streaming processing on Kubernetes is a significant effort and is not recommended. Option D is not correct because creating a custom application for streaming processing on Compute Engine is a significant effort and is not recommended.

114. Your cryptocurrency trading company visualizes prices to help your customers make trading decisions. Because different trades happen in real time, the price data is fed to a data pipeline that uses Dataflow for processing. You want to compute moving averages. What should you do?
    - Use hopping windows in Dataflow.
    - Use session windows in Dataflow.
    - Use tumbling windows in Dataflow.
    - Use Dataflow SQL, and compute averages grouped by time.

Ans: Option A is correct because you use hopping windows to compute moving averages. Option B is not correct because session windows are not used to calculate moving averages. Option C is not correct because tumbling windows are not used to calculate moving averages.  Option D is not correct because grouping by time alone does not give you a moving average.

115. You are building the trading platform for a stock exchange with millions of traders. Trading data is written rapidly. You need to retrieve data quickly to show visualizations to the traders, such as the changing price of a particular stock over time. You need to choose a storage solution in Google Cloud. What should you do?
    - Use Bigtable.
    - Use Firestore.
    - Use Cloud SQL.
    - Use Memorystore.

Ans: Option A is correct because Bigtable is the recommended database for time series data that requires high throughput reads and writes. Option B is not correct because Firestore does not have the high throughput capabilities that are suitable for time-series data.  Option C is not correct because Cloud SQL does not the have high throughput capabilities that are suitable for time-series data. Option D is not correct because Memorystore is a fast in-memory database that is not suitable for persistently storing large amounts of data.

116. Your customer uses Hadoop and Spark to run data analytics on-premises. The main data is stored in hard disks that are centrally accessed. Your customer needs to migrate their workloads to Google Cloud efficiently while considering scalability. You want to select an architecture that requires minimal effort. What should you do?
    - Use Dataproc to run Hadoop and Spark jobs. Move the data to Cloud Storage.
    - Use Dataflow to recreate the jobs in a serverless approach. Move the data to Cloud Storage.
    - Use Dataproc to run Hadoop and Spark jobs. Retain the data on a Compute Engine VM with an attached persistent disk.
    - Use Dataflow to recreate the jobs in a serverless approach. Retain the data on a Compute Engine VM with an attached persistent disk.

Ans: Option A is correct because Dataproc is a fully managed service for hosting open source distributed processing platforms, such as Apache Spark, Presto, Apache Flink and Apache Hadoop on Google Cloud. Cloud Storage is the preferred storage option for all persistent storage needs. Option B is not correct because using Dataflow requires you to rewrite all the jobs. Option C is not correct because storing the centrally accessed data on persistent disks is not recommended. Option D is not correct because using Dataflow requires you to rewrite all the jobs. Storing the centrally accessed data on persistent disks is not recommended.

117. You used a small amount of data to build a machine learning model that gives you good inferences during testing. However, the results show more errors when real-world data is used to run the model. No additional data can be collected for testing. You want to get a more accurate view of the model's capability. What should you do?
    - Reduce the amount of data to improve the model.
    - Cross-validate the data, and re-run the model building process.
    - Create feature crosses that will add new columns to increase the data.
    - Duplicate the data twice to increase the data, and re-run the model building process.

Ans: Option A is not correct because this model is not underfitting. Option B is correct because this model appears to be overfitting. Using cross-validation will run the validation on multiple folds of the data, which reduces the overfitting. Option C is not correct because adding new columns will not reduce the overfitting. Option D is not correct because duplicating the data will not reduce the overfitting.

118. Your organization has been collecting information for many years about your customers, including their address and credit card details. You plan to use this customer data to build machine learning models on Google Cloud. You are concerned about private data leaking into the machine learning model. Your management is also concerned that direct leaks of personal data could damage the company's reputation. You need to address these concerns about data security. What should you do?
    - Remove all the tables that contain sensitive data.
    - Use libraries like SciPy to build the ML models on your local computer.
    - Remove the sensitive data by using the Cloud Data Loss Prevention (DLP) API.
    - Identify the rows that contain sensitive data, and apply SQL queries to remove only those rows.

Ans: Option A is not correct because removing data, such as entire tables, could reduce the effectiveness of the resulting model. Option B is not correct because building machine learning models on individual computers is not a viable approach when it involves large amounts of data. Option C is correct because Cloud DLP is the recommended approach to redact, mask, tokenize, and transform text and images to help protect data privacy. Option D is not correct because removing data, such as full rows, could reduce the effectiveness of the resulting model.

119. Your healthcare application has a backend system that accepts event data directly from IoT devices. Recent increases of the application's users and devices are causing a sudden influx of data that overwhelms the system. You need to redesign the data pipeline to ensure that all data is processed and that no events are lost. You want to follow Google-recommended practices. What should you do?  
    - Use Kafka with pull mode.
    - Use Pub/Sub with pull mode.
    - Use Pub/Sub with push mode.
    - Run Cloud Scheduler at fixed intervals.

Ans:  Option A is not correct because Kafka is not a managed solution in Google Cloud. The Google-recommended option is Pub/Sub, a fully managed, serverless solution. Option B is correct because pull mode allows new event data to be pulled for processing on demand when the previous data is processed. Pub/Sub will absorb and retain new events in the interim without losing them. Option C is not correct because Pub/Sub in push mode could continue to overwhelm the system. Option D is not correct because new event data should be pulled for processing when the previous processing is completed, and that is not expected to be at fixed intervals.

120. 
