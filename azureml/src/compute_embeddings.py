"""Script that computes word embeddings for all English Words and pushes the results to an Azure Datastore as a Data Asset.

The script uses nltk to download the English words and then compute the embeddings using langchain and HugginFace models. The embeddings are then pushed to an Azure Datastore as a Data Asset.
"""

import pathlib

import nltk
import pandas as pd
import typer

nltk.download("words")
import logging

from nltk.corpus import words
from sentence_transformers import SentenceTransformer
from typing_extensions import Annotated

# Set up logging
logging.basicConfig(level=logging.INFO)


def main(output_folder: Annotated[pathlib.Path, typer.Option()]):
    """Main script for computing word embeddings."""
    # Retrieve English words with nltk
    logging.info("Retrieving English words with nltk.")
    english_words = words.words()

    # Load a pre-trained HuggingFace model for embeddings
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    embeddings_model = SentenceTransformer(model_name)

    # Compute word embeddings
    logging.info("Computing word embeddings.")
    embeddings = list(embeddings_model.encode(english_words))
    df = pd.DataFrame.from_dict({"word": english_words, "embedding": embeddings})

    # Save embeddings
    logging.info(f"Saving word embeddings to {output_folder}.")
    output_folder.mkdir(parents=True, exist_ok=True)
    df.to_parquet(output_folder / "word_embeddings.parquet", index=False)


if __name__ == "__main__":
    typer.run(main)
