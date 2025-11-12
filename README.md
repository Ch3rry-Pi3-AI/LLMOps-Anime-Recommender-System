# 🧠 **Vector Store Creation — LLMOps Anime Recommender System**

This stage introduces the **vector store component** of the **LLMOps Anime Recommender System**.
The `VectorStoreBuilder` class constructs a **Chroma vector database** from the preprocessed anime dataset, allowing fast and efficient **semantic search** and **similarity retrieval** for recommendations powered by large language models.

## 🗂️ **Project Structure (Updated)**

```text
llmops_anime_recommender_system/
├── .env                             
├── .gitignore                       
├── .python-version                  
├── app/                             
├── config/
│   └── config.py                    
├── data/
├── pipeline/                        
├── src/
│   ├── data_loader.py               
│   └── vector_store_builder.py      # 🧠 Builds and loads the Chroma vector store
├── utils/
│   ├── __init__.py
│   ├── custom_exception.py          
│   └── logger.py                    
├── pyproject.toml                   
├── requirements.txt                 
├── setup.py                         
├── uv.lock                          
└── README.md                        # 📖 Documentation (you are here)
```

## ⚙️ **Overview of `vector_store_builder.py`**

The **`VectorStoreBuilder`** class, located in `src/vector_store_builder.py`, handles embedding generation and vector database construction.

### Key Functions

1. **Loads the processed CSV** (from the data loader output).
2. **Splits text** into manageable chunks using `CharacterTextSplitter` for optimal embedding performance.
3. **Generates embeddings** with `HuggingFaceEmbeddings` (`all-MiniLM-L6-v2`).
4. **Stores embeddings** in a persistent **Chroma vector database** for efficient similarity search.
5. Provides a **loader method** to easily reload the stored vector database for later use.

### Example Usage

```python
from src.vector_store_builder import VectorStoreBuilder

builder = VectorStoreBuilder(
    csv_path="data/processed_anime.csv",
    persist_dir="chroma_db"
)

# Build and save the Chroma vector store
builder.build_and_save_vectorstore()

# Load the vector store when needed
vector_store = builder.load_vector_store()
print("✅ Vector store loaded successfully.")
```

### Output Example

```
✅ Vector store loaded successfully.
Chroma database persisted at: chroma_db/
```

The generated Chroma database (`chroma_db/`) will store all anime embeddings locally, enabling quick access for future recommendation queries.

## ✅ **In Summary**

This stage establishes the **semantic foundation** of the LLMOps Anime Recommender System:

* Introduces `VectorStoreBuilder` for **embedding generation and persistence**.
* Enables **semantic similarity search** across anime descriptions.
* Prepares the groundwork for **retrieval-augmented recommendations** and **LLM-powered reasoning** in subsequent stages.
