"""
recommender.py

Defines the AnimeRecommender class, which connects the vector
retriever and LLM to generate context-aware anime recommendations.
"""

# --------------------------------------------------------------
# Imports
# --------------------------------------------------------------
from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq
from src.prompt_template import get_anime_prompt


class AnimeRecommender:
    """
    A recommendation engine that uses a retriever and a Groq LLM
    to provide personalised anime recommendations.

    Parameters
    ----------
    retriever : BaseRetriever
        The retriever instance (e.g., Chroma retriever) that provides
        context from the vector database.
    api_key : str
        The Groq API key used for authentication.
    model_name : str
        The name of the Groq model to be used for inference.
    """

    def __init__(self, retriever, api_key: str, model_name: str):
        # Initialise the Groq LLM with zero temperature for factual, stable outputs
        self.llm = ChatGroq(api_key=api_key, model=model_name, temperature=0)

        # Load the prompt template for structured recommendations
        self.prompt = get_anime_prompt()

        # Set up the RetrievalQA chain that combines the retriever and LLM
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=retriever,
            return_source_documents=True,
            chain_type_kwargs={"prompt": self.prompt}
        )

    def get_recommendation(self, query: str) -> str:
        """
        Generate anime recommendations based on a user query.

        Parameters
        ----------
        query : str
            The user's input query describing their anime preferences.

        Returns
        -------
        str
            The model-generated recommendation response.
        """
        # Run the RetrievalQA chain with the user's query
        result = self.qa_chain({"query": query})

        # Return only the text output (recommendation response)
        return result["result"]
