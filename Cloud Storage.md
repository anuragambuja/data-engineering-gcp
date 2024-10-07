
# Cloud Storage 

- Object storage solution in GCP with no minimum Object Size and 5TB as max size. 
- High Durability – 99.999999999% annual
- Cloud Storage allows world-wide storage and retrieval of any amount of data at any time. You can use Cloud Storage for a range of scenarios including serving website content, storing data for archival and disaster recovery, or distributing large data objects to users via direct download.
- The site, storage.cloud.google.com, uses TLS HTTPS to transport your data, which protects credentials as well as data in transit.
> Storage Class - How frequently access data ?
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
- Global unique name for bucket. Bucket level lock with data retention policy. Object are immutable and can be versioned. Choosing a region close to where the data will be processed will reduce latency. And if you are processing the data using cloud services within the region, it will save you on network egress charges.
- For a multi-region bucket, the objects are replicated across regions.And for a single-region bucket, the objects are replicated across zones. In any case, when the object is retrieved, it is served up from the closest replica to the requester, and that is how low latency occurs. Multiple requesters could be retrieving the objects at the same time from different replicas, and that is how high throughput is achieved.

- IAM is standard across the Google Cloud. It is set at the bucket level and applies uniform access rules to all objects within a bucket. Access control lists can be applied at the bucket level or on individual objects, so it provides more fine-grained access control. IAM provides project roles and bucket roles, including bucket reader, bucket writer and bucket owner. The ability to create or change access control lists is an IAM bucket role and the ability to create and delete buckets and to set IAM policy is a project level role. When you create a bucket, you are offered the option of disabling access lists and only using IAM. You can disable access lists even if they were in-force previously. As an example, you might give some bob@example.com reader access to a bucket through IAM, and also give them write access to a specific file in that bucket through access control lists.

> Encryption Options
We use two levels of encryption. First, the data is encrypted using a data encryption key. Then the data encryption key itself is encrypted using a key encryption key, or KEK. The KEKs are automatically rotated on a schedule, and the current KEK is stored in Cloud KMS, Cloud Key Management Service.
- Google managed Encryption keys
	- No Configuration
	- Fully managed
- Customer managed Encryption keys
	- Create keyring in Cloud KMS
	- key will be managed by customer. Like Key rotation
- Customer supplied Encryption keys
	- We will generate Key with : openssl rand =base64 32
	- gsutil – encrypt with CSEK

Data locking is different from encryption. Where encryption prevents someone from understanding the data, locking prevents them from modifying the data.
![image](https://user-images.githubusercontent.com/19702456/222905709-675cb9ef-c156-42fd-9d04-b4a24c6a84af.png)


![image](https://user-images.githubusercontent.com/19702456/222905711-ec1f16bb-3370-4642-8702-06d65792f90b.png)

![image](https://user-images.githubusercontent.com/19702456/222905716-a129c097-4409-4e49-babf-97a12ef02bbb.png)

> Customer supplied Encryption keys
```bash
# generate your key 
$ openssl rand -base64 32
=+kkqTwwF+yrL2+WTG2ToHN5ZuT/q8OFOXppM7jUfpbM=

# copy file to bucket
$ gsutil -o 'GSUtil:encryption_key='=+kkqTwwF+yrL2+WTG2ToHN5ZuT/q8OFOXppM7jUfpbM= cp README.txt gs://proven-audio-376216-testing

# Get the content of file
$ gsutil -o 'GSUtil:encryption_key='=+kkqTwwF+yrL2+WTG2ToHN5ZuT/q8OFOXppM7jUfpbM= cat gs://proven-audio-376216-testing/README.txt
```

![image](https://user-images.githubusercontent.com/19702456/222905728-8f1ecb68-7654-482a-912b-3ce4a50cae45.png)

![image](https://user-images.githubusercontent.com/19702456/222905733-b3806ad0-8ff9-4e2a-9395-163202b61980.png)

![image](https://user-images.githubusercontent.com/19702456/222905739-d7f76fb3-d1db-4625-95f5-1ad3473b26a4.png)

![image](https://user-images.githubusercontent.com/19702456/222905692-d380329e-cb55-4c85-95eb-c9528e0efab6.png)


> Object Versioning
- Help to prevent accidental deletion of object
- Enable/Disable versioning at bucket level
```
$ gsutil versioning get gs://proven-audio-376216-testing
gs://proven-audio-376216-testing: Suspended

$ gsutil versioning set on  gs://proven-audio-376216-testing
Enabling versioning for gs://proven-audio-376216-testing/...

$ gsutil versioning get gs://proven-audio-376216-testing
gs://proven-audio-376216-testing: Enabled

$ gsutil ls -a gs://proven-audio-376216-testing/filename.txt
$ gsutil ls -cat gs://proven-audio-376216-testing/filename.txt#12345
$ gsutil ls -rm gs://proven-audio-376216-testing/filename.txt#12345
```

## **Controlling access**

- ### **Uniform level access**
	- Apply at Bucket level
	- No Object level permission
	- Apply uniform at all object inside bucket

- ### **Fine grained permission**
	- Legacy access control method
	- Access Control List – ACL For Each object Separately

- ### **Signed URL**
	- Temporary access
	- you can give read or write access on objects to user who doesn’t have Google Account.
	- URL expired after time period defined.
	- Max period for which URL is valid is 7 days.
	
	```
	pip install pyopenssl
	gsutil signurl -d 10m -u gs://<bucket>/<object>
	```
- ### **Signed Policy Documnets**
	- Specify what can be uploaded to a bucked
	- Control - Size, Type and other upload characteristics


- Apply Project level
	- IAM
	- Different Predefined Role
		- Storage Admin
		- Storage Object Admin
		- Storage Object Creator
		- Storage Object Viewer
	- Create Custom Role
- Assign Bucket level Role
	- Select bucket & assign role too users or to other GCP services or product


## **Retention Policy**
- Minimum duration for which bucket will be protected from Deletion or modification

## **Lifecycle management**
- Based on condition what action needs to perform on object.
- Condition
	- Object age
	- Number of versions of object
	- Created Before
	- Is Live
	- Matches Storage Class
- Action
	- Transition to different storage class for high performance
		- Multi-reginal --> Nearline, Coldline, Archive
		- Standard --> Nearline, Coldline, Archive
		- Nearline --> Coldline, Archive
		- Coldline --> Archive
	- if versioned, deleting live version creates non current version but deleting non-current version deletes object permanently.

## **Pricing**

## **Cloud Transfer Service**

### **gsutil**
- Online mode of transfer
- install locally Google Cloud SDK
- gsutil -m cp large_number_of_small_files (-m for parallel upload)

### **Transfer Service**
- Transfer Jobs
	- Quickly and securely transfer data to, from, and between cloud and on-premises storage systems. Sources include Google Cloud Storage, Amazon S3, Azure Storage, filesystems, and more.
- Agent Pools
	- Agent pools enable you to transfer data to/from POSIX filesystems and from S3-compatible object storage, with control over deployment, network path, and bandwidth to optimize performance and cost. Each pool consists of one or more self-hosted agents that work in parallel to move data for a particular source or destination

### **Transfer Appliance**
- Physical device which securely transfer large amounts of data to Google Cloud Platform
- When data that exceeds 20 TB or would take more than a week to upload.

![image](https://user-images.githubusercontent.com/19702456/224366561-bced85de-a512-4aba-aea7-6801762c21a5.png)

![image](https://user-images.githubusercontent.com/19702456/224348225-b7ad8464-3a93-4b34-be45-4192827635ef.png)

![image](https://user-images.githubusercontent.com/19702456/224348396-6d69edc7-84c4-43a8-87b9-848233aa4e12.png)



## Commands
```bash
$ gsutil mb gs://bucket-name
$ gsutil cp filename gs://bucket-name
```

