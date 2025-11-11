# 🎨 **App Front-End — LLMOps Anime Recommender System**

This folder contains the **Streamlit front-end application** for the **LLMOps Anime Recommender System**.
The app provides a clean, interactive interface where users can describe their anime preferences or select from predefined themes, and receive **personalised, LLM-powered recommendations** in real time.

## 🗂️ **Folder Overview**

```text
app/
└── app.py   # 🎌 Streamlit front-end for user interaction and recommendations
```

## ⚙️ **Overview of `app.py`**

The Streamlit app acts as the **final layer** of the project — connecting directly to the backend recommendation pipeline to deliver human-friendly results.

### Key Features

1. **Intuitive Interface** — Users can type free-text descriptions (e.g. *“dark thriller with psychological twists”*) or click themed buttons (*Action, Romance, Drama, Slice of Life*).
2. **Real-Time Recommendations** — On clicking “Get Recommendations” or pressing Enter, the app triggers the backend `AnimeRecommendationPipeline` to generate context-aware suggestions.
3. **Dynamic Rendering** — Recommendations are displayed as structured, readable cards showing:

   * **Title**
   * **Plot Summary**
   * **Why it matches the user’s preferences**
4. **Session Memory** — The app remembers the last query entered for seamless reruns within the same session.
5. **Automatic Triggering** — Typing or selecting a theme automatically fetches new recommendations without needing to press the button manually.

## 🧠 **How It Works**

1. **Pipeline Connection**
   The app initialises and caches the backend `AnimeRecommendationPipeline`, which internally uses:

   * `AnimeDataLoader` for data preparation
   * `VectorStoreBuilder` for Chroma-based embeddings
   * `AnimeRecommender` for Groq LLM inference

2. **User Input & Theming**

   * Input is collected via a centered text box.
   * Predefined theme buttons auto-populate the query for quick testing.

3. **Result Rendering**

   * Results are formatted into clean Markdown cards.
   * The renderer gracefully handles different response formats (list, dict, or plain text).

## 🧩 **Example Usage**

Launch the app from the project root:

```bash
streamlit run app/app.py
```

Once launched, open your browser and enter a query such as:

> *“Wholesome slice of life with school setting and strong friendships.”*

or select a quick theme (e.g., *Dark Thriller* or *Romance*).

The app will display structured recommendations like:

```
1. Violet Evergarden — A young woman learns to express emotions through letter writing.
   Why it matches your preferences: Deep emotional storytelling and elegant visual design.

2. Clannad: After Story — A touching continuation exploring family, love, and loss.
   Why it matches your preferences: Powerful emotional arcs and heartfelt drama.
```

## ✅ **In Summary**

The `app.py` module transforms the LLMOps Anime Recommender System into a **user-facing product** by:

* Delivering a polished, interactive interface for anime discovery.
* Seamlessly integrating with the underlying Groq LLM-powered recommendation pipeline.
* Laying the groundwork for future UI enhancements — such as search history, filters, and visual analytics.

This marks the **final deployment-ready stage** of the project, bridging advanced LLM reasoning with an accessible, engaging user experience.
