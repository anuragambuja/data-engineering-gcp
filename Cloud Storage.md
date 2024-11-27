
# Cloud Storage 

   ![image](https://github.com/user-attachments/assets/5937ad7a-6ea4-4620-8a2e-b2c4f0832fc2)

- Object storage solution in GCP with no minimum Object Size and 5TB as max size. The objects stored have an ID, metadata, attributes, and the actual data.
- High Durability – 99.999999999% annual
- Cloud Storage supports multithreaded, resumable loads. 
- Retention Policy defines the minimum duration for which bucket will be protected from deletion or modification of objects.
- Global unique name for bucket.
- Object are immutable and can be versioned. Object Versioning helps to prevent accidental deletion of object. It is enabled/disabled at bucket level. When Object Versioning is enabled, you can list archived versions of an object, restore the live version of an object to an older state, or permanently delete an archived version, as needed. You can turn versioning on or off for a bucket at any time. Turning versioning off leaves existing object versions in place and causes the bucket to stop accumulating new archived object versions.
- Choosing a region close to where the data will be processed will reduce latency. And if you are processing the data using cloud services within the region, it will save you on network egress charges. For a multi-region bucket, the objects are replicated across regions. And for a single-region bucket, the objects are replicated across zones. In any case, when the object is retrieved, it is served up from the closest replica to the requester, and that is how low latency occurs. Multiple requesters could be retrieving the objects at the same time from different replicas, and that is how high throughput is achieved.
- Normally, deleting an object cannot be undone. Soft delete provides bucket-level protection against accidental or malicious deletion by retaining recently deleted objects for a retention period that you select—seven days by default, which can be increased up to 90 days or be disabled altogether


> ## Storage Class
- How frequently access data ?
  
	![image](https://user-images.githubusercontent.com/19702456/222905739-d7f76fb3-d1db-4625-95f5-1ad3473b26a4.png)

	![image](https://github.com/user-attachments/assets/6be28b8c-b1c8-4ddc-af56-5186a074b376)


> ## Autoclass 
- The Autoclass feature automatically transitions objects in your bucket to appropriate storage classes based on each object's access pattern.
- The feature moves data that is not accessed to colder storage classes to reduce storage cost and moves data that is accessed to Standard storage to optimize future accesses.
- All objects added to the bucket begin in Standard storage, even if a different storage class is specified in the request.
- By default, the terminal storage class for Autoclass is Nearline storage, which means objects transition to Nearline storage and remain in that storage class until they're accessed. Optionally, you can configure Autoclass so that the terminal storage class is Archive storage.
- Objects smaller than 128 KiB don't transition to colder storage classes. Instead, they are permanently stored in Standard storage. Only object data, not object metadata, is considered when determining whether the object is smaller than 128 KiB.
- Soft-deleted objects retain their existing storage classes until the end of their retention duration. When a soft-deleted object is restored, the resulting object begins in Standard storage, regardless of the storage class of the soft-deleted object.
- When an object's data is read, the object transitions to Standard storage if it's not already stored in Standard storage. Reading or editing an object's metadata does not cause the object to transition to Standard storage. Any object that isn't accessed for 30 days transitions to Nearline storage.
	- Any object that isn't accessed for 90 days transitions to Coldline storage. Such objects spent at least 30 days in Standard storage and 60 days in Nearline storage.
	- Any object that isn't accessed for 365 days transitions to Archive storage. Such objects spent at least 30 days in Standard storage, 60 days in Nearline storage and 275 days in Coldline storage. 
- There is no Class A operation charge when Autoclass transitions an object from Nearline storage to Standard storage. When Autoclass transitions an object from Coldline storage or Archive storage to Standard storage or Nearline storage, each such transition incurs a Class A operation charge.


> ## Lifecycle management
- Object Lifecycle: What action like delete or transition to different storage class should be performed based on certain condition like age or type of object
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
- Object inspection occurs in asynchronous batches, so rules may not be applied immediately. Also, updates to your lifecycle configuration may take up to 24 hours to go into effect.


> ## Data Security
  - By default 100% of data in Cloud Storage is automatically encrypted at rest and in transit with no configuration required by customers.
  - Two levels of encryption. First, the data is encrypted using a data encryption key. Then the data encryption key itself is encrypted using a key encryption key, or KEK. The KEKs are automatically rotated on a schedule, and the current KEK is stored in Cloud KMS, Cloud Key Management Service.
	  - Google managed Encryption keys (GMEK): No Configuration and Fully managed by Google
	  - Customer managed Encryption keys (CMEK) via Google Cloud Key Management Service (KMS): You can define access controls to encryption keys, establish rotation policies, and gather additional logging into encryption/decryption activities. In both the default and customer-managed case, Google remains the root of trust for encryption/decryption activities.
	  - Customer supplied Encryption keys (CSEK): Using CSEK comes with some additional risk of data loss, as Google cannot help you decrypt data if you lose your encryption keys. CSEK only available for Cloud Storage and Compute Engine

	![image](https://user-images.githubusercontent.com/19702456/222905716-a129c097-4409-4e49-babf-97a12ef02bbb.png)


> ## Controlling access
- IAM is standard across the Google Cloud. It is set at the bucket level and applies uniform access rules to all objects within a bucket. Access control lists can be applied at the bucket level or on individual objects, so it provides more fine-grained access control. IAM provides project roles and bucket roles, including bucket reader, bucket writer and bucket owner. The ability to create or change access control lists is an IAM bucket role and the ability to create and delete buckets and to set IAM policy is a project level role. When you create a bucket, you are offered the option of disabling access lists and only using IAM. You can disable access lists even if they were in-force previously. As an example, you might give some bob@example.com reader access to a bucket through IAM, and also give them write access to a specific file in that bucket through access control lists.
	- Uniform level access
		- Apply at Bucket level
		- No Object level permission
		- Apply uniform at all object inside bucket
	- Fine grained permission
		- Legacy access control method
		- Access Control List – ACL For Each object Separately
	- Signed URL
		- Temporary access
		- you can give read or write access on objects to user who doesn’t have Google Account.
		- URL expired after time period defined.
		- Max period for which URL is valid is 7 days.
    
		```
		pip install pyopenssl
		gsutil signurl -d 10m -u gs://<bucket>/<object>
		```
	- Signed Policy Documnets
		- Specify what can be uploaded to a bucket
		- Control - Size, Type and other upload characteristics

- An ACL is a mechanism you can use to define who has access to your buckets and objects, as well as what level of access they have. The maximum number of ACL entries you can create for a bucket or object is 100. Each ACL consists of one or more entries, and these entries consist of two pieces of information:
	- A scope, which defines who can perform the specified actions (for example, a specific user or group of users).
	- And a permission, which defines what actions can be performed (for example, read or write).


