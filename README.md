# 🎨 **Streamlit Application — LLMOps Anime Recommender System**

This stage introduces the **front-end layer** of the **LLMOps Anime Recommender System**, transforming the backend pipelines into an **interactive web application** built with **Streamlit**.
The app provides a clean, responsive interface for users to describe their anime preferences or select predefined themes and receive **real-time, LLM-powered recommendations**.

<p align="center">
  <img src="img/streamlit/streamlit_app.gif" alt="Anime Recommender Streamlit App Demo" width="100%" />
</p>

## 🗂️ **Project Structure (Updated)**

```text
llmops_anime_recommender_system/
├── .env                          
├── .gitignore                      
├── .python-version                
├── app/
│   └── app.py                       # 🎨 Streamlit front-end for user interaction
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
│   └── streamlit/streamlit_app.gif  # 🎞️ Demonstration of the final Streamlit interface
├── pyproject.toml                   
├── requirements.txt                
├── setup.py                        
├── uv.lock                         
└── README.md                        # 📖 Documentation (you are here)
```

## ⚙️ **Overview of the Streamlit App**

The **`app.py`** module serves as the **presentation layer** of the project — integrating directly with the `AnimeRecommendationPipeline` to deliver a polished, user-friendly recommendation experience.

### 🧩 Core Features

1. **Interactive Query Input**
   Users can enter free-text descriptions of their preferences or choose from preset themes like *Action*, *Romance*, *Drama*, or *Slice of Life*.

2. **Automatic Generation on Enter or Click**
   Pressing *Enter* or selecting a theme automatically triggers a recommendation query without additional input.

3. **Real-Time Recommendations**
   The app fetches responses from the Groq-powered LLM pipeline and displays them in a structured format with:

   * **Title**
   * **Plot Summary**
   * **Why it matches your preferences**

4. **Dynamic Layout and Styling**
   Centered input layout, responsive design, and Markdown-based cards ensure clear readability and a professional presentation.

## 🚀 **Running the Application**

From the project root, start the app with:

```bash
streamlit run app/app.py
```

Once launched, Streamlit will open a local browser window (typically at `http://localhost:8501`).

You can then type prompts such as:

> *“Dark thriller anime with psychological themes and mystery.”*

or select a theme button like *Romance* or *Action*.

The system will respond with structured, concise recommendations, for example:

```
1. Death Note — A brilliant student discovers a notebook with deadly powers.
   Why it matches your preferences: Dark psychological tension and moral complexity.

2. Paranoia Agent — Surreal exploration of anxiety, guilt, and shared delusion.
   Why it matches your preferences: Psychological mystery and layered storytelling.

3. Monster — A gripping cat-and-mouse chase between a doctor and his former patient.
   Why it matches your preferences: Complex moral undertones and psychological suspense.
```

## ✅ **In Summary**

This stage marks the **transition from backend logic to user-facing interaction**, completing the full LLMOps cycle:

* Integrates the **recommendation pipeline** into a web interface.
* Provides an **intuitive and aesthetic** way for users to explore anime suggestions.
* Demonstrates how **LLM reasoning** and **retrieval-augmented workflows** can be deployed interactively.

The **Streamlit application** now represents the project’s **final deployment layer** — turning your engineered recommendation system into a live, accessible experience.
