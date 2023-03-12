# Bigtable

- Fully managed but Not serverless (you need to start cluster with provided number of nodes, region, or SSD/HDDD)
- Wide column NOSQL database. Better to store data in one table than many. Small tables are problematic since querying multiple tables increases connection overhead and latency and is more difficult to load balance. 
- Scale horizontally with Multiple Nodes
- Data stored at column wise. Columns are grouped into column family
- Milli second latency
- Handles millions of request per second
- How to access
  - cbt – command line (part of cloud sdk)
  - Hbase API
- No Multi column index. Only Row key based indexing. Row Keys are analogous to a primary key in relational databases. Bigtable does not support joins, so no concept of foreign keys. Row keys determine where data is written. 
  - Bigtable writes data to multiple servers (nodes) which handles a subset of workload. Within nodes there are multiple sorted-string tables(SSTables). Data is sharded into blocks of continuous rows, called tablets. Tablets are stored in Colossus file system. So, metadata is stored on node and data is stored in Colossus. 
       ![image](https://user-images.githubusercontent.com/19702456/224545732-62e08dd3-da7b-4f24-8fb2-436fbc54fa19.png)
  - Design Row key by keeping in your mind
    - Avoid using monotonically increasing key to avoid Hot spotting
    - Avoid low cardinality attributes
    - Better design option: concatenate multiple attributes. Start with high cardinality attributes eg. IoT sensor ID, then add time such as date and hour i.e. low cardinality attributes near the end of the key. eg. sensor ID + reverse datetime: 12345 + (00|23|21|08|2023)
  - Empty columns do not take any space
- Used for
  - Financial data
  - Time series Data eg. IoT

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
