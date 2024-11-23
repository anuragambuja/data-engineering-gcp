# Cloud Function
- Server less
- Fully managed
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


# Cloud Run Functions

- Cloud Run functions allow you to execute code in response to various Google Cloud events. These events can originate from sources like HTTP requests, Pub/Sub messages, Cloud Storage changes, Firestore updates, or custom events through Eventarc.
- When triggered, a Cloud Run function provides a serverless execution environment where your code runs, supporting multiple programming languages for flexibility.

  ![image](https://github.com/user-attachments/assets/a986f985-c895-49f8-b307-08139ce84985)
