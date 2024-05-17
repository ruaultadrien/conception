"""Defines the VectorDBClient interface and ChromaClient implementation."""
import abc
import logging
import os

import chromadb
import chromadb.api
import chromadb.config
from chromadb.utils import embedding_functions

from src.constants import COLLECTION_NAME


class VectorDBClient(abc.ABC):
    """Interface for a vector database client."""
    
    @abc.abstractmethod
    def add_words(self, words: list[str]) -> None:
        """Add words to the vector database."""
        pass

    @abc.abstractmethod
    def get_most_similar_words(self, word: str) -> list[str]:
        """Get the most similar words to a given word."""
        pass

class ChromaClient(VectorDBClient):
    """Chroma client for the vector database. Implements the VectorDBClient interface."""
    def __init__(self):
        """Initialize the Chroma client."""
        self.chroma_client = self._get_vector_db_chroma_client()
        
        embeddings_model = embedding_functions.HuggingFaceEmbeddingFunction(
        api_key=os.environ["HUGGINGFACEHUB_API_TOKEN"],
        model_name="sentence-transformers/all-MiniLM-l6-v2",
    )
        self.collection = self.chroma_client.get_or_create_collection(COLLECTION_NAME, embedding_function=embeddings_model)

    def add_words(self, words: list[str]) -> None:
        """Add words to the vector database."""
        self.collection.add(documents=words, ids=words)

    def get_most_similar_words(self, word: str) -> list[str]:
        """Get the most similar words to a given word."""
        result = self.collection.query(query_texts=[word], n_results=5)["documents"]
        most_similar_words = result[0]
        return most_similar_words

    def _get_vector_db_chroma_client(self) -> chromadb.api.ClientAPI:
        """Get a Chroma client for the vector database."""
        use_ssl = os.environ.get("RENDER", False)
        logging.info(f"Chroma host used for Chroma client creation: {os.environ['CHROMA_HOST']}")
        chroma_port = self._resolve_chroma_port_from_environment()
        return chromadb.HttpClient(
            host=os.environ["CHROMA_HOST"],
            port=chroma_port,
            settings=chromadb.config.Settings(anonymized_telemetry=False),
            ssl=use_ssl,
        )
    
    @classmethod
    def _resolve_chroma_port_from_environment(cls):
        """Resolve the Chroma port based on the environment."""
        if os.environ.get("RENDER", False):
            return 443
        else:
            return os.environ["CHROMA_PORT"]