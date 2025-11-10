"""
data_loader.py

Module for loading and preprocessing the anime dataset
for the LLMOps Anime Recommender System.
"""

import pandas as pd


class AnimeDataLoader:
    """
    Load and process the anime dataset into a usable format.

    Parameters
    ----------
    original_csv : str
        Path to the original CSV file containing the raw anime data.
    processed_csv : str
        Path where the processed CSV file will be saved.
    """

    def __init__(self, original_csv: str, processed_csv: str):
        # Store file paths for input and output CSVs
        self.original_csv = original_csv
        self.processed_csv = processed_csv

    def load_and_process(self):
        """
        Read the original dataset, validate required columns,
        combine relevant text fields, and export a processed CSV.

        Returns
        -------
        str
            Path to the processed CSV file.
        """
        # Load the CSV, skip problematic lines, and drop missing rows
        df = pd.read_csv(self.original_csv, encoding="utf-8", on_bad_lines="skip").dropna()

        # Define required columns and check for any missing ones
        required_cols = {"Name", "Genres", "sypnopsis"}
        missing = required_cols - set(df.columns)
        if missing:
            raise ValueError("Missing column(s) in CSV file")

        # Combine title, synopsis, and genres into a single text field
        df["combined_info"] = (
            "Title: " + df["Name"] + " Overview: " + df["sypnopsis"] + " Genres: " + df["Genres"]
        )

        # Save the processed data with only the combined text field
        df[["combined_info"]].to_csv(self.processed_csv, index=False, encoding="utf-8")

        # Return the output path for downstream use
        return self.processed_csv
