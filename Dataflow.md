# Dataflow

  ![image](https://github.com/user-attachments/assets/a602c48b-f31e-4beb-ba39-e5e7039aa4e9)



> ### Schema
- A schema describe a type in terms of fields and values
- Fields can be int, long, string etc
- Some fields can be marked as optional,  sometimes referred to as nullable or requited.
- Often records have a nested structure. These structure records have some commonly feature array or map type fields.


> ### State & Timers
- With stateful ParDos, there are many aggregations that can be implemented without having to use a combiner or a GroupByKey. State is maintained per key. For streaming pipelines, the state is also maintained per window.
- The state can be read and mutated during the processing of each one of the elements. The state is local to each one of the transformers. For instance, two different keys process, and two different workers are not able to share a common state, but all elements in the same key can share a common state. The state variables allow you to batch the request by accumulating elements in a buffer and making batch calls to the external services, that, for example, you can make a call every 10 messages. It is important to remember to clear the state once it has been used. The DoFn will not finish entirely unless the whole state has been clear.
- Timers are used in combination with state variables, to ensure that the state is cleared at regular intervals of time. There are 2 types of times avaialble in Beam:
  - Processing time timers are good for implementing timeouts. The time in processing time is relative to the previous messages and you will have periodic outputs based on that relative time
  - event time timers are good for output based on data completeness. Event time timers are based on the timestamps of the messages being processed. Always make sure to clear the state after emitting the output. If you leave the state behind, then the function will keep waiting for new data and that will consume resources in your pipeline.

    ![image](https://github.com/user-attachments/assets/a3687929-6057-4841-9d6c-96f231443a5c)
 
- Depending on the kind of state that you want to accumulate, you can use a different type of state variables.
  - Value: It can hold any kind of value of any type.
  - Bag: If you want to add several elements, use a bag state for a more efficient pipeline. Bag will return the objects that were added previously, but with no guarantee of order. Appending objects to a bag is very fast.
  - Combining: For any kind of aggregation that is associative and commutative, it is better to use the combining state.
  - Map: if you are going to maintain a set of key values, a dictionary or map, use map state. With a map, you have random access given a key.Map state is more efficient than other state variables for retrieving specific keys.
  - Set: available in the Apache Beam programming model, but not supported in data flow.

       ![image](https://user-images.githubusercontent.com/19702456/226947028-89465617-e588-425e-a7d6-dfbf8c1cc6a4.png)
  
       ![image](https://user-images.githubusercontent.com/19702456/226947218-53b5376f-fa2f-488e-b066-e096509d2e98.png)

  - What can you do with state and timers:
  
      ![image](https://github.com/user-attachments/assets/5a70a022-5a60-452e-858e-7bb7477e412a)


> ### Dataflow Shuffle Service
A shuffle is a Dataflow-based operation behind transforms such as GroupByKey, CoGroupByKey, and Combine. The Dataflow Shuffle operation partitions and groups data by key in a scalable, efficient, fault-tolerant manner. Currently, Dataflow uses a shuffle implementation that runs entirely on worker virtual machines and consumes worker CPU, memory, and persistent disk storage. The service-based Dataflow Shuffle feature available for batch pipelines only moves the shuffle operations out of the worker VMs and into the Dataflow service backend. The worker nodes will benefit from a reduction in consumed CPU, memory, and persistent disk storage resources, and your pipelines will have better autoscaling because the worker nodes VMs no longer hold any shuffle data, and can therefore be scaled down earlier. Also, because of the service, you will get better fault tolerance.An unhealthy VM holding Dataflow Shuffle data will not cause the entire job to fail, which would happen without the feature.

   ![image](https://user-images.githubusercontent.com/19702456/226877535-90a1d25e-df87-46da-b2d2-65272b7cf680.png)


> ### Dataflow Streaming Engine
Just like shuffle component in batch, the streaming engine offloads the window state storage from the persistent disks attached to worker VMs to a back-end service. It also implements an efficient shuffle for streaming cases. Worker nodes continue running your user code and implements data transforms and transparently communicate with a streaming engine to source state. Streaming engine works best with smaller worker machine types like n1-standard-2, and does not require persistent disks beyond a smaller worker boot disk. With streaming engine, your pipeline will be more responsive to variations to incoming data volume.


> ### Flexible Resource Scheduling (FlexRS)
When you submit a FlexRS job, the Dataflow service places the job into a queue and submits it for execution within six hours from job creation. This makes FlexRS suitable for workloads that are not time-critical, such as daily or weekly jobs that can be completed within a certain time window. As soon as you submit your FlexRS job, Dataflow records a job ID and performs an early validation run to verify execution parameters, configurations, quota and permissions. FlexRS leverages a mix of preemptible and normal VMs.


> ### Sources and Sinks
- A source is when you read input data into a Beam pipeline. A sink is where you would write output data from your Beam pipeline. A sink is a PTransform that performs a write to the specified destination.
- bounded source: A bounded source is a source that reads a finite amount of input commonly associated with batch processing. A bounded source will be responsible for splitting up the work of reading an input into bundles. Bundles are groupings of elements in the pipeline for a unit of work. If the bundles can be broken down into smaller chunks, Dataflow will dynamically rebalance work to achieve better performance.
- unbounded source: An unbounded source is a source that reads from an unbounded amount of input commonly associated with streaming. Checkpoints allow for the ability to bookmark where the data has been read in the source, which means that data that has been processed in the stream doesn’t need to be re-read. Some unbounded sources, for example PubSub IO, have the ability to pass a record ID to allow deduplication of messages.
- IOs
  - Text IO & File IO
  - Bigquery IO:
  - PubSub IO:
  - Kafka IO: Kafka IO is built in Java. Python's Kafka IO module uses the cross-language transform to enable Kafka IO on Python.
  - BigTable IO: Big table IO serves as the module that will communicate between big table and dataflow. You are able to include a row filter when reading from Big Table.
  - Avro IO: Avro IO allows you to read and write to that file type. Avro files provide the schema and the data so the files can be self-describing.


> ### Windows
- In Dataflow, when you are reading messages from Pub/Sub, every message will have a timestamp that is a Pub/Sub message timestamp.
- Windows divides data into time-based finite chunks. It is required when doing aggregations over unbounded data using Beam primitives (GroupBy Key, Combiners). 
- Types of windows
    - Fixed windows (Tumbling in Dataflow) - are those that are divided into time slices. For example, hourly, daily, monthly. Fixed time windows consist of consistent, non-overlapping intervals.
    - Sliding windows (Hopping in Dataflow) - represent intervals in the data stream. Sliding time windows can overlap. For example, in a running average. The frequency with which a sliding windows begin is called a period. For example, give me 30 minutes' worth of data and compute that every 5 minutes. 
    - Session windows - are for situations where the communication is bursty. It might correspond to a web session. An example might be if a user comes in and uses four to five pages and leaves. It will have a time-out period, and it will flush the window at the end of that time out period.

    ![image](https://user-images.githubusercontent.com/19702456/226908765-bbc317d5-c411-42cd-9197-3c72de9954d6.png)

    ![image](https://user-images.githubusercontent.com/19702456/226908783-9e76ca62-aa59-4a05-a8fa-d60742084cd4.png)


> ### Watermark
- Watermark keep tracks of lag time which can be due to network delays, system backlogs, processing delays, pubsub latency etc. The watermark is the relationship between the processing timestamp and the event. The processing timestamp is the moment the message arrives at the pipeline.  Any message that arrives before the watermark is said to be early. if it arrives right after the watermark is said to be on time and if it arrives later, then it is late. So, Dataflow is going to do is continuously compute the watermark, which is how far behind we are.
- Data flow estimates the watermark as the oldest timestamp waiting to be processed. This estimation is continuously updated with every new message that is received. 
- Data freshness is the amount of time between real time and the output watermark (timestamp of the oldest message waiting to be processed). So data freshness is a measurement of how far the oldest messages is from the current moment. When you see a monotonically increase in value it means that data has to wait at the input for more time waiting to start to be processed. There could be two reasons for the additional wait:
   - It could be because the pipeline is busy processing messages
   - It could be because the input has increased very quickly and data is accumulating at the input.
  
- System latency is the current maximum duration that an item of data has been processing or awaiting processing. Latency measures the time it takes to fully process a message.This includes any waiting time in the input source. So if system latency remains constant or reduces and does not monotonically increase and data freshness value is monotonically increasing, that could be because there are many more messages at the input.
  
- Dataflow ordinarily is going to wait until the watermark it has computed has elapsed. Beams default windowing configuration tries to determine when all data has arrived based on the type of data source, and then advances the watermark past the end of the window. This default configuration does not allow late data. The default behavior is to trigger at the watermark. If you don't specify a trigger, you are actually using the trigger after watermark. After watermark is an event time trigger. The message's time stamps are used to measure time with these triggers. But we could also add custom triggers.
- The watermark is the relationship between the processing timestamp and the event timestamp. The processing timestamp is the moment the message arrives at the pipeline. Ideally, the both should be the same with no delays. However, this rarely happens. Any message that arrives before the watermark is set to be Everly. If it arrives right after the watermark is said to be on time and if it arrives later, then it is late data.

    ![image](https://user-images.githubusercontent.com/19702456/226929266-404bc908-c88f-4e0c-a7e5-0e740fbe7643.png)

    ![image](https://user-images.githubusercontent.com/19702456/226929604-0cc56331-7a73-4bc5-8115-b046c5cb8ecf.png)
- Apache Beam uses a number of heuristics to make an educated guess about what the watermark is. Instead of using general-purpose heuristics, pipeline designers need to thoughtfully consider the following questions in order to determine what tradeoffs are appropriate:
  - Completeness: How important is it to have all of your data before you compute your result?
  - Latency: How long do you want to wait for data? For example, do you wait until you think you have all data, or do you process data as it arrives?
  - Cost: How much compute power and money are you willing to spend to lower the latency?


> ### Triggers
- When collecting and grouping data into windows, Beam uses triggers to determine when to emit the aggregated results of each window (referred to as a pane).
- Triggers determine at what point during processing time results will be materialized. Each specific output for a window is referred to as a pane of the window. Triggers fire panes when the trigger’s conditions are met. In Apache Beam, those conditions include watermark progress, processing time progress (which will progress uniformly, regardless of how much data has actually arrived), element counts (such as when a certain amount of new data arrives), and data-dependent triggers, like when the end of a file is reached.
- A trigger’s conditions may lead it to fire a pane many times. When you trigger the the window several times, you have to decide on the desired accumulation mode. Consequently, it’s also necessary to specify how to accumulate these results.
- Apache Beam currently supports two accumulation modes:
  - which accumulates results together
  - other which returns only the portions of the result that are new since the last pane fired.
- There are two accumulation modes in apache beam
  - accumulate:  With accumulate every time you trigger it again in the same window, the calculation is just repeated with all the messages that have been included in the window so far. If your window is very wide, using accumulate as the accumulation mode may consume considerable resources, as the accumulated output has to be stored while the window is still open.

       ![image](https://github.com/user-attachments/assets/eba2385a-37e3-4de3-aaf5-bdf1ecc02335)
    
  - discard: With discard once some messages have been used for a calculation those messages are discarded. If new messages arrive later and there is a new trigger, the result will only include the new messages and those messages will be discarded again. If the calculation you need to make with the windows is associative and commutative, you can safely update that calculation using discard mode without any loss of accuracy. The main advantage of using the discard mode is that the performance will not suffer even if you use a very wide window, because no state, no accumulation is stored for very long, only until the next trigger is released.

      ![image](https://github.com/user-attachments/assets/785a82e1-d2e8-4dc0-9225-18aa3d193357)
  
- Beam provides a number of pre-built triggers that you can set:
  - Event time triggers. These triggers operate on the event time, as indicated by the timestamp on each data element. Beam’s default trigger is event time-based.
  - Processing time triggers. These triggers operate on the processing time – the time when the data element is processed at any given stage in the pipeline.
  - Data-driven triggers. These triggers operate by examining the data as it arrives in each window, and firing when that data meets a certain property. Currently, data-driven triggers only support firing after a certain number of data elements.
  - Composite triggers. These triggers combine multiple triggers in various ways.
    
      ![image](https://user-images.githubusercontent.com/19702456/226931988-5604dea1-a983-4324-bfed-35d4e19efc5c.png)   

  
      ![image](https://github.com/user-attachments/assets/f900834b-e57c-440d-bfb1-fc4dae2a9249)


> ### Dataflow SQL
- Dataflow SQL integrates with Apache Beam SQL and supports a variant of the ZetaSQL query syntax, using SQLTransforms in a Dataflow Flex template
- It can be used as a long-running batch engine.
- Dataflow SQL is not only restricted to GCP-native services like BigQuery or Pub/Sub.
- A Dataflow Template can be implemented using either Calcite SQL or ZetaSQL dialects.


> ### Dataflow Snapshots
- Dataflow snapshots saves the state of streaming pipeline
- Restart a pipeline without reprocessing in-flight data
- No data loss with minimal downtime
- Option to create a snapshot with pub/sub source 
- However, Dataflow Snapshots cannot help migrate to a different region in the event of a regional outage.


> ### Dataflow Templates
- Templates allow you to call data flow pipelines by making an API call without the fuss of installing runtime dependencies in your development environment.
- Classic Templates: staged as execution graphs on Cloud Storage
- Flex Templates: package the pipeline as a docker image and stage these images on your project's container registry or artifact registry 

- Classic Templates Challenges:
  - Value providers support for beam IO transforms.
  - lack of support for dynamic DAG.

   ![image](https://github.com/user-attachments/assets/4b9064b0-ee1d-49c6-8585-b579116548af)


> ### Dataflow Deployment strategy

  ![image](https://user-images.githubusercontent.com/19702456/226887738-61e7b35b-8f34-4367-8786-644ed6b8b155.png)
  
-  if it's the first time deploying the pipeline, there's no existing state to consider. So you just deploy the pipeline
-  If there's an existing pipeline, and you want to update it, you should take a snapshot of your pipeline.This ensures that you have a working state you can revert your pipeline to if you observe an issue with your new deployment.Once you’ve taken a snapshot, you’re ready to update your job. You need to account for any changes to the names of the pipeline's transformations by providing the mapping from old names to the new.If the updated pipeline is compatible, the update will succeed, and you'll get a new pipeline in place of the old, without losing the state of the previous version of the pipeline.
-  If the update is not possible, then you’ll need to choose between drain and cancel options. If you can replay the source, then you can choose to cancel the pipeline, which will drop any in-flight data.You can then deploy the new pipeline, and replay the data from the source. If replay is not possible, then you can drain the pipeline. Ingestion stops immediately, windows are closed, and processing of in flight elements will be allowed to complete. This will not lose data, but you may end up with incomplete aggregations in your output sink.Once the pipeline has been drained, you can relaunch the pipeline.

    ![image](https://user-images.githubusercontent.com/19702456/226887770-31f995d2-b42f-4fc8-811d-1e4170d763af.png)


> ### Dataflow Performace
- Key Space and Parallelism: the maximum amount of parallelism is determined by the number of keys. More machines will not be able to do any more work if key space is limited.
  - Too many keys: If the key space is very large, consider using hashes separating keys out internally. This is especially useful if keys carry date/time information. In this case you can "re-use" processing keys from the past that are no longer active, essentially for free.
  - Limited keyspace will make it hard to share workload, and per-key ordering will kill performance. Increase number of keys eg. if windows are distinct, use composite(window + keys) keys. If reading from files, prefer reading from splittable compression formats like Avro
- Consider using combine when you can instead of GroupByKey, especially if your data is heavily skewed.


> ### Dataframe differences from standard Pandas
- Operations are deferred, and the result of a given operation may not be available for control flow or interactive visualizations. For example, you can compute a sum, but you can't branch on the result.
- Result columns must be computable without access to the data. For example, you can't use transpose.
- PCollections in Beam are inherently unordered, so Pandas operations that are sensitive to the ordering rows are unsupported. For example, head and tail are not supported. 






-----------------------------



  

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
![image](https://github.com/user-attachments/assets/c000bdeb-abe1-4ee9-8c95-49a7731458d2)

  

- When a Dataflow job is created, a cloud storage bucket is used to store binary files containing pipeline code. A cloud storage bucket is also used to temporarily store export or import data. By default, when data is stored in any of these locations, a Google-managed key is used to encrypt the data. When your pipeline starts and the data is loaded into the worker memory, data keys used in key-based operations, such as windowing, grouping, and joining, will be decrypted using your CMEK keys. Using CMEK requires both the Dataflow service account and the Controller Agent service account to have the cloud KMS CryptoKey Encrypter/Decrypter role. When you launch a job that uses CMEK, the region for your key and the regional input for your Dataflow job must be the same.
While the job is running, persistent disks attached to Dataflow workers are used for persistent disk-based shuffle and streaming state storage. If a batch job is using Dataflow Shuffle, the backend stores the batch pipeline state during execution. If a job is using Dataflow Streaming Engine, the backend stores the streaming pipeline state during execution. By default, when data is stored in any of these locations, a Google-managed key is used to encrypt the data.

    ![image](https://user-images.githubusercontent.com/19702456/226963260-a4cb6ad1-d144-4794-854c-42cabeadeb0f.png)

    A pipeline identifies the data to be processed and the actions to be taken on the data. The data is held in a distributed data abstraction called a P collection. The P collection is immutable. Any change that happens in a pipeline ingests one P collection and creates a new one. It does not change the incoming P collection. The action or code is contained in an abstraction called a P transform. P transform handles input, transformation, an output of the data. The data in the P collection is passed along a graph from one P transform to another. Pipeline runners are analogous to container hosts such as Google Kubernetes Engine. The identical pipeline can be run on a local computer, data center VM, or on a service such as Dataflow in the Cloud. The services the runner uses to execute the code is called a backend system. A P collection represents both streaming data and batch data. There is no size limit to a P collection. Streaming data is an unbounded P collection that doesn't end. Each element inside a P collection can be individually accessed and processed. Elements represent different data types. In a P collection, all data types are stored in a serialized state as byte strings. This way, there is no need to serialize data prior to network transfer and deserialize it when it is received.Instead, the data moves through the system in a serialized state and is only deserialized when necessary for the actions of a P transform.

   ![image](https://user-images.githubusercontent.com/19702456/226963349-5765d651-f9b4-42c2-8bd1-64d8ff69ce8d.png)

   ![image](https://user-images.githubusercontent.com/19702456/226964415-cf1d6c9a-7329-41c6-92f0-84bf78a52415.png)
   
   ![image](https://user-images.githubusercontent.com/19702456/226964539-2449f160-a634-456c-a8fd-6df1fa870cb1.png)

- If you are launching a private IP Dataflow job (--no_use_public_ips flag), no in-use IP address quota will be taken up.
  
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
      
    - A side input is an additional input other than main input (equivalent to a broadcast join in Datawarehouses) that your do function can access each time it processes an element in the input PCollection. When you specify a side input, you create a view of some other data that can be read from within the ParDo transform's do function while processing each element. Side inputs are useful if your ParDo needs to inject additional data when processing each element in the input PCollection, but the additional data needs to be determined at runtime and not hard coded. Such values might be determined by the input data or depend on a different branch of your pipeline. eg. Check if any given word is shorter or longer than the average word length, first we need to compute the average word length which is then fed as side input.
    <img width="383" alt="image" src="https://github.com/user-attachments/assets/600a2b21-6752-4432-a3a2-34b12f3a2ffd">
When choosing a side input pattern in Dataflow, what factors should you consider? - Both the size/update frequency of the side input and the DoFn's processing needs are crucial.
  

- When you run your pipeline on Dataflow, it uses the service account service-yourproject@dataflow-service-producer-prod.iam.gserviceaccount.com. This account is automatically created when the Dataflow API is enabled. It is assigned the Dataflow service agent role and has the necessary permissions to run a Dataflow job in your project. The controller service account is assigned to the Compute Engine VMs to run your Dataflow pipeline.
By default, workers use your project's Compute Engine default service account as the controller service account. This service account, <project-number>-compute@developer.gservices.com, is automatically created when you enable the Compute Engine API for your project from the API's page in the Google Cloud console. The Dataflow service account is responsible for the interaction happening between your project and Dataflow.

- When you launch a batch pipeline, the ratio of VMs to PDs is 1:1. For each VM, only one persistent disk is attached. For jobs running Shuffle on worker VMs, the default size of each persistent disk is 250 gigabytes. If the batch job is running using Shuffle Service, the default persistent disk size is 25 gigabytes. Streaming pipelines, however, are deployed with a fixed pool of persistent disks. Each worker must have at least one persistent disk attached to it while the maximum is 15 persistent disks per worker instance. When you run a job using the Dataflow back end, the feature that is used is Dataflow Streaming Engine. For jobs launched to execute in the worker VMs, the default persistent disk size is 400 gigabytes. Jobs launched using Streaming Engine have a persistent disk size of 30 gigabytes. It is important to note that the amount of disk allocated in a streaming pipeline is equal to the maxNumWorkers flag. For example, if you launch a job with three workers initially and set the maximum number of workers to 25, 25 disks will count against your quota and not three. For streaming jobs that do not use Streaming Engine, the maxNumWorkers flag is optional. The default is 100.

- If your pipeline sources, syncs, and staging locations are all in the same region, you will not be charged for network egress because all the info remains in the same region. If you have a pipeline with workers in northamerica-northeast and its regional endpoint is set to us-central1, your network egress charge will increase because of the metadata that is transferred between your project and the regional endpoint.

- Challenges with Processing Streaming Data
  - Scalability:  being able to handle the volume of data as it gets larger and/or more frequent.
  - Fault Tolerance: The larger you get, the more sensitive you are to going down unexpectedly.
  - Model:  is the model being used--streaming or repeated batch.
  - Timing:  latency of the data. eg. what if the network has a delay or a sensor goes bad and messages can't be sent?













# Apache Beam
- comprehensive portability framework for data processing pipelines, one that allows you to write your pipeline once in the programming language of your choice and run it with minimal effort on the execution engine of your choice.
- With Apache Beam, you can define your pipeline in popular languages like Java, Python, Go, SQL.
- With portability, every runner can work with every supported language. Containerization allows us a configurable, hermetic worker environment.
- Beam portability framework:
  - A language-agnostic way to represent pipelines
  - A set of protocols for executing pipelines
- To use the portability features mentioned earlier, you must use the Dataflow Runner v2. This runner is packaged together with the Dataflow Shuffle service and Streaming Engine
- To create a custom container image locally, create a Docker file in which you specify the Apache Beam image as the parent image.
![image](https://github.com/user-attachments/assets/4512b32c-7488-46a1-9954-273a48e318a3)
- Cross Language Transforms: no longer limited to a single language in a given pipeline
![image](https://github.com/user-attachments/assets/c0c6f522-32c1-4ac1-96db-3acb4f4f16d0)

# Piepline Optimization:
-  Filter data early in pipeline. Move any step that reduce data volume up in the pipeline
-  Apply data transformations serially to let dataflow optimize the DAG. Whenever transformations are applied serially, they can be merged together in single stage, enabling them to be processed in the same worker nodes and reducing costly IO network operations.
-  Enabling auto scaling for Dataflow pipelines is also a good idea. If for some reason your external system is backlogged, your Dataflow pipeline can scale down instead of underutilizing pipeline resources.

> ### Beam SQL
- Works with Stream and Batch Pipeline
- Your SQL query is embedded using SQLTransforms, an encapsulated segment of a Beam pipeline similar to PTransforms, which can be mized with PTransform
- It also supports User-Defined Functions. 
- Supports multiple dialects:
  - Beam Calcite SQL: The Beam Calcite SQL is a variant of Apache Calcite, a dialect widespread in big data processing, compatible with Apache Flink SQL. supports Java UDFs
  - Google ZetaSQL: Beam ZetaSQL is more compatible with BigQuery, so it’s especially useful in pipelines that write to or read from BigQuery tables.
-  it integrates Schema PCollections
-  supports windowing when aggregating unbounded data

## Testing
We use unit tests in Beam to assert behavior of one small testable piece of your production pipeline. These small portions are usually either individual DoFns or PTransforms. These tests should complete quickly, and they should run locally with no dependencies on external systems. Beam uses JUnit 4 for unit testing. Test pipeline is a class included in the beam SDK specifically for testing transforms.







