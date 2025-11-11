# 🌸 **LLMOps Anime Recommender System — Project Overview**

This repository presents a **complete LLMOps workflow** for an **anime recommendation system**, covering every layer from **data processing and embedding generation** to **LLM reasoning**, **containerisation**, and **cloud deployment** on **Google Cloud Platform (GCP)** using **Docker** and **Kubernetes**.

<p align="center">
  <img src="img/streamlit/streamlit_app.gif" alt="Streamlit App Demo" width="100%">
</p>

## 🧩 **Grouped Stages**

|     #     | Stage                            | Description                                                                                                                   |
| :-------: | :------------------------------- | :---------------------------------------------------------------------------------------------------------------------------- |
|   **00**  | **Project Setup**                | Established the base VS Code structure, environment setup, and configuration files.                                           |
| **01–05** | **Core LLM Logic**               | Built the data loader, vector store, prompt template, and recommender class, then unified them through a modular pipeline.    |
|   **06**  | **Streamlit Application**        | Developed a responsive front end that allows users to generate personalised anime recommendations.                            |
|   **07**  | **Containerisation & Manifests** | Authored the Dockerfile and Kubernetes YAML manifests for scalable deployment.                                                |
|   **08**  | **GCP VM & Docker Setup**        | Configured a GCP Virtual Machine and installed Docker Engine for container management.                                        |
| **09–11** | **Cluster & Deployment**         | Installed Minikube and kubectl, configured firewall rules, deployed the app on Kubernetes, and exposed it via an external IP. |
|   **12**  | **Grafana Cloud Monitoring**     | Integrated Grafana Cloud for visualising metrics, system health, and performance trends.                                      |

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

The **LLMOps Anime Recommender System** demonstrates how to take a **retrieval-augmented generation (RAG)** workflow from prototype to production.
It combines **LLM reasoning**, **vector-based retrieval**, and **prompt engineering** within a robust **MLOps pipeline** deployed on **Kubernetes**, forming a scalable foundation for future **LLMOps-driven applications**.

