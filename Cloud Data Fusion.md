# Cloud Data Fusion

  ![image](https://github.com/user-attachments/assets/da09fd25-0a33-416d-805e-0d40058c0241)

- Fully-managed, cloud native solution to quickly building data pipelines. You need to create an instance of Data Fusion.
- CDAP is a unified and integrated open source platform to build data analytics applications. Cloud Data Fusion is a native CDAP application for building data pipelines. Started as an open source project in 2011. Acquired by Google in 2018.
- Code free, Drag-n-drop ETL/ELT development tool
- Supports batch and real-time data pipelines
- 150+ preconfigured connectors & transformations
- Built with Open-source CDAP
- extensible: This includes the ability to templatize pipelines, create conditional triggers, and manage and templatize plugins.
- Two major user interface components:
  - Wrangler UI for exploring data sets visually, and building pipelines with no code
  - Data Pipeline UI for drawing pipelines right on to a canvas
- 3 Edition are available
  - Developer
  - Basic
  - Enterprise
- Pricing : https://cloud.google.com/data-fusion/pricing#cloud-data-fusion-pricing
- The Control Center gives you the ability to see everything at a glance and search for what you need, whether it's a particular data set, pipeline or other artifact, like a data dictionary, 
- There are two components in Administration, management and configuration. Under management, you have services and metrics. Under configuration, you have namespace, compute profiles, preferences, system artifacts and the REST client.
- Cloud Data Fusion translates your visually built pipeline into an Apache Spark or MapReduce program that executes transformations on an ephemeral Cloud Dataproc cluster in parallel. 
- Cloud Data Fusion supports DAGs in a pipeline, which allows for non-linear pipeline execution. You can fork from a stage, where output from a stage can be sent to two or more stages. Two or more forked stages can merge at a transform or a sink stage.

    ![image](https://github.com/user-attachments/assets/3bff3abd-5a48-4918-b251-7b428f72e134)
- Data and Control Flow: Processing in the pipeline is governed by the following aspects:
    - Data flow is the movement of data, in the form of records, from one step of a pipeline to another. When data arrives at a stage, it triggers that stage's processing of the data and then the transference of results (if any) to the next stage.
    - Control flow is a parallel process that triggers a stage based on the result from another process, independent of the pipeline. Currently, control flow can be applied only to the initial stages (before any data flow stages run) and final stages (after all other data flow stages run) of a pipeline. A post-run stage is available after each pipeline run, successful or otherwise.

![image](https://user-images.githubusercontent.com/19702456/224944491-d5b1378c-aa7c-4129-b743-007806c41e20.png)

![image](https://github.com/user-attachments/assets/c5a03c82-0271-4ebf-993a-f9b02bc42faa)

![image](https://github.com/user-attachments/assets/fe34b11d-bd59-44bb-87c5-65b35af1f7be)
*Planned for a future release
