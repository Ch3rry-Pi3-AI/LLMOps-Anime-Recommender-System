# --------------------------------------------------------------
# 🐍 Dockerfile — LLMOps Anime Recommender App
# --------------------------------------------------------------

# Base image: match your pyproject requires-python (>=3.12)
FROM python:3.12-slim AS base

# Environment
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Working dir
WORKDIR /app

# System deps (wheel building, etc.)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
 && rm -rf /var/lib/apt/lists/*

# Upgrade pip tooling first (often avoids build issues)
RUN python -m pip install --upgrade pip setuptools wheel

# Copy project
COPY . .

# Install your package (editable)
RUN pip install --no-cache-dir -e .

# Expose Streamlit
EXPOSE 8501

# Entrypoint
CMD ["streamlit", "run", "app/app.py", \
     "--server.port=8501", \
     "--server.address=0.0.0.0", \
     "--server.headless=true"]
