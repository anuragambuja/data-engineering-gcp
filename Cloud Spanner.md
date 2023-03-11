
# Cloud Spanner
- Distributed, Horizontally Scalable (Petabyte scale) and Fully managed solution for RDBMS in GCP.
- Use when Data volume > 2 TB. Upto 2 TB per node
- Costlier than Cloud SQL
- Cloud SQL has just Read replicas, where as in cloud spanner horizontal read/write across region
- Data is strongly typed.
  - Must define schema database
  - Datatype for each column of each table must be defined.
- 99.999% availability 
- Regional/ Multi-region level instance can be created
- Data export
  - can not export with gcloud
  - Cloud Console or Cloud Dataflow Job

### Hot Spotting
- Hot spots occur when many read and write operations happen on the same node
- Can happen with sequential primary keys
  - Auto-increment values
  - Timestamps
- Consider using 
  - hash value of primary
  - Bit-reverse sequential values
  - Promote high cardinality attributes in multi-attribute primary key

### Interleaved Tables
- Parent-Child relationship
  - Order to order line 
  - Person to addresses
- Row from parent table stored with rows from child table
- More efficient when retriving data from both

### Cloud SQL v/s Cloud Spanner

![image](https://user-images.githubusercontent.com/19702456/224495479-ff046073-a3f8-4edb-b0a4-3d779607e0e0.png)

