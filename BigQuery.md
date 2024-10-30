
# BigQuery

![image](https://github.com/user-attachments/assets/92aa8a0f-6c45-4a46-bfe2-3e003ee7b621)

- Data warehouse solution in GCP just like Relational database – SQL schema. 
- BQ is ***serverless***. There are no servers to manage or database software to install; this is managed by Google and it's transparent to the customers.
- BQ is ***scalable*** and has ***high availability***. Google takes care of the underlying software and infrastructure.
- BQ has built-in features like Machine Learning, Geospatial Analysis and Business Intelligence among others.
- BQ maximizes flexibility by separating data analysis and storage in different _compute engines_, thus allowing the customers to budget accordingly and reduce costs.
- This is for Analytical database and not for Transactional purpose. Alternative to OpenSource Apache Hive. Some alternatives to BigQuery from other cloud providers would be AWS Redshift or Azure Synapse Analytics.
- Built using BigTable + GCP Infrastructure
- BigQuery is Columnar storage. Cloud SQL databases are RECORD-based storage, meaning the entire record must be opened on disk even if you just selected a single column in your query.
- GoogleSQL, used by both BigQuery and Spanner uses 2011 ANSI SQL
- Avro, ORC, and Parquet files are all now supported for federated querying.
- Exabyte scale
- BQ managed Transfer Service allows to move data into BQ from SaaS services. You can schedule loades and automatically scale and access other data sources through various connectors.
- Datasets are collections of tables that can be divided along business lines or a given analytical domain. Each dataset is tied to a Google Cloud project.
- Identity and Access Management is used to grant permission to perform specific actions in BigQuery. This replaces the SQL GRANT and REVOKE statements that are used to manage access permissions in traditional SQL databases.
- Storage resources are allocated as you consume them and deallocated as you remove data or drop tables. Query resources are allocated according to query type and complexity. Each query uses some number of slots, which are units of computation that comprise a certain amount of CPU and RAM.
- Query using
  - Standard SQL
  - legacy SQL
- Schema auto-detection
  - Schema auto-detection enables BigQuery to infer the schema for CSV, JSON, or Google Sheets data. 
  - Schema auto-detection is available when you load data into BigQuery and when you query an external data source.
  - You don't need to enable schema auto-detection for Avro, Parquet, ORC, Firestore export, or Datastore export files. These file formats are self-describing, so BigQuery automatically infers the table schema from the source data. For Parquet, Avro, and Orc files, you can optionally provide an explicit schema to override the inferred schema.

## External Tables
- An external data source is a data source that you can query directly from BigQuery, even though the data is not stored in BigQuery storage. BigQuery has two different mechanisms for querying external data:

  - external tables: External tables are similar to standard BigQuery tables, in that these tables store their metadata and schema in BigQuery storage. However, their data resides in an external source. There are four kinds of external tables:
    - BigLake tables: BigLake tables let you query structured data in external data stores with access delegation. Access delegation decouples access to the BigLake table from access to the underlying data store. Because the service account handles retrieving data from the data store, you only have to grant users access to the BigLake table.
    - BigQuery Omni tables: With BigQuery Omni, you can run BigQuery analytics on data stored in Amazon Simple Storage Service (Amazon S3) or Azure Blob Storage using BigLake tables.
    - Object tables: Object tables let you analyze unstructured data in Cloud Storage. You can perform analysis with remote functions or perform inference by using BigQuery ML, and then join the results of these operations with the rest of your structured data in BigQuery. Like BigLake tables, object tables use access delegation, which decouples access to the object table from access to the Cloud Storage objects.
    - Non-BigLake external tables: Non-BigLake external tables let you query structured data in external data stores. To query a non-BigLake external table, you must have permissions to both the external table and the external data source. 
      - Bigtable
      - Cloud Storage: If you create a non-BigLake external table based on Cloud Storage, then you can use multiple external data sources, provided those data sources have the same schema. This isn't supported for non-BigLake external table based on Bigtable or Google Drive. You can use non-BigLake external tables with the following data stores:
      - Google Drive

  - federated queries: Federated queries let you send a query statement to AlloyDB, Spanner, or Cloud SQL databases and get the result back as a temporary table.  You use the EXTERNAL_QUERY function to send a query statement to the external database, using that database's SQL dialect.

![image](https://github.com/user-attachments/assets/e9c09763-a08b-49dc-8638-b74d4d06c6f2)

## External datasets
- In addition to BigQuery datasets, you can create external datasets (federated datasets), which are links to external data sources:
  - Spanner external dataset
  - AWS Glue federated dataset
- Once created, external datasets contain tables from a referenced external data source. Data from these tables aren't copied into BigQuery, but queried every time they are used.
- External datasets don't support table expiration, replicas, time travel, default collation, default rounding mode or the option to enable or disable case insensitive tables name.

- How to access BigQuery
  - Cloud Console
  - bq – command line tool
  - Client library - written in C#, Go, Java, Node.js, PHP, Python, and Ruby
- Data organization: `project.dataset.table`
- Support for AI/ML, GIS data
- Data Types
  - Avro is the preferred format for loading data into BigQuery. Compresed Avro files not supported but compressed Avro data blocks are supported. Parquet has better compression ratio and smaller files. For CSV and JSON, BQ can load uncompressed files significantly faster than compressed
  - Array Type
    - Arrays of arrays not allowed
    - Arrays of structs allowed
    - Declare as ARRAY<T>
  - Struct Type
    - Declare as STRUCT<T> eg. STRUCT<a int64, b string>
    - Structs can be directly compared using equality operators: =, != or <>, [NOT] IN
- Data Access Controls
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
- Query caching is based on exact string comparison. So even whitespaces can cause a cache miss. Queries are never cached if they exhibit non-deterministic behavior (for example, they use CURRENT_TIMESTAMP or RAND), if the table or view being queried has changed (even if the columns/rows of interest to the query are unchanged), if the table is associated with a streaming buffer (even if there are no new rows), if the query uses DML statements, or queries external data sources.
- You can recover a deleted table only if another table with the same ID in the dataset has not been created. In particular, this means you cannot recover a deleted table if it is being streamed to, chances are that the streaming pipeline would have already created an empty table and started pushing rows into it. using Create or Replace table because this makes the table irrecoverable.
- BigQuery supports user-defined functions or UDF. Java Script is currently the only external language supported. BigQuery can optimize the execution of SQL much better than it can for JavaScript.
  
```bash
# Get details
$ bq show --format=prettyjson dataset:tablename
```

Cross join: combines each row of the first dataset with each row of the second dataset, where every combination is represented in the output.
Inner join: requires that key values exist in both tables for the records to appear in the results table. Records appear in the merge only if there are matches in both tables for the key values.
Left join: Each row in the left table appears in the results, regardless of whether there are matches in the right table.
Right join: the reverse of a left join. Each row in the right table appears in the results, regardless of whether there are matches in the left table.

- BigQuery natively supports arrays. Array values must share a data type. Arrays are called REPEATED fields in BigQuery.
  - finding the number of elements with ARRAY_LENGTH(<array>)
  - deduplicating elements with ARRAY_AGG(DISTINCT <field>)
  - ordering elements with ARRAY_AGG(<field> ORDER BY <field>)
  - limiting ARRAY_AGG(<field> LIMIT 5)

- A STRUCT can have:
  - One or many fields in it
  - The same or different data types for each field
  - It's own alias
  - Structs are containers that can have multiple field names and data types nested inside. Arrays can be one of the field types inside of a Struct (as shown above with the splits field).

## Architecture

BigQuery is built on 4 infrastructure technologies.
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

## Best practices

Here's a list of [best practices for BigQuery](https://cloud.google.com/bigquery/docs/best-practices-performance-overview):

* Cost reduction
  * Avoid `SELECT *` . Reducing the amount of columns to display will drastically reduce the amount of processed data and lower costs.
  * Price your queries before running them.
  * Use clustered and/or partitioned tables if possible.
  * Use [streaming inserts](https://cloud.google.com/bigquery/streaming-data-into-bigquery) with caution. They can easily increase cost.
  * [Materialize query results](https://cloud.google.com/bigquery/docs/materialized-views-intro) in different stages.
* Query performance
  * Filter on partitioned columns.
  * [Denormalize data](https://cloud.google.com/blog/topics/developers-practitioners/bigquery-explained-working-joins-nested-repeated-data).
  * Use [nested or repeated columns](https://cloud.google.com/blog/topics/developers-practitioners/bigquery-explained-working-joins-nested-repeated-data).
  * Use external data sources appropiately. Constantly reading data from a bucket may incur in additional costs and has worse performance.
  * Reduce data before using a `JOIN`.
  * Do not threat `WITH` clauses as [prepared statements](https://www.wikiwand.com/en/Prepared_statement).
  * Avoid [oversharding tables](https://cloud.google.com/bigquery/docs/partitioned-tables#dt_partition_shard).
  * Avoid JavaScript user-defined functions.
  * Use [approximate aggregation functions](https://cloud.google.com/bigquery/docs/reference/standard-sql/approximate_aggregate_functions) rather than complete ones such as [HyperLogLog++](https://cloud.google.com/bigquery/docs/reference/standard-sql/hll_functions).
  * Order statements should be the last part of the query.
  * [Optimize join patterns](https://cloud.google.com/bigquery/docs/best-practices-performance-compute#optimize_your_join_patterns).
  * Place the table with the _largest_ number of rows first, followed by the table with the _fewest_ rows, and then place the remaining tables by decreasing size. This is due to how BigQuery works internally: the first table will be distributed evenly and the second table will be broadcasted to all the nodes.

## Pricing

BigQuery pricing is divided in 2 main components: processing and storage. There are also additional charges for other operations such as ingestion or extraction. The cost of storage is fixed and at the time of writing is US$0.02 per GB per month; you may check the current storage pricing [in this link](https://cloud.google.com/bigquery/pricing#storage).

Data processing has a [2-tier pricing model](https://cloud.google.com/bigquery/pricing#analysis_pricing_models):
- Bigquery On demand pricing (default): US$6.25 per TB per month; the first TB of the month is free.
- BigQuery Editions: The idea with big query editions is that the consumer doesn't need to have to figure out all their reservations and how many Flex jobs or Flex slots they would need and variable loads they can configure this all in their bigquery Edition as an autoscaling solution autoscaling up and autoscaling down and the customer consumes the slots as required but also controls the volume and velocity if you will of those slots being used.
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

![image](https://github.com/user-attachments/assets/31f8fe67-b64e-46cd-85de-55d659dd2386)


- BigQuery Autoscaler: Dynamically adjusts the capacity in response to planned or unplanned changes in demand to help ensure you pay only for what you use. Autoscaling is the core functionality available in a new
commercial model

  ![image](https://github.com/user-attachments/assets/96797479-f758-4493-861e-f0cc909e6291)

- Storage billing models
  - two dataset storage billing models:
    - Logical bytes
    - Physical bytes
  - When you create a dataset, the storage used by that dataset is billed to you using logical bytes as the default unit of consumption. However, you can choose to use physical bytes for billing instead. You can also change an existing dataset's storage billing model to use physical bytes.
  - When you set your storage billing model to use physical bytes, the total active storage costs you are billed for include the bytes used for time travel and fail-safe storage. You can configure the time travel window to balance storage costs with your data retention needs. For more information on forecasting your storage costs, see Forecast storage billing.
  - When you change a dataset's billing model, it takes 24 hours for the change to take effect.
  - Once you change a dataset's storage billing model, you must wait 14 days before you can change the storage billing model again.

- A rate limit limit or a quota it is a hard ceiling cost control but budgets are not a hard ceiling they are a guideline of how much money you are spending on variety of services
- The cost of a query is always assigned to the active project from where the query is executed.

- Difference between Uncompresses and Compressed storage pricing
  ![image](https://github.com/user-attachments/assets/53a3571e-af71-4c28-9a75-2eb052e6575d)

## Time Travel
-  time travel is a background copy of all your data in your tables in your data set for a rolling seven days
-  time travel lets you query data that was updated or deleted, restore a table that was deleted, or restore a table that expired. you cannot retrieve deleted table through the console you have to do that through the cloudshell `bq` command
-  You can set the duration of the time travel window, from a minimum of two days to a maximum of seven days.
-  You set the time travel window at the dataset level, which then applies to all of the tables within the dataset.
-  Using a shorter time travel window lets you save on storage costs when using the physical storage billing model. These savings don't apply when using the logical storage billing model.
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

# Analytics Hub - Data share solution
- Platform for secure data sharing with authorized users (internal and external)
- Construct of data providers, subscribers and data exchange, data discovery
- Built on top of BigQuery
- Data Sharing through Bigquery:
![image](https://github.com/user-attachments/assets/509b622e-de43-4461-88cc-f053a874f161)


## Partitioning and Clustering  

### Partitions 
  
- Table is divided into segments called partitions  
- [Partition tables](https://cloud.google.com/bigquery/docs/partitioned-tables) are very useful to improve performance and reduce costs, because BQ will not process as much data per query.
- You may partition a table by:
  - ***Time-unit column***: tables are partitioned based on a `TIMESTAMP`, `DATE`, or `DATETIME` column in the table. Special partitions: __NULL__ when nulls in partition column and __UNPARTITIONED__ when values in column outside allowed range
  - ***Ingestion time***: tables are partitioned based on the timestamp when BigQuery ingests the data. Creates pseudo-column _PARTITIONTIME 
  - ***Integer range***: tables are partitioned based on an integer column.
  - For Time-unit and Ingestion time columns, the partition may be daily (the default option), hourly, monthly or yearly.
  - BigQuery limits the amount of partitions to 4000 per table. If you need more partitions, consider clustering
  - Requiring partition filter using _partitioning_filter parameter and is specified at table level
- The _Details_ tab of the table will specify the field which was used for partitioning the table and its datatype.

Here's an example query for creating a partitioned table:

```sql
CREATE OR REPLACE TABLE taxi-rides-ny.nytaxi.yellow_tripdata_partitoned
PARTITION BY
  DATE(tpep_pickup_datetime) AS
SELECT * FROM taxi-rides-ny.nytaxi.external_yellow_tripdata;
```

  You may check the amount of rows of each partition in a partitioned table with a query such as this:

```sql
SELECT table_name, partition_id, total_rows
FROM `nytaxi.INFORMATION_SCHEMA.PARTITIONS`
WHERE table_name = 'yellow_tripdata_partitoned'
ORDER BY total_rows DESC;
```
  
This is useful to check if there are data imbalances and/or biases in your partitions.  
  
### Clustering 

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
- BigQuery supports clustering for both partitioned and non-partitioned tables. When you use clustering and partitioning together, the data can be partitioned by a date, date time or timestamp column, and then clustered on a different set of columns.
A partitioned table can also be clustered. Here's an example query for creating a partitioned and clustered table:

```sql
CREATE OR REPLACE TABLE taxi-rides-ny.nytaxi.yellow_tripdata_partitoned_clustered
PARTITION BY DATE(tpep_pickup_datetime)
CLUSTER BY VendorID AS
SELECT * FROM taxi-rides-ny.nytaxi.external_yellow_tripdata;
```

Just like for partitioned tables, the _Details_ tab for the table will also display the fields by which the table is clustered.

Here are 2 identical queries, one for a partitioned table and the other for a partitioned and clustered table:

```sql
SELECT count(*) as trips
FROM taxi-rides-ny.nytaxi.yellow_tripdata_partitoned
WHERE DATE(tpep_pickup_datetime) BETWEEN '2019-06-01' AND '2020-12-31'
  AND VendorID=1;
```
* Query to non-clustered, partitioned table.
* This will process about 1.1GB of data.

```sql
SELECT count(*) as trips
FROM taxi-rides-ny.nytaxi.yellow_tripdata_partitoned_clustered
WHERE DATE(tpep_pickup_datetime) BETWEEN '2019-06-01' AND '2020-12-31'
  AND VendorID=1;
```
* Query to partitioned and clustered data.
* This will process about 865MB of data.

### Partitioning vs Clustering

As mentioned before, you may combine both partitioning and clustering in a table, but there are important differences between both techniques that you need to be aware of in order to decide what to use for your specific scenario:

| Clustering | Partitioning |
|---|---|
| Cost benefit unknown. BQ cannot estimate the reduction in cost before running a query. | Cost known upfront. BQ can estimate the amount of data to be processed before running a query. |
| High granularity. Multiple criteria can be used to sort the table. | Low granularity. Only a single column can be used to partition the table. |
| Clusters are "fixed in place". | Partitions can be added, deleted, modified or even moved between storage options. |
| Benefits from queries that commonly use filters or aggregation against multiple particular columns. | Benefits when you filter or aggregate on a single column. |
| Unlimited amount of clusters; useful when the cardinality of the number of values in a column or group of columns is large. | Limited to 4000 partitions; cannot be used in columns with larger cardinality. |

You may choose clustering over partitioning when partitioning results in a small amount of data per partition, when partitioning would result in over 4000 partitions or if your mutation operations modify the majority of partitions in the table frequently (for example, writing to the table every few minutes and writing to most of the partitions each time rather than just a handful).

BigQuery has _automatic reclustering_: when new data is written to a table, it can be written to blocks that contain key ranges that overlap with the key ranges in previously written blocks, which weaken the sort property of the table. BQ will perform automatic reclustering in the background to restore the sort properties of the table.
* For partitioned tables, clustering is maintaned for data within the scope of each partition.
  
> Install bigquery api in notebook:  `! pip install google-cloud-bigquery==1.25.0 --use-feature=2020-resolver`  
  
  
## Streaming in Bigquery
- Streaming Inserts allows you to insert one item at a time into a table.
- New tables can be created from a temporary table that identifies the schema to be copied. The data enters a streaming buffer where it is held briefly until it can be inserted into the table.
- You can disable best effort de-duplication by not populating the insert ID field for each row inserted.
  ![image](https://github.com/user-attachments/assets/9483f15d-597a-4b54-b182-fb23722c24e4)


## ML in BigQuery
- High precision means a low false positive rate, meaning you really punish a model's precision if it makes a ton of bad guesses. Recall, on the other hand, is the ratio of correctly predicted positive observations to the all observations in actual class. Accuracy is simply true positives plus true negatives over the entire set of observations.
- 

![image](https://github.com/user-attachments/assets/caf50cf7-033d-4f11-bb99-79eb4a878170)


![image](https://github.com/user-attachments/assets/7c491018-23ce-475b-805c-adec6271cfab)

- For classification problems in ML, you want to minimize the False Positive Rate (predict that the user will return and purchase and they don't) and maximize the True Positive Rate (predict that the user will return and purchase and they do). This relationship is visualized with a ROC (Receiver Operating Characteristic) curve like the one shown here, where you try to maximize the area under the curve or AUC:
![image](https://github.com/user-attachments/assets/17e5af1c-cd1c-4b8a-9f82-bded16a42616)


## BI Engine
-  BI Engine can accelerate SQL queries from any source, including those written by data visualization tools, and can manage cached tables for on-going optimization.
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
    
  ![image](https://github.com/user-attachments/assets/bf22f8c1-97d1-4b36-b5ba-11016af5145c)

## Bigquery Notebooks
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

## BigQuery Data Transfer Service
- BigQuery Data Transfer Service automates data movement into BigQuery on a scheduled, managed basis.
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
