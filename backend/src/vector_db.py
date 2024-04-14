"""Functions to interact with the vector database."""
import logging
import os

import chromadb
from chromadb.utils import embedding_functions
from english_words import get_english_words_set

from src.constants import N_WORDS, N_WORDS_PER_CHUNK
from src.utils import get_vector_db_chroma_client


def post_data() -> None:
    """Post English words to the vector database."""
    english_words = get_english_words()

    english_words = filter_words_based_on_environment(english_words)

    embeddings_model = embedding_functions.HuggingFaceEmbeddingFunction(
        api_key=os.environ["HUGGINGFACEHUB_API_TOKEN"],
        model_name="sentence-transformers/all-MiniLM-l6-v2",
    )

    logging.info("Creating Chroma client...")
    chroma_client = get_vector_db_chroma_client()

    logging.info("Creating collection...")
    collection = chroma_client.get_or_create_collection("english_words", embedding_function=embeddings_model)

    n_iter = len(english_words) // N_WORDS_PER_CHUNK
    for i in range(n_iter):
        logging.info(f"Adding documents to collection ({i+1}/{n_iter})...")
        words_iter = english_words[i * N_WORDS_PER_CHUNK : (i + 1) * N_WORDS_PER_CHUNK]
        add_words_to_collection(collection, words_iter)
    # Add the remaining words
    logging.info(f"Adding remaining documents to collection...")
    remaining_words = english_words[n_iter * N_WORDS_PER_CHUNK :]
    add_words_to_collection(collection, remaining_words)

    logging.info("Adding documents to collection...")
    collection.add(
        documents=english_words,
        ids=english_words,
    )


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
