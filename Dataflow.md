# Dataflow

- Fully managed Managed service for both batch + stream Processing. Horizontal autoscaling of worker
<img width="424" alt="image" src="https://github.com/user-attachments/assets/0b413927-8525-4c92-85ec-031135af3d0b">

  
- An advanced unified programming model to implement batch and streaming data processing jobs that run on various execution engine/ runner
    
    ![image](https://user-images.githubusercontent.com/19702456/226647382-4e6a3bc0-f4fb-4dfa-b5e7-d5c186e47ff1.png)

- Cloud version of Apache Beam = (Batch + Stream)
- Jobs created with
  - Pre-define template - Dataflow Templates allow users who don't have any coding capability to execute their Dataflow job.
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

- When a Dataflow job is created, a cloud storage bucket is used to store binary files containing pipeline code. A cloud storage bucket is also used to temporarily store export or import data. By default, when data is stored in any of these locations, a Google-managed key is used to encrypt the data. When your pipeline starts and the data is loaded into the worker memory, data keys used in key-based operations, such as windowing, grouping, and joining, will be decrypted using your CMEK keys. Using CMEK requires both the Dataflow service account and the Controller Agent service account to have the cloud KMS CryptoKey Encrypter/Decrypter role. When you launch a job that uses CMEK, the region for your key and the regional input for your Dataflow job must be the same.

    ![image](https://user-images.githubusercontent.com/19702456/226963260-a4cb6ad1-d144-4794-854c-42cabeadeb0f.png)

    A pipeline identifies the data to be processed and the actions to be taken on the data. The data is held in a distributed data abstraction called a P collection. The P collection is immutable. Any change that happens in a pipeline ingests one P collection and creates a new one. It does not change the incoming P collection. The action or code is contained in an abstraction called a P transform. P transform handles input, transformation, an output of the data. The data in the P collection is passed along a graph from one P transform to another. Pipeline runners are analogous to container hosts such as Google Kubernetes Engine. The identical pipeline can be run on a local computer, data center VM, or on a service such as Dataflow in the Cloud. The services the runner uses to execute the code is called a backend system. A P collection represents both streaming data and batch data. There is no size limit to a P collection. Streaming data is an unbounded P collection that doesn't end. Each element inside a P collection can be individually accessed and processed. Elements represent different data types. In a P collection, all data types are stored in a serialized state as byte strings. This way, there is no need to serialize data prior to network transfer and deserialize it when it is received.Instead, the data moves through the system in a serialized state and is only deserialized when necessary for the actions of a P transform.

   ![image](https://user-images.githubusercontent.com/19702456/226963349-5765d651-f9b4-42c2-8bd1-64d8ff69ce8d.png)

   ![image](https://user-images.githubusercontent.com/19702456/226964415-cf1d6c9a-7329-41c6-92f0-84bf78a52415.png)
   
   ![image](https://user-images.githubusercontent.com/19702456/226964539-2449f160-a634-456c-a8fd-6df1fa870cb1.png)


- All data in Apache Beam pipelines reside in PCollections. To create your pipeline’s initial PCollection, apply a root transform to your pipeline object. A root transform creates a PCollection from either an external data source or some local data you specify. There are two kinds of root transforms in the Beam SDKs: Read and Create. Read transforms read data from an external source, such as a text file or a database table. Create transforms create a PCollection from an in-memory list and are especially useful for testing.
    - PCollections are immutable. Applying transformation on a PCollection results in creation of a new PCollection
    - The elements in a PCollection may be of any type, but all must be of the same type.
    - PCollection does not support grained operations. We cannot apply transformations on some specific elements in a PCollection.
    - Each element in a PCollection has an associated timestamp with it. In Unbounded PCollections - source assign the timestamps. In Bounded PCollections - evenry elemnt is set to same timestamp. We can also assign the timestamps incase if it is not available.

- Bundles are groupings of elements in the pipeline for a unit of work. Checkpoints allow for the ability to bookmark where the data has been read in the source, which means that the data that has been processed in the stream doesn't need to be reread. 

- Transforms are what change your data. In Apache Beam, transforms are done by the PTransform class. At runtime, these operations will be performed on a number of independent workers. The input and output to every PTransform is a PCollection.

- ParDo is a Beam transform for generic parallel processing. The ParDo processing paradigm is similar to the “Map” phase of a Map/Shuffle/Reduce-style algorithm: a ParDo transform considers each element in the input PCollection, performs some processing function (your user code) on that element, and emits zero, one, or multiple elements to an output PCollection. You might use it to extract certain fields from a set of raw input records or convert raw input into a different format.
  You might use ParDo to extract certain fields from a set of raw input records or convert raw input into a different format. You might also use ParDo to convert process data into an output format, like table rows for BigQuery or strings for printing. You can use ParDo to consider each element in a PCollection and either output that element to a new collection or discard it. If your input PCollection contains elements that are of a different type or format than you want, you can use ParDo to perform a conversion on each element and output the result to a new PCollection.

    ![image](https://user-images.githubusercontent.com/19702456/226965334-039ec168-4923-4dcf-b527-b898e2631e84.png)

    - When you apply a ParDo transform, you need to provide code in the form of a DoFn object. A DoFn is a Beam SDK class that defines a distributed processing function. Your DoFn code must be fully serializable, item potent and thread safe.
      
    - A side input is an additional input other than main imput that your do function can access each time it processes an element in the input PCollection. When you specify a side input, you create a view of some other data that can be read from within the ParDo transform's do function while processing each element. Side inputs are useful if your ParDo needs to inject additional data when processing each element in the input PCollection, but the additional data needs to be determined at runtime and not hard coded. Such values might be determined by the input data or depend on a different branch of your pipeline. eg. Check if any given word is shorter or longer than the average word length, first we need to compute the average word length which is then fed as side input.
    <img width="383" alt="image" src="https://github.com/user-attachments/assets/600a2b21-6752-4432-a3a2-34b12f3a2ffd">


- When you run your pipeline on Dataflow, it uses the service account service- @dataflow-service-producer-prod.iam.gserviceaccount.com. This account is automatically created when the Dataflow API is enabled. It is assigned the Dataflow service agent role and has the necessary permissions to run a Dataflow job in your project. By default, workers use your project's Compute Engine default service account as the controller service account. This service account, <project-number>-compute @developer.gservices.com, is automatically created when you enable the Compute Engine API for your project from the API's page in the Google Cloud console.

- When you launch a batch pipeline, the ratio of VMs to PDs is 1:1. For each VM, only one persistent disk is attached. For jobs running Shuffle on worker VMs, the default size of each persistent disk is 250 gigabytes. If the batch job is running using Shuffle Service, the default persistent disk size is 25 gigabytes. Streaming pipelines, however, are deployed with a fixed pool of persistent disks. Each worker must have at least one persistent disk attached to it while the maximum is 15 persistent disks per worker instance. When you run a job using the Dataflow back end, the feature that is used is Dataflow Streaming Engine. For jobs launched to execute in the worker VMs, the default persistent disk size is 400 gigabytes. Jobs launched using Streaming Engine have a persistent disk size of 30 gigabytes. It is important to note that the amount of disk allocated in a streaming pipeline is equal to the maxNumWorkers flag. For example, if you launch a job with three workers initially and set the maximum number of workers to 25, 25 disks will count against your quota and not three. For streaming jobs that do not use Streaming Engine, the maxNumWorkers flag is optional. The default is 100.

> ### Windows
- Windows divides data into time-based finite chunks. It is required when doing aggregations over unbounded data using Beam primitives (GroupBy Key, Combiners). 
- Types of windows
    - Fixed windows - are those that are divided into time slices. For example, hourly, daily, monthly. Fixed time windows consist of consistent, non-overlapping intervals.
    - Sliding windows - represent intervals in the data stream. Sliding time windows can overlap. For example, in a running average. The frequency with which a sliding windows begin is called a period. For example, give me 30 minutes' worth of data and compute that every 5 minutes. 
    - Session windows - are for situations where the communication is bursty. It might correspond to a web session. An example might be if a user comes in and uses four to five pages and leaves. It will have a time-out period, and it will flush the window at the end of that time out period.

    ![image](https://user-images.githubusercontent.com/19702456/226908765-bbc317d5-c411-42cd-9197-3c72de9954d6.png)

    ![image](https://user-images.githubusercontent.com/19702456/226908783-9e76ca62-aa59-4a05-a8fa-d60742084cd4.png)

> ### Watermark
- Watermark keep tracks of lag time. The watermark is the relationship between the processing timestamp and the event. The processing timestamp is the moment the message arrives at the pipeline.  Any message that arrives before the watermark is said to be early. if it arrives right after the watermark is said to be on time and if it arrives later, then it is late.
- Data flow estimates the watermark as the oldest timestamp waiting to be processed. This estimation is continuously updated with every new message that is received. 
- Data freshness is the amount of time between real time and the output watermark (timestamp of the oldest message waiting to be processed). 
- System latency is the current maximum duration that an item of data has been processing or awaiting processing. Latency measures the time it takes to fully process a message.This includes any waiting time in the input source.
- Dataflow ordinarily is going to wait until the watermark it has computed has elapsed. Beams default windowing configuration tries to determine when all data has arrived based on the type of data source, and then advances the watermark past the end of the window. This default configuration does not allow late data. The default behavior is to trigger at the watermark. If you don't specify a trigger, you are actually using the trigger after watermark. After watermark is an event time trigger. The message's time stamps are used to measure time with these triggers. But we could also add custom triggers.

    ![image](https://user-images.githubusercontent.com/19702456/226929266-404bc908-c88f-4e0c-a7e5-0e740fbe7643.png)

    ![image](https://user-images.githubusercontent.com/19702456/226929604-0cc56331-7a73-4bc5-8115-b046c5cb8ecf.png)
    
> ### Triggers
- Triggers determine at what point during processing time results will be materialized. Each specific output for a window is referred to as a pane of the window. Triggers fire panes when the trigger’s conditions are met. In Apache Beam, those conditions include watermark progress, processing time progress (which will progress uniformly, regardless of how much data has actually arrived), element counts (such as when a certain amount of new data arrives), and data-dependent triggers, like when the end of a file is reached.
- A trigger’s conditions may lead it to fire a pane many times. Consequently, it’s also necessary to specify how to accumulate these results. Apache Beam currently supports two accumulation modes, one which accumulates results together and the other which returns only the portions of the result that are new since the last pane fired. There are two accumulation modes in apache beam - accumulate and discard. With accumulate every time you trigger it again in the same window, the calculation is just repeated with all the messages that have been included in the window so far. With discard once some messages have been used for a calculation those messages are discarded. If new messages arrive later and there is a new trigger, the result will only include the new messages and those messages will be discarded again.

    ![image](https://user-images.githubusercontent.com/19702456/226931988-5604dea1-a983-4324-bfed-35d4e19efc5c.png)

> ### State & Timers
- With stateful ParDos, there are many aggregations that can be implemented without having to use a combiner or a GroupByKey. State is maintained per key. For streaming pipelines, the state is also maintained per window. The state can be read and mutated during the processing of each one of the elements. The state is local to each one of the transformers. For instance, two different keys process, and two different workers are not able to share a common state, but all elements in the same key can share a common state. The state variables allow you to batch the request by accumulating elements in a buffer and making batch calls to the external services, that, for example, you can make a call every 10 messages. It is important to remember to clear the state once it has been used. The DoFn will not finish entirely unless the whole state has been clear.
- Timers are used in combination with state variables, to ensure that the state is cleared at regular intervals of time.
       
     ![image](https://user-images.githubusercontent.com/19702456/226947028-89465617-e588-425e-a7d6-dfbf8c1cc6a4.png)

     ![image](https://user-images.githubusercontent.com/19702456/226947218-53b5376f-fa2f-488e-b066-e096509d2e98.png)

> ### Dataflow Suffle Service
A shuffle is a Dataflow-based operation behind transforms such as GroupByKey, CoGroupByKey, and Combine. The Dataflow Shuffle operation partitions and groups data by key in a scalable, efficient, fault-tolerant manner. Currently, Dataflow uses a shuffle implementation that runs entirely on worker virtual machines and consumes worker CPU, memory, and persistent disk storage. The service-based Dataflow Shuffle feature available for batch pipelines only moves the shuffle operations out of the worker VMs and into the Dataflow service backend. The worker nodes will benefit from a reduction in consumed CPU, memory, and persistent disk storage resources, and your pipelines will have better autoscaling because the worker nodes VMs no longer hold any shuffle data, and can therefore be scaled down earlier.

![image](https://user-images.githubusercontent.com/19702456/226877535-90a1d25e-df87-46da-b2d2-65272b7cf680.png)

> ### Dataflow Streaming Engine
Just like shuffle component in batch, the streaming engine offloads the window state storage from the persistent disks attached to worker VMs to a back-end service. Worker nodes continue running your user code and implements data transforms and transparently communicate with a streaming engine to source state. Streaming engine works best with smaller worker machine types like n1-standard-2, and does not require persistent disks beyond a smaller worker boot disk.

> ### Flexible Resource Scheduling (FlexRS)
When you submit a FlexRS job, the Dataflow service places the job into a queue and submits it for execution within six hours from job creation. As soon as you submit your FlexRS job, Dataflow records a job ID and performs an early validation run to verify execution parameters, configurations, quota and permissions.

> ### Dataframe differences from standard Pandas
- Operations are deferred, and the result of a given operation may not be available for control flow or interactive visualizations. For example, you can compute a sum, but you can't branch on the result.
- Result columns must be computable without access to the data. For example, you can't use transpose.
- PCollections in Beam are inherently unordered, so Pandas operations that are sensitive to the ordering rows are unsupported. For example, head and tail are not supported. 

> ### Beam SQL
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

## Testing
We use unit tests in Beam to assert behavior of one small testable piece of your production pipeline. These small portions are usually either individual DoFns or PTransforms. These tests should complete quickly, and they should run locally with no dependencies on external systems. Beam uses JUnit 4 for unit testing. Test pipeline is a class included in the beam SDK specifically for testing transforms.

## Deployment

![image](https://user-images.githubusercontent.com/19702456/226887738-61e7b35b-8f34-4367-8786-644ed6b8b155.png)

![image](https://user-images.githubusercontent.com/19702456/226887770-31f995d2-b42f-4fc8-811d-1e4170d763af.png)


## Note
- Consider using combine when you can instead of GroupByKey, especially if your data is heavily skewed.    

