# 🔁 **Pipeline Orchestration — LLMOps Anime Recommender System**

This stage brings together all the **core backend workflows** of the **LLMOps Anime Recommender System**, combining data ingestion, embedding generation, and end-to-end anime recommendation logic.
It introduces two main pipelines — one for building the system’s vector database and another for producing live recommendations via the Groq-powered LLM.

## 🗂️ **Project Structure (Updated)**

```text
llmops_anime_recommender_system/
├── .env                             # 🔑 API keys (Groq & Hugging Face)
├── .gitignore                       # 🚫 Git ignore rules
├── .python-version                  # 🐍 Python version pin for consistency
├── app/                             # 🎨 Streamlit application (to be developed)
├── config/
│   └── config.py                    # ⚙️ Loads environment variables and model configuration
├── data/                            # 📊 Contains raw and processed anime datasets
├── pipeline/
│   ├── build_pipeline.py             # 🏗️ Builds data and vector store pipeline
│   └── recommendation_pipeline.py    # 🤖 Executes full recommendation workflow
├── src/
│   ├── data_loader.py               # 📥 Loads and preprocesses anime data
│   ├── vector_store_builder.py      # 🧠 Builds and loads the Chroma vector store
│   ├── prompt_template.py           # 💬 Defines structured LLM prompt
│   └── recommender.py               # 🔗 Connects retriever and Groq LLM via LCEL
├── utils/
│   ├── __init__.py
│   ├── custom_exception.py          # Unified error handling
│   └── logger.py                    # Centralised logging setup
├── pyproject.toml                   # 🧩 Project metadata and uv configuration
├── requirements.txt                 # 📦 Dependencies
├── setup.py                         # 🔧 Editable install support
├── uv.lock                          # 🔒 Dependency lock file
└── README.md                        # 📖 Documentation (you are here)
```

## ⚙️ **Overview of the Pipeline Stage**

### 🏗️ `build_pipeline.py`

Automates the full data-to-vector workflow:

1. Loads and preprocesses the anime dataset using `AnimeDataLoader`.
2. Builds embeddings from processed text via `VectorStoreBuilder`.
3. Saves a persistent **Chroma vector store** for downstream retrieval.
4. Provides a reproducible foundation for all later inference steps.

**Example:**

```bash
python pipeline/build_pipeline.py
```

**Output:**

```
🚀 Starting pipeline build...
✅ Data successfully loaded and processed.
✅ Vector store built and persisted successfully.
🎯 Pipeline build completed successfully.
```

### 🤖 `recommendation_pipeline.py`

Implements the runtime recommendation logic:

1. Loads the stored **Chroma vector database**.
2. Initialises the **AnimeRecommender** class with the retriever, Groq LLM, and structured prompt.
3. Accepts user queries and returns detailed, context-aware anime recommendations.

**Example:**

```bash
python pipeline/recommendation_pipeline.py
```

**Sample Output:**

```
1. Violet Evergarden — A young woman trained as a weapon learns to write letters that connect people...
2. Clannad: After Story — A heartfelt exploration of love, loss, and family...
3. Your Lie in April — A touching story of music, grief, and personal growth...

Each of these anime explores emotional themes and strong character arcs.
```

## ✅ **In Summary**

The **pipeline stage** unifies the entire backend logic of the project:

* `build_pipeline.py` prepares and embeds the dataset into a Chroma vector store.
* `recommendation_pipeline.py` retrieves context and generates structured recommendations through the Groq LLM.

Together, they form the **operational core** of the LLMOps Anime Recommender System — seamlessly linking data, embeddings, and intelligent recommendations, and providing a robust backend for future Streamlit interface integration.
