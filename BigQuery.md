
# BigQuery

- Data warehouse solution in GCP just like Relational database – SQL schema. 
- BQ is ***serverless***. There are no servers to manage or database software to install; this is managed by Google and it's transparent to the customers.
- BQ is ***scalable*** and has ***high availability***. Google takes care of the underlying software and infrastructure.
- BQ has built-in features like Machine Learning, Geospatial Analysis and Business Intelligence among others.
- BQ maximizes flexibility by separating data analysis and storage in different _compute engines_, thus allowing the customers to budget accordingly and reduce costs.
- This is for Analytical database and not for Transactional purpose. Alternative to OpenSource Apache Hive. Some alternatives to BigQuery from other cloud providers would be AWS Redshift or Azure Synapse Analytics.
- Built using BigTable + GCP Infrastructure
- BigQuery is Columnar storage
- Exabyte scale
- BQ managed Transfer Service allows to move data into BQ from SaaS services. You can schedule loades and automatically scale and access other data sources through various connectors.
- Query using
  - Standard SQL
  - legacy SQL
- Big Query can query from external data source.
  - Cloud storage, SQL, Big Table
- Biquery can load data from various sources - CSV, JSONL, Avro, SQL and many more
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
-  On demand pricing (default): US$5 per TB per month; the first TB of the month is free.
-  Flat rate pricing: based on the number of pre-requested _slots_ (virtual CPUs).
   -  A minimum of 100 slots is required for the flat-rate pricing which costs US$2,000 per month.
   -  Queries take up slots. If you're running multiple queries and run out of slots, the additional queries must wait until other queries finish in order to free up the slot. On demand pricing does not have this issue.
   -  The flat-rate pricing only makes sense when processing more than 400TB of data per month.
- The cost of a query is always assigned to the active project from where the query is executed.
  
When running queries on BQ, the top-right corner of the window will display an approximation of the size of the data that will be processed by the query. Once the query has run, the actual amount of processed data will appear in the _Query results_ panel in the lower half of the window. This can be useful to quickly calculate the cost of the query.
  
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
  
  
  
  
  
  
  
