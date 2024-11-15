# Google Kubernetes Engine (GKE)
- Developed by Google , Launched in 2014 – Kubernetes. In 2015, Google Launched cloud version - GKE
- Cloud Agnostics. Written in Go language
- Google Kubernetes Engine (GKE) provides a managed environment for deploying, managing, and scaling your containerized applications using Google infrastructure. The Kubernetes Engine environment consists of multiple machines (specifically Compute Engine instances) grouped to form a container cluster. Kubernetes (master) instance manages node instances which runs a kubelet agent instance which communicates with kubernetes and manages pod which runs multiple containers inside it. Container disks are ephemeral (data is lost once the container is restarted) so use GCEPersistentDIsk. Network load balancing works with container engine. For HTTP load balancing, need to integrate with Compute Engine load balancing. Managed master runs the kubernetes API server which services REST requests, schedules pod creation & deletion on worker nodes, and synchronizes pod information (such as open ports and location).
When you run a GKE cluster, you also gain the benefit of advanced cluster management features that Google Cloud provides. These include:
  -	Load balancing for Compute Engine instances
  -	Node pool is subset of machines within a cluster that all have the same configuration. You can run multiple kubernetes node versions on each node pool in your cluster, update each node pool independently and target different node poola for specific deployments. Node pools to designate subsets of nodes within a cluster for additional flexibility
  -	Automatic scaling of your cluster's node instance count
  -	Automatic upgrades for your cluster's node software
  -	Node auto-repair to maintain node health and availability
  -	Logging and Monitoring with Cloud Monitoring for visibility into your cluster
- Cluster : Group of Compute Engine instances:
  - Master Node(s) (Control plane) - Manages the cluster
    - Components:
      - API Server - Handles all communication for a K8S cluster (from nodes and outside)
      - Scheduler - Decides placement of pods
      - Control Manager - Manages deployments & replicasets
      - etcd - Distributed database storing the cluster state
  - Worker Node(s) - Run your workloads (pods) and has Kubelet which manages communication with master node(s)
- GKE Cluster Types

  ![image](https://user-images.githubusercontent.com/19702456/230727841-ba947699-9052-4a41-b1bf-49cf2bf219b0.png)
- Pods
  - Smallest deployable unit in Kubernetes
  - A Pod contains one or more containers
  - Each Pod is assigned an ephemeral IP address
  - All containers in a pod share:
    - Network
    - Storage
    - IP Address
    - Ports and
    - Volumes (Shared persistent disks)
  - POD statuses : Running /Pending /Succeeded /Failed /Unknown

  ![image](https://user-images.githubusercontent.com/19702456/230727936-260be543-2676-4505-9ae4-153597a17deb.png)

- Deployment vs Replica Set
  - A deployment is created for each microservice:
    - kubectl create deployment m1 --image=m1:v1
    - Deployment represents a microservice (with all its releases)
    - Deployment manages new releases ensuring zero downtime
  - Replica set ensures that a specific number of pods are running for a specific microservice version
    - kubectl scale deployment m2 --replicas=2
    - Even if one of the pods is killed, replica set will launch a new one

- Kubernetes Service Types
  - ClusterIP: Exposes Service on a cluster-internal IP
    - Use case: You want your microservice only to be available inside the cluster (Intra cluster communication)
  - LoadBalancer: Exposes Service externally using a cloud provider's load balancer
    - Use case: You want to create individual Load Balancer's for each microservice
  - NodePort: Exposes Service on each Node's IP at a static port (the NodePort)
    - Use case: You DO not want to create an external Load Balancer for each microservice (You can create one Ingress component to load balance multiple microservices)

- Ingress
  - Recommended Approach for providing external access to services in a cluster
    - Provides load balancing and SSL termination
    - Control traffic by defining rules on the Ingress resource
    - Recommendation: NodePort Service for each microservice. Expose using a Ingress.
      - Advantage: One Load Balancer can serve multiple microservices!

  ```yaml
  apiVersion: networking.k8s.io/v1
  kind: Ingress
  metadata:
    name: gateway-ingress
  spec:
    rules:
    - http:
      paths:
      - path: /currency-exchange/*
        backend:
          serviceName: currency-exchange
          servicePort: 8000
      - path: /currency-conversion/*
        backend:
          serviceName: currency-conversion
          servicePort: 8100
  ```

  ```
  # Connect to the Kubernetes Cluster
  gcloud container clusters get-credentials autopilot-cluster-1 --region us-central1 --project proven-audio-376216
  
  #Create deployment
  kubectl create deployment hello-world-rest-api --image=in28min/hello-world-rest-api:0.0.1.RELEASE
  kubectl get deployment
  
  # Create service
  kubectl expose deployment hello-world-rest-api --type=LoadBalancer --port=8080
  kubectl get services [--watch]
  curl 35.202.65.199:8080/hello-world
  
  # Increase number of instances of your microservice
  kubectl scale deployment hello-world-rest-api --replicas=3
  # Increase number of nodes in your Kubernetes cluster
  gcloud container clusters resize my-cluster --node-pool default-pool --num-nodes=2 --zone=us-central1-c
  
  # Setup auto scaling for your microservice
  kubectl autoscale deployment hello-world-rest-api --max=4 --cpu-percent=70
  kubectl get hpa
  
  # Add some application configuration for your microservice
  kubectl create configmap hello-world-config --from-literal=RDS_DB_NAME=todos
  kubectl get configmap
  kubectl describe configmap hello-world-config
  
  # Add password configuration for your microservice
  kubectl create secret generic hello-world-secrets-1 --from-literal=RDS_PASSWORD=dummytodos
  kubectl get secret
  kubectl describe secret hello-world-secrets-1
  
  # Kubernetes Deployment YAML
  kubectl apply -f deployment.yaml
  ```
  
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
labels:
  app: hello-world-rest-api
name: hello-world-rest-api
namespace: default
spec:
replicas: 3
selector:
  matchLabels:
    app: hello-world-rest-api
template:
  metadata:
    labels:
      app: hello-world-rest-api
  spec:
    containers:
      - image: 'in28min/hello-world-rest-api:0.0.3.RELEASE'
        name: hello-world-rest-api
```
  
  ```yaml
  apiVersion: v1
  kind: Service
  metadata:
    labels:
  app: hello-world-rest-api
    name: hello-world-rest-api
    namespace: default
  spec:
    ports:
    - port: 8080
    protocol: TCP
    targetPort: 8080
    selector:
  app: hello-world-rest-api
    sessionAffinity: None
    type: LoadBalancer
  
  ```
  
  ```
  gcloud container node-pools list --zone=us-central1-c --cluster=my-cluster
  kubectl get pods -o wide

  kubectl set image deployment hello-world-rest-api hello-world-rest-api=in28min/hello-world-rest-api:0.0.2.RELEASE
  kubectl get replicasets
  kubectl delete pod hello-world-rest-api-58dc9d7fcc-8pv7r
  kubectl scale deployment hello-world-rest-api --replicas=1
  kubectl delete service hello-world-rest-api
  kubectl delete deployment hello-world-rest-api
  gcloud container clusters delete my-cluster --zone us-central1-c
  ```

- GKE - Scenarios

![image](https://user-images.githubusercontent.com/19702456/230731997-8e176c46-1df9-44ae-b326-974c097dd7af.png)


