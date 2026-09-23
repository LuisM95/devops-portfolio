# Kubernetes Documentation

## Kubernetes & the Problem it Solves 
Kubernetes is a tool for orchestrating docker containers, with which you can automate things such as deployment, scaling, networking and others.

## Kubernetes and air controller analogy.
Kubernetes in analogy is like an air controller which gives instructions to planes, decides how many planes fly, what route they take, what happends if one falls, how to land without interrupting traffic.

## Kubernetes Architecture.

    ### Control Plane 
    - Api Server
    - Scheduler 
    - etcd
    - Controller manager 


    Give Instructions to:

    - Worker Nodes 
        - node 1
        - node 2
        - node 3

Control plane - Brain 
- Make decisions
- Monitor the status 
- Respond to events 

Worker nodes
- Where the containers run 
- They executes the control plane instructions

## Main Objects of Kubernetes
- Pods: Minimal unit 
    Is one or more containers, that share the same IP, storage, and runs together.
- Deployments: manage the pods.
    A deployment tells Kubernetes how many pods i want, what image to use and how to update without downtime.
- Service: expose the pods to the world.
    - Pods have IPs that are constantly changing.
        If one pods dies and another is born, it has a different IP 
    - The service has a fixed IP that never changes
        Traffic reaches the service
        The service distributes it to the available Pods
    - It's like the reception of the building.
        Visitors go to reception(service)
        Receptions sends them to the correct departament(pod)

- Config Map & Secret
    - ConfigMap -> non-sensitive config -> URL's, names, ports
    - Secret -> sensitive config -> passwords, tokens, keys

## Essential Commands 
``` BASH
kubectl get pods                              ~  List all pods running
kubectl get pods -n <namespace>               ~  Pods in a specific namespace
kubectl get service                           ~  List all services 
kubectl get deployments                       ~  List all deployments 
kubectl describe pod <name>                   ~  Detailed information of a pod
kubectl logs <name>                           ~  View logs of a pod 
kubectl exec -it <name> bash                  ~  Enter inside a pod 
kubectl apply -f <name_file.yaml>             ~  Creates/Update resource from a file
kubectl delete pod <name>                     ~  Delete a pod 
kubectl delete deployment <name>              ~  Delete a Deployment 
kubectl rollout restart deployment <name>     ~  Restart a Deployment
kubectl rollout status deployment <name>      ~  Status of the rolling update 
kubectl port-fordward pod/<name> 8080:8080    ~  Access a pod locally 
kubectl scale deplpoyment <name> --replicas=5 ~  Scale a replicas
```

## MiniKube 
Is a complete Kubernetes runnning on a single macchine locally. Its perfecto to learning to develop without the need for a cloud cluster.

## Essential Commands 
```BASH 
- minikube start      ~  Start the cluster
- minikube status     ~  Status of cluster
- miniikube stop      ~  Stop the cluster 
- minikube dashboard  ~  Open the UI web of Kubernetes
```

## Rolling Update Method 
Deployments strategy that updates pods gradually wihtout donwtime. With this strategy, Kubernetes replace old pods while keeping the app available. If something fails, it rollbacks automatically. 
