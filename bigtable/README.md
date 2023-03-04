Bigtable is ideal for applications that need very high throughput and scalability for nonstructured key value data, where each value is typically no larger than 10 Megabytes. Bigtable is not well suited for highly structured data, transactional data, small data volumes less than one terabyte, and anything requiring SQL queries and SQL-like joins.

![image](https://user-images.githubusercontent.com/19702456/222904488-52c75876-f9b1-402e-8d65-7c4c9b821ed3.png)

Bigtable stores data in a file system called Colossus. Colossus also contains data structures called tablets that are used to identify and manage the data. Metadata about the tablets is what is stored on the VMs in the Bigtable cluster itself. It can manipulate the actual data. It can manipulate the tablets that point to and describe the data, or it can manipulate the metadata that points to the tablets. 


![image](https://user-images.githubusercontent.com/19702456/222904496-438c5b00-d715-479d-ac8e-8e947be572b6.png)


![image](https://user-images.githubusercontent.com/19702456/222904500-83640ae8-4079-4f13-b246-9fb453099459.png)


Bigtable is a learning system. It detects hot stops, where a lot of activity is going through a single tablet and splits the tablet in two. It can also re-balance the processing by moving the pointer to a tablet to a different VM in the cluster. When a node is lost in the cluster, no data is lost, and recovery is fast because only the metadata needs to be copied to the replacement node. Bigtable stores the actual data elements in tables, and to begin with, it is just a table with rows and columns. However, unlike other table-based data systems like spreadsheets and SQL databases, Bigtable has only one index. That index is called the row key. When data is entered, it is organized lexicographically by the row key. 

![image](https://user-images.githubusercontent.com/19702456/222904515-44c164d0-ed5f-43cc-9051-0ac217e9c100.png)


When you delete data, the row is marked for deletion and skipped during subsequent processing. It is not immediately removed. If you make a change to data, the new row is upended sequentially to the end of the table, and the previous version is marked for deletion. So both rows exist for a period of time. Periodically, Bigtable compacts the table, removing rows marked for deletion and reorganizing the data for read and write efficiency. Bigtable can handle up to 100 column families without losing performance, and it is much more efficient to retrieve data from one or more column families than retrieving all of the data in a row.

![image](https://user-images.githubusercontent.com/19702456/222904522-1fbde117-0bb4-473b-a9ba-b473b682a6f2.png)

Bigtable takes time to process cells within a row, so if there are fewer cells within a row, it will generally provide better performance than more cells. The goal when optimizing for streaming is to avoid creating hot spots when writing, which would cause Bigtable to have to split tablets and adjust loads. Replication for Bigtable enables you to increase the availability and durability of your data by copying it across multiple regions or multiple zones within the same region. You can also isolate workloads by routing different types of requests to different clusters. If a Bigtable cluster becomes unresponsive, replication makes it possible for incoming traffic to failover to another cluster in the same instance.
Key Visualizer is a tool that helps you analyze your Bigtable usage patterns. It generates visual reports for your tables that break down your usage based on the row keys that you access. Key Visualizer automatically generates hourly and daily scans for every table in your instance that meets at least one of the following criteria: During the previous 24 hours, the table contained at least 30 gigabytes of data at some point in time. During the previous 24 hours, the average of all reads or all writes was at least 10,000 rows per second.

![image](https://user-images.githubusercontent.com/19702456/222904535-3d806f04-ec45-427c-9d5d-5cc131564e9f.png)


![image](https://user-images.githubusercontent.com/19702456/222904540-f638fe3e-6243-4813-96d4-0db1da21467a.png)




