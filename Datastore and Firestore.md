# Datastore

- Serverless and Highly scalable NoSQL database
- Document kind data storage – MongoDB
- SQL Like Queries – GQL
- Support ACID Transactions
- Multiple indexes
- Data replication across different region
- Use case
  - Session Info
  - Product catlog
- Export data from gcloud and console
- App Engine + Datastore
- Entity Value Types
  - Atomic Values: Integers, Floats, Strings, Dates
  - Arrays
  - Entities: Entity Group is an entity and all its decendents
- Indexes
  - No Scannig. Indexes required for all queries
  - Types: Single field and Composite
  - Automatically create some indexes
    - Atomic values, ascending and descending
    - Maps and arrays also

![image](https://user-images.githubusercontent.com/19702456/224506020-6295dd2c-dfad-4ae0-9d16-14f2abd98221.png)

** You can use either Datastore or Firestore within a project but not both. 

# Firestore

- Firestore is the next generation of Datastore
- ACID Transactions
- High availability of reads and writes. Multi-region replication
- Highly scalable NoSQL database
- Collection & Document Model
- Two mode
  - native Mode: supports all Firebase features
    - Uses Firebase API
    - Not supported with older App Engine runtimes 
  - datastore mode: does not support all Firestore features like offline support for mobile devices and synchronization
- Real-time updates
- Mobile, web, and IoT apps at global scale
- Live synchronization and offline support
- Limitations of Transactions type:
   - Maximum duration of 60 seconds and 10 second idle expiration after 30 seconds
   - Modify upto 500 entities in a single transaction
   - Transaction can fail due to too many concurrent modifications, exceeds resource limits or internal error
![image](https://user-images.githubusercontent.com/19702456/224506464-e6fd2383-82f4-4aec-aa31-a1a561ffaa88.png)

- Choosing between Firestore and Bigtable
  
![image](https://github.com/user-attachments/assets/6bab4c08-0868-420d-b831-bf02b9377841)
