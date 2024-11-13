## SQL

> ##### Get number of rows, last modified and creation time of all the tables in a dataset
```sql
SELECT
   project_id
  ,dataset_id
  ,table_id AS table_name
  ,TIMESTAMP_MILLIS(creation_time) AS creation_tm
  ,TIMESTAMP_MILLIS(last_modified_time) AS last_modified_tm
  ,row_count AS record_count
FROM `project.dataset.__TABLES__`
ORDER BY 1, 2, 3
;
```

> ##### Get region details of all datasets in the project 
```sql
SELECT
   catalog_name
  ,schema_name
  ,location
FROM `project`.INFORMATION_SCHEMA.SCHEMATA
ORDER BY 1, 2
;
```

> ##### Get list of all tables in the region
```sql
SELECT
   table_catalog
  ,table_schema
  ,table_name
  ,table_type
FROM `project.region-REGION`.INFORMATION_SCHEMA.TABLES
ORDER BY 1, 2, 3
;
```
