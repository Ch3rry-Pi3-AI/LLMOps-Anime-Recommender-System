"""
vector_store.py

Module for building and loading the Chroma vector store
used in the LLMOps Anime Recommender System.
"""

# --------------------------------------------------------------
# Imports
# --------------------------------------------------------------
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class VectorStoreBuilder:
    """
    Handles creation and loading of a Chroma vector store
    using Hugging Face sentence embeddings.

    Parameters
    ----------
    csv_path : str
        Path to the processed CSV file containing text data.
    persist_dir : str, optional
        Directory where the Chroma database will be stored,
        by default 'chroma_db'.
    """

    def __init__(self, csv_path: str, persist_dir: str = "chroma_db"):
        # Store dataset and persistence paths
        self.csv_path = csv_path
        self.persist_dir = persist_dir

        # Initialise Hugging Face embeddings model
        self.embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    def build_and_save_vectorstore(self):
        """
        Build the Chroma vector store from the processed CSV file
        and persist it locally for reuse.
        """
        # Load data from the CSV file
        loader = CSVLoader(
            file_path=self.csv_path,
            encoding="utf-8",
            metadata_columns=[]
        )
        data = loader.load()

        # Split text into smaller chunks for better embedding performance
        splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        texts = splitter.split_documents(data)

        # Create and persist the Chroma vector store
        db = Chroma.from_documents(texts, self.embedding, persist_directory=self.persist_dir)

    def load_vector_store(self):
        """
        Load the existing Chroma vector store from the persistence directory.

        Returns
        -------
        Chroma
            A Chroma vector store instance ready for querying.
        """
        return Chroma(persist_directory=self.persist_dir, embedding_function=self.embedding)
