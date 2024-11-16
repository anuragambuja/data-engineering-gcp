## Compute
> ### Overview
  - Compute Compute Engine lets you create virtual machines that run different operating systems, including multiple flavors of Linux (Debian, Ubuntu, Suse, Red Hat, CoreOS) and Windows Server, on Google infrastructure. 
  - Resources that live in a zone are referred to as zonal resources. Virtual machine instances and persistent disks live in a zone. If you want to attach a persistent disk to a virtual machine instance, both resources must be in the same zone. Similarly, if you want to assign a static IP address to an instance, the instance must be in the same region as the static IP address.

> ### Google Compute Engine (GCE)
- IAAS – Full Control, more flexibility, more responsibility
- Important parameter : Zone, Service Account, Machine family – CPU, RAM, Boot Disk, Storage, Virtual Private Cloud
- The more sphisticated load balancing need to be done, the higher you need to go in OSI stack.
- Projects can have upto 5 VPC(virtual private netword). Each GCE instance belongs in one VPC. Instances within VPC communicate on LAN. Instances across VPC communicate on internet.
- Every VM instance comes with a small root persistent disk containing the OS. 
- When you stop an VM instance, External IP address is lost. Static IP can be switched to another VM instance in same project. You are billed for an Static IP when you are NOT using it!. Static IP remains attached even if you stop the instance. You have to
manually detach it.
- You cannot change the zone of the machine once instanciated.
- Different Machine Families for Different Workloads:
  - General Purpose (E2, N2, N2D, N1) : Best price-performance ratio
      - Web and application servers, Small-medium databases, Dev environments
  - Memory Optimized (M2, M1): Ultra high memory workloads
    - Large in-memory databases and In-memory analytics
  - Compute Optimized (C2): Compute intensive workloads
    - Gaming applications
- Hands-on : Setting up a HTTP server   
  ```
  #! /bin/bash
  sudo su
  apt update
  apt -y install apache2
  sudo service apache2 start
  sudo update-rc.d apache2 enable
  echo "Hello World" > /var/www/html/index.html
  echo "Hello world from $(hostname) $(hostname -I)" > /var/www/html/index.html
  ```
![image](https://user-images.githubusercontent.com/19702456/230639657-628833a5-e7a7-40e7-b126-dcbf4052a8f0.png)
- Instance Group - Group of VM instances managed as a single entity.
  - Managed: Identical VMs created using a template. Instance template is mandatory
    - Features: Auto scaling, auto healing and managed releases
      - Rolling updates: Release new version step by step (gradually). Update a percentage of instances to the new version at a time.
      - Canary Deployment: Test new version with a group of instances before releasing it across all instances.
  - Unmanaged: Different configuration for VMs in same group:
    - Does NOT offer auto scaling, auto healing & other services
    - NOT Recommended unless you need different kinds of VMs
- Load Balancing
  - Network Layer - Transfer bits and bytes. IP (Internet Protocol): Transfer bytes. Unreliable.
  - Transport Layer - Are the bits and bytes transferred properly ?
    - TCP (Transmission Control): Reliability > Performance
    - TLS (Transport Layer Security): Secure TCP
    - UDP (User Datagram Protocol): Performance > Reliability
  - Application Layer - Make REST API calls and Send Emails
    - HTTP(Hypertext Transfer Protocol): Stateless Request Response Cycle
    - HTTPS: Secure HTTP
    - SMTP: Email Transfer Protocol
  
  ![image](https://user-images.githubusercontent.com/19702456/230649398-063274c7-67c7-4d49-94dd-2bd63954d79d.png)

  ![image](https://user-images.githubusercontent.com/19702456/230650183-c9c0f718-5edb-41ec-945a-c55688528338.png)

- Sustained use discounts (Automatic discounts for running VM instances for significant portion of the billing month) Does NOT apply on certain machine types (example: E2 and A2), or to VMs created by App Engine flexible and Dataflow. Applicable for instances created by Google Kubernetes Engine and Compute Engine.
- Committed use discounts with predictable resource needs. Applicable for instances created by Google Kubernetes Engine and Compute Engine. Does NOT apply to VMs created by App Engine flexible and Dataflow. Commit for 1 year or 3 years. 
- Spot VMs - Latest version of preemtible VMs but does not have a maximumum runtime of 24 hours.
- Managed Services for Compute

  ![image](https://user-images.githubusercontent.com/19702456/230710552-dc31cd82-a9ba-4bac-a72b-c1f5769b4180.png)


# Cloud Load Balancing

  ![image](https://github.com/user-attachments/assets/679a2e03-c5de-477f-bce3-d3823e908900)

- Cloud Load Balancing is a fully distributed load balancing solution that balances user traffic (HTTP(s), HTTPS/2 with gRPC, TCP/SSL, UDP, and QUIC) to multiple backends to avoid congestion, reduce latency, increase security, and reduce costs.
  - Software-defined network (SDN) Cloud Load Balancing is not an instance- or device-based solution, which means you won't be locked into physical infrastructure or face HA, scale, and management challenges. 
  - Single global anycast IP and autoscaling: Cloud Load Balancing front-ends all your backend instances in regions around the world. It provides cross-region load balancing, including automatic multi-region failover, which gradually moves traffic in fractions if backends become unhealthy or scales automatically if more resources are needed.
 
- Cloud Load Balancing supports multiple SSL certificates, enabling you to serve multiple domains using the same load balancer IP address and port. It absorbs and dissipates layer 3 and layer 4 volumetric attacks across Google’s global load balancing infrastructure.
- Additionally, with Cloud Armor, you can protect against Layer 3 to Layer 7 application level attacks
- By using Identity Aware Proxy and firewalls you can authenticate and authorize access to backend services. 
