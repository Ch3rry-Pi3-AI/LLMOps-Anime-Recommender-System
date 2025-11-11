# 🌸 **LLMOps Anime Recommender System — Project Overview**

This project implements a complete **LLMOps workflow** for an **anime recommender system**, combining data preparation, vector storage, prompt engineering, LLM reasoning, and full deployment on **Google Cloud Platform (GCP)** using **Docker** and **Kubernetes**.

<p align="center">
  <img src="img/streamlit/streamlit_app.gif" alt="Streamlit App Demo" width="100%">
</p>

## 🧩 **Grouped Stages**

* **00 — Project Setup**
  Established the base VS Code structure, environment setup, and configuration files.

* **01–05 — Core LLM Logic**
  Implemented the data loader, vector store, prompt template, recommender class, and integrated them through the pipeline.

* **06 — Streamlit Application**
  Built the front-end interface for generating recommendations interactively.

* **07 — Containerisation and Manifests**
  Created the Dockerfile and Kubernetes deployment YAML files.

* **08 — GCP VM and Docker Setup**
  Configured a GCP Virtual Machine and installed Docker Engine.

* **09–11 — Cluster and Deployment**
  Installed Minikube and kubectl, created firewall rules, deployed the application on Kubernetes, and exposed it via an external IP.

* **12 — Grafana Cloud Monitoring**
  Integrated Grafana for system monitoring and performance tracking.

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
├── Dockerfile                 # Container image definition
├── llmops-k8s.yaml            # Kubernetes Deployment + Service manifest
├── pyproject.toml
├── requirements.txt
├── setup.py
├── uv.lock
└── README.md
```

## ✅ **Summary**

This project demonstrates how to take a **retrieval-augmented generation (RAG)** system from concept to production deployment. It combines **LLM-driven recommendation logic**, **container orchestration**, and **cloud deployment** in a single cohesive MLOps pipeline — forming a complete foundation for future scalable LLMOps applications.
