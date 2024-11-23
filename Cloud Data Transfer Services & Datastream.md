# Cloud Data Transfer Services

  ![image](https://github.com/user-attachments/assets/b27488b4-2c16-472d-baf4-1a630bc087d2)

- Google provides a range of data transfer methods to get data into the Cloud
  - Web console, gsutil, gcloud storage, REST API
  - Storage Transfer Service: service specifically built to bring files and objects into Google Cloud Storage
  - BigQuery Data Transfer Service: specifically bring data into big query tables
  - Transfer Appliance: physical object that is sent to a customer's location. Once data transfer is complete, the appliance is erased per NIST 800-88 standards for media sanitization. The Transfer Appliance has two modes:
    - Offline transfer: Data is copied to the appliance until it is full. The appliance is shipped back to Google and the copied data is moved to your Cloud Storage bucket.
    - Online transfer: Data copied to the appliance is streamed to your Cloud Storage bucket. After the data is uploaded to your Cloud Storage bucket, it is removed from the appliance. Online transfer compresses and encrypts the data in transit and accelerates data transfer compared to gsutil and other command-line tools. You can toggle between offline and online mode



## Datastream

  ![image](https://github.com/user-attachments/assets/afc94e3d-a840-4b6c-83f5-cb313a21399c)

  ![image](https://github.com/user-attachments/assets/ae85c89c-bf75-4e48-b04f-e1d4dce3fa28)

- Datastream provides seamless replication from operational databases directly into BigQuery, reliably and with minimal latency, to support real-time analytics, enhance operational efficiencies, and improve customer experiences
- supports direct replication into BigQuery for analytics
- allows custom data processing in Dataflow before loading into BigQuery
- facilitates event-driven architectures
- eg. Datastream can be used with Dataflow templates for seamless database replication and migration tasks

  ![image](https://github.com/user-attachments/assets/e4612ff7-8c21-4e84-8bf9-58cda20c348f)

- Datastream taps into the source database's write-ahead log (WAL) to capture and process changes for propagation downstream. Datastream supports reading the logging mechanisms for the specific source database such as LogMiner for Oracle, binary log for MySQL, PostgreSQL's logical decoding, and transaction logs from SQL Server.

![image](https://github.com/user-attachments/assets/557041a1-4178-42ce-9bdc-cf9f937c52cf)

- Datastream event messages contain two main sections: generic metadata and payload. Metadata provides context about the data, like source table, timestamps, and related information. Payload contains the actual data changes in a key-value format, reflecting column names and their corresponding values.

## Compare migration and replication options
![image](https://github.com/user-attachments/assets/d84d9a46-1e75-4a87-9691-9610c4091486)
