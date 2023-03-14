# Cloud DataProc

- Dataproc is fully managed service for running Hadoop and Spark data processing workloads. 
- Cluster type
  - Standard (1 master, N workers)
  - Single Node (1 master, 0 workers)
  - High Availability (3 masters, N workers)
- Worker node regular VM or Preemptible VM (Cost reduction)
- Job Supported: Hadoop, SparkR, Spark, SparkSQL, Hive, Pig, PySpark
- Monitoring
  - Job Driver Output
  - Cloud Monotoring
  - Cloud Logging


![image](https://user-images.githubusercontent.com/19702456/222905812-b96b7e40-6a27-4dd8-ae91-341dd2125dfc.png)

Inside of a Google data center, the internal name for the massively distributed storage layer is called Colossus. Under the network inside the data center is Jupyter.

![image](https://user-images.githubusercontent.com/19702456/222905822-8241a5b3-9eb7-4c9e-89b2-093384a41e10.png)

In general, you want to use a push-based model for any data that you know you will need while pull-based may be a useful model if there is a lot of data that you might not ever need to migrate.
To get the most from Dataproc, customers need to move to an ephemeral model of only using clusters when they need them.












