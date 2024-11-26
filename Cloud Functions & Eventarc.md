# Cloud Function

- Fully managed serverless execution environment
- Scalable functions-as-a-service (FaaS) platform
- Can be invoked directly from an HTTP request or event
- Build small micro service
- Auto scaling as traffic increase
- Events are triggered from
  - Cloud Storage
  - Cloud Pub/Sub
  - HTTP POST/GET/DELETE/PUT/OPTIONS
  - Firebase
  - Cloud Firestore
  - Stack driver logging
- 2 product versions
  - Cloud Functions (1st gen): First version
  - Cloud Functions (2nd gen): New version built on top of Cloud Run and Eventarc


- Pay only for what you use
  - Number of invocations
  - Compute time of the invocations
  - Memory and CPU provisioned
    
- Key Enhancements in 2nd gen:
  - Longer Request timeout: Up to 60 minutes for HTTP-triggered functions
  - Larger instance sizes: Up to 16GiB RAM with 4 vCPU (v1: Up to 8GB RAM with 2 vCPU)
  - Concurrency: Upto 1000 concurrent requests per function instance (v1: 1 concurrent request per function instance)
  - Multiple Function Revisions and Traffic splitting supported (v1: NOT supported)
  - Support for 90+ event types - enabled by Eventarc (v1: Only 7)
  - With Eventarc, event-driven functions can be triggered from more than 125 Google, external SaaS event sources, and custom sources by publishing to Pub/Sub.



# Cloud Run Functions

- Cloud Run functions allow you to execute code in response to various Google Cloud events. These events can originate from sources like HTTP requests, Pub/Sub messages, Cloud Storage changes, Firestore updates, or custom events through Eventarc.
- When triggered, a Cloud Run function provides a serverless execution environment where your code runs, supporting multiple programming languages for flexibility.

  ![image](https://github.com/user-attachments/assets/a986f985-c895-49f8-b307-08139ce84985)


  # Eventarc

- Eventarc offers a standardized solution to manage the flow of state changes, called events, between decoupled microservices. An event is a data record expressing an occurrence and its context. For example, an event might be a change to data in a database, a file added to a storage system, or a scheduled job.
- Eventarc offers a standardized solution to manage the flow of state changes, called events, between decoupled microservices. When triggered, Eventarc routes these events to various destinations (Event destinations) while managing delivery, security, authorization, observability, and error-handling for you.
- Eventarc enables deep monitoring of logging and other events which occur less frequently on Google Cloud.
- Eventarc connects various event sources, including Google Cloud services, third-party systems, and custom events via Pub/Sub to a range of event targets like Cloud Run functions, and more.

  ![image](https://github.com/user-attachments/assets/c910dcfd-3b86-4c68-a28d-d7df47bfeb60)
  


