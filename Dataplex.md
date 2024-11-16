# Dataplex

![image](https://github.com/user-attachments/assets/79be532d-24f5-458e-93d8-17e56c4d3dac)

- Dataplex is an intelligent data fabric that enables organizations to centrally discover, manage, monitor, and govern their data across data lakes, data warehouses, and data marts to power analytics at scale. Specifically, you can use Dataplex to build a data mesh architecture, which is an organizational and technical approach that decentralizes data ownership among domain data owners.

Dataplex manages data in a way that doesn’t require data movement or duplication. As you add new data assets, Dataplex harvests the metadata for both structured and unstructured data, and automatically registers all metadata in a secure, unified metastore. Data and metadata can then be assessed via Google Cloud services such as Data Catalog and BigQuery.

![image](https://github.com/user-attachments/assets/cb688470-b9d6-47d3-86d4-bc75190acda5)


- After you create a lake, you can add zones to the lake. Zones are subdomains within a lake that you can use to categorize data further. Data stored in Cloud Storage buckets or BigQuery datasets can be attached as assets to zones within a Dataplex lake. To delete a lake, you must first detach assets and then delete the zones. There are two types of zones:
  - Raw zones contain data in raw formats (such as files in Cloud Storage buckets) and are not subject to strict type-checking.
  - Curated zones contain data that is cleaned, formatted, and ready for analytics such as BigQuery tables.
 
- To start tagging data, you first need to create one or more tag templates. A tag template can be a public or private tag template. Users who have the required view permissions for a data asset can view all the public tags associated with it. This supports simple search for discovery while also adhering to data access controls already implemented on the underlying data.

Dataplex provides a flexible security model that allows you to manage who can access and perform actions on Dataplex resources. Specifically, Dataplex security is implemented using different Dataplex IAM roles that allow users to administer Dataplex lakes, access data in the lake through the attached assets such as a Cloud Storage bucket or BigQuery dataset, or access metadata about the data connected to a lake.
Following the Google recommendation of least privilege, Dataplex allows Dataplex administrators to grant Dataplex IAM roles to users at the level of the project, lake, zone, and individual assets like a Cloud Storage bucket.

A valuable feature of Dataplex is the ability to define and run data quality checks on Dataplex assets such as BigQuery tables and Cloud Storage files. Using Dataplex data quality tasks, you can integrate data quality checks into everyday workflows by validating data that is part of a data production pipline, regularly monitoring the quality of your data against a set of criteria, and building data quality reports for regulatory requirements.

- Dataplex data quality check requirements are defined using CloudDQ YAML specification files. Once created, the YAML specification file is uploaded to a Cloud Storage bucket that is made accessible to the data quality job. The YAML file has four keys sections:
  - a list of rules to run (either pre-defined or customized rules)
  - row filters to select a subset of data for validation
  - rule bindings to apply the defined rules to the table(s)
  - optional rule dimensions to specify the types of the rules that the YAML file can contain
sample file: https://github.com/anuragambuja/data-engineering-gcp/blob/main/codelines/dataplex-data-validation-on-bq-table.yaml

https://github.com/GoogleCloudPlatform/cloud-data-quality/blob/main/REFERENCE.md
Check the `failed_records_query` column in the final table to review the data quality checks. 


In Dataplex, a lake is the highest organizational domain that represents a specific data area or business unit. For example, you can create a lake for each department or data domain in your organization, so that you can organize and provide data for specific user groups.
After you create a lake, you can add zones to the lake. Zones are subdomains within a lake that you can use to categorize data further. For example, you can categorize data by stage, usage, or restrictions.
There are two types of zones:
- Raw zones contain data in raw formats (such as files in Cloud Storage buckets) and are not subject to strict type-checking.
- Curated zones contain data that is cleaned, formatted, and ready for analytics such as BigQuery tables.

Data stored in Cloud Storage buckets or BigQuery datasets can be attached as assets to zones within a Dataplex lake.

To delete a lake, you must first detach assets and then delete the zones.

> Tagging 
To start tagging data, you first need to create one or more tag templates. A tag template can be a public or private tag template. When you create a new tag template, the option to create a public tag template is the default and recommended option. Users who have the required view permissions for a data asset can view all the public tags associated with it. This supports simple search for discovery while also adhering to data access controls already implemented on the underlying data.
After you create a tag template, you can use it to attach tags to any number of desired data assets to which you have access.



To control access:
1. Create/Add Lake , Zone and assets.
2. Assign Dataplex role to the users (Dataplex > Secure >Dataplex resources >Grant access )


> ## Data mesh with Dataplex
- In Dataplex, a data domain is represented by a data lake
  - A lake is a container for data from different data sources
  - A data lake is created within a Google Cloud region
- Lakes contain one or more zones
  - Zones are either regional or multi-regional
  - Zones can contain either raw or curated data
- Zones contain assets
  - Assets represent the data being shared
  - Assets represent data in Cloud Storage buckets or BigQuery datasets

    ![image](https://github.com/user-attachments/assets/f3d3f629-6c56-4936-91e4-cccf61e19166)

> ## 
