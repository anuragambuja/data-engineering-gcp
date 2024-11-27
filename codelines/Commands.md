## App Engine

```bash
# Initialize your SDK
$ gcloud init

# Deploy your code to App Engine 
$ gcloud app deploy

# stream logs of your application
$ gcloud app logs tail -s default

# view your application - will provide URL for the browser
$ gcloud app browse
```
```
cd default-service
gcloud app deploy
gcloud app services list
gcloud app versions list
gcloud app instances list
gcloud app deploy --versio
n=v2
gcloud app versions list
gcloud app browse
gcloud app deploy --version=v3 --no-promote
gcloud app browse --version v3
gcloud app services set-traffic splits=v3=.5,v2=.5
watch curl https://melodic-furnace-304906.uc.r.appspot.com/
gcloud app services set-traffic --splits=v3=.5,v2=.5 --split-by=random
 
cd ../my-first-service/
gcloud app deploy
gcloud app browse --service=my-first-service
 
gcloud app services list
gcloud app regions list
```

## Cloud SQL 
> ### **Connect to MySQL instance**

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


> ### **Data Migration to Cloud SQL**

```bash
# 1. Get the database dump
$ mysqldump -u root -p database-name > backup.sql

# 2. Upload the backup.sql to cloud storage and provide location under Overview > Import
```

## 
