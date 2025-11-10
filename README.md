# 💬 **Prompt Engineering Integration — LLMOps Anime Recommender System**

This stage adds the **prompt engineering component** to the **LLMOps Anime Recommender System**.
The `get_anime_prompt()` function introduces a structured **LangChain `PromptTemplate`** that guides the LLM in generating high-quality, context-aware anime recommendations.
Combined with the vector store and data loader, this marks the transition from **data preparation** to **LLM-driven retrieval and reasoning**.

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
│   └── prompt_template.py           # 💬 Defines the LLM prompt structure for recommendations
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

## ⚙️ **Overview of `prompt_template.py`**

The **`get_anime_prompt()`** function defines a **LangChain `PromptTemplate`** that ensures consistent, structured responses from the LLM.
It sets clear behavioural instructions for the model to act as an *expert anime recommender* and respond within a specific, well-formatted structure.

### Key Features

1. **Consistent Response Format** — Generates exactly three recommendations, each with a title, short plot summary, and rationale.
2. **Context-Aware Reasoning** — Incorporates vector-retrieved context to make the responses relevant to user preferences.
3. **Controlled Output** — Instructs the LLM not to fabricate information if insufficient context is available.
4. **Reusability** — Encapsulated in a single callable function for clean integration with the LangChain pipeline.

### Example Usage

```python
from src.prompt_template import get_anime_prompt

prompt = get_anime_prompt()
formatted_prompt = prompt.format(
    context="Top-rated anime featuring adventure and strong female leads.",
    question="Can you suggest anime similar to Violet Evergarden?"
)

print(formatted_prompt)
```

### Output Example

```
You are an expert anime recommender. Your job is to help users find the perfect anime...

Context:
Top-rated anime featuring adventure and strong female leads.

User's question:
Can you suggest anime similar to Violet Evergarden?

Your well-structured response:
```

The formatted prompt ensures that downstream LLM responses are both **coherent** and **contextually grounded**.

## ✅ **In Summary**

This stage completes the **retrieval and prompt engineering foundation** of the system:

* Adds `get_anime_prompt()` for structured, consistent LLM communication.
* Connects the **data**, **vector store**, and **prompt** layers into a unified retrieval-augmented workflow.
* Prepares the system for the next phase — **end-to-end recommendation inference and Streamlit integration**.
