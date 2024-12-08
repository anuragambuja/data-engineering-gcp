# Compute

  ![image](https://github.com/user-attachments/assets/da0719b9-9f0c-4e9b-9f73-29caddff415b)

- Compute Compute Engine lets you create virtual machines that run different operating systems, including multiple flavors of Linux (Debian, Ubuntu, Suse, Red Hat, CoreOS) and Windows Server, on Google infrastructure. 
- Resources that live in a zone are referred to as zonal resources. Virtual machine instances and persistent disks live in a zone. If you want to attach a persistent disk to a virtual machine instance, both resources must be in the same zone. Similarly, if you want to assign a static IP address to an instance, the instance must be in the same region as the static IP address.
- Pricing
  - All vCPUs, GPUs, and GB of memory are charged a minimum of 1 minute. After 1 minute, instances are charged in 1-second increments.
  - Compute Engine uses a resource-based pricing model, where each vCPU and each GB of memory on Compute Engine is billed separately rather than as a part of a single machine type.
  - If your workload is stable and predictable, you can purchase a specific amount of vCPUs and memory for a discount off of normal prices in return for committing to a usage term of 1 year or 3 years. The discount is up to 57% for most machine types or custom machine types. The discount is up to 70% for memory-optimized machine types.
  - The discount increases with usage, and you can get up to 30% net discount for instances that run the entire month.





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
    - Features: Auto scaling, auto healing, regional (multiple zone) deployment, automatic updating and managed releases
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


