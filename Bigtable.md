# Bigtable

  ![image](https://github.com/user-attachments/assets/0a51b2a5-7fa5-487b-a4a4-0cdf9ed31f77)


- Cloud Bigtable stores data in massively scalable tables, each of which is a sorted key/value map. Each row is indexed by a single row key, and columns that are related to one another are typically grouped together into a column family. Each column is identified by a combination of the column family and a column qualifier, which is a unique name within the column family. Cloud Bigtable tables are sparse; if a cell does not contain any data, it does not take up any space. Columns can be unused in a row.

- Fully managed but Not serverless (you need to start cluster with provided number of nodes, region, or SSD/HDDD)
- Wide column NOSQL database. Better to store data in one table than many. Small tables are problematic since querying multiple tables increases connection overhead and latency and is more difficult to load balance. 
- Scale horizontally with Multiple Nodes
- Strongly consistent in a single cluster; replication adds eventual consistency across two to four clusters. Eventual consistency is a consistency model used in distributed computing to achieve high availability that informally guarantees that, if no new updates are made to a given data item, eventually all accesses to that item will return the last updated value. Strong consistency means data will get passed on to all the replicas as soon as a write request comes to one of the replicas of the database.
- Data stored at column wise. Columns are grouped into column family. Empty columns do not take any space.
- Bigtable also provides Column Families. By accessing the Column Family, you can pull some of the data you need without pulling all of the data from the row or having to search for it and assemble it. Bigtable can handle up to 100 column families without losing performance.
- Consistent sub-10ms latency
- Handles millions of request per second.
- Learns and adjusts to access patterns.
- Ideal for Ad Tech, Fintech, and IoT. y. It’s also a great storage engine for machine learning applications. 
- Easy integration with open source big data tools like HBase
- Integrates with big data tools like Hadoop, Dataflow, and Dataproc.
- Throughput scales linearly: Increase QPS (queries per second) by adding Cloud Bigtable nodes
- Seamless cluster resizing: Dynamically add and remove Cloud Bigtable cluster nodes without restarting
- Support 1-node production instances
- Bigtable is ideal for applications that need very high throughput and scalability for non-structured key/value data, where each value is typically no larger than 10 MB. Bigtable is not well suited for highly structured data, transactional data, small data volumes less than 1 TB, and anything requiring SQL Queries and SQL-like joins.

  ![image](https://github.com/user-attachments/assets/eef740ec-786a-493c-a8a0-fb7a6d072003)

- BigTable does not support security restrictions on Row-level or, Column-level or, Cell-level 
- Storage Model
  ![image](https://github.com/user-attachments/assets/d15e03af-0522-43b3-839a-440205b5e8f9)

  - Characteristics
    - Only one index (row-key)
    - Atomic single-row transactions
    - Empty cells take no space
    - All values in a single row
      - Recommended limit 100 MB
      - Hard limit 256 MB
  - Compression
    - Data is compressed
    - Not configurable
  - Compactions
    - Periodically rewrites data
    - Not Configurable
    - Mutations and deletions take up extra storage space until compaction
      
- How to access
  - cbt – command line (part of cloud sdk)

    ```bash
    $ cat .cbtrc
    project = proven-audio-376216
    instance = bigtable-1

    $ cbt createtable emp
    $ cbt ls
    $ cbt ls emp
    $ cbt createfamily emp professional_data_cf
    $ cbt set emp J1 personal_data_cf:name=john
    $ cbt read emp
    $ cbt count emp
    $ cbt help
    ```
  - Hbase API

- No Multi column index. Only Row key based indexing. There are no alternate indexes or secondary indexes. 
And when data is entered, it is organized lexicographically by the Row Key. Row Keys are analogous to a primary key in relational databases. Bigtable does not support joins, so no concept of foreign keys. Row keys determine where data is written. 
    
    ![image](https://user-images.githubusercontent.com/19702456/227278313-b483add6-6cc5-451c-a8c4-f219286116df.png)

- Bigtable stores data in a file system called Colossus. Colossus also contains data structures called Tablets that are used to identify and manage the data. And metadata about the Tablets is what is stored on the VMs in the Bigtable cluster itself.
  ![image](https://github.com/user-attachments/assets/ece04843-5896-4bcd-82eb-d328bd1cab9f)


- Bigtable writes data to multiple servers (nodes) which handles a subset of workload. Within nodes there are multiple sorted-string tables(SSTables). Data is sharded into blocks of continuous rows, called tablets. Tablets are similar to HBase regions. Tablets are stored in Colossus file system. So, metadata is stored on node and data is stored in Colossus. An SSTable provides a persistent, ordered immutable map from keys to values, where both keys and values are arbitrary byte strings.
  
    ![image](https://user-images.githubusercontent.com/19702456/224545732-62e08dd3-da7b-4f24-8fb2-436fbc54fa19.png)
       
- Bigtable is a learning system. It detects hot stops, where a lot of activity is going through a single tablet and splits the tablet in two. It can also re-balance the processing by moving the pointer to a tablet to a different VM in the cluster. 

- When a node is lost in the cluster, no data is lost, and recovery is fast because only the metadata needs to be copied to the replacement node.
- Bigtable limits you to 1000 tables per instance. Avoid creating many small tables as it Increases backend connection overhead and Disrupt the load balancing
  
- When you delete data, the row is marked for deletion and skipped during subsequent processing. It is not immediately removed. If you make a change to data, the new row is upended sequentially to the end of the table, and the previous version is marked for deletion. So both rows exist for a period of time. Periodically, Bigtable compacts the table, removing rows marked for deletion and reorganizing the data for read and write efficiency.
 ![image](https://github.com/user-attachments/assets/5bc8e2e6-4fc3-4753-b60e-64801a27933d)
      
- Optimizing BIgtable Performance:
  - It's essential to design a schema that allows reads and writes to be evenly distributed across the Bigtable cluster. Otherwise individual nodes can get overloaded, slowing performance.
  - The workload isn't appropriate for Bigtable. If you are testing with a small amount, less than 300 gigabytes of data, or for a very short period of time, seconds rather than minutes or hours, Bigtable won't be able to properly optimize your data.
  - The Bigtable cluster doesn't have enough nodes. Adding more nodes can therefore improve performance.
  - Bigtable takes time to process cells within a row, so if there are fewer cells within a row, it will generally provide better performance than more cells.
  - Replication for Bigtable enables you to increase the availability and durability of your data by copying it across multiple regions or multiple zones within the same region. If a Bigtable cluster becomes unresponsive, replication makes it possible for incoming traffic to failover to another cluster in the same instance.
  
- Design Row key by keeping in your mind
  - Avoid using monotonically increasing key to avoid Hot spotting
  - Avoid low cardinality attributes
  - Better design option: concatenate multiple attributes. Start with high cardinality attributes eg. IoT sensor ID, then add time such as date and hour i.e. low cardinality attributes near the end of the key. eg. sensor ID + reverse datetime: 12345 + (00|23|21|08|2023). By reversing the timestamp, you can design a row key where the most recent event appears at the start of the table instead of the end.

    ![image](https://user-images.githubusercontent.com/19702456/227277588-4a0d8fe4-fa0f-44d2-abce-5858958ce5cd.png)
- Used for
  - Time-series data, such as CPU and memory usage over time for multiple servers.
  - Marketing data, such as purchase histories and customer preferences.
  - Financial data, such as transaction histories, stock prices, and currency exchange rates.
  - Internet of Things data, such as usage reports from energy meters and home appliances.
  - Graph data, such as information about how users are connected to one another.

- Throughput scales linearly to thousands of nodesy, so for every single node that you do add, you're going to see a linear scale of throughput performance, up to hundreds of nodes. 
- The Cloud Bigtable cluster uses HDD disks. Using HDD disks instead of SSD disks means slower response times and a significantly lower cap on the number of read requests handled per second (500 QPS for HDD disks vs. 10,000 QPS for SSD disks). 

    
## Key Visualizer
- Key Visualizer is a tool that helps you analyze your Bigtable usage patterns. It generates visual reports for your tables that break down your usage based on the row keys that you access. The core of a Key Visualizer scan is the heat map, which shows the value of a metric over time broken down into contiguous ranges of row keys. The X-axis of the heat map represents time, and the Y-axis represents row keys. If the metric has a low value for a group of row keys at a point in time, the metric is cold, and it appears in a dark color. A high value is hot, and it appears in a bright color. The highest values appear in white. Key Visualizer automatically generates hourly and daily scans for every table in your instance that meets at least one of the following criteria:
  - During the previous 24 hours, the table contained at least 30 gigabytes of data at some point in time.
  - During the previous 24 hours, the average of all reads or all writes was at least 10,000 rows per second.

- Key Visualizer divides all of the row keys into 1,000 contiguous ranges, with roughly the same number of row keys in each range. These ranges are known as key buckets. Key Visualizer reports most metrics as averages over each key bucket, or as maximum values within each key bucket.

- Uses for Key Visualizer include the following:
  - Iteratively designing a schema or improving the design of an existing schema. In each iteration, you check Key Visualizer to spot problems your schema may be causing, then tweak your schema and check again.
  - Troubleshooting performance issues.
  - Getting a better understanding of how you access the data that you store in Bigtable.

- To accomplish these goals, Key Visualizer can help you complete the following tasks:
  - Check whether your reads or writes are creating hotspots on specific rows
  - Find rows that contain too much data
  - Look at whether your access patterns are balanced across all of the rows in a table

- Key Visualizer data is available for the last 14 days. This limit also means that if you bookmark or share the URL for a Key Visualizer scan, the URL has a maximum life of 14 days.

## Row keys
- The most efficient Bigtable queries retrieve data using one of the following:
  - Row key
  - Row key prefix
  - Range of rows defined by starting and ending row keys 
- A row key must be 4 KB or less
- Store multiple delimited values in each row key. Row key segments are usually separated by a delimiter, such as a colon, slash, or hash symbol.
- Design to retrieve a well-defined range of rows. Well-planned row key prefixes let you take advantage of Bigtable's built-in sorting order to store related data in contiguous rows. Bigtable stores data lexicographically. Pad the integers with leading zeroes
- Examples to avoid
  - Standard, non-reversed domain names: services.company.com will be in separate range than product.company.com instead reverse → com.company.product
  - Sequential numeric IDs For example, UserID – New users might be more active than older ones (hotspotting on one node)
  - Non-defined range of rows. For example, monitoring performance metrics of machines: 1425330757685#machine_42234 No way to select a machine and get performance metrics --> instead reverse
  - Hashed-values: No longer recommended as debugging becomes difficult with non-readable keys

## Application Profiles
- If an instance uses replication, you use application profiles to specify routing policies. Application profile routing policies let you control which clusters handle incoming requests from your applications.
- Differnet Routing Policies:
  - Single-cluster routing: Sends all requests to a single cluster.
  - Multi-cluster routing to any cluster: Sends requests to the nearest available cluster in an instance.
  - Cluster group routing: Sends requests to the nearest available cluster within a selected group of clusters in an instance.
- Application profiles also determine whether you can perform single-row transactions, which include read-modify-write operations (including increments and appends) and check-and-mutate operations (also known as conditional mutations or conditional writes).


## Bigtable Studio
- 


