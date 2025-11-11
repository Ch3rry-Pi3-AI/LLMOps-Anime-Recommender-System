"""
recommender.py

Defines the AnimeRecommender class, which connects the retriever and Groq LLM
using LCEL (LangChain Expression Language) runnables.
This version avoids all legacy `langchain.chains` imports.
"""

from typing import Any, Iterable
from langchain_groq import ChatGroq
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from src.prompt_template import get_anime_prompt


def _format_docs(docs: Iterable[Any]) -> str:
    """
    Combine retrieved documents into a single formatted context string.

    Parameters
    ----------
    docs : Iterable[Any]
        List or iterable of LangChain Document objects or plain strings.

    Returns
    -------
    str
        Concatenated text representing document content.
    """
    parts = []
    for doc in docs:
        parts.append(getattr(doc, "page_content", str(doc)))
        if len(parts) >= 8:  # limit context to keep prompt concise
            break
    return "\n\n".join(parts)


class AnimeRecommender:
    """
    Anime recommender pipeline built with LCEL runnables.

    Parameters
    ----------
    retriever : Any
        Retriever instance (e.g., Chroma retriever) supporting `.invoke(question)`.
    api_key : str
        Groq API key.
    model_name : str
        Groq model name (e.g., "llama-3.1-8b-instant").
    """

    def __init__(self, retriever: Any, api_key: str, model_name: str):
        self.retriever = retriever
        self.llm = ChatGroq(api_key=api_key, model=model_name, temperature=0)
        self.prompt = get_anime_prompt()  # expects {context} and {question}

        # Build LCEL chain: question → retriever → context → prompt → LLM → text
        self.chain = (
            {
                "question": RunnablePassthrough(),
                "context": RunnablePassthrough()
                | self.retriever
                | RunnableLambda(_format_docs),
            }
            | self.prompt
            | self.llm
            | StrOutputParser()
        )

    def get_recommendation(self, query: str) -> str:
        """
        Generate an anime recommendation response for a given query.

        Parameters
        ----------
        query : str
            The user’s input describing their preferences.

        Returns
        -------
        str
            The LLM-generated recommendation text.
        """
        return self.chain.invoke(query)
