# `pipeline/` README — Pipeline Orchestration

This folder contains the **orchestration scripts** that connect all components of the **LLMOps Anime Recommender System** — from data processing and embedding generation to full recommendation inference.
Each pipeline script provides a high-level workflow that coordinates modules from the `src/`, `config/`, and `utils/` directories.

## 📁 Folder Overview

```text
pipeline/
├── build_pipeline.py                # ⚙️ Builds the full data → vector store pipeline
└── anime_recommendation_pipeline.py # 🤖 Runs the end-to-end recommendation pipeline
```

## ⚙️ Description

* **`build_pipeline.py`**
  Executes the complete backend setup workflow:

  1. Loads and processes the anime dataset using `AnimeDataLoader`.
  2. Builds a **Chroma vector store** from the processed dataset using `VectorStoreBuilder`.
  3. Logs progress and handles exceptions gracefully via the project’s custom utilities.

* **`anime_recommendation_pipeline.py`**
  Defines the **`AnimeRecommendationPipeline`** class, which:

  1. Loads the stored vector database and initialises the LLM recommender (`AnimeRecommender`).
  2. Accepts a user query and returns a structured, context-aware anime recommendation.
  3. Provides a single entry point for integrating the backend with the future **Streamlit front-end app**.

Together, these scripts form the **operational layer** of the LLMOps system — automating data preparation, embedding persistence, and real-time recommendation generation.
