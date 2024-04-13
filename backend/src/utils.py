"""Utility functions for backend."""

import logging
import chromadb
import chromadb.api
import chromadb.config
import os
from english_words import get_english_words_set


def get_english_words() -> list:
    """Get all English words."""
    english_words = list(get_english_words_set(sources=["web2"]))
    assert len(set(english_words)) == len(english_words), "English words are unique."
    return english_words


def get_vector_db_chroma_client() -> chromadb.api.ClientAPI:
    """Get a Chroma client for the vector database."""
    use_ssl = os.environ.get("RENDER", False)
    logging.info(f"Chroma host used for Chroma client creation: {os.environ['CHROMA_HOST']}")
    chroma_port = resolve_chroma_port_from_environment()
    return chromadb.HttpClient(
        host=os.environ["CHROMA_HOST"], port=chroma_port, settings=chromadb.config.Settings(anonymized_telemetry=False), ssl=use_ssl
    )

def resolve_http_or_https_from_environment(host):
    if os.environ.get("RENDER", False):
        return f"https://{host}"
    else:
        return f"http://{host}"

def resolve_chroma_port_from_environment():
    if os.environ.get("RENDER", False):
        return 443
    else:
        return os.environ["CHROMA_PORT"]