"""
recommendation_pipeline.py

Defines the AnimeRecommendationPipeline class, which connects
the vector store and recommender to produce anime suggestions
based on user queries.
"""

# --------------------------------------------------------------
# Imports
# --------------------------------------------------------------
from src.vector_store import VectorStoreBuilder
from src.recommender import AnimeRecommender
from config.config import GROQ_API_KEY, MODEL_NAME
from utils.logger import get_logger
from utils.custom_exception import CustomException


# --------------------------------------------------------------
# Logger Setup
# --------------------------------------------------------------
logger = get_logger(__name__)


# --------------------------------------------------------------
# Anime Recommendation Pipeline
# --------------------------------------------------------------
class AnimeRecommendationPipeline:
    """
    High-level pipeline for generating anime recommendations.

    Parameters
    ----------
    persist_dir : str, optional
        Directory containing the persisted Chroma vector database.
        Defaults to "chroma_db".
    """

    def __init__(self, persist_dir: str = "chroma_db"):
        try:
            logger.info("🚀 Initialising Anime Recommendation Pipeline...")

            # Load the existing Chroma vector store
            vector_builder = VectorStoreBuilder(csv_path="", persist_dir=persist_dir)
            retriever = vector_builder.load_vector_store().as_retriever()

            # Create the recommender with the retriever and LLM
            self.recommender = AnimeRecommender(retriever, GROQ_API_KEY, MODEL_NAME)

            logger.info("✅ Pipeline initialised successfully.")
        except Exception as e:
            logger.error(f"❌ Failed to initialise pipeline: {str(e)}")
            raise CustomException("Error during pipeline initialisation", e)

    def recommend(self, query: str) -> str:
        """
        Generate anime recommendations for a given user query.

        Parameters
        ----------
        query : str
            The user’s query or description of anime preferences.

        Returns
        -------
        str
            The generated recommendation response.
        """
        try:
            logger.info(f"📝 Received query: {query}")

            # Generate recommendations via the LLM-powered recommender
            recommendation = self.recommender.get_recommendation(query)

            logger.info("✅ Recommendation generated successfully.")
            return recommendation
        except Exception as e:
            logger.error(f"❌ Failed to generate recommendation: {str(e)}")
            raise CustomException("Error while generating recommendation", e)
