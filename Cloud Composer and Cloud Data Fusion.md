# Cloud Composer

- Fully Managed Apache Airflow which in GCP
- Airflow is a workflow & orchestration engine
  - With Airflow, one can programmatically schedule and monitor workflows
  - Workflows are defined as directed acyclic graphs (DAGs)
  - DAGs are written in Python 3.x
- Cloud SQL stores Airflow metadata.
- Cloud Storage buckets are used for staging workflow DAGs, plugins, logs and data dependencies.
- Redis is used as message broker for CeleryExecutor. Uses stateful sets to persist messages across container restarts. 

# Cloud Data Fusion
- Fully-managed, cloud native solution to quickly building data pipelines
- Code free, Drag-n-drop ETL/ELT development tool
- 150+ preconfigured connectors & transformations
- Built with Open-source CDAP
- 3 Edition are available
   Developer
   Basic
   Enterprise
- Pricing : https://cloud.google.com/data-fusion/pricing#cloud-data-fusion-pricing
