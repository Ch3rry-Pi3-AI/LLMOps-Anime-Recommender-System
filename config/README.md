# `config/` README — Environment & Model Configuration

This folder contains configuration files for the **LLMOps Anime Recommender System**.
It handles environment setup and defines global constants used across the project.

## 📁 Folder Overview

```text
config/
└─ config.py   # Loads environment variables and defines model settings
```

## ⚙️ Description

* `config.py` loads the `.env` file, retrieves API keys, and sets the model name.
* Centralises key configuration values for consistency across modules.