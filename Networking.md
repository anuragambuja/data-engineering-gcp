


## Zone & Region
> ### Overview
A region is a specific geographical location where you can run your resources. Each region has one or more zones. For example, the us-central1 region denotes a region in the Central United States that has zones us-central1-a, us-central1-b, us-central1-c, and us-central1-f. Resources that live in a zone are referred to as zonal resources. Virtual machine Instances and persistent disks live in a zone. To attach a persistent disk to a virtual machine instance, both resources must be in the same zone. Similarly, if you want to assign a static IP address to an instance, the instance must be in the same region as the static IP.

![image](https://github.com/anuragambuja/data-engineering-gcp/assets/19702456/e726ba05-ff2d-42f0-b724-04db01d6b400)

- Zones – Independent data Center. Each Zone has one or more discrete clusters. Failures in one zone do not affect the other zones in a region. Resources in different zones have no common points of failure
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

> ## Virtual Private Cloud

A Virtual Private Cloud (VPC) network is a virtual version of a physical network that is implemented inside of Google's production network by using Andromeda (Google Cloud Platform’s network virtualization stack). It is a managed networking service for Google Cloud infrastructure. A single VPC can span across multiple regions all over the workd, securely, without communicating across the public internet. VPCs are sharable across projects and with organizations in some cases. Each Google Cloud project has a default network to get you started. A VPC network is a global resource which consists of a list of regional virtual subnetworks (subnets) in data centers, all connected by a global wide area network (WAN). VPC networks are logically isolated from each other in Google Cloud. Each subnet is associated with a Google Cloud region and a private RFC 1918 CIDR block for its internal IP addresses range and a gateway.

Note: The deny-all-ingress and allow-all-egress rules are also displayed, but you cannot check or uncheck them as they are implied. These two rules have a lower Priority (higher integers indicate lower priorities) so that the allow ICMP, custom, RDP and SSH rules are considered first.

Routes tell VM instances and the VPC network how to send traffic from an instance to a destination, either inside the network or outside of Google Cloud. Notice that there is a route for each subnet and one for the Default internet gateway (0.0.0.0./0).
Every VPC network has two implied firewall rules that block all incoming connections and allow all outgoing connections.  there are 4 Ingress firewall rules for the default network: These firewall rules allow ICMP, RDP and SSH ingress traffic from anywhere (0.0.0.0/0) and all TCP, UDP and ICMP traffic within the network (10.128.0.0
default-allow-icmp
default-allow-internal
default-allow-rdp
default-allow-ssh

If an instance is stopped, any ephemeral external IP addresses assigned to the instance are released back into the general Compute Engine pool and become available for use by other projects. When a stopped instance is started again, a new ephemeral external IP address is assigned to the instance.

The Internal IP should be 10.202.0.2 as x.x.x.1 is reserved for the gateway and you have not configured any other instances in that subnet.
- allow-icmp firewall rule allows the ping to vm's external IP address.
- allow-custom firewall rule allows to ping to vm's internal IP.
- allow-ssh firewall rule aloows to SSH to the VM.
- Create a firewall rule to allow external traffic to the VM instances: `gcloud compute firewall-rules create <firewall name> --target-tags <target tags> --allow tcp:80`

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
  - Premium Tier delivers traffic over Google’s well-provisioned, low latency, highly reliable global network. This network consists of an extensive global private fiber network with over 100 points of presence (POPs) across the globe.
  - Global network with low latency: Leverage Google's high-performance global network for global reach and consistent performance.
  - High availability and scalability: Ensure continuous availability and seamless scaling for mission-critical applications.
  - Ideal for production workloads and demanding applications.

    ![image](https://github.com/user-attachments/assets/5388c6c5-6f93-4b62-99cd-e951ffb14000)

- Standard Tier:
  - Standard tier is priced lower than Premium because your traffic between Google Cloud and your end-user (Internet) is delivered over transit (ISP) networks instead of Google’s network.
  - Regional network with cost-effectiveness: Utilize a regional network with lower costs for less demanding workloads.
  - Suitable for development, testing, and non-production environments.
  - Choose Standard Tier for cost-sensitive scenarios.

      ![image](https://github.com/user-attachments/assets/1d7b214e-ef1c-435e-b09e-59568588bb78)

> Load Balancer 
- Network Load Balancer
- HTTP(s) Load Balancer: HTTP(S) Load Balancing is implemented on Google Front End (GFE). GFEs are distributed globally and operate together using Google's global network and control plane. You can configure URL rules to route some URLs to one set of instances and route other URLs to other instances. Requests are always routed to the instance group that is closest to the user, if that group has enough capacity and is appropriate for the request. If the closest group does not have enough capacity, the request is sent to the closest group that does have capacity. To set up a load balancer with a Compute Engine backend, your VMs need to be in an instance group.

- 







An internal load balancer consists of a:
- Forwarding rule which binds an internal IP address.
- Backend service (which is regional) linking to one or more backend instance groups (which are zonal).
- Health check attached to the backend service that determines which instances can receive new connections.

![image](https://github.com/anuragambuja/data-engineering-gcp/assets/19702456/d224c403-f1d6-41d4-aecc-d75948c37f91)




## Subnet
- Each VPC network consists of one or more IP address ranges called subnets. Subnets are regional resources, and have IP address ranges associated with them.
- A network must have at least one subnet before you can use it. Auto mode VPC networks create subnets in each region automatically.
- Machines in the same network can communicate via their private IPs regardless of their region. By default, VMs in different networks can only communicate with public IPs
- Shared VPC allows a network to be shared across multiple projects


  ![image](https://github.com/user-attachments/assets/c38a2344-e814-4bec-9c1b-f0b52b0192d1)

## VPC Network Peering
- Two VPC networks can be privately connected with VPC Network Peering
  - Allows machines in different networks to communicate with private IPs
  - The subnet IP ranges in peered VPC networks cannot overlap
  - The two networks can even be in different projects and organizations
- VPC Network Peering can: 
  - Reduce latency: Connecting via private IPs will have lower latency than public IPs
  - Reduce cost: Google Cloud charges egress bandwidth when using public IPs to communicate
  - Increase security: VMs may no longer require public access


## Shared VPC
- Shared VPCs allows you to connect resources from multiple projects to a common VPC network
- The host project is the single point of control for all the service projects that you link to the host project.
- From the host project, consistent access control policies can be applied at the organization level.
- Share resources from one VPC to other VPCs










