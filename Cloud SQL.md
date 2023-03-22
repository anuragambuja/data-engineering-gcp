
# **Cloud SQL**  
- Fully managed Relational database services for MySQL, PostgreSQL & SQL Server. No maintenance & auto update. Generally used for storing Transactional database
- Regional Database with 99.95% SLA. Multiple zones for high availability and multi-region for backups only. 
- Storage up to 30 TB
- Vertical Scale up to 96 core & 416 GB Memory. Horizontal Scaling with only Read replicas – To transfer workload to other instance. If you need horizontal read-write scaling, consider Cloud Spanner. Google Cloud SQL supports three read replica scenarios: 
  - Cloud SQL instances replicating from a Cloud SQL primary instances
  - Cloud SQL instances replicating from an external primary instance
  - External MySQL instances replicating from a Cloud SQL primary instance.
- Data is encrypted with Google managed key or CMEK
- Back-up Database: On-demand Backup and Scheduled backup
- Database migration service (DMS)
  - migrate data from different SQL system to Cloud SQL
- Point-in Time Recovery
- Export data: gcloud utility or Cloud Console to SQL/CSV format
- To failover, the sql instance should not reside in single zone

Its Structurured data, predefined schema, ACID transactions, strong consistency, used data structures – Tables, Indexes, views, constraints, partitions.

![image](https://user-images.githubusercontent.com/19702456/222904899-8cffc71a-1a33-4ccb-bb9d-591961e17af3.png)


Limitations:
Its for regional data store with multiple zones for high availability. Multi – region for backups only. Upto 30TB per database. It is managed service. Using one of PostgreSQL, MySQL and SQL server. 


### **Connect to MySQL instance**

```bash
# 1. Using cloud shell
$ gcloud sql connect <sql-instance-name> --user=username --quiet
```

```bash
# 2. using external agent after whitelisting the ip

# get the external ip
$ curl 'https://api.ipify.org?format=json' 

# Add the external ip address under instance's connections > add network to whitelist the ip

# connect to mysql instance
$ mysql -h <white-listed-ip> -u <username> -p
```

```bash
# 3. Using Cloud SQL Auth Proxy - recommended way as it provides easier connection authorization

# 1. Download and install the Cloud SQL Auth proxy.
# 2. Run cloud-sql-proxy. Get the CONNECTIOn_NAME from instance's Overview.
$ ./cloud_sql_proxy -instance=<INSTANCE_CONNECTION_NAME>=tcp:5432

```
![image](https://user-images.githubusercontent.com/19702456/224492626-a92ca471-f5ef-4c4c-aee4-e47b4781da8a.png)

Source: https://cloud.google.com/sql/docs/mysql/sql-proxy


### **Data Migration to Cloud SQL**

```bash
# 1. Get the database dump
$ mysqldump -u root -p database-name > backup.sql

# 2. Upload the backup.sql to cloud storage and provide location under Overview > Import
```
