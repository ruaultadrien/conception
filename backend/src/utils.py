"""Utility functions for backend."""
import chromadb
import os
from english_words import get_english_words_set


def get_english_words() -> list:
    """Get all English words."""
    english_words = list(get_english_words_set(sources=["web2"]))
    assert len(set(english_words)) == len(english_words), "English words are unique."
    return english_words

def get_vector_db_chroma_client() -> chromadb.HttpClient:
    """Get a Chroma client for the vector database."""
    return chromadb.HttpClient(host=os.environ["CHROMA_HOST"], port=8000)