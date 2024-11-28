# PubSub

  ![image](https://github.com/user-attachments/assets/545f1bd4-4350-40ff-9517-58f7fc78fd42)

- Google Cloud Pub/Sub is a fully-managed real-time asynchronous global messaging service that allows you to send and receive messages between independent applications. By decoupling senders and receivers, it allows for secure and highly available communication between independently written applications.
- Pub/Sub delivers low-latency, durable messaging.
- Pub/Sub is a HIPAA compliant service, offering fine grained access controls and end to end encryption. Messages are encrypted in transit and at rest. Messages are stored in multiple locations for durability and availability.
- Pay for what you use. You don't incur egress fees for the messages that Pub/Sub automatically acknowledges you incur message delivery fees and seek related storage fees for these messages.
- Scale to billions of message per day
  
- Core Conceps:
  - Topic: A named resource to which messages are sent by publishers. Pub/Sub just sends raw bites. So, you can text, images etc with the limit of 10 Megabytes. The Pub/Sub client that creates the topic is called the publisher.
  - Subscription: A named resource representing the stream of messages from a single, specific topic, to be delivered to the subscribing application. The Pub/Sub client that creates the subscription is called the subscriber. A topic can have multiple subscriptions, but a given subscription belongs to a single topic.
  - Message: The combination of data and (optional) attributes that a publisher sends to a topic and is eventually delivered to subscribers.
  - Message attribute: A key-value pair that a publisher can define for a message.

- Topic message retention also allows a subscription to replay messages published before a subscription was created. If topic message retention is enabled, storage costs for the messages retained by the topic are to be built to the topic's project. Subscribers can work individually or as a group.

- Push & Pull way to deliver/access messages
  - Pull – In the pull model, your clients are subscribers, and will be periodically calling for messages, and Pub Sub will just be delivering the messages since the last call. In the pull model, you're going to have to acknowledge the message as a separate step. In the pull model, the messages are stored for up to seven days. Pull is the default. eg. Dataflow jobs are pull subscribers
  - Push –  In the push model, it actually uses an HTTP endpoint. You register a web hook as your subscription, and Pub Sub infrastructure itself will call you with the latest messages. In the case of push, you just respond with status 200 OK for the HTTP call, and that tells Pub Sub the message delivery was successful. It will actually use the rate of your success responses to self-limit so that it doesn't overload your worker. The way the acknowledgments work is to ensure every message gets delivered at least once. What happens is when you acknowledge a message, you acknowledge on a per subscription basis. There is a replay mechanism as well that you can rewind and go back in time and have it replay messages. But in any case, you will always be able to go back seven days. App Engine and Cloud Run applications are ideal push subscribers

     ![image](https://user-images.githubusercontent.com/19702456/222902406-d38d24e7-1e1a-409d-b60f-5c0c1c9849df.png)

- Publish / Subscribe Patterns
  - The first pattern is just a basic straight through flow, where one publisher publishes messages into a topic, which then get consumed by the one subscriber through the one subscription.
  - (Fan in) The second pattern is fan-in or load balancing, multiple publishers can publish the same topic, and multiple subscribers can pull from the same subscription, leveraging parallel processing.
  - (Fan out) Multiple subscribers, where you have multiple use case for same piece of data, and all data is sent to multiple different subscribers. 

    ![image](https://github.com/user-attachments/assets/62483277-4b46-4ccd-8166-7ce183315cd5)

- Message ordering is a feature in Pub/Sub that lets you receive messages in your subscriber clients in the order that they were published by the publisher clients. For example, assume that a publisher client in a region publishes messages 1, 2, and 3 in order. With message ordering, the subscriber client receives the published messages in the same order. To be delivered in order, the publisher client must publish the messages in the same region. Ordering in Pub/Sub is determined by the following:
  - Ordering key: This is a string that is used in the Pub/Sub message metadata and represents the entity for which messages must be ordered. The ordering key can be up to 1 KB in length. To receive a set of ordered messages in a region, you must publish all messages with the same ordering key in the same region. Some examples of ordering keys are customer IDs and the primary key of a row in a database. An ordering key is not equivalent to a partition in a partition-based messaging system as ordering keys are expected to have a much higher cardinality than partitions.
  - Enable message ordering: This is a subscription setting. When a subscription has message ordering enabled, the subscriber clients receive messages published in the same region with the same ordering key in the order in which they were received by the service. You must enable this setting in the subscription.

- When the Pub/Sub service redelivers the message with an ordering key, the Pub/Sub service also redelivers every subsequent message with the same ordering key, including acknowledged messages. If both message ordering and a dead letter topic are enabled on a subscription, the ordering may not be true, as Pub/Sub forwards messages to dead letter topics on a best effort basis. 


> ## Pub/Sub Lite
- A zonal service
- Run publisher, subscriber and topics in the same zone
- Designed to minimize networking egress cost and latency
- High speed replacement for Kafka and Spark structured streaming
- Unlimited Retention period and storage
- Pay for the capacity that you provision

    <img src="https://github.com/user-attachments/assets/f5562b22-8885-4c9d-85d8-e51b12491431" width="700" height="350" >

> ## Features comparison table

   ![image](https://github.com/user-attachments/assets/f6dd3e73-f17d-413c-8580-054bf261db07)
   
  <img src="https://github.com/user-attachments/assets/6628bf44-e4b3-4a9a-92b9-b90cbbd850f9" width="700" height="500" >
  

