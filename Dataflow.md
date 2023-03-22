# Dataflow

- Fully managed Managed service for both batch + stream Processing. Horizontal autoscaling of worker
- An advanced unified programming model to implement batch and streaming data processing jobs that run on various execution engine/ runner
    
    ![image](https://user-images.githubusercontent.com/19702456/226647382-4e6a3bc0-f4fb-4dfa-b5e7-d5c186e47ff1.png)

- Cloud version of Apache Beam = (Batch + Stream)
- Jobs created with
  - Pre-define template
  - Notebook instance
   - Write Data Pipeline job in Java, Python, SQL
  - From Cloud Shell/Local Machine
- Execution
  - Direct Runner
    - Scaling issue
  - Apache Flink
  - Apache Spark
  - Cloud DataFlow
- Job States: Running, Not Started, Queues, Cancelling/Cancelled, Draining/Drained, Updating/Updated, Succeeded, Failed

# Apache Beam
-  A pipeline is a graph of transformations that a user constructs that defines the data processing they want to do.
-  IO-Transform - https://beam.apache.org/documentation/io/built-in/
-  Pcollection - Fundamental data type in Beam
-  Ptransform - The [operations](https://beam.apache.org/documentation/programming-guide/#transforms) executed within a pipeline - 
-  Runner - Execution engine
