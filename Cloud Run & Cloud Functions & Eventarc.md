# Cloud Run

  ![image](https://github.com/user-attachments/assets/23567de6-de08-4402-9af8-f224dc840a9e)

- fully managed serverless platform that allows you to easily create applications seamlessly
- It takes care of everything behind the scenes, from setting up servers to automatically scaling your app based on demand. 
- only pay when code is running


# Cloud Function

  ![image](https://github.com/user-attachments/assets/9a66d324-9d3e-4253-b8c4-6aa1c8494e40)

- Cloud functions allow you to execute code in response to various Google Cloud events. These events can originate from sources like HTTP requests, Pub/Sub messages, Cloud Storage changes, Firestore updates, or custom events through Eventarc.
- Event-driven service runs your code only when specific things happen, like a file upload or a database change.
- Fully managed serverless execution environment.
- Scalable functions-as-a-service (FaaS) platform.
- Can be invoked directly from an HTTP request or event. Events are triggered from
  - Cloud Storage
  - Cloud Pub/Sub
  - HTTP POST/GET/DELETE/PUT/OPTIONS
  - Firebase
  - Cloud Firestore
  - Stack driver logging

- Pay only for what you use
  - Number of invocations
  - Compute time of the invocations
  - Memory and CPU provisioned

- 2 product versions
  - Cloud Functions (1st gen): First version
  - Cloud Functions (2nd gen): New version built on top of Cloud Run and Eventarc. Key Enhancements in 2nd gen:
    - Longer Request timeout: Up to 60 minutes for HTTP-triggered functions
    - Larger instance sizes: Up to 16GiB RAM with 4 vCPU (v1: Up to 8GB RAM with 2 vCPU)
    - Concurrency: Upto 1000 concurrent requests per function instance (v1: 1 concurrent request per function instance)
    - Multiple Function Revisions and Traffic splitting supported (v1: NOT supported)
    - Support for 90+ event types - enabled by Eventarc (v1: Only 7)
    - With Eventarc, event-driven functions can be triggered from more than 125 Google, external SaaS event sources, and custom sources by publishing to Pub/Sub.

> ### Cloud Run Functions
- When triggered, a Cloud Run function provides a serverless execution environment where your code runs, supporting multiple programming languages for flexibility.

     <img src="https://github.com/user-attachments/assets/a986f985-c895-49f8-b307-08139ce84985" width="500" >


# Eventarc

- Eventarc offers a standardized solution to manage the flow of state changes, called events, between decoupled microservices. An event is a data record expressing an occurrence and its context. For example, an event might be a change to data in a database, a file added to a storage system, or a scheduled job. When triggered, Eventarc routes these events to various destinations (Event destinations) while managing delivery, security, authorization, observability, and error-handling for you.
- Eventarc enables deep monitoring of logging and other events which occur less frequently on Google Cloud.
- Eventarc connects various event sources, including Google Cloud services, third-party systems, and custom events via Pub/Sub to a range of event targets like Cloud Run functions, and more.

     ![image](https://github.com/user-attachments/assets/c910dcfd-3b86-4c68-a28d-d7df47bfeb60)

- Eventarc is offered in two editions:
  - Eventarc Advanced: It lets you collect events that occur in a system and publish them to a central bus. Interested services can subscribe to specific messages by creating enrollments. You can use the bus to route events from multiple sources in real time and publish them to multiple destinations, and optionally transform events prior to delivery to a target. By providing administrators with enhanced and centralized visibility and control, Eventarc Advanced enables organizations to connect multiple teams across different projects.

    <img src="https://github.com/user-attachments/assets/ea47f250-6fe8-46ea-bb00-1832660f161b" width="700" height="400">

  - Eventarc Standard: Eventarc Standard is recommended for applications where the focus is on simply delivering events from event provider to event destination. It lets you quickly and easily consume Google events by defining triggers that filter inbound events according to their source, type, and other attributes, and then route them to a specified destination.

    <img src="https://github.com/user-attachments/assets/bc6ace70-b822-4ab2-a549-15ffcd604c04" width="700" height="400" >

