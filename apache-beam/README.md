# Apache Beam

- Apache Open Source Project started in 2016
- Unified programming model (process both batch and streaming data) that can build portable big data pipeline
- Batch + Stream = Beam
- Supports Python, Java, Go
- A pipeline is a graph of transformations that a user constructs that defines the data processing they want to do. Once pipeline is created, it can be excuted on any execution framework - Spark, Flink, Apex, Cloud Dataflow
- Installation
    - Local
    ```
    pip install apache-beam
    pip install apache-beam[gcp]
    ```
    - Use [Colab](https://colab.research.google.com)
    - Use Notebook from GCP Dataflow

- Concepts
    - Pcollection
      - Data is held on a distributed data instruction called a P collection. Fundamental data type in Beam.
      - A P collection is immutable.
        
    - Ptransform
      - The [operations](https://beam.apache.org/documentation/programming-guide/#transforms) executed within a pipeline
      - The actions are contained in an instruction called a P transform. A P transform handles input, transformation and output of the data.
    
    - Runner
      - Pipeline runners are analagous to container hosts, such as Kubernetes Engine. These are Execution engine
      - The integral pipeline can be run on a local computer, in a virtual machine, in a data center or in a service in the cloud, such as Dataflow.
        
    - In Apache Beam, transforms are done by the PTransform class. At runtime, these operations will be performed on a number of independent workers. The input and output to every PTransform is a PCollection. 
    - ParDo is a Beam transform for generic parallel processing. The ParDo processing paradigm is similar to the “Map” phase of a Map/Shuffle/Reduce-style algorithm: a ParDo transform considers each element in the input PCollection, performs some processing function (your user code) on that element, and emits zero, one, or multiple elements to an output PCollection
    - There are two kinds of root transforms in the Beam SDKs: Read and Create.
        - Read transforms read data from an external source, such as a text file or a database table.
        - Create transforms create a PCollection from an in-memory list and are especially useful for testing. The process/process Element method of a DoFn be called as many times as there are elements in the PCollection.
    ![image](https://user-images.githubusercontent.com/19702456/226645917-ea418df1-d894-4b12-be51-7643ad9ef04e.png)

    - Input --> PTranform --> Output . The input and output to Ptranform is PCollection

![image](https://github.com/user-attachments/assets/4ce70762-2d40-4aab-be1e-8abde3f76114)

- Transforms
    - ParDo: ParDo lets you apply a function to each one of the elements of a P collection.
    - Combine: If your group is very large or the data is very skewed, you have a so-called hotkey and you're going to apply a commutative and associative operation, you can use Combine instead. Combine will make the transformation in a hierarchy of several steps. For large groups, this will have much better performance than GroupByKey.
    - GroupByKey: GroupByKey let you join two P collections by a common key. With GroupByKey, you put all the elements with the same key together in the same worker. You can create a left or right, outer join, inner join and so on using GroupByKey.
    - Flatten: Flatten also receives two or more input P collections and fuses them together. If two P collections contain exactly the same type, they can be fused together in just one P collection using the Flatten transform.
    - Partition: It divides your P collection into several output P collections by applying a function that assigns a group to ID each element in the input P collection.

> References
- [Apache Beam Documentation](https://beam.apache.org/documentation/)
