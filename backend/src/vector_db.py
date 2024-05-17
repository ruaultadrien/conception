"""Functions to interact with the vector database."""
import logging
import os

import chromadb
from english_words import get_english_words_set

from src.constants import N_WORDS, N_WORDS_PER_CHUNK
from src.vector_db_clients import ChromaClient

#from src.utils import get_vector_db_chroma_client





def post_data() -> None:
    """Post English words to the vector database."""
    english_words = get_english_words()

    english_words = filter_words_based_on_environment(english_words)

    logging.info("Creating Chroma client...")
    chroma_client = ChromaClient()

    n_iter = len(english_words) // N_WORDS_PER_CHUNK
    for i in range(n_iter):
        logging.info(f"Adding documents to collection ({i+1}/{n_iter})...")
        words_iter = english_words[i * N_WORDS_PER_CHUNK : (i + 1) * N_WORDS_PER_CHUNK]
        chroma_client.add_words(words_iter)
    # Add the remaining words
    remaining_words = english_words[n_iter * N_WORDS_PER_CHUNK :]
    if len(remaining_words) > 0:
        logging.info(f"Adding remaining documents to collection...")
        chroma_client.add_words(remaining_words)


def filter_words_based_on_environment(english_words) -> int:
    """Filter words based on the environment. All words id in RENDER mode. Only N_WORDS words otherwise."""
    if os.environ.get("RENDER", False):
        return english_words
    else:
        return english_words[:N_WORDS]


def get_english_words() -> list:
    """Get all English words."""
    english_words = list(get_english_words_set(sources=["web2"]))
    assert len(set(english_words)) == len(english_words), "English words are unique."
    return english_words


def add_words_to_collection(collection: chromadb.Collection, words_iter: list[str]):
    """Add words to the collection."""
    collection.add(
        documents=words_iter,
        ids=words_iter,
    )
