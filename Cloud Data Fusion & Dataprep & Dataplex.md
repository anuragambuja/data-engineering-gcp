# Cloud Data Fusion

  ![image](https://github.com/user-attachments/assets/da09fd25-0a33-416d-805e-0d40058c0241)

  <img src="https://github.com/user-attachments/assets/c5a03c82-0271-4ebf-993a-f9b02bc42faa" width="700" >

- Fully-managed, Code free, Drag-n-drop ETL/ELT development tool. You need to create an instance of Data Fusion. 150+ preconfigured connectors & transformations
- CDAP is a unified and integrated open source platform to build data analytics applications. Cloud Data Fusion is a native CDAP application for building data pipelines. Started as an open source project in 2011. Acquired by Google in 2018.
- Supports batch and real-time data pipelines
- Extensible: This includes the ability to templatize pipelines, create conditional triggers, and manage and templatize plugins.

- Two major user interface components:
  - Wrangler UI for exploring data sets visually, and building pipelines with no code
  - Data Pipeline UI for drawing pipelines right on to a canvas
- 3 Edition are available
  - Developer
  - Basic
  - Enterprise
- There are two components in Administration:
  - Management: Under management, you have services and metrics.
  - Configuration: Under configuration, you have namespace, compute profiles, preferences, system artifacts and the REST client.

- The Control Center gives you the ability to see everything at a glance and search for what you need, whether it's a particular data set, pipeline or other artifact, like a data dictionary. 
- Cloud Data Fusion translates your visually built pipeline into an Apache Spark or MapReduce program that executes transformations on an ephemeral Cloud Dataproc cluster in parallel.
  
- Cloud Data Fusion supports DAGs in a pipeline, which allows for non-linear pipeline execution. You can fork from a stage, where output from a stage can be sent to two or more stages. Two or more forked stages can merge at a transform or a sink stage. Processing in the pipeline is governed by the following aspects:
    - Data flow is the movement of data, in the form of records, from one step of a pipeline to another. When data arrives at a stage, it triggers that stage's processing of the data and then the transference of results (if any) to the next stage.
    - Control flow is a parallel process that triggers a stage based on the result from another process, independent of the pipeline. Currently, control flow can be applied only to the initial stages (before any data flow stages run) and final stages (after all other data flow stages run) of a pipeline. A post-run stage is available after each pipeline run, successful or otherwise.

        <img src="https://github.com/user-attachments/assets/3bff3abd-5a48-4918-b251-7b428f72e134" >



# Cloud Dataprep
- Cloud Dataprep by Trifacta is an intelligent data service for visually exploring, cleaning, and preparing data for analysis.
- With Alteryx / Dataprep, you can get a visual representation of the data and use wranglers andrecipes to remove out of scope and erroneous data.
- Serverless, runs on top of Dataflow
- Alteryx / Dataprep ELT pipeline architecture

  ![image](https://github.com/user-attachments/assets/708b9cdb-955b-48db-a06e-ff5fc9807fb7)



# Dataplex
- Dataplex is an intelligent data fabric that enables organizations to centrally discover, manage, monitor, and govern their data across data lakes, data warehouses, and data marts to power analytics at scale. Specifically, you can use Dataplex to build a data mesh architecture, which is an organizational and technical approach that decentralizes data ownership among domain data owners.

  <img src="https://github.com/user-attachments/assets/cb688470-b9d6-47d3-86d4-bc75190acda5" width="500" height="400">
  
- Dataplex manages data in a way that doesn’t require data movement or duplication. As you add new data assets, Dataplex harvests the metadata for both structured and unstructured data, and automatically registers all metadata in a secure, unified metastore. Data and metadata can then be assessed via Google Cloud services such as Data Catalog and BigQuery.

- In Dataplex, a lake is the highest organizational domain that represents a specific data area or business unit. For example, you can create a lake for each department or data domain in your organization, so that you can organize and provide data for specific user groups. After you create a lake, you can add zones to the lake. Zones are subdomains within a lake that you can use to categorize data further. Data stored in Cloud Storage buckets or BigQuery datasets can be attached as assets to zones within a Dataplex lake. To delete a lake, you must first detach assets and then delete the zones. There are two types of zones:
  - Raw zones contain data in raw formats (such as files in Cloud Storage buckets) and are not subject to strict type-checking.
  - Curated zones contain data that is cleaned, formatted, and ready for analytics such as BigQuery tables.

      <img src="https://github.com/user-attachments/assets/f3d3f629-6c56-4936-91e4-cccf61e19166" width="500" height="250">

- Dataplex provides a flexible security model that allows you to manage who can access and perform actions on Dataplex resources. Specifically, Dataplex security is implemented using different Dataplex IAM roles that allow users to administer Dataplex lakes, access data in the lake through the attached assets such as a Cloud Storage bucket or BigQuery dataset, or access metadata about the data connected to a lake.
Following the Google recommendation of least privilege, Dataplex allows Dataplex administrators to grant Dataplex IAM roles to users (Dataplex > Secure >Dataplex resources >Grant access) at the level of the project, lake, zone, and individual assets like a Cloud Storage bucket.

- A valuable feature of Dataplex is the ability to define and run data quality checks on Dataplex assets such as BigQuery tables and Cloud Storage files. Using Dataplex data quality tasks, you can integrate data quality checks into everyday workflows by validating data that is part of a data production pipline, regularly monitoring the quality of your data against a set of criteria, and building data quality reports for regulatory requirements. Dataplex data quality check requirements are defined using CloudDQ YAML specification files. Once created, the YAML specification file is uploaded to a Cloud Storage bucket that is made accessible to the data quality job. The YAML file has four keys sections:
  - a list of rules to run (either pre-defined or customized rules)
  - row filters to select a subset of data for validation
  - rule bindings to apply the defined rules to the table(s)
  - optional rule dimensions to specify the types of the rules that the YAML file can contain
 
- To start tagging data, you first need to create one or more tag templates. A tag template can be a public or private tag template. When you create a new tag template, the option to create a public tag template is the default and recommended option. Users who have the required view permissions for a data asset can view all the public tags associated with it. This supports simple search for discovery while also adhering to data access controls already implemented on the underlying data. After you create a tag template, you can use it to attach tags to any number of desired data assets to which you have access.



