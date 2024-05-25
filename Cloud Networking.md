


## Zone & Region
> ### Overview
A region is a specific geographical location where you can run your resources. Each region has one or more zones. For example, the us-central1 region denotes a region in the Central United States that has zones us-central1-a, us-central1-b, us-central1-c, and us-central1-f. Resources that live in a zone are referred to as zonal resources. Virtual machine Instances and persistent disks live in a zone. To attach a persistent disk to a virtual machine instance, both resources must be in the same zone. Similarly, if you want to assign a static IP address to an instance, the instance must be in the same region as the static IP.

![image](https://github.com/anuragambuja/data-engineering-gcp/assets/19702456/e726ba05-ff2d-42f0-b724-04db01d6b400)

- Zones – Independent data Center. Each Zone has one or more discrete clusters.
- Region – Specific geographical location to host your resources
- Multi-region - Geographical Collection
- Global - Anywhere
- Point of presence (PoP) - Connects public internet to Google Cloud. Provides services like CDN, Media CDN, Interconnects.

![image](https://user-images.githubusercontent.com/19702456/222907494-543244ac-2303-470b-8db1-240333a0c5e4.png)

> ### Why Zones & Regions ?
- Low latency
- Adhere to government regulations
- High availability
- Disaster recovery
- Global Footprint

Find the updated zones and regions [here](https://cloud.google.com/about/locations).

> ### What is RTO & RPO ?
- RTO – Recovery Time objective: Maximum time for which system can be down
- RPO - Recovery Point objective: Maximum time for which organization can tolerate Dataloss

![image](https://user-images.githubusercontent.com/19702456/224393217-f29fcfe6-87ea-482d-8dba-acd4808bbdf7.png)

Virtual Private Cloud
It is a managed networking service for Google Cloud infrastructure. A single VPC can span across multiple regions all over the workd, securely, without communicating across the public internet. VPCs are sharable across projects and with organizations in some cases. 

Network services
- Load Balancing: Distribute incoming traffic across multiple instances of an application or service, ensuring high availability and scalability.
- Cloud DNS: Translate domain names into IP addresses, enabling users to access websites and services seamlessly.
- Cloud CDN: Accelerate content delivery to users worldwide by caching content in edge locations close to their devices.
- Cloud NAT: Enable instances within a private network to access the internet without requiring public IP addresses, enhancing security and simplifying network management.

Google Cloud network connectivity solutions
- Cloud VPN: Establish secure encrypted connections between on-premises networks and VPCs, enabling hybrid cloud deployments.
- Cloud Interconnect: Provide high-bandwidth, low-latency connectivity between on-premises networks and VPCs, ideal for mission-critical applications.
- Cross-Cloud Interconnect: Provides direct, high-bandwidth, low-latency connectivity between Google Cloud and other cloud providers.
- Network Connectivity Center: Centralized logical hub for managing and monitoring connection. With support for hybrid spokes and VPC spokes.

Google Cloud network security solutions provide comprehensive protection against network threats and vulnerabilities. 
- Cloud Armor: Safeguard applications and websites against denial-of-service (DoS) attacks, OWASP top 10 and other malicious traffic.
- Cloud IDS (Intrusion Detection System): Continuously monitor network traffic for suspicious activity, enabling early detection of potential threats.
- Cloud Firewall: Define firewall rules to control incoming and outgoing traffic, preventing unauthorized access and protecting against cyberattacks. These also provide advanced capabilities such as Intrusion Prevention System (IPS) for Cloud Firewall Plus editions.
  - Cloud Firewall Essentials: Foundational and gives global and regional network firewall policies, micrp-segmentation with tags, and address groups. 
  - Cloud Firewall Standard: Adds the use of Google Cloud threat intelligence as well as fully qualified domain name (FQDN) objects and geolocation objects. 
  - Cloud Firewall Plus: Gives ability to detect and block threats from network based on latest threat sigatures. 


Google Cloud Network Intelligence Center provides a comprehensive suite of tools for monitoring, troubleshooting, and optimizing your network performance. These tools include:
- Network Topology: Visualize the topology of your Virtual Private Cloud (VPC) networks and their associated metrics, enabling you to identify and resolve connectivity issues.
- Connectivity Tests: Test network connectivity to and from your VPC network, ensuring that your network is functioning properly and that your resources are accessible.
- Performance Dashboard: Monitor and visualize the performance of your Google Cloud network and resources.
- Firewall Insights: Gain insights into firewall rules usage, identify misconfigurations, and optimize your firewall rules to improve security and performance.
- Network Analyzer: Monitor network traffic and identify potential issues, such as high latency, packet loss, and routing problems.


 Network Service Tiers
 - Premium Tier:
  - Global network with low latency: Leverage Google's high-performance global network for global reach and consistent performance.
  - High availability and scalability: Ensure continuous availability and seamless scaling for mission-critical applications.
  - Ideal for production workloads and demanding applications.
- Standard Tier:
  - Regional network with cost-effectiveness: Utilize a regional network with lower costs for less demanding workloads.
  - Suitable for development, testing, and non-production environments.
  - Choose Standard Tier for cost-sensitive scenarios.
  







