# 🧩 **Data Loader Creation — LLMOps Anime Recommender System**

This stage introduces the **first core module** in the **LLMOps Anime Recommender System**: a simple yet essential **data loader** responsible for reading and preprocessing the anime dataset.
The `AnimeDataLoader` class ensures that all required fields are present, handles basic cleaning, and produces a compact processed file ready for later embedding and recommendation tasks.

## 🗂️ **Project Structure (Updated)**

```text
llmops_anime_recommender_system/
├── .env                             
├── .gitignore                       
├── .python-version                  
├── app/                             
├── config/
│   └── config.py                    # ⚙️ Loads environment variables and model configuration
├── data/
│   └── anime__with__synopsis.csv    # 📊 Dataset used by the data loader
├── pipeline/                        
├── src/
│   └── data_loader.py               # 📥 Loads and preprocesses the anime dataset
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

## ⚙️ **Overview of `data_loader.py`**

The **`AnimeDataLoader`** class, located in `src/data_loader.py`, performs three key functions:

1. **Loads** the raw anime dataset from the `data/` directory.
2. **Validates** required columns (`Name`, `Genres`, `sypnopsis`) and raises an error if any are missing.
3. **Combines** text fields into a single column (`combined_info`) to streamline downstream text embedding.

### Example Usage

```python
from src.data_loader import AnimeDataLoader

loader = AnimeDataLoader(
    original_csv="data/anime__with__synopsis.csv",
    processed_csv="data/processed_anime.csv"
)

processed_path = loader.load_and_process()
print(f"Processed dataset saved at: {processed_path}")
```

### Output Example

```
Processed dataset saved at: data/processed_anime.csv
```

The resulting file includes one column (`combined_info`) containing the formatted combination of title, synopsis, and genres for each anime.

## ✅ **In Summary**

This update marks the **first data-processing milestone** in the project:

* Introduces `AnimeDataLoader` for reliable dataset ingestion and preparation.
* Adds structure and validation logic to ensure consistency for later stages.
* Prepares the data for **embedding generation and recommendation modelling** in upcoming phases.
