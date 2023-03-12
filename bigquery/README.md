# Bigquery

- Serverless Data warehouse solution in GCP just like Relational database – SQL schema. 
- This is for Analytical database and not for Transactional purpose. Alternative to OpenSource Apache Hive
- Built using BigTable + GCP Infrastructure
- BigQuery is Columnar storage
- Exabyte scale
- Query using
  - Standard SQL
  - legacy SQL
- Big Query can query from external data source.
- Cloud storage, SQL, Big Table
- Biquery can load data from various sources - CSV, JSONL, Avro, SQL and many more
- Query costs around $5 for 1 TB of data scanned
- How to access BigQuery
  - Cloud Console
  - bq – command line tool
  - Client library - written in C#, Go, Java, Node.js, PHP, Python, and Ruby
- Data organization: `project.dataset.table`
- Pricing
  - On-Demand
  - Flat rate pricing
- Support for AI/ML, GIS data


### BigQuery Architecture

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


