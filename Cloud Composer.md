# Airflow
- Airflow is a platform to programmatically author, schedule and monitor workflows.
- DAG: A Directed Acyclic Graph is a collection of all the tasks you want to run, organized in a way that reflects their relationships and dependencies. DAGs are defined in standard Python files that are placed in Airflow's DAG_FOLDER. Airflow will execute the code in each file to dynamically build the DAG objects.
- Operator: The description of a single task, it is usually atomic. For example, the BashOperator is used to execute bash commands.
- Task: A parameterised instance of an Operator; a node in the DAG.
- Task Instance: A specific run of a task; characterized as: a DAG, a Task, and a point in time. It has an indicative state: running, success, failed, skipped



# Cloud Composer

- Fully Managed Apache Airflow which in GCP
- Airflow is a workflow & orchestration engine
  - With Airflow, one can programmatically schedule and monitor workflows
  - Workflows are defined as directed acyclic graphs (DAGs)
  - DAGs are written in Python 3.x
- Cloud SQL stores Airflow metadata.
- Cloud Storage buckets are used for staging workflow DAGs, plugins, logs and data dependencies.
- Redis is used as message broker for CeleryExecutor. Uses stateful sets to persist messages across container restarts. 

![image](https://github.com/user-attachments/assets/4d466e6b-44f8-4dcc-9314-1c5470371c3e)
