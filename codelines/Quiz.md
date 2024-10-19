# Dataflow

1. Select options we can use to mitigate data skew in Dataflow pipelines?
  A. Add composite windows and triggers.
  B. Use Dataflow shuffle for batch pipelines and Dataflow streaming option for streaming pipelines.
  C. Add more worker machines.
  D. Use api like “withFanout” or “withHotKeyFanout”.
Ans. D. “withFanout” or “withHotKeyFanout” API can be used to provision more resources for hot keys.

3. Which one of the following is not a consideration for designing performant pipelines in Dataflow?
  A. Coders and decoders used in pipeline.
  B. SDK used for developing the pipeline.
  C. Filtering data early.
  D. Logging
Ans: B. SDK is selected based on other relevant requirements like developer skills, libraries used etc.

4. When we should avoid fusion in a Dataflow pipeline?
  A. Never
  B. Only in specific scenarios, like if your pipeline involves massive fanouts.
  C. Always
Ans: B. A pipeline involving massive fanout operations is one such scenario.

5. Using anonymous subclasses in your ParDos is an anti-pattern because:
  A. ParDos are required to contain a concrete subclass of a DoFn.
  B. Anonymous subclasses are bad for the performance of your pipeline.
  C. Anonymous subclasses are harder to test than concrete subclasses.
Ans. C. Anonymous subclasses are more difficult to test because of their lack of identifiability, coupling, and reusability.

6. When draining a streaming pipeline, what should you expect to happen?
  A. A snapshot is taken of the source, then ingestion is stopped. Windows are closed and processing of in-flight elements will be allowed to complete.
  B. Ingestion stops immediately, windows are closed, and processing of in flight elements will be allowed to complete.
  C. Any open windows will wait for new data so that aggregations are completed. Then the pipeline will be canceled.
  D. Both processing and ingestion stop immediately.
Ans. B

7. You want to launch a streaming Dataflow job in europe-west4 and want to protect your pipeline from zonal stockouts. Which launch command will achieve these requirements?
  A. $ python3 -m apache_beam.examples.wordcount \ --input gs://dataflow-samples/shakespeare/kinglear.txt \ --output gs://$BUCKET/results/outputs --runner DataflowRunner \ --project $PROJECT --temp_location gs://$BUCKET/tmp/ \ --region europe-west4
  B. $ python3 -m apache_beam.examples.wordcount \ --input gs://dataflow-samples/shakespeare/kinglear.txt \ --output gs://$BUCKET/results/outputs --runner DataflowRunner \ --project $PROJECT --temp_location gs://$BUCKET/tmp/ \ --region europe-west4 --worker_zone europe-west4-b
  C. $ python3 -m apache_beam.examples.wordcount \ --input gs://dataflow-samples/shakespeare/kinglear.txt \ --output gs://$BUCKET/results/outputs --runner DataflowRunner \ --project $PROJECT --temp_location gs://$BUCKET/tmp/ 
Ans. A. if you specify the region without any zonal specification, the Dataflow service will select the best zone within the region based on the available zone capacity at the time of the job creation request. This adds a degree of protection from being affected by zonal stockouts.

8. How long is the retention for Dataflow Snapshots?
  A. Seven days
  B. Indefinitely
  C. Three days
Ans. A. If you schedule a Dataflow snapshot at least once a week, you can ensure that you never lose data in the event of an outage.

9. Which of the following is a challenge associated with classic templates?
  A. Increased latency while launching templates.
  B. Lack of support for runtime parameters.
  C. Lack of support for Dynamic DAG (Directed Acyclic Graph).
Ans. C. Since DAG is generated during template construction, the graph cannot change based on the runtime options.

10. Into which of the following categories are the Google-provided templates classified?
  A. Streaming and utility only
  B. Batch, streaming, and utility
  C. Batch and streaming only
  D. Batch and utility only
Ans.  B.
 
11. How are Flex Templates packaged?
  A. Jar/Pex
  B. Docker image
  C. Tar file
  D. ProtoBuf binary
Ans.  B. Flex Templates packages pipeline artifacts into a docker image.

12. Which two of the following statements are true for failures while building the pipeline?
  A. The failure is reproducible with the Direct Runner.
  B. The failure can be caused by insufficient permissions granted to the controller service account.
  C. The error message is visible in Dataflow.
  D. The failure can be caused by incorrect input/output specifications.
Ans. A & D. 

13. Your Dataflow batch job fails after running for close to 5 hours. Which two of the following troubleshooting steps would you take to understand the root cause of the failure?
  A. Investigate the wall time of the individual steps in the job.
  B. Check the Dataflow worker logs for warnings or errors related to work item failures.
  C. Monitor the Data Freshness and System Latency graphs to understand the job performance
  D. Log the failing elements and check the output using Cloud Logging.
Ans. B & D

14. Your batch job has failed, and when viewing the Diagnostic tab, you see the following insights:
    - Out of memory: Kill process
    - Shutting down JVM after consecutive periods of measured GC thrashing
  Which of the options below is the best one to undertake to resolve the issue?
  A. Use a larger machine size
  B. Increase persistent disk size
  C. Increase the number of machines used
  D. Switch Beam code from Java to Python
Ans. A.

15. Select all that apply - the BigQuery Jobs tab shows jobs from:
  A. Load jobs
  B. Streaming Inserts
  C. Streaming Extracts
  D. Query jobs
Ans. A & D

16. You have a Pub/Sub subscription with data that hasn’t been processed for 3 days. You set up a streaming pipeline that reads data from the subscription, does a few Beam transformations, and then sinks to Cloud Storage. When the pipeline is launched, it is able to read from Pub/Sub, but cannot sink data to Cloud Storage due to the service account missing permissions to write to the bucket. When viewing the Job Metrics tab, what do you expect to see in the data freshness graph?
  A. Initial start point at 3 days, with a downward sloping line.
  B. Initial start point at 3 days, with an upward sloping line.
  C. Initial start point at 3 days, with a flat horizontal line.
  D. Initial start point at 0 days, with an upward sloping line to 3 days and beyond.
Ans. B.

17. You would like to set up an alerting policy to catch whether the processed data is still fresh in a streaming pipeline. Which metrics can be used to monitor whether the processed data is still fresh?
  A. job/is_failed
  B. job/per_stage_data_watermark_age
  C. job/system_lag
  D. job/data_watermark_age
Ans. B & D

18.
  A.
  B.
  C.
  D.
Ans.

19.
  A.
  B.
  C.
  D.
Ans.

20.
  A.
  B.
  C.
  D.
Ans. 
