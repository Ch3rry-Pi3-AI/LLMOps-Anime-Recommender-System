# 🚢 Containerisation & Kubernetes Deployment — LLMOps Anime Recommender System

This stage packages the app into a Docker image and provides a Kubernetes manifest to run it as a service. You can run the container locally for quick checks, then deploy it to a cluster (Minikube, kind, or a managed cloud).

## 🗂️ Project Structure (Updated)

```text
llmops_anime_recommender_system/
├── .env
├── .gitignore
├── .python-version
├── app/
│   └── app.py
├── config/
│   └── config.py
├── data/
├── pipeline/
│   ├── build_pipeline.py
│   └── recommendation_pipeline.py
├── src/
│   ├── data_loader.py
│   ├── vector_store.py
│   ├── prompt_template.py
│   └── recommender.py
├── utils/
│   ├── __init__.py
│   ├── custom_exception.py
│   └── logger.py
├── img/
│   └── streamlit/streamlit_app.gif
├── Dockerfile                 # New: container image definition
├── llmops-k8s.yaml            # New: Deployment + Service manifest
├── pyproject.toml
├── requirements.txt
├── setup.py
├── uv.lock
└── README.md
```

## 🧱 Build the Image

```bash
# From repo root
docker build -t llmops-app:latest .
```

Run locally to verify:

```bash
# Uses your .env for secrets; app serves on 8501
docker run --rm -p 8501:8501 --env-file .env llmops-app:latest
```

Open [http://localhost:8501](http://localhost:8501) to confirm it’s up.

## 🔐 Create Kubernetes Secrets

The manifest expects a secret named `llmops-secrets`. Create it from your `.env`:

```bash
kubectl create secret generic llmops-secrets --from-env-file=.env
```

If you’re using a namespace, add `-n <your-namespace>` here and in all following commands.

## ☸️ Deploy to Kubernetes

```bash
kubectl apply -f llmops-k8s.yaml
kubectl get pods
kubectl get svc llmops-service
```

The service is a `LoadBalancer`:

* **Minikube:** expose and open

  ```bash
  minikube image load llmops-app:latest
  minikube service llmops-service
  ```
* **kind:** load local image

  ```bash
  kind load docker-image llmops-app:latest
  kubectl apply -f llmops-k8s.yaml
  kubectl get svc llmops-service
  ```
* **Managed cloud (e.g., GKE/AKS/EKS):** ensure `image` points to a registry (e.g., `gcr.io/.../llmops-app:tag`) and that your nodes can pull it.

## 🧩 What the Manifest Does

* **Deployment**

  * Name: `llmops-app`
  * Image: `llmops-app:latest` with `IfNotPresent` (good for local clusters when you load the image)
  * Port: container listens on `8501`
  * Injects env vars from `llmops-secrets`

* **Service**

  * Name: `llmops-service`
  * Type: `LoadBalancer` for external access
  * Port: `80` → `targetPort: 8501`

## 🛠️ Tips and Troubleshooting

* **Local image not found by cluster**

  * Minikube: `minikube image load llmops-app:latest`
  * kind: `kind load docker-image llmops-app:latest`
  * Or push to a remote registry and update the `image:` in `llmops-k8s.yaml`.

* **Stuck on Pending External IP**

  * On local clusters, `LoadBalancer` may not provision an external IP. Use `minikube service llmops-service` or change the service to `NodePort`:

    ```yaml
    spec:
      type: NodePort
      ports:
        - port: 80
          targetPort: 8501
          nodePort: 30080
    ```

* **Secret updates**

  * Update `.env`, then:

    ```bash
    kubectl delete secret llmops-secrets
    kubectl create secret generic llmops-secrets --from-env-file=.env
    kubectl rollout restart deployment/llmops-app
    ```

* **Production notes**

  * Pin a specific image tag (e.g., `llmops-app:v1.0.0`), avoid `latest`.
  * Add `resources.requests/limits` and `readinessProbe`/`livenessProbe` if you need tighter reliability.

That’s it for this stage: you now have a reproducible **Docker image** and a **Kubernetes manifest** to run the app consistently across environments.
