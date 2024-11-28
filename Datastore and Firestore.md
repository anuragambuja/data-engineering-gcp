# Firestore

![image](https://github.com/user-attachments/assets/cc40b401-e9de-44eb-95db-320a6953d4dc)

- Firestore is a serverless, fully managed NoSQL document database that scales from zero to global scale without configuration or downtime. All of your data is stored in “documents” and then “collections”.  You can think of a document as a JSON object. It's a dictionary with a set of key-value mappings, where the values can be several different supported data types including strings, numbers or binary values. These documents are stored in collections. Documents can't directly contain other documents, but they can point to subcollections that contain other documents, which can point to subcollections, and so on. This structure brings with it a number of advantages. For starters, all queries that you make are shallow, meaning that you can grab a document without worrying about grabbing all the data underneath it. And this means that you can structure your data hierarchically in a way that makes sense to you logically, without having to worry about grabbing tons of unnecessary data. 

- Supports effortless real time data synchronization with changes in your database as they happen.
- Robust support for offline mode, so your users can keep interacting with your app even when the internet isn't available or is unreliable.
- Firestore also offers deep one-click integrations with a growing set of 3rd party partners via Firebase Extensions to help you even more rapidly build applications.
- Firestore is the next generation of Datastore
- Suports ACID Transactions
- High availability ( 99.999% availability ) of reads and writes. Multi-region replication
- Two mode
  - native Mode: supports all Firebase features
    - Uses Firebase API
    - Not supported with older App Engine runtimes
    - supports up to 10K writes per second, and over a million connections. 
  - datastore mode:
    - does not support all Firestore features like offline support for mobile devices and synchronization
    - supports only server-side usage of Firestore, but supports unlimited scaling, including writes. 

- Mobile, web, and IoT apps at global scale
- Limitations of Transactions type:
   - Maximum duration of 60 seconds and 10 second idle expiration after 30 seconds
   - Modify upto 500 entities in a single transaction
   - Transaction can fail due to too many concurrent modifications, exceeds resource limits or internal error

- Relational vs. Firestore Terminology

   <img src="https://github.com/user-attachments/assets/bd243c35-3623-46c3-8870-dc30bed54976" width="300" height="150" >


# Datastore
- Serverless and Highly scalable NoSQL Document based database like MongoDB
- SQL Like Queries – GQL
- Support ACID Transactions
- Multiple indexes
- Data replication across different region
- Use case
  - Session Info
  - Product catlog
- Export data from gcloud and console
- Generally used along with App Engine
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

        <img src="https://github.com/user-attachments/assets/5cea5f90-f9b8-4861-b3c2-dc897a8dc374" widht="300" height="150" >


** You can use either Datastore or Firestore within a project but not both. 

