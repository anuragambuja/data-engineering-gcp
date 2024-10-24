# Bigtable

- Fully managed but Not serverless (you need to start cluster with provided number of nodes, region, or SSD/HDDD)
- Wide column NOSQL database. Better to store data in one table than many. Small tables are problematic since querying multiple tables increases connection overhead and latency and is more difficult to load balance. 
- Scale horizontally with Multiple Nodes
- Data stored at column wise. Columns are grouped into column family. Empty columns do not take any space.
- Bigtable also provides Column Families. By accessing the Column Family, you can pull some of the data you need without pulling all of the data from the row or having to search for it and assemble it. Bigtable can handle up to 100 column families without losing performance.
- Consistent sub-10ms latency
- Handles millions of request per second.
- Learns and adjusts to access patterns.
- Ideal for Ad Tech, Fintech, and IoT
- Easy integration with open source big data tools like HBase
- Throughput scales linearly: Increase QPS (queries per second) by adding Cloud Bigtable nodes
- Seamless cluster resizing: Dynamically add and remove Cloud Bigtable cluster nodes without restarting
- Support 1-node production instances
- Bigtable is ideal for applications that need very high throughput and scalability for non-structured key/value data, where each value is typically no larger than 10 MB. Bigtable is not well suited for highly structured data, transactional data, small data volumes less than 1 TB, and anything requiring SQL Queries and SQL-like joins.

  ![image](https://github.com/user-attachments/assets/eef740ec-786a-493c-a8a0-fb7a6d072003)

- Storage Model
  ![image](https://github.com/user-attachments/assets/d15e03af-0522-43b3-839a-440205b5e8f9)

  - Characteristics
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


- Bigtable writes data to multiple servers (nodes) which handles a subset of workload. Within nodes there are multiple sorted-string tables(SSTables). Data is sharded into blocks of continuous rows, called tablets. Tablets are stored in Colossus file system. So, metadata is stored on node and data is stored in Colossus.
  
    ![image](https://user-images.githubusercontent.com/19702456/224545732-62e08dd3-da7b-4f24-8fb2-436fbc54fa19.png)
       
- Bigtable is a learning system. It detects hot stops, where a lot of activity is going through a single tablet and splits the tablet in two. It can also re-balance the processing by moving the pointer to a tablet to a different VM in the cluster. 

- When a node is lost in the cluster, no data is lost, and recovery is fast because only the metadata needs to be copied to the replacement node.

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
    
- Key Visualizer is a tool that helps you analyze your Bigtable usage patterns. It generates visual reports for your tables that break down your usage based on the row keys that you access. The core of a Key Visualizer scan is the heat map, which shows the value of a metric over time broken down into contiguous ranges of row keys. The X-axis of the heat map represents time, and the Y-axis represents row keys. If the metric has a low value for a group of row keys at a point in time, the metric is cold, and it appears in a dark color. A high value is hot, and it appears in a bright color. The highest values appear in white. Key Visualizer automatically generates hourly and daily scans for every table in your instance that meets at least one of the following criteria:
  - During the previous 24 hours, the table contained at least 30 gigabytes of data at some point in time.
  - During the previous 24 hours, the average of all reads or all writes was at least 10,000 rows per second.

- Used for
  - Financial data
  - Time series Data eg. IoT


