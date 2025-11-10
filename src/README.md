# `src/` README — Core Source Code

This folder contains the **core source modules** for the **LLMOps Anime Recommender System**.
These scripts form the foundation of the system’s backend logic — handling **data loading**, **vector storage**, and **prompt engineering** for the language model’s recommendation workflow.

## 📁 Folder Overview

```text
src/
├── data_loader.py          # Loads and preprocesses the anime dataset
├── vector_store_builder.py # Builds and loads the Chroma vector store
└── prompt_template.py      # Defines the structured prompt for the LLM recommender
```

## ⚙️ Description

* **`data_loader.py`**
  Reads the raw anime dataset, validates required columns, and merges key fields (title, synopsis, genres) into a single text feature for embedding and recommendation tasks.

* **`vector_store_builder.py`**
  Generates and stores vector embeddings using **Hugging Face sentence transformers** (`all-MiniLM-L6-v2`), building a **Chroma vector database** for semantic similarity search.

* **`prompt_template.py`**
  Defines a reusable **LangChain `PromptTemplate`** for the anime recommender.
  The template ensures structured, natural responses by instructing the LLM to:

  * Recommend **three anime titles** per query
  * Provide concise plot summaries and matching explanations
  * Avoid fabricating information if context is insufficient

Together, these modules enable **data ingestion**, **semantic search**, and **prompt-driven reasoning**, forming the **core intelligence layer** of the Anime Recommender System.
