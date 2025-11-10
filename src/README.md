# `src/` README — Core Source Code

This folder contains the **main source code** for the **LLMOps Anime Recommender System**.
It includes data loading, preprocessing, and other core logic modules that power the system’s backend workflows.

## 📁 Folder Overview

```text
src/
└── data_loader.py   # Loads and preprocesses the anime dataset
```

## ⚙️ Description

* `data_loader.py` reads the raw anime dataset, validates required columns, and combines text fields (title, synopsis, and genres) into a single feature for later embedding and recommendation tasks.

As the project develops, this folder will expand to include modules for **data processing**, **embedding generation**, and **model integration**.
