
# BigQuery

   ![image](https://github.com/user-attachments/assets/92aa8a0f-6c45-4a46-bfe2-3e003ee7b621)

- Two modernization routes: Open fromat datalake and BigQuery based datalake

   ![image](https://github.com/user-attachments/assets/07ec45e3-7463-450e-a62c-88c35f6c1de1)

- BQ is ***serverless***, ***scalable***, ***high availaible*** SQL based ***data warehouse*** solution in GCP to analyse petabyte scale of data
- BQ is analytical database and not for Transactional purpose alternative to OpenSource Apache Hive. Some alternatives to BigQuery from other cloud providers would be AWS Redshift or Azure Synapse Analytics.
- GoogleSQL, used by both BigQuery and Spanner uses 2011 ANSI SQL. You can query using Standand and legacy SQL in Bigquery.
- Datasets are collections of tables that can be divided along business lines or a given analytical domain. Each dataset is tied to a Google Cloud project.
- Identity and Access Management is used to grant permission to perform specific actions in BigQuery. This replaces the SQL GRANT and REVOKE statements that are used to manage access permissions in traditional SQL databases.
- Schema auto-detection
  - Schema auto-detection enables BigQuery to infer the schema for CSV, JSON, or Google Sheets data. 
  - Schema auto-detection is available when you load data into BigQuery and when you query an external data source.
  - You don't need to enable schema auto-detection for Avro, Parquet, ORC, Firestore export, or Datastore export files. These file formats are self-describing, so BigQuery automatically infers the table schema from the source data. For Parquet, Avro, and Orc files, you can optionally provide an explicit schema to override the inferred schema.

- BigQuery writes all query results to a table. The table is either explicitly identified by the user (a destination table), or it is a temporary, cached results table. Temporary, cached results tables are maintained per-user, per-project. There are no storage costs for temporary tables

- BigQuery architecture is built on 4 infrastructure technologies.
    - ***Dremel***: the _compute_ part of BQ. It executes the SQL queries.
      - Dremel turns SQL queries into _execution trees_. The leaves of these trees are called _slots_ and the branches are called _mixers_.
      - The _slots_ are in charge of reading data from storage and perform calculations.
      - The _mixers_ perform aggregation.
      - Dremel dinamically apportions slots to queries as needed, while maintaining fairness for concurrent queries from multiple users.
    - ***Colossus***: Google's global storage system.
      - BQ leverages a _columnar storage format_ and compression algorithms to store data.
      - Colossus is optimized for reading large amounts of structured data.
      - Colossus also handles replication, recovery and distributed management.
    - ***Jupiter***: the network that connects Dremel and Colossus.
      - Jupiter is an in-house network technology created by Google which is used for interconnecting its datacenters.
    - ***Borg***: an orchestration solution that handles everything.
      - Borg is a precursor of Kubernetes.
  
        ![image](https://user-images.githubusercontent.com/19702456/218378202-7a953293-4430-4091-b194-9471db807cb7.png)

- BigQuery is Columnar storage.  When performing queries, Dremel modifies them in order to create an _execution tree_: parts of the query are assigned to different mixers which in turn assign even smaller parts to different slots which will access Colossus and retrieve the data. The columnar storage format is perfect for this workflow as it allows very fast data retrieval from colossus by multiple workers, which then perform any needed computation on the retrieved datapoints and return them to the mixers, which will perform any necessary aggregation before returning that data to the root server, which will compose the final output of the query.

    ![image](https://user-images.githubusercontent.com/19702456/218378411-6f62d0c2-670a-4783-96d4-0f38c20bdb05.png)

- Query caching is based on exact string comparison. So even whitespaces can cause a cache miss. Queries are never cached if they exhibit non-deterministic behavior (for example, they use CURRENT_TIMESTAMP or RAND), if the table or view being queried has changed (even if the columns/rows of interest to the query are unchanged), if the table is associated with a streaming buffer (even if there are no new rows), if the query uses DML statements, or queries external data sources.
- You can recover a deleted table only if another table with the same ID in the dataset has not been created. In particular, this means you cannot recover a deleted table if it is being streamed to, chances are that the streaming pipeline would have already created an empty table and started pushing rows into it. using Create or Replace table because this makes the table irrecoverable.
- BigQuery supports user-defined functions or UDF. Java Script is currently the only external language supported. BigQuery can optimize the execution of SQL much better than it can for JavaScript.


> ### Data Types
  - Avro is the preferred format for loading data into BigQuery. Compresed Avro files not supported but compressed Avro data blocks are supported. Parquet has better compression ratio and smaller files. For CSV and JSON, BQ can load uncompressed files significantly faster than compressed
  - Array Type
    - Arrays of arrays not allowed
    - Arrays of structs allowed
    - Declare as ARRAY<T>
    - BigQuery natively supports arrays. Array values must share a data type. Arrays are called REPEATED fields in BigQuery.
      - finding the number of elements with ARRAY_LENGTH(<array>)
      - deduplicating elements with ARRAY_AGG(DISTINCT <field>)
      - ordering elements with ARRAY_AGG(<field> ORDER BY <field>)
      - limiting ARRAY_AGG(<field> LIMIT 5)
  - Struct Type
    - Structs are containers that can have multiple field names and data types nested inside. Arrays can be one of the field types inside of a Struct. Declare as STRUCT<T> eg. STRUCT<a int64, b string>
    - Structs can be directly compared using equality operators: =, != or <>, [NOT] IN


> ### Data Access Controls
  - Organization or project level for all project's BQ resources
  - dataset level for access to a specific data set
  - table or view level for access to specific tables or views in a dataset
- Column Level Security
  - Restrict access to sensitive information in a table
  - Define Taxonomy of tags in Data Catalog and assign tags to columns in Bigquery
  - USe IAM roles to restrict access to each policy tag
- Row Level Security
  - Filter data in a table based on user conditions
  - Row level policy is applied to table
  ![image](https://user-images.githubusercontent.com/19702456/224623322-b8b93a8c-3087-4a03-9c2a-552ec7f3d6ab.png)


> ### Views vs Authorized Views
- The main difference between a regular view and an authorized view is which authority is used for controlling access to the source table data
- A regular view's access to source table data is checked on behalf of the end user's authority. The view's SQL query can be used to restrict the columns (fields) the users are able to query
- An authorized view's access to source table data is checked using the authorized view's own authority
   - The view's SQL query can be used to restrict the columns (fields) the users are able to query ○
   - Authorized views enables us to mask the restricted columns data, without changing the underlying tables data


> ### Partitioning and Clustering  
#### Partitioning 

- [Partition tables](https://cloud.google.com/bigquery/docs/partitioned-tables) are very useful to improve performance and reduce costs, because BQ will not process as much data per query.
- You may partition a table by:
  - ***Time-unit column***: tables are partitioned based on a `TIMESTAMP`, `DATE`, or `DATETIME` column in the table. Special partitions: __NULL__ when nulls in partition column and __UNPARTITIONED__ when values in column outside allowed range
  - ***Ingestion time***: tables are partitioned based on the timestamp when BigQuery ingests the data. Creates pseudo-column _PARTITIONTIME 
  - ***Integer range***: tables are partitioned based on an integer column.
  - For Time-unit and Ingestion time columns, the partition may be daily (the default option), hourly, monthly or yearly.
  - BigQuery limits the amount of partitions to 4000 per table. If you need more partitions, consider clustering
  - Requiring partition filter using _partitioning_filter parameter and is specified at table level
- Partition limits:
   - Number of partitions per partitioned table = 10,000 partitions
   - Number of partitions modified by a single job (query or load) = 10,000 partitions
   - Number of partition modifications per ingestion-time partitioned table per day = 5,000 modifications
   - Number of partition modifications per column-partitioned table per day = 30,000 modifications
   - Project can run up to 50 modifications per partitioned table every 10 seconds
   - A range-partitioned table can have up to 10,000 possible ranges
  
#### Clustering 

- ***Clustering*** consists of rearranging a table based on the values of its columns so that the table is ordered according to any criteria. Clustering can be done based on one or multiple columns up to 4; the ***order*** of the columns in which the clustering is specified is important in order to determine the column priority.
- Clustering may improve performance and lower costs on big datasets for certain types of queries, such as queries that use filter clauses and queries that aggregate data.
- tables with less than 1GB don't show significant improvement with partitioning and clustering; doing so in a small table could even lead to increased cost due to the additional metadata reads and maintenance needed for these features.
- Clustering columns must be ***top-level***, ***non-repeated*** columns. The following datatypes are supported:
  * `DATE`
  * `BOOL`
  * `GEOGRAPHY`
  * `INT64`
  * `NUMERIC`
  * `BIGNUMERIC`
  * `STRING`
  * `TIMESTAMP`
  * `DATETIME`
- BigQuery supports clustering for both partitioned and non-partitioned tables. When you use clustering and partitioning together, the data can be partitioned by a date, date time or timestamp column, and then clustered on a different set of columns. A partitioned table can also be clustered.
- columns that contain more distinct values (high cardinality) or, columns which are frequently used in WHERE filters or JOIN conditions are the columns which should be used for clustering.
- A table can be clustered on four columns at most.
- Clustering - Best Practices
   - Do not use clustered columns in complex filter expressions. If you use a clustered column in a complex filter expression, the performance of the query is not optimized because block pruning cannot be applied. eg. `CAST(customer_id AS STRING) = "10000"`.  The query will not prune blocks because a clustered column—customer_id—is used in a function in the filter expression.
   - Filter clustered columns by sort order
   - Do not compare clustered columns to other columns. If a filter expression compares a clustered column to another column (either a clustered column or a non-clustered column), the performance of the query is not optimized because block pruning cannot be applied.

| Clustering | Partitioning |
|---|---|
| Cost benefit unknown. BQ cannot estimate the reduction in cost before running a query. | Cost known upfront. BQ can estimate the amount of data to be processed before running a query. |
| High granularity. Multiple criteria can be used to sort the table. | Low granularity. Only a single column can be used to partition the table. |
| Clusters are "fixed in place". | Partitions can be added, deleted, modified or even moved between storage options. |
| Benefits from queries that commonly use filters or aggregation against multiple particular columns. | Benefits when you filter or aggregate on a single column. |
| Unlimited amount of clusters; useful when the cardinality of the number of values in a column or group of columns is large. | Limited to 10,000 partitions; cannot be used in columns with larger cardinality. |
| Can cluster the table up to four columns | Single partition column |
| No limit on DML statements | Partitioning limits DML statements to max 10 K affected partitions per statement) |
| Clustering supports: INT64, TIMESTAMP, DATE, DATETIME, BOOL, GEOGRAPHY, NUMERIC, BIGNUMERIC, STRING | Partitioning supports: INT64, TIMESTAMP, DATE, and DATETIME |
| Clustering enables pruning data down to block-level | (partitioning prunes down to file-level |


You may choose clustering over partitioning when partitioning results in a small amount of data per partition, when partitioning would result in over 4000 partitions or if your mutation operations modify the majority of partitions in the table frequently (for example, writing to the table every few minutes and writing to most of the partitions each time rather than just a handful).

BigQuery has _automatic reclustering_: when new data is written to a table, it can be written to blocks that contain key ranges that overlap with the key ranges in previously written blocks, which weaken the sort property of the table. BQ will perform automatic reclustering in the background to restore the sort properties of the table. For partitioned tables, clustering is maintaned for data within the scope of each partition.


> ### External datasets
- In addition to BigQuery datasets, you can create external datasets (federated datasets), which are links to external data sources:
  - Spanner external dataset
  - AWS Glue federated dataset
- Once created, external datasets contain tables from a referenced external data source. Data from these tables aren't copied into BigQuery, but queried every time they are used.
- External datasets don't support table expiration, replicas, time travel, default collation, default rounding mode or the option to enable or disable case insensitive tables name.


> ### External Tables
- An external data source is a data source that you can query directly from BigQuery, even though the data is not stored in BigQuery storage. BigQuery has two different mechanisms for querying external data:

  - ***External Tables***: External tables are similar to standard BigQuery tables, in that these tables store their metadata and schema in BigQuery storage. However, their data resides in an external source. There are four kinds of external tables:
    - BigLake tables: BigLake tables let you query structured data in external data stores with access delegation. Access delegation decouples access to the BigLake table from access to the underlying data store. Because the service account handles retrieving data from the data store, you only have to grant users access to the BigLake table. The staleness for BigLake's metadata cache can be configured between 30 minutes to 7 days and can be refreshed automatically or manually.
    - BigQuery Omni tables: BigQuery Omni is a flexible, multi-cloud analytics solution powered by Anthos that lets you cost-effectively access and securely analyze data stored in Amazon Simple Storage Service (Amazon S3) or Azure Blob Storage using BigLake tables. Single pane of glass to view all your data

      ![image](https://github.com/user-attachments/assets/f92cdf02-8409-4dcb-8195-4351672922ae)

    - Object tables: Object tables let you analyze unstructured data in Cloud Storage. You can perform analysis with remote functions or perform inference by using BigQuery ML, and then join the results of these operations with the rest of your structured data in BigQuery. Like BigLake tables, object tables use access delegation, which decouples access to the object table from access to the Cloud Storage objects.
    - Non-BigLake external tables: Non-BigLake external tables let you query structured data in external data stores. To query a non-BigLake external table, you must have permissions to both the external table and the external data source. 
      - Bigtable
      - Cloud Storage: If you create a non-BigLake external table based on Cloud Storage, then you can use multiple external data sources, provided those data sources have the same schema. This isn't supported for non-BigLake external table based on Bigtable or Google Drive. You can use non-BigLake external tables with the following data stores:
      - Google Drive

  - ***Federated Queries***: Federated queries let you send a query statement to AlloyDB, Spanner, or Cloud SQL databases and get the result back as a temporary table.  You use the EXTERNAL_QUERY function to send a query statement to the external database, using that database's SQL dialect.
     - Federated queries are subject to the optimization technique known as SQL pushdowns. They improve the performance of a query by delegating operations like filtering down to the external data source instead of performing them in BigQuery. Reducing the amount of data transferred from the external data source can reduce query execution time and lower costs.
     - You can perform federated queries to PostgreSQL and MySQL on instances that have Private IP only

    ![image](https://github.com/user-attachments/assets/e9c09763-a08b-49dc-8638-b74d4d06c6f2)

- Performance considerations
   - Amount of data being queried: The benefit of using Parquet as opposed to CSV or Avro only grows as the amount of data being queried gets larger and the query complexity increases.
   - Compression: CSV.gzip and ORC.snappy take up nearly equal amounts of space. Compressing Parquet with snappy does very little to reduce the amount of space that the data takes up in Cloud Storage. With larger payloads (>50 GB), the CSV files compressed with GZIP performs better than uncompressed when the chunks of data are about 50 MB each. For smaller payloads (5 GB), uncompressed performs better.
   - File format: ORC files seem to take less storage space followed by Parquet, Avro, and CSV file types.
   - Region:
      - Using a single region Cloud Storage bucket with a single region external table offers the fastest run time. When using this combination, your external table and your Cloud Storage bucket must be in the same region.
      - Avoid using multi-region buckets with external tables to avoid cross region issues.
      - If data redundancy is critical, use dual-region.
   - Slot allocation: In general, it would be expected, especially for more complex queries, that as the slot allocation goes up, the run time will decrease.


> ### BigLake API
- BigLake is a storage engine that unifies data warehouses and lakes, by providing uniform fine-grained access control, performance acceleration across multi-cloud storage and open formats.
- The BigLake API provides access to BigLake Metastore, a serverless, fully managed, highly available metastore for open-source data that can be used for quesrying Apache Iceberg tables in Bigquery.

    <img src="https://github.com/user-attachments/assets/1c927258-8443-415b-b0cb-a0d8a2bfc8cb" width="400" height="300" >


> ### Time Travel
  -  Time travel is a background copy of all your data in your tables in your data set for a rolling seven days. You can set the duration of the time travel window, from a minimum of two days to a maximum of seven days.
  -  Time travel lets you query data that was updated or deleted, restore a table that was deleted, or restore a table that expired. you cannot retrieve deleted table through the console you have to do that through the cloudshell `bq` command
  - Time Travel SELECTs are considered as Query jobs and billed on the bytes read. These SELECTs can be executed in the console or at the bq command prompt as the table has not
been deleted.
  - You set the time travel window at the dataset level, which then applies to all of the tables within the dataset.
  - Using a shorter time travel window lets you save on storage costs when using the physical storage billing model. These savings don't apply when using the logical storage billing model.
  - valid reason for modifying the BigQuery dataset number of days for Time Travel?
    - Lower storage costs.
    - Enforcing Data Governance data life.
    - Faster data exports.
  - The table must be stored in BigQuery; it cannot be an external table. 
  - After you replace an existing table by using the CREATE OR REPLACE TABLE statement, you can use FOR SYSTEM_TIME AS OF to query the previous version of the table. If the table was deleted, then the query fails and returns an error. However, you can restore the table by copying from a point in time to a new table. To restore data from a deleted table, you need to have the bigquery.admin role on the corresponding table.
  - You can query a table's historical data from any point in time within the time travel window by using a FOR SYSTEM_TIME AS OF clause. There is no limit on table size when using SYSTEM_TIME AS OF. eg. query returns a historical version of the table from one hour ago:
          ```
          SELECT *
          FROM `mydataset.mytable`
            FOR SYSTEM_TIME AS OF TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 1 HOUR);
          ```

> ### Table Snapshots
- Table snapshots are point-in-time copies of tables.
- Table snapshots are read-only, but you can restore a table from a table snapshot.
- BigQuery only stores the delta between a table snapshot and its base table.


> ### BI Engine
-  BI Engine can accelerate SQL queries from any source, including those written by data visualization tools, and can manage cached tables for on-going optimization.
-  BI Engine doesn’t require you to build OLAP cubes on your own, it handles that for you.
-  It works on top of the same storage, same network, same shuffle layer and working alongside BigQuery workers (which are Slots). Stateful workers, persist unlike standard BQ slots that get unallocated after they are used makes it possible for BI Engine to get such dramatic performance improvements
-  Full visibility into metrics including aggregate refresh time, cache hit ratios, query latency inside Google Operations
-  BI Engine provides the following advantages:
    - BigQuery API: Any BI solution or custom application that works with the BigQuery API through standard mechanisms such as REST or JDBC and ODBC drivers can use BI Engine without modification.
    - Vectorized runtime: Using vectorized processing in an execution engine makes more efficient use of modern CPU architecture, by operating on batches of data at a time.
    - Seamless integration: BI Engine works with BigQuery features and metadata, including authorized views, column level security, and data masking.
    - Reservations: BI Engine reservations manage memory allocation at the project location level. BI Engine caches specific columns or partitions that are queried, prioritizing those in tables marked as preferred.
- BI Engine is useful in the following use cases:
  - You use BI tools to analyze your data
  - You have certain tables that are queried most frequently
- BI Engine might not fit your needs in the following cases:
  - You use wildcards in your queries
  - You rely heavily on BigQuery features which BI Engine doesn't support
    
     <img src="https://github.com/user-attachments/assets/bf22f8c1-97d1-4b36-b5ba-11016af5145c" width="400" height="300" >
  

> ### Bigquery Notebooks
- You can use notebooks to complete analysis and machine learning (ML) workflows by using SQL, Python, and other common packages and APIs.
- Notebooks offer improved collaboration and management with the following options: 
  - Share notebooks with specific users and groups by using Identity and Access Management (IAM).
  - Review the notebook version history.
  - Revert to or branch from previous versions of the notebook.
- Notebooks in BigQuery offer the following benefits:
  - BigQuery DataFrames is integrated into notebooks, no setup required. BigQuery DataFrames is a Python API that you can use to analyze BigQuery data at scale by using the pandas DataFrame and scikit-learn APIs.
  - Assistive code development powered by Gemini generative AI.
  - Auto-completion of SQL statements, the same as in the BigQuery editor.
  - The ability to save, share, and manage versions of notebooks.
  - The ability to use matplotlib, seaborn, and other popular libraries to visualize data at any point in your workflow.


> ## Data Migration Tool (DMT)
- Automate schema migration, data migration, sql translation & validation
- Open Source orchestration tool
- Reports migration insights
- Common DMT tools:
   - Bigquery Data Transfer Service (BQDTS):
      - BigQuery Data Transfer Service is serverless service which enables seamless loading of structured data from diverse sources, like SaaS applications, object stores, and other data warehouses into BigQuery on a scheduled, managed basis.
      - You can access the BigQuery Data Transfer Service using the:
        - Google Cloud console
        - bq command-line tool
        - BigQuery Data Transfer Service API
      - You cannot use the BigQuery Data Transfer Service to transfer data out of BigQuery.
      - The BigQuery Data Transfer Service supports loading data from the following data sources: (30-10-2024)
        - Amazon S3
        - Amazon Redshift
        - Azure Blob Storage
        - Campaign Manager
        - Cloud Storage
        - Display & Video 360
        - Facebook Ads (Preview)
        - Google Ad Manager
        - Google Ads
        - Google Merchant Center (Preview)
        - Google Play
        - Oracle (Preview)
        - Salesforce (Preview)
        - Salesforce Marketing Cloud (Preview)
        - Search Ads 360
        - ServiceNow (Preview)
        - Teradata
        - YouTube Channel
        - YouTube Content Owner
       
   - Data Validation Tool (DVT):
      - Open source python command line tool: Suuports data validation between on-premises and other cloud data warehouse
      - Multi-level validations: Compares the source and target data by table, column, row and custom sql query
      - Inegrates with Google Cloud services such as cloud composer, cloud functions, cloud run
   
   - Batch SQL translator:
      - Translates scripts written in other SQL dialects into GoogleSQL queries
     

> ### Streaming in Bigquery
- Streaming Inserts allows you to insert one item at a time into a table.
- New tables can be created from a temporary table that identifies the schema to be copied. The data enters a streaming buffer where it is held briefly until it can be inserted into the table.
- You can disable best effort de-duplication by not populating the insert ID field for each row inserted.
  
    ![image](https://github.com/user-attachments/assets/9483f15d-597a-4b54-b182-fb23722c24e4)


> ### ML in BigQuery

  ![image](https://github.com/user-attachments/assets/0dd88997-05bf-4864-ae3d-6e4cf198186e)

  ![image](https://github.com/user-attachments/assets/caf50cf7-033d-4f11-bb99-79eb4a878170)



> ## Gemini Models in BiqQuery
- BigQuery Insights
   - It's a helpful tool for exploring and understanding your data, especially if you're new to SQL or want to get started with data analysis.
   - It uses Gemini to generate queries based on your data's metadata, making it easier to find relevant insights.
- DataCanvas
   - discover and visualize the query workflow in BigQuery.
- Table Explorer:
   - It's a visual tool to explore one table at a time.
   - It doesn't support complex operations like joins across multiple tables.
   - It generates basic SQL queries. For example, you cannot create complex WHERE clause statements including operands like AND or OR.
   - It doesn't provide AI-powered assistance for complex queries.
 
     
   ![image](https://github.com/user-attachments/assets/c1105b0d-cbe2-4ef6-b0f4-d81ef5aee8db)


> ### Analytics Hub - Data share solution
- Platform for secure data sharing with authorized users (internal and external)
- Construct of data providers, subscribers and data exchange, data discovery
- Built on top of BigQuery

    ![image](https://github.com/user-attachments/assets/509b622e-de43-4461-88cc-f053a874f161)


> ### Pricing

![image](https://github.com/user-attachments/assets/006ebf8a-c685-42b0-af62-43a49a0c1bc0)

- A rate limit limit or a quota it is a hard ceiling cost control but budgets are not a hard ceiling they are a guideline of how much money you are spending on variety of services
- The cost of a query is always assigned to the active project from where the query is executed.

- Data Transfer Service pricing
  - After data is transferred to BigQuery, standard BigQuery storage and query pricing applies.
  - Extraction, uploading to a Cloud Storage bucket, and loading data into BigQuery is free.

- Free operations
  - Load data: Free using the shared slot pool. Customers can choose editions pricing for guaranteed capacity. Once the data is loaded into BigQuery, you are charged for storage. 
  - Copy data: You are not charged for copying a table, but you do incur charges Data ingestion editions pricing or storing the new table and the table you copied.
  - Export data: Free using the shared slot pool, but you do incur charges for storing the data in Cloud Storage. Customers can choose editions pricing for guaranteed capacity. When you use the EXPORT DATA SQL statement, you are charged for query processing.
  - Delete operations:	You are not charged for deleting datasets or tables, deleting individual table partitions, deleting views, or deleting user-defined functions
  - Metadata operations: You are not charged for list, get, patch, update and delete calls. Examples include (but are not limited to): listing datasets, updating a dataset's access control list, updating a table's description, or listing user-defined functions in a dataset. Metadata caching operations for BigLake tables aren't included in free operations.

- When BI Engine accelerates a query, the query stage that reads table data is free. Subsequent stages depend on the type of BigQuery pricing you're using:
  - For on-demand pricing, stages that use BI Engine are charged for 0 scanned bytes. Subsequent stages will not incur additional on-demand charges.
  - For editions pricing, the first stage consumes no BigQuery reservation slots. Subsequent stages use slots from the BigQuery reservation.
  
- BigQuery pricing has two main components:
  - ***Storage pricing***: Storage pricing is the cost to store data that you load into BigQuery. The cost of storage is fixed and at the time of writing is US$0.02 per GB per month. Two dataset storage billing models are present in bigquery: Logical bytes and Physical bytes
    - When you create a dataset, the storage used by that dataset is billed to you using logical bytes as the default unit of consumption. However, you can choose to use physical bytes for billing instead. You can also change an existing dataset's storage billing model to use physical bytes.
    - When you set your storage billing model to use physical bytes, the total active storage costs you are billed for include the bytes used for time travel and fail-safe storage. You can configure the time travel window to balance storage costs with your data retention needs. For more information on forecasting your storage costs, see Forecast storage billing.
    - When you change a dataset's billing model, it takes 24 hours for the change to take effect.
    - Once you change a dataset's storage billing model, you must wait 14 days before you can change the storage billing model again.
    - The dataset storage billing model is only available for your datasets if your organization does not have any existing flat-rate slot commitments located in the same region as the dataset. Your organization can enroll datasets for physical storage billing when there are no flat-rate commitments located in the same region as the dataset.
    - Difference between Uncompresses and Compressed storage pricing

        ![image](https://github.com/user-attachments/assets/53a3571e-af71-4c28-9a75-2eb052e6575d)
    
  - ***Compute pricing***: Compute pricing is the cost to process queries, including SQL queries, user-defined functions, scripts, and certain data manipulation language (DML) and data definition language (DDL) statements.
    - ***On-demand pricing (per TiB)***: With this pricing model, you are charged for the number of bytes processed by each query. US$6.25 per TB per month; the first TB of the month is free.
    - ***Capacity pricing (per slot-hour)***: With this pricing model, you are charged for compute capacity used to run queries, measured in slots (virtual CPUs) over time. This model takes advantage of BigQuery editions. You can use the BigQuery autoscaler or purchase slot commitments, which are dedicated capacity that is always available for your workloads, at a lower price.

      - The idea with big query editions is that the consumer doesn't need to have to figure out all their reservations and how many Flex jobs or Flex slots they would need. For variable loads they can configure this all in their bigquery Edition as an autoscaling solution (autoscaling up and autoscaling down) and the customer consumes the slots as required.
        - BigQuery editions slot capacity:
          - is available in 3 editions: Standard, Enterprise, and Enterprise Plus.
          - applies to query costs, including BigQuery ML, DML, and DDL statements.
          - does not apply to storage costs or BI Engine costs.
          - does not apply to streaming inserts and using the BigQuery Storage API.
          - can leverage the BigQuery autoscaler.
          - is billed per second with a one minute minimum
            
        - Optional BigQuery editions slot commitments:
          - are available for one or three year periods with higher discounts
          - are available in Enterprise and Enterprise Plus editions.
          - are regional capacity. Commitments in one region or multi-region cannot be used in another region or multi-region and cannot be moved.
          - can be shared across your entire organization. There is no need to buy slot commitments for every project.
          - are offered with a 100-slot minimum and increments of 100 slots.
          - are automatically renewed unless set to cancel at the end of the period.

            ![image](https://github.com/user-attachments/assets/31f8fe67-b64e-46cd-85de-55d659dd2386)

    - Advantages of using Bigquery Editions:
      - Flexibility:
        - Match workloads to tiers, so you only pay for
        - Mix and match editions for the best price performance per workload
      - Price Predictability:
        - 1-year and 3-year commitments with higher discounts
        - Leverage autoscale to pay only for what you use. No need to overpay for underused capacity
        - Low cost storage
      - Control:
        - Autoscaling with baseline and max thresholds to intelligently manage costs.
        - BigQuery BI Engine dynamically manages slots while queries are running! BI Engine Slots are stateful.
      - BigQuery Autoscaler: Dynamically adjusts the capacity in response to planned or unplanned changes in demand to help ensure you pay only for what you use. Autoscaling is the core functionality available in a new
      commercial model
      
        <img src="https://github.com/user-attachments/assets/96797479-f758-4493-861e-f0cc909e6291" width="500" height="500" >
  

> ### Data Lineage API
- Lineage is a record of data being transformed from sources to targets
- The API collects that information and organizes it into a hierarchy of processes, runs, and events
   - A process is a data transformation within a dataset
   - A run is an execution of a process
   - An event represents a point in time when the process took place
- BigQuery automatically tracks lineage
   - Copy jobs
   - Load jobs
   - CREATE TABLE queries
   - CREATE VIEW queries
   - DML statements such as INSERT, UPDATE, MERGE, DELETE
- You can programmatically track lineage for custom sources by using the API
- Interpreting the query plan
   - If there is a significant difference between avg and max time for workers consider using APPROX_TOP_COUNT to check 
   - If there are a lot of reads in intermediate steps consider filtering early
   - For long periods of time spent on CPU tasks consider approx functions  filtering early and optimize your UDF usage with a persistent UDF or avoid using all together

> ### Best practices
* Cost reduction
  * Avoid `SELECT *` . Reducing the amount of columns to display will drastically reduce the amount of processed data and lower costs.
  * Use clustered and/or partitioned tables if possible.
  * Use [streaming inserts](https://cloud.google.com/bigquery/streaming-data-into-bigquery) with caution. They can easily increase cost.
  * [Materialize query results](https://cloud.google.com/bigquery/docs/materialized-views-intro) in different stages.
* Query performance
  * Filter on partitioned columns.
  * [Denormalize data](https://cloud.google.com/blog/topics/developers-practitioners/bigquery-explained-working-joins-nested-repeated-data).
  * Use [nested or repeated columns](https://cloud.google.com/blog/topics/developers-practitioners/bigquery-explained-working-joins-nested-repeated-data).
  * Use external data sources appropiately. Constantly reading data from a bucket may incur in additional costs and has worse performance.
  * Reduce data before using a `JOIN`.
  * Do not treat `WITH` clauses as [prepared statements](https://www.wikiwand.com/en/Prepared_statement).
  * Avoid [oversharding tables](https://cloud.google.com/bigquery/docs/partitioned-tables#dt_partition_shard).
  * Avoid JavaScript user-defined functions.
  * Use [approximate aggregation functions](https://cloud.google.com/bigquery/docs/reference/standard-sql/approximate_aggregate_functions) rather than complete ones such as [HyperLogLog++](https://cloud.google.com/bigquery/docs/reference/standard-sql/hll_functions).
  * Order statements should be the last part of the query.
  * [Optimize join patterns](https://cloud.google.com/bigquery/docs/best-practices-performance-compute#optimize_your_join_patterns).
  * Place the table with the _largest_ number of rows first, followed by the table with the _fewest_ rows, and then place the remaining tables by decreasing size. This is due to how BigQuery works internally: the first table will be distributed evenly and the second table will be broadcasted to all the nodes.




# Dataform 
- Dataform is a service for data analysts to develop, test, version control, and schedule complex SQL workflows for data transformation in BigQuery.
- Dataform lets you perform the following data transformation actions:
  - Develop and execute SQL workflows for data transformation.
  - Collaborate with team members on SQL workflow development through Git.
  - Manage a large number of tables and their dependencies.
  - Declare source data and manage table dependencies.
  - View a visualization of the dependency tree of your SQL workflow.
  - Manage data with SQL code in a central repository.
  - Reuse code with JavaScript.
  - Test data correctness with quality tests on source and output tables.
  - Version control SQL code.
  - Document data tables inside SQL code.
- With Dataform, developers create and compile SQL workflows using SQL and JavaScript
  
- Dataform has the following known limitations:
  - Dataform in Google Cloud runs on a plain V8 runtime and does not support additional capabilities and modules provided by Node.js. 
  - git+https:// URLs for dependencies in package.json are not supported.
  - Manually running unit tests is not available.
  - Searching for file content in development workspaces is not available.

![image](https://github.com/user-attachments/assets/389afccc-bae7-4e87-8dd5-1b6fab71a6de)
- primary purpose of assertions in Dataform is to define data quality tests, ensuring data consistency and accuracy.
  
- Dataform provides two methods to manage dependencies:
  - implicit declaration: Implicit declaration is when you reference tables or views directly within your SQL using the ref() function. It is also possible to use the resolve() function to reference without creating a dependency.
    ```
    config {
      ...
    }
    SELECT ...
    FROM ${ref("customer_details")}
    ```
  - explicit declaration: Explicit declaration is when you list dependencies within a config block using the dependencies array.
    ```
    config {
      ...
      dependencies: ["customer_details"]
    }
    SELECT ...
    ```

![image](https://github.com/user-attachments/assets/f95cdf9e-f064-47fc-906c-ad565c49acf4)


