# Dataproc

  ![image](https://github.com/user-attachments/assets/74cc36c1-0274-4c6e-af6e-151297c89c72)

- Dataproc is fully managed service for running Hadoop and Spark data processing workloads. Job Supported: Hadoop, SparkR, Spark, SparkSQL, Hive, Pig, PySpark
- The results can then be easily stored in various destinations like Cloud Storage, BigQuery, or NoSQL databases like Bigtable, all within the Google Cloud ecosystem.
- Cluster type
  - Standard (1 master, N workers)
  - Single Node (1 master, 0 workers)
  - High Availability (3 masters, N workers)
- Worker nodes can be regular VM or Preemptible VM (for cost reduction)
- Internals

    ![image](https://github.com/user-attachments/assets/2c218d2f-1a85-46f6-a624-ef201a7ba889)

- The Pub/Sub Lite Spark Connector is an open-source Java client library that supports the use of Pub/Sub Lite as an input and output source for Apache Spark Structured Streaming. Supports read/write Spark Streaming functionality including pyspark.sql.


> ### Dataproc Metastore
  - Dataproc Metastore is a fully managed, highly available, autohealing serverless Apache Hive metastore that runs on Google Cloud.
  - A centralized metadata repository that can be shared across multiple Dataproc Clusters running different open source engines such as Hive, Spark and Presto.
  - Provides a unified view of open source tables, providing interoperability between cloud-native services and various other open source-based offerings.

> ### Enhanced Flexibility Mode
  - When nodes are removed, either manually or autoscaled, data may be required to be shuffled from one node to another. This can add processing delays to running jobs. EFM manages shuffling data between workers to minimize job progress delays. Two user-selectable modes:
    - Primary-worker shuffle. Mappers write data to primary workers. This mode is only available to Spark jobs.
    - HCFS (Hadoop Compatible File System). This mode can benefit jobs with small amounts of data.

> ### Optimizing Dataproc
- Make sure that the Cloud storage bucket is in the same regional location as your Dataproc region.
- Be sure that you do not have any network rules or roots that funnel Cloud storage traffic through a small number of VPN gateways before it reaches your cluster.
- Make sure you are not dealing with more than around 10,000 input files. If you find yourself in this situation try to combine or union the data into larger file sizes.
- If this file volume reduction means that now you are working with larger datasets more than approximately 50,000 Hadoop partitions you should consider adjusting the setting fs.gs.block.size to a larger value accordingly.
- Is the size of your persistent disk limiting your throughput? Often times when getting started with Google Cloud you may have just a small table that you want to benchmark. This is generally a good approach as long as you do not choose a persistent disk that assigns to such a small quantity of data, it will most likely limit your performance. Standard persistent disk scale linearly with volume size.
- Did you allocate enough virtual machines to your cluster? Running prototypes and benchmarking with real data and real jobs is crucial to informing the actual VM allocation decision. Employing job scoped clusters is a common strategy for Dataproc clusters
- Local HDFS is a good option if:
  - Your jobs require a lot of metadata operations—for example, you have thousands of partitions and directories, and each file size is relatively small.
  - You modify the HDFS data frequently or you rename directories. Cloud Storage objects are immutable, so renaming a directory is an expensive operation because it consists of copying all objects to a new key and deleting them afterwards.
  - You heavily use the append operation on HDFS files.
  - You have workloads that involve heavy I/O. For example, you have a lot of partitioned writes, such as in this example `spark.read.write.partitionBy(...).parquet("gs://")`
  - You have I/O workloads that are especially sensitive to latency. For example, you require single-digit millisecond latency per storage operation.

> ### Dataproc Serverless
  - Dataproc Serverless lets you run Spark batch workloads without requiring you to provision and manage your own cluster.
  - The service will run the workload on a managed compute infrastructure, autoscaling resources as needed. Estimating the correct number of worker nodes for a current and ongoing cluster can be challenging and prone to repetitive experiments. Dataproc Auto Scaling automates the process.
    - Requires an Autoscale Policy to be defined.
    - Autoscaling can be added to an existing cluster or as part of the definition before a cluster is created.
    - Only applies to workers not masters.
    - Best results when applying to Secondary workers.
  - Dataproc Serverless charges apply only to the time when the workload is executing.
  - Schedule Dataproc Serverless for Spark batch workloads: You can schedule a Spark batch workload as part of an Airflow or Cloud Composer workflow using an Airflow batch operator.
  - There are two ways to run Dataproc Serverless workloads:
    - Dataproc Serverless for Spark Batch: Use the Google Cloud console, Google Cloud CLI, or Dataproc API to submit a batch workload to the Dataproc Serverless service  and are ideal for automated or scheduled jobs
    - Dataproc Serverless for Spark Interactive: Interactive sessions leverage JupyterLab, either locally or within the Google Cloud environment, for interactive development and exploration.

      ![image](https://github.com/user-attachments/assets/890297d5-c81c-43a4-a70e-caabd37ae6ee)

> ### Monitoring
  - Job Driver Output - The best way to find what error caused a Spark job failure is to look at the driver output and the logs generated by the Spark executioners. It's possible to see the logs for each container from the spark app Web UI, or from the history server after the program ends in the executer's tab. You need to browse through each Spark container to view each log.
  - Cloud Monotoring - can monitor the cluster's CPU, disk, network usage and Yarn resources.
  - Cloud Logging - provides a consolidated and concise view of all logs so that you don't need to spend time browsing among container logs to find errors.

> ### Migration Tools
  - DistCp tool: Distributed copy tool from Hadoop.
  - Cloud Storage connector for Hadoop: A complete, end-to-end, data transfer solution for Hadoop-based data lakes to Cloud Storage.
    -  Zero Coding effort
    -  Support for push and pull models
    -  Built-in fault tolerance, error handling
    -  Data integrity check using CRC32C checksum and byte to byte comparison

    ![image](https://github.com/user-attachments/assets/82a9f059-b377-44a4-9068-1ef7046a77f9)

  - Dataproc Templates: Ready to use, open sourced, customizable templates based on serverless Spark (Dataproc).
    - Tasks include data import, data export, data backup and data restore as well as bulk API operations
    - Offers simplified event-based scheduling of Dataproc jobs via Cloud Functions or Cloud Scheduler
    - Parameterization enables the reusability of the workflow templates for different environments- DEV, STAGE, PROD
    - Workflows are ideal for complex job flows. You can create job dependencies so that a job starts only after its dependencies complete successfully
    - Supports automated provisioning of Ephemeral cluster or submitting jobs to long-lived clusters
    - Templates are provided in the following language and execution environments:
      - Airflow Orchestration templates: Run Spark jobs from DAGs in Airflow
      - Java templates: Run Spark batch workloads or jobs on Dataproc Serverless or an existing Dataproc cluster
      - Python templates: Run PySpark batch workloads on Dataproc Serverless
      - Notebook templates: Run Spark jobs using Vertex AI Notebooks

 
