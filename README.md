# 🚀 **Kubernetes Deployment — LLMOps Anime Recommender System**

In this stage, we deploy the **LLMOps Anime Recommender System** onto a **Kubernetes cluster** running on our **Minikube setup within a GCP VM**.
This stage brings the entire project to life — containerising the application and serving it publicly via Kubernetes services.

## 🧭 **Step 1 — Connect Docker to Minikube**

In your VM terminal, run the following command:

```bash
eval $(minikube docker-env)
```

This command ensures Docker points to Minikube’s internal environment so that your image builds directly inside Minikube’s Docker daemon.

Now, build your Docker image:

```bash
docker build -t llmops-app:latest .
```

This may take a few minutes to complete, as it will install all dependencies and package your Streamlit app into a container.

Once complete, verify that your image was successfully built:

```bash
docker images
```

You should see output similar to:

```
IMAGE                                             ID             DISK USAGE   
gcr.io/k8s-minikube/storage-provisioner:v5        6e38f40d628d       31.5MB      
llmops-app:latest                                 ec877b27d650       8.64GB      
registry.k8s.io/coredns/coredns:v1.12.1           52546a367cc9         75MB      
registry.k8s.io/etcd:3.6.4-0                      5f1f5298c888        195MB      
registry.k8s.io/kube-apiserver:v1.34.0            90550c43ad2b         88MB      
registry.k8s.io/kube-controller-manager:v1.34.0   a0af72f2ec6d       74.9MB      
registry.k8s.io/kube-proxy:v1.34.0                df0860106674       71.9MB      
registry.k8s.io/kube-scheduler:v1.34.0            46169d968e92       52.8MB      
registry.k8s.io/pause:3.10.1                      cd073f4c5f6a        736kB 
```

Your `llmops-app:latest` image is now built and ready to deploy.

## 🔐 **Step 2 — Inject Secrets into Kubernetes**

Next, we need to securely inject your **Groq** and **Hugging Face API keys** into the Kubernetes environment.

Run the following command:

```bash
kubectl create secret generic llmops-secrets \
  --from-literal=GROQ_API_KEY="" \
  --from-literal=HUGGINGFACEHUB_API_TOKEN=""
```

Make sure to replace the empty quotation marks `""` with your actual API keys.

Example:

```bash
kubectl create secret generic llmops-secrets \
  --from-literal=GROQ_API_KEY="your_groq_key_here" \
  --from-literal=HUGGINGFACEHUB_API_TOKEN="your_huggingface_key_here"
```

You should see confirmation:

```
secret/llmops-secrets created
```

## 🧩 **Step 3 — Deploy the Application**

Now apply your Kubernetes deployment and service configuration:

```bash
kubectl apply -f llmops-k8s.yaml
```

Expected output:

```
deployment.apps/llmops-app created
service/llmops-service created
```

You can verify the pods are running with:

```bash
kubectl get pods
```

Example output:

```
NAME                         READY   STATUS    RESTARTS   AGE
llmops-app-8fb4d677f-bzm9k   1/1     Running   0          32s
```

This confirms that your container is up and running successfully inside the cluster.

## 🌐 **Step 4 — Create a Minikube Tunnel**

To expose your service externally, start a **Minikube tunnel**:

```bash
minikube tunnel
```

Expected output:

```
Status:
        machine: minikube
        pid: 31651
        route: 10.96.0.0/12 -> 192.168.49.2
        minikube: Running
        services: [llmops-service]
    errors: 
                minikube: no errors
                router: no errors
                loadbalancer emulator: no errors
```

Leave this terminal **running** — it maintains the connection that allows external access to your app.

## 💻 **Step 5 — Forward Ports and Access the App**

Open a **new SSH terminal** (keeping the tunnel active in the previous one).
Navigate back to your project directory and run:

```bash
kubectl port-forward svc/llmops-service 8501:80 --address 0.0.0.0
```

This forwards external traffic from port **8501** to your Streamlit app inside Kubernetes.

Keep this terminal open while your application is running.

Now, return to your **GCP Console → VM Instances** page, find your **External IP address**, and click **Copy**.
In your browser, visit:

```
http://<YOUR_EXTERNAL_IP>:8501
```

For example:

```
http://136.114.199.97:8501
```

*(Note: do not use `https://` — it may cause connection issues in some environments.)*

If everything is configured correctly, your **LLMOps Anime Recommender System** web app will load in your browser and be fully interactive!

## ✅ **In Summary**

You have now successfully:

* Built and containerised your application using **Docker**.
* Deployed it on **Kubernetes** via **Minikube**.
* Injected API secrets into the cluster securely.
* Exposed the service externally using a **Minikube tunnel** and **port forwarding**.

Your **LLMOps Anime Recommender System** is now live and running inside a fully functional Kubernetes environment on **Google Cloud Platform** — completing your end-to-end cloud deployment.
