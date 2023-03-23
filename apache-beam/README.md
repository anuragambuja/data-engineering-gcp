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
    - Pcollection - Fundamental data type in Beam
    - Ptransform - The [operations](https://beam.apache.org/documentation/programming-guide/#transforms) executed within a pipeline - 
    - Runner - Execution engine
    - In Apache Beam, transforms are done by the PTransform class. At runtime, these operations will be performed on a number of independent workers. The input and output to every PTransform is a PCollection. 
    - ParDo is a Beam transform for generic parallel processing. The ParDo processing paradigm is similar to the “Map” phase of a Map/Shuffle/Reduce-style algorithm: a ParDo transform considers each element in the input PCollection, performs some processing function (your user code) on that element, and emits zero, one, or multiple elements to an output PCollection
    - There are two kinds of root transforms in the Beam SDKs: Read and Create. Read transforms read data from an external source, such as a text file or a database table. Create transforms create a PCollection from an in-memory list and are especially useful for testing.
    ![image](https://user-images.githubusercontent.com/19702456/226645917-ea418df1-d894-4b12-be51-7643ad9ef04e.png)

    - Input --> PTranform --> Output . The input and output to Ptranform is PCollection

> References
- [Apache Beam Documentation](https://beam.apache.org/documentation/)
