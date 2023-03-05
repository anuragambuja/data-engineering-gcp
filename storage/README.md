# Cloud Storage 

- Object storage solution in GCP with no minimum Object Size and 5TB as max size. 
- High Durability – 99.999999999% annual
- Cloud Storage allows world-wide storage and retrieval of any amount of data at any time. You can use Cloud Storage for a range of scenarios including serving website content, storing data for archival and disaster recovery, or distributing large data objects to users via direct download.
- Storage Class: How frequently access data ?
  - Standard
    - Good for Hot data
    - Storage Costliest
    - Access cost is very low
    - Low latency
    - SLA : 99.95% Multi/Dual and 99.9% Regional
  - Near line
    - Low Frequency access, once in a 30 days
    - Storage is Cheaper than standard
    - Access cost will increase
    - data backups long tail multimedia content or data archiving
    - SLA : 99.9% Multi/Dual and 99.0% for Regional
  - Cold line
    - Very low frequency to access 
    - Once in 90 days
    - Storage is Cheaper than Near line
    - SLA : 99.9% Multi/Dual and 99.0% for Regional
  - Archive
    - Offline data
    - Data access is once in year
    - Storage Cheapest
    - Access cost very high
    - ideal for data archiving online backup and disaster recovery 
    - No SLA
- Cloud Storage supports multithreaded, resumable loads. 
- Object Lifecycle: What action like delete or transition to different storage class should be performed based on certain condition like age or type of object
- Global unique name for bucket. Bucket level lock with data retention policy. Object are immutable and can be versioned.

- IAM is standard across the Google Cloud. It is set at the bucket level and applies uniform access rules to all objects within a bucket. Access control lists can be applied at the bucket level or on individual objects, so it provides more fine-grained access control. IAM provides project roles and bucket roles, including bucket reader, bucket writer and bucket owner. The ability to create or change access control lists is an IAM bucket role and the ability to create and delete buckets and to set IAM policy is a project level role. When you create a bucket, you are offered the option of disabling access lists and only using IAM. You can disable access lists even if they were in-force previously. As an example, you might give some bob@example.com reader access to a bucket through IAM, and also give them write access to a specific file in that bucket through access control lists.

- Encryption Options:

![image](https://user-images.githubusercontent.com/19702456/222905709-675cb9ef-c156-42fd-9d04-b4a24c6a84af.png)


![image](https://user-images.githubusercontent.com/19702456/222905711-ec1f16bb-3370-4642-8702-06d65792f90b.png)

![image](https://user-images.githubusercontent.com/19702456/222905716-a129c097-4409-4e49-babf-97a12ef02bbb.png)

![image](https://user-images.githubusercontent.com/19702456/222905728-8f1ecb68-7654-482a-912b-3ce4a50cae45.png)

![image](https://user-images.githubusercontent.com/19702456/222905733-b3806ad0-8ff9-4e2a-9395-163202b61980.png)

![image](https://user-images.githubusercontent.com/19702456/222905739-d7f76fb3-d1db-4625-95f5-1ad3473b26a4.png)

![image](https://user-images.githubusercontent.com/19702456/222905692-d380329e-cb55-4c85-95eb-c9528e0efab6.png)
