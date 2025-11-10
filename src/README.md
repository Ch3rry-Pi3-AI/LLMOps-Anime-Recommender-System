# `src/` README — Core Source Code

This folder contains the **main source code** for the **LLMOps Anime Recommender System**.
It includes modules for **data loading**, **text preprocessing**, and **vector store construction**, forming the foundation for the system’s recommendation pipeline.

## 📁 Folder Overview

```text
src/
├── data_loader.py          # Loads and preprocesses the anime dataset
└── vector_store_builder.py # Builds and loads the Chroma vector store
```

## ⚙️ Description

* `data_loader.py` reads the raw anime dataset, validates required columns, and combines text fields (title, synopsis, and genres) into a single feature for embedding and recommendation tasks.
* `vector_store_builder.py` creates a **Chroma vector store** from the processed dataset using **Hugging Face embeddings**, then saves it locally for fast retrieval and querying.

Together, these modules form the **core backend** for preparing and storing the data that powers the LLM-based anime recommender system.
