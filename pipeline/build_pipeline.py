"""
build_pipeline.py

End-to-end build script for the LLMOps Anime Recommender System.
Loads the dataset, processes it, and builds the Chroma vector store.
"""

# --------------------------------------------------------------
# Imports
# --------------------------------------------------------------
from src.data_loader import AnimeDataLoader
from src.vector_store import VectorStoreBuilder
from dotenv import load_dotenv
from utils.logger import get_logger
from utils.custom_exception import CustomException


# --------------------------------------------------------------
# Environment and Logger Setup
# --------------------------------------------------------------
load_dotenv()
logger = get_logger(__name__)


# --------------------------------------------------------------
# Main Pipeline Function
# --------------------------------------------------------------
def main():
    """
    Executes the full data processing and vector store build pipeline.
    """
    try:
        logger.info("🚀 Starting pipeline build...")

        # Step 1 — Load and process the anime dataset
        loader = AnimeDataLoader("data/anime_with_synopsis.csv", "data/processed_anime.csv")
        processed_csv = loader.load_and_process()
        logger.info("✅ Data successfully loaded and processed.")

        # Step 2 — Build and persist the Chroma vector store
        vector_builder = VectorStoreBuilder(processed_csv)
        vector_builder.build_and_save_vectorstore()
        logger.info("✅ Vector store built and persisted successfully.")

        logger.info("🎯 Pipeline build completed successfully.")
    except Exception as e:
        logger.error(f"❌ Pipeline execution failed: {str(e)}")
        raise CustomException("Error during pipeline execution", e)


# --------------------------------------------------------------
# Entry Point
# --------------------------------------------------------------
if __name__ == "__main__":
    main()
