# Cloud SQL  

  ![image](https://github.com/user-attachments/assets/5a094bab-96e0-4f42-be72-e64f9b4bf259)

- Fully managed Relational database services for MySQL, PostgreSQL & SQL Server. No maintenance & auto update. Generally used for storing Transactional database
- Regional Database with 99.95% SLA. Multiple zones for high availability and multi-region for backups only. 
- Storage up to 64 TB per instance
- Vertical Scale up to 60,000 IOPS & 624 GB Memory. Horizontal Scaling with only Read replicas – To transfer workload to other instance. If you need horizontal read-write scaling, consider Cloud Spanner.
- Data is encrypted with Google managed key or CMEK
- Back-up Database: On-demand Backup and Scheduled backup
- Cloud SQL is SSAE 16, ISO 27001, PCI DSS v3.0, and HIPAA compliant
- Its Structurured data, predefined schema, ACID transactions, strong consistency, used data structures – Tables, Indexes, views, constraints, partitions.
- To failover, the sql instance should not reside in single zone
- A Cloud SQL read replica is an exact copy of a primary Cloud SQL instance. Data and other changes on the primary instance are updated in almost real time on the read replica. You can manually increase the machine configuration of a Cloud SQL read replica after it is created. However, you cannot decrease the size of the read replica.
- Point-in Time Recovery
- Export data: gcloud utility or Cloud Console to SQL/CSV format  
- As Cloud SQL MySQL exclusively relies on InnoDB for persistence, your on-premise MyISAM storage engine necessitates conversion during migration.
- Cloud SQL SQLServer supports up to 32,767 connections.


> ## Cloud SQL Editions
- Cloud SQL editions are only available for Cloud SQL for MySQL and Cloud SQL for PostgreSQL.

  ![image](https://github.com/user-attachments/assets/9c6fad54-6a48-488a-92fa-0188eced80e8)


> ## Replication Options
  - Replication is the ability to create copies of a Cloud SQL instance or an on-premises database, and offload work to the copies. When referring to a Cloud SQL instance, the instance that is replicated is called the primary instance and the copies are called read replicas.
  - A read replica is charged at the same rate as a standard Cloud SQL instance. There is no charge for the data replication. Pricing for a cross-region read replica is the same as for creating a new Cloud SQL instance in the region.
  - Reasons for using replication:
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


> ## High availability (HA)
- 99.95% Uptime SLA for HA instances. During an incident in Zone A, Cloud SQL automatically fails over to the standby in Zone B
- Synchronous replication with Regional Persistent Disk offers zero data loss.
- High-availability-configured instance is charged at double the price of a standalone instance (this includes CPU, RAM, and storage)
- HA instance components:
  - Primary and standby instances
  - Health checking agents
  - Regional persistent disk

      ![image](https://github.com/user-attachments/assets/d7e7cfc7-17a3-4fd9-8d79-720097b468d3)

    
> ## Backup and restore
- Backups
  - Incremental disk-level snapshots
  - Automated and on-demand with a customizable retention period
  - Schedule on-demand backups with Cloud Scheduler
  - Default location is the closest Cloud Storage multiregional bucket. Custom locations available to make data residency compliance easier

- Restore
  - Restore to the same or a different Cloud SQL instance
  - Point-in-time recovery at a microsecond granularity, up to 7 days.


> ## Connecting to a Cloud SQL instance
- If your are connecting an application that is hosted within the same Google Cloud project as your Cloud SQL instance, and it is collocated in the same region, choosing the Private IP connection will provide you with the most performant and secure connection using private connectivity. In other words, traffic is never exposed to the public internet.
- If the application is hosted in another region or project, or if you are trying to connect to your Cloud SQL instance from outside of Google Cloud, you have 3 options.
  - In this case, we recommend using Cloud Proxy, which handles authentication, encryption, and key rotation for you.
  - If you need manual control over the SSL connection, you can generate and periodically rotate the certificates yourself.
  - Otherwise, you can use an unencrypted connection by authorizing a specific IP address to connect to your SQL server over its external IP address. 
  
  ![image](https://github.com/user-attachments/assets/bb8291eb-37e6-4458-b12b-256789882d52)


> ## Query insights
- Query insights helps you detect, diagnose, and prevent query performance problems for Cloud SQL databases. 
- With Query insights, you can monitor performance at an application level and trace the source of a problematic query across the application stack by model, view, controller, route, user, and host.
- The Query insights tool can integrate with your existing application monitoring (APM) tools and Google Cloud services by using open standards and APIs. 
- There is no additional cost for Query Insights
- Metrics available through the console, gcloud commands and REST API

> ## Cloud SQL Studio







