
### **Cloud SQL**  
- Fully managed Relational database services for MySQL, PostgreSQL & SQL Server. No maintenance & auto update. Generally used for storing Transactional database
- Regional Database with 99.95% SLA. Multiple zones for high availability and multi-region for backups only. 
- Storage up to 30 TB
- Vertical Scale up to 96 core & 416 GB Memory. No Horizontal Scaling
- Data is encrypted with Google managed key or CMEK
- Back-up Database: On-demand Backup and Scheduled backup
- Database migration service (DMS)
  - migrate data from different SQL system to Cloud SQL
- Point-in Time Recovery
- Scale with Read replicas – To transfer workload to other instance
- Export data: gcloud utility or Cloud Console to SQL/CSV format
- To failover, the sql instance should not reside in single zone

> Connect to MySQL instance

```bash
# 1. using cloud shell
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

> Data Migration to Cloud SQL

```bash
# 1. Get the database dump
$ mysqldump -u root -p database-name > backup.sql

# 2. Upload the backup.sql to cloud storage and provide location under Overview > Import
```
