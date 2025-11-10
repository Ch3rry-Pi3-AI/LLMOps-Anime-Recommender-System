# `src/` README — Core Source Code

This folder contains the **main backend logic** for the **LLMOps Anime Recommender System**.
It brings together data preparation, vector storage, prompt engineering, and retrieval-augmented generation (RAG) to enable accurate, context-driven anime recommendations powered by large language models.

## 📁 Folder Overview

```text
src/
├── data_loader.py          # 📥 Loads and preprocesses the anime dataset
├── vector_store_builder.py # 🧠 Builds and loads the Chroma vector store
├── prompt_template.py      # 💬 Defines the structured LLM prompt
└── recommender.py          # 🤖 Generates recommendations using LLM + retriever
```

## ⚙️ Description

* **`data_loader.py`**
  Reads the raw anime dataset, checks for missing columns, and merges text fields (title, synopsis, genres) into one combined feature for embedding and retrieval.

* **`vector_store_builder.py`**
  Uses `HuggingFaceEmbeddings` (`all-MiniLM-L6-v2`) to convert text into embeddings and store them in a **Chroma vector database** for semantic search and similarity retrieval.

* **`prompt_template.py`**
  Defines a **LangChain `PromptTemplate`** that instructs the LLM to act as an expert anime recommender, producing exactly three structured recommendations with short summaries and explanations.

* **`recommender.py`**
  Implements the **`AnimeRecommender`** class, which links the retriever and the Groq LLM via `RetrievalQA`.
  It takes user queries, retrieves relevant context from the vector store, and produces well-structured, fact-based recommendations using the prompt template.
  
Together, these modules form the **core engine** of the system — enabling:

* Clean and validated data ingestion
* Efficient vector embedding and persistence
* Structured LLM prompting
* End-to-end retrieval-augmented recommendation generation
