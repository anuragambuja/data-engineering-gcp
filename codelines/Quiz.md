# Dataflow
1. Select options we can use to mitigate data skew in Dataflow pipelines?
  A. Add composite windows and triggers.
  B. Use Dataflow shuffle for batch pipelines and Dataflow streaming option for streaming pipelines.
  C. Add more worker machines.
  D. Use api like “withFanout” or “withHotKeyFanout”.
Ans. D. “withFanout” or “withHotKeyFanout” API can be used to provision more resources for hot keys.

2. Which one of the following is not a consideration for designing performant pipelines in Dataflow?
  A. Coders and decoders used in pipeline.
  B. SDK used for developing the pipeline.
  C. Filtering data early.
  D. Logging
Ans: B. SDK is selected based on other relevant requirements like developer skills, libraries used etc.

3. When we should avoid fusion in a Dataflow pipeline?
  A. Never
  B. Only in specific scenarios, like if your pipeline involves massive fanouts.
  C. Always
Ans: B. A pipeline involving massive fanout operations is one such scenario.

4. Using anonymous subclasses in your ParDos is an anti-pattern because:
  A. ParDos are required to contain a concrete subclass of a DoFn.
  B. Anonymous subclasses are bad for the performance of your pipeline.
  C. Anonymous subclasses are harder to test than concrete subclasses.
Ans. C. Anonymous subclasses are more difficult to test because of their lack of identifiability, coupling, and reusability.

5. When draining a streaming pipeline, what should you expect to happen?
  A. A snapshot is taken of the source, then ingestion is stopped. Windows are closed and processing of in-flight elements will be allowed to complete.
  B. Ingestion stops immediately, windows are closed, and processing of in flight elements will be allowed to complete.
  C. Any open windows will wait for new data so that aggregations are completed. Then the pipeline will be canceled.
  D. Both processing and ingestion stop immediately.
Ans. B

4.
  A.
  B.
  C.
  D.
Ans. 

4.
  A.
  B.
  C.
  D.
Ans. 

4.
  A.
  B.
  C.
  D.
Ans. 

4.
  A.
  B.
  C.
  D.
Ans. 

4.
  A.
  B.
  C.
  D.
Ans. 

4.
  A.
  B.
  C.
  D.
Ans. 

4.
  A.
  B.
  C.
  D.
Ans. 
