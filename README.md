# 🤖 **LLM-Powered Recommender Integration — LLMOps Anime Recommender System**

This stage introduces the **final core backend component** of the **LLMOps Anime Recommender System** — the **anime recommender engine**.
The `AnimeRecommender` class integrates the **retriever**, **vector store**, **prompt template**, and **Groq LLM**, enabling **end-to-end, retrieval-augmented anime recommendations**.

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
├── pipeline/                        # 🔁 Placeholder for workflow scripts
├── src/
│   ├── data_loader.py               # 📥 Loads and preprocesses the anime dataset
│   ├── vector_store_builder.py      # 🧠 Builds and loads the Chroma vector store
│   ├── prompt_template.py           # 💬 Defines the structured LLM prompt
│   └── recommender.py               # 🤖 Generates LLM-based anime recommendations
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

## ⚙️ **Overview of `recommender.py`**

The **`AnimeRecommender`** class serves as the heart of the system — connecting the vector store retriever and the Groq LLM via a **RetrievalQA** chain.
This module completes the **retrieval-augmented generation (RAG)** pipeline that powers the anime recommendation process.

### Key Functions

1. **Initialises the Groq LLM** (`ChatGroq`) with a fixed temperature for consistent, factual responses.
2. **Combines** the retriever, prompt template, and LLM into a single LangChain `RetrievalQA` chain.
3. **Retrieves relevant anime context** from the Chroma vector database.
4. **Generates structured, user-specific recommendations** using the LLM and predefined prompt.

### Example Usage

```python
from src.recommender import AnimeRecommender
from src.vector_store_builder import VectorStoreBuilder
from config.config import GROQ_API_KEY, MODEL_NAME

# Load vector store and create retriever
builder = VectorStoreBuilder(csv_path="data/processed_anime.csv")
vector_store = builder.load_vector_store()
retriever = vector_store.as_retriever()

# Create the recommender
recommender = AnimeRecommender(
    retriever=retriever,
    api_key=GROQ_API_KEY,
    model_name=MODEL_NAME
)

# Generate recommendations
query = "Recommend anime with deep character development and emotional storytelling."
response = recommender.get_recommendation(query)
print(response)
```

### Output Example

```
1. Violet Evergarden — A young woman trained as a weapon learns to write letters that connect people...
2. Clannad: After Story — A heartfelt exploration of love, loss, and family...
3. Your Lie in April — A touching story of music, grief, and personal growth...

Each of these anime explores emotional themes and strong character arcs.
```

The recommender retrieves relevant context from the **Chroma vector store**, injects it into the **prompt template**, and uses the **Groq LLM** to generate meaningful, structured, and human-like responses.

## ✅ **In Summary**

This stage completes the **core backend workflow** of the project:

* Integrates `AnimeRecommender` for **end-to-end RAG-based inference**.
* Connects the **data loader**, **vector store**, and **prompt template** into a unified recommendation pipeline.
* Establishes a fully functional **LLM-powered anime recommendation engine**, paving the way for Streamlit frontend integration in the next phase.
