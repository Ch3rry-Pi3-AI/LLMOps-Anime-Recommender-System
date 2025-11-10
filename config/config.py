"""
config.py

Load environment variables and define model configuration
for the LLMOps Anime Recommender System.
"""

# --------------------------------------------------------------
# Imports and environment setup
# --------------------------------------------------------------
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Retrieve the Groq API key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Define the LLM model name
MODEL_NAME = "llama-3.1-8b-instant"
