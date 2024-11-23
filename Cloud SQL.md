
# **Cloud SQL**  

  ![image](https://github.com/user-attachments/assets/5a094bab-96e0-4f42-be72-e64f9b4bf259)

- Fully managed Relational database services for MySQL, PostgreSQL & SQL Server. No maintenance & auto update. Generally used for storing Transactional database
- Regional Database with 99.95% SLA. Multiple zones for high availability and multi-region for backups only. 
- Storage up to 64 TB per instance
- Vertical Scale up to 60,000 IOPS & 624 GB Memory. Horizontal Scaling with only Read replicas – To transfer workload to other instance. If you need horizontal read-write scaling, consider Cloud Spanner. Google Cloud SQL supports three read replica scenarios: 
  - Cloud SQL instances replicating from a Cloud SQL primary instances
  - Cloud SQL instances replicating from an external primary instance
  - External MySQL instances replicating from a Cloud SQL primary instance.
- Data is encrypted with Google managed key or CMEK
- Back-up Database: On-demand Backup and Scheduled backup
- Cloud SQL is SSAE 16, ISO 27001, PCI DSS v3.0, and HIPAA compliant
- Database migration service (DMS)
  - migrate data from different SQL system to Cloud SQL
- Point-in Time Recovery
- Export data: gcloud utility or Cloud Console to SQL/CSV format
- To failover, the sql instance should not reside in single zone
- A Cloud SQL read replica is an exact copy of a primary Cloud SQL instance. Data and other changes on the primary instance are updated in almost real time on the read replica. You can manually increase the machine configuration of a Cloud SQL read replica after it is created. However, you cannot decrease the size of the read replica.
- As Cloud SQL MySQL exclusively relies on InnoDB for persistence, your on-premise MyISAM storage engine necessitates conversion during migration.
- Cloud SQL SQLServer supports up to 32,767 connections.
  
Its Structurured data, predefined schema, ACID transactions, strong consistency, used data structures – Tables, Indexes, views, constraints, partitions.

![image](https://user-images.githubusercontent.com/19702456/222904899-8cffc71a-1a33-4ccb-bb9d-591961e17af3.png)

- Cloud SQL Editions: Cloud SQL editions are only available for Cloud SQL for MySQL and Cloud SQL for PostgreSQL.
![image](https://github.com/user-attachments/assets/9c6fad54-6a48-488a-92fa-0188eced80e8)

  
- Limitations:
Its for regional data store with multiple zones for high availability. Multi – region for backups only. Upto 30TB per database. It is managed service. Using one of PostgreSQL, MySQL and SQL server. 



- Replication Options
  - Replication is the ability to create copies of a Cloud SQL instance or an on-premises database, and offload work to the copies. When referring to a Cloud SQL instance, the instance that is replicated is called the primary instance and the copies are called read replicas.
  - reason for using replication:
    - scale the use of data in a database without degrading performance
    - Migrating data between regions
    - Migrating data between platforms
    - Migrating data from an on-premises database to Cloud SQL
    - Additionally, a replica could be promoted if the original instance becomes corrupted.
  - Cloud SQL supports the following types of replicas:
    - Read replicas: You use a read replica to offload work from a Cloud SQL instance. The read replica is an exact copy of the primary instance. Read replicas are read-only; you cannot write to them. 
    - Cross-region read replicas: Cross-region replication lets you create a read replica in a different region from the primary instance.
    - Cross-region replicas:
      - Improve read performance by making replicas available closer to your application's region.
      - Provide additional disaster recovery capability to guard against a regional failure.
      - Let you migrate data from one region to another.
    - Cascading read replicas: Cascading replication lets you create a read replica under another read replica in the same or a different region.
      - The following scenarios are use cases for using cascading replicas: Disaster recovery, Performance improvements, Scale Reads, Cost reduction (You can reduce networking costs by using a single cascading replica with cross-region replication in other regions.)
    
![image](https://github.com/user-attachments/assets/7bfea9a2-a7e8-482a-befa-fcf58125542f)
  - A read replica is charged at the same rate as a standard Cloud SQL instance. There is no charge for the data replication. Pricing for a cross-region read replica is the same as for creating a new Cloud SQL instance in the region.


## Backup and restore
- Backups
  - Incremental disk-level snapshots
  - Automated and on-demand with a customizable retention period
  - Schedule on-demand backups with Cloud Scheduler
  - Default location is the closest Cloud Storage multiregional bucket. Custom locations available to make data residency compliance easier

- Restore
  - Restore to the same or a different Cloud SQL instance
  - Point-in-time recovery at a microsecond granularity, up to 7 days.

## Connecting to a Cloud SQL instance
  
  ![image](https://github.com/user-attachments/assets/bb8291eb-37e6-4458-b12b-256789882d52)
  
## High availability (HA)
- 99.95% Uptime SLA for HA instances. During an incident in Zone A, Cloud SQL automatically fails over to the standby in Zone B
- Synchronous replication with Regional Persistent Disk offers zero data loss.
- High-availability-configured instance is charged at double the price of a standalone instance (this includes CPU, RAM, and storage)
- HA instance components:
  - Primary and standby instances
  - Health checking agents
  - Regional persistent disk

      ![image](https://github.com/user-attachments/assets/d7e7cfc7-17a3-4fd9-8d79-720097b468d3)

## Query insights
- Query insights helps you detect, diagnose, and prevent query performance problems for Cloud SQL databases. 
- With Query insights, you can monitor performance at an application level and trace the source of a problematic query across the application stack by model, view, controller, route, user, and host.
- The Query insights tool can integrate with your existing application monitoring (APM) tools and Google Cloud services by using open standards and APIs. 
- There is no additional cost for Query Insights
- Metrics available through the console, gcloud commands and REST API

## Cloud SQL Studio







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
