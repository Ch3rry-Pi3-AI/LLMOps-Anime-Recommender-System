"""
app.py

Streamlit front-end for the LLMOps Anime Recommender System.
Provides an intuitive interface for users to enter their anime preferences
and receive personalised recommendations via the underlying recommendation pipeline.
"""

# --------------------------------------------------------------
# Imports
# --------------------------------------------------------------
import streamlit as st
from dotenv import load_dotenv
from pipeline.recommendation_pipeline import AnimeRecommendationPipeline


# --------------------------------------------------------------
# Streamlit Page Configuration
# --------------------------------------------------------------
st.set_page_config(page_title="Anime Recommender", layout="wide")
load_dotenv()


# --------------------------------------------------------------
# Pipeline Initialisation
# --------------------------------------------------------------
@st.cache_resource
def init_pipeline() -> AnimeRecommendationPipeline:
    """Initialise and cache the Anime Recommendation Pipeline."""
    return AnimeRecommendationPipeline()


pipeline = init_pipeline()


# --------------------------------------------------------------
# Page Title and Description
# --------------------------------------------------------------
st.markdown(
    "<h1 style='text-align:center;'>🎌 Anime Recommender System</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='text-align:center;'>Enter a short description of the kind of anime you enjoy, "
    "or select a theme to get tailored recommendations.</p>",
    unsafe_allow_html=True,
)


# --------------------------------------------------------------
# Session State Setup
# --------------------------------------------------------------
if "query_text" not in st.session_state:
    st.session_state.query_text = ""
if "auto_run" not in st.session_state:
    st.session_state.auto_run = False


def set_query_text(theme: str) -> None:
    """Set query text when a theme button is clicked."""
    st.session_state.query_text = theme
    st.session_state.auto_run = True  # trigger generation automatically


# --------------------------------------------------------------
# Input Layout
# --------------------------------------------------------------
_, main_col, _ = st.columns([0.15, 0.7, 0.15])

with main_col:
    query = st.text_input(
        "Describe your preferences:",
        value=st.session_state.query_text,
        placeholder=(
            "Examples: dark thriller with psychological twists; "
            "action with strong female lead; wholesome slice of life..."
        ),
        key="query_box",
    )

    st.write("Quick themes:")
    button_columns = st.columns(5)
    themes = ["Dark Thriller", "Action", "Romance", "Drama", "Slice of Life"]

    for i, theme in enumerate(themes):
        if button_columns[i].button(theme, use_container_width=True):
            set_query_text(theme)

    run = st.button("Get Recommendations", type="primary", use_container_width=True)

    # Detect Enter press → Streamlit reruns the app when you hit Enter
    # If query changed, auto-trigger recommendation
    if query and query != st.session_state.query_text:
        st.session_state.query_text = query
        st.session_state.auto_run = True


# --------------------------------------------------------------
# Helper Function — Render Recommendations
# --------------------------------------------------------------
def render_recommendations(response) -> None:
    """Display the recommendations returned by the pipeline."""

    st.markdown("<h2 style='text-align:center;'>Recommendations</h2>", unsafe_allow_html=True)

    _, rec_col, _ = st.columns([0.1, 0.8, 0.1])
    with rec_col:

        def render_item(index: int, item: dict) -> None:
            """Render a single recommendation card."""
            title = (
                item.get("title")
                or item.get("name")
                or item.get("anime")
                or f"Recommendation {index}"
            )
            plot = item.get("plot") or item.get("summary") or item.get("synopsis")
            why = (
                item.get("why")
                or item.get("why_it_matches")
                or item.get("why_it_fits")
                or item.get("reason")
            )

            st.markdown(f"**{index}. {title}**")
            if plot:
                st.markdown(f"**Plot:** {plot}")
            if why:
                st.markdown(f"**Why it matches your preferences:** {why}")
            st.markdown("")

        if isinstance(response, list):
            if all(isinstance(x, dict) for x in response):
                for i, item in enumerate(response, start=1):
                    render_item(i, item)
            else:
                for i, item in enumerate(response, start=1):
                    st.markdown(f"**{i}.** {item}")

        elif isinstance(response, dict):
            render_item(1, response)
        else:
            st.write(response)


# --------------------------------------------------------------
# Generate and Display Recommendations
# --------------------------------------------------------------
if (run or st.session_state.auto_run) and st.session_state.query_text:
    with st.spinner("Fetching recommendations for you..."):
        response = pipeline.recommend(st.session_state.query_text)
        render_recommendations(response)
        st.session_state.auto_run = False
