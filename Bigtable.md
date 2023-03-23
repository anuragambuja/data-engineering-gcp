# Bigtable

- Fully managed but Not serverless (you need to start cluster with provided number of nodes, region, or SSD/HDDD)
- Wide column NOSQL database. Better to store data in one table than many. Small tables are problematic since querying multiple tables increases connection overhead and latency and is more difficult to load balance. 
- Scale horizontally with Multiple Nodes
- Data stored at column wise. Columns are grouped into column family. Empty columns do not take any space.
- Milli second latency.
- Handles millions of request per second.
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

- No Multi column index. Only Row key based indexing. Row Keys are analogous to a primary key in relational databases. Bigtable does not support joins, so no concept of foreign keys. Row keys determine where data is written. 
    
    ![image](https://user-images.githubusercontent.com/19702456/227278313-b483add6-6cc5-451c-a8c4-f219286116df.png)

- Bigtable writes data to multiple servers (nodes) which handles a subset of workload. Within nodes there are multiple sorted-string tables(SSTables). Data is sharded into blocks of continuous rows, called tablets. Tablets are stored in Colossus file system. So, metadata is stored on node and data is stored in Colossus.
  
    ![image](https://user-images.githubusercontent.com/19702456/224545732-62e08dd3-da7b-4f24-8fb2-436fbc54fa19.png)
       
- Bigtable is a learning system. It detects hot stops, where a lot of activity is going through a single tablet and splits the tablet in two. It can also re-balance the processing by moving the pointer to a tablet to a different VM in the cluster. 

- When a node is lost in the cluster, no data is lost, and recovery is fast because only the metadata needs to be copied to the replacement node.

- When you delete data, the row is marked for deletion and skipped during subsequent processing. It is not immediately removed. If you make a change to data, the new row is upended sequentially to the end of the table, and the previous version is marked for deletion. So both rows exist for a period of time. Periodically, Bigtable compacts the table, removing rows marked for deletion and reorganizing the data for read and write efficiency.       

- Design Row key by keeping in your mind
  - Avoid using monotonically increasing key to avoid Hot spotting
  - Avoid low cardinality attributes
  - Better design option: concatenate multiple attributes. Start with high cardinality attributes eg. IoT sensor ID, then add time such as date and hour i.e. low cardinality attributes near the end of the key. eg. sensor ID + reverse datetime: 12345 + (00|23|21|08|2023)

    ![image](https://user-images.githubusercontent.com/19702456/227277588-4a0d8fe4-fa0f-44d2-abce-5858958ce5cd.png)
    
- Key Visualizer is a tool that helps you analyze your Bigtable usage patterns. It generates visual reports for your tables that break down your usage based on the row keys that you access. Key Visualizer automatically generates hourly and daily scans for every table in your instance that meets at least one of the following criteria: During the previous 24 hours, the table contained at least 30 gigabytes of data at some point in time. During the previous 24 hours, the average of all reads or all writes was at least 10,000 rows per second.

- Used for
  - Financial data
  - Time series Data eg. IoT


