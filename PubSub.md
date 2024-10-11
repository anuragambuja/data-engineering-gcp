# PubSub

- Google Cloud Pub/Sub is a fully-managed real-time messaging service that allows you to send and receive messages between independent applications.
- Pub/Sub is an asynchronous global messaging service. By decoupling senders and receivers, it allows for secure and highly available communication between independently written applications. Pub/Sub delivers low-latency, durable messaging.
- Pub/Sub is a HIPAA compliant service, offering fine grained access controls and end to end encryption. Messages are encrypted in transit and at rest. Messages are stored in multiple locations for durability and availability.
- The Pub/Sub client that creates the topic is called the publisher.
- The Pub/Sub client that creates the subscription is called the subscriber.
- The subscription connects the topic to a subscriber application that receives and processes messages published to the topic. A topic can have multiple subscriptions, but a given subscription belongs to a single topic.
- You don't incur egress fees for the messages that Pub/Sub automatically acknowledges you incur message delivery fees and seek related storage fees for these messages.
- Pub/Sub just sends raw bites. So, you can text, images etc with the limit of 10 Megabytes.
- Scale to billions of message per day
- Publisher – App send message to Topic
- Push & Pull way to access messages
  - Pull – Subscriber pull message
  - Push – Message will be sent to subscriber via webhook
- Publish / Subscribe Patterns
  - The first pattern is just a basic straight through flow, where one publisher publishes messages into a topic, which then get consumed by the one subscriber through the one subscription.
  - The second pattern is fan-in or load balancing, multiple publishers can publish the same topic, and multiple subscribers can pull from the same subscription, leveraging parallel processing.
  - The second pattern is fan-in or load balancing, multiple publishers can publish the same topic, and multiple subscribers can pull from the same subscription, leveraging parallel processing.
![image](https://github.com/user-attachments/assets/62483277-4b46-4ccd-8166-7ce183315cd5)

- One topic – Multiple Subscriber
- One subscriber – Multiple Topic

![image](https://user-images.githubusercontent.com/19702456/224790417-c6e118d9-74d9-45c4-b9a5-594cc99b2a12.png)

In Pub/Sub, publisher applications and subscriber applications connect with one another through the use of a shared string called a topic. A publisher application creates and sends messages to a topic. Subscriber applications create a subscription to a topic to receive messages from it.

![image](https://user-images.githubusercontent.com/19702456/222902428-ee0eb675-fe4f-4f68-b22f-c4d64c6a5087.png)

Pub Sub allows for both push and pull delivery. In the pull model, your clients are subscribers, and will be periodically calling for messages, and Pub Sub will just be delivering the messages since the last call. In the pull model, you're going to have to acknowledge the message as a separate step. In the pull model, the messages are stored for up to seven days.  In the push model, it actually uses an HTTP endpoint. You register a web hook as your subscription, and Pub Sub infrastructure itself will call you with the latest messages. In the case of push, you just respond with status 200OK for the HTTP call, and that tells Pub Sub the message delivery was successful. It will actually use the rate of your success responses to self-limit so that it doesn't overload your worker. The way the acknowledgments work is to ensure every message gets delivered at least once. What happens is when you acknowledge a message, you acknowledge on a per subscription basis. There is a replay mechanism as well that you can rewind and go back in time and have it replay messages. But in any case, you will always be able to go back seven days.

![image](https://user-images.githubusercontent.com/19702456/222902406-d38d24e7-1e1a-409d-b60f-5c0c1c9849df.png)

Topic message retention also allows a subscription to replay messages published before a subscription was created. If topic message retention is enabled, storage costs for the messages retained by the topic are to be built to the topic's project. Subscribers can work individually or as a group.
In the case of a push subscription, you only have one web endpoint so you will only have one subscriber typically, but that one subscriber could be an App Engine standard app or cloud run container image which auto scales. So it is one web endpoint but it can have auto scale workers behind the scenes.

When the Pub/Sub service redelivers the message with an ordering key, the Pub/Sub service also redelivers every subsequent message with the same ordering key, including acknowledged messages. If both message ordering and a dead letter topic are enabled on a subscription, the ordering may not be true, as Pub/Sub forwards messages to dead letter topics on a best effort basis. To receive the messages in order, set the message ordering property on the subscription you receive messages from.
Dataflow will de-duplicate messages based on the message ID, because in Pub/Sub, if a message is delivered twice, it will have the same ID in both cases. Element Source adds a default date timestamp, or DTS, which is the time of entry to the system rather than the time the sensor data was captured. A PTransform extracts the date timestamp from the data portion of the element and modifies the DTS metadata so the time of data capture can be used in window processing.



