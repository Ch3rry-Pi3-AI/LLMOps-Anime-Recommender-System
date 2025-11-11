# 🌸 **LLMOps Anime Recommender System — Project Overview**

This repository presents a **fully operational LLMOps workflow** for an **anime recommendation system**, integrating all stages from **data ingestion and embedding generation** to **LLM reasoning**, **containerisation**, and **cloud deployment** on **Google Cloud Platform (GCP)** using **Docker** and **Kubernetes**.

<p align="center">
  <img src="img/streamlit/streamlit_app.gif" alt="Streamlit App Demo" width="100%">
</p>

## 🧩 **Grouped Stages**

| Stage                                   | Description                                                                                                                                          |
| :-------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------- |
| **00 — Project Setup**                  | Initialised the VS Code structure, virtual environment, and configuration files.                                                                     |
| **01–05 — Core LLM Logic**              | Built the data loader, vector store, prompt template, and recommender class, then unified them through a modular pipeline.                           |
| **06 — Streamlit Application**          | Developed an interactive front end for generating personalised anime recommendations.                                                                |
| **07 — Containerisation and Manifests** | Authored the Dockerfile and Kubernetes YAML manifests for deployment.                                                                                |
| **08 — GCP VM and Docker Setup**        | Configured a GCP Virtual Machine and installed Docker Engine for container management.                                                               |
| **09–11 — Cluster and Deployment**      | Installed Minikube and kubectl, configured networking and firewall rules, deployed the application to Kubernetes, and exposed it via an external IP. |
| **12 — Grafana Cloud Monitoring**       | Integrated Grafana Cloud for system metrics and real-time monitoring dashboards.                                                                     |

## 🗂️ **Project Structure**

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
├── Dockerfile                 # Defines container image
├── llmops-k8s.yaml            # Kubernetes Deployment + Service manifest
├── pyproject.toml
├── requirements.txt
├── setup.py
├── uv.lock
└── README.md
```

## 🚀 **Summary**

The **LLMOps Anime Recommender System** showcases how a **retrieval-augmented generation (RAG)** pipeline can be transformed from concept to **production-grade deployment**.
It unites **LLM reasoning**, **vector-based retrieval**, and **prompt engineering** within a robust **DevOps and MLOps infrastructure**, serving as a foundational blueprint for future **scalable and monitored LLM applications**.