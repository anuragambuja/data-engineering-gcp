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

- All data in Apache Beam pipelines reside in PCollections. To create your pipeline’s initial PCollection, apply a root transform to your pipeline object. A root transform creates a PCollection from either an external data source or some local data you specify. There are two kinds of root transforms in the Beam SDKs: Read and Create. Read transforms read data from an external source, such as a text file or a database table. Create transforms create a PCollection from an in-memory list and are especially useful for testing.
- Bundles are groupings of elements in the pipeline for a unit of work. Checkpoints allow for the ability to bookmark where the data has been read in the source, which means that the data that has been processed in the stream doesn't need to be reread. 
- Transforms are what change your data. In Apache Beam, transforms are done by the PTransform class. At runtime, these operations will be performed on a number of independent workers. The input and output to every PTransform is a PCollection.
- ParDo is a Beam transform for generic parallel processing. The ParDo processing paradigm is similar to the “Map” phase of a Map/Shuffle/Reduce-style algorithm: a ParDo transform considers each element in the input PCollection, performs some processing function (your user code) on that element, and emits zero, one, or multiple elements to an output PCollection.
- When you run your pipeline on Dataflow, it uses the service account service- @dataflow-service-producer-prod.iam.gserviceaccount.com. This account is automatically created when the Dataflow API is enabled. It is assigned the Dataflow service agent role and has the necessary permissions to run a Dataflow job in your project. 
- When you launch a batch pipeline, the ratio of VMs to PDs is 1:1. For each VM, only one persistent disk is attached. For jobs running Shuffle on worker VMs, the default size of each persistent disk is 250 gigabytes. If the batch job is running using Shuffle Service, the default persistent disk size is 25 gigabytes. Streaming pipelines, however, are deployed with a fixed pool of persistent disks. Each worker must have at least one persistent disk attached to it while the maximum is 15 persistent disks per worker instance. When you run a job using the Dataflow back end, the feature that is used is Dataflow Streaming Engine. For jobs launched to execute in the worker VMs, the default persistent disk size is 400 gigabytes. Jobs launched using Streaming Engine have a persistent disk size of 30 gigabytes. It is important to note that the amount of disk allocated in a streaming pipeline is equal to the maxNumWorkers flag. For example, if you launch a job with three workers initially and set the maximum number of workers to 25, 25 disks will count against your quota and not three. For streaming jobs that do not use Streaming Engine, the maxNumWorkers flag is optional. The default is 100.
- 

- Dataflow Suffle Service
A shuffle is a Dataflow-based operation behind transforms such as GroupByKey, CoGroupByKey, and Combine. The Dataflow Shuffle operation partitions and groups data by key in a scalable, efficient, fault-tolerant manner. Currently, Dataflow uses a shuffle implementation that runs entirely on worker virtual machines and consumes worker CPU, memory, and persistent disk storage. The service-based Dataflow Shuffle feature available for batch pipelines only moves the shuffle operations out of the worker VMs and into the Dataflow service backend. The worker nodes will benefit from a reduction in consumed CPU, memory, and persistent disk storage resources, and your pipelines will have better autoscaling because the worker nodes VMs no longer hold any shuffle data, and can therefore be scaled down earlier.

![image](https://user-images.githubusercontent.com/19702456/226877535-90a1d25e-df87-46da-b2d2-65272b7cf680.png)

- Dataflow Streaming Engine
Just like shuffle component in batch, the streaming engine offloads the window state storage from the persistent disks attached to worker VMs to a back-end service. Worker nodes continue running your user code and implements data transforms and transparently communicate with a streaming engine to source state. Streaming engine works best with smaller worker machine types like n1-standard-2, and does not require persistent disks beyond a smaller worker boot disk.

- Flexible Resource Scheduling (FlexRS)
When you submit a FlexRS job, the Dataflow service places the job into a queue and submits it for execution within six hours from job creation. As soon as you submit your FlexRS job, Dataflow records a job ID and performs an early validation run to verify execution parameters, configurations, quota and permissions.

- Dataframe differences from standard Pandas
    - Operations are deferred, and the result of a given operation may not be available for control flow or interactive visualizations. For example, you can compute a sum, but you can't branch on the result.
    - Result columns must be computable without access to the data. For example, you can't use transpose.
    - PCollections in Beam are inherently unordered, so Pandas operations that are sensitive to the ordering rows are unsupported. For example, head and tail are not supported. 

- Beam SQL
    - Works with stream and batch inputs.
    - Can be embedded in an existing pipeline using SqlTransform, which can be mixed with PTransforms.
    - Supports UDFs in Java
    - Supports multiple dialects
        - Beam Calcite SQL
            - Provides compatibility with other OSS SQL dialects (e.g. Flink SQL). Copy-paste queries may require changes to table names, array indexing
            - Supports Java UDFs
        - Google ZetaSQL
            - Provides BigQuery compatibility. Copy-paste queries may require changes to table names
    - Integrated with Schemas
        - Uses Row
    - Stream aggregations support windows

### Testing
We use unit tests in Beam to assert behavior of one small testable piece of your production pipeline. These small portions are usually either individual DoFns or PTransforms. These tests should complete quickly, and they should run locally with no dependencies on external systems. Beam uses JUnit 4 for unit testing. Test pipeline is a class included in the beam SDK specifically for testing transforms.

### Deployment

![image](https://user-images.githubusercontent.com/19702456/226887738-61e7b35b-8f34-4367-8786-644ed6b8b155.png)

![image](https://user-images.githubusercontent.com/19702456/226887770-31f995d2-b42f-4fc8-811d-1e4170d763af.png)




