"""Main module for the backend FastAPI application."""

import logging
import os

import chromadb
from chromadb.utils import embedding_functions
from fastapi import FastAPI
from pydantic import BaseModel
import requests
from src.constants import COLLECTION_NAME, N_WORDS
from src.utils import get_english_words, get_vector_db_chroma_client

logging.getLogger().setLevel(logging.INFO)

app = FastAPI()


class WordRequest(BaseModel):
    """Request model for a word."""

    word: str


class WordsResponse(BaseModel):
    """Response model for a list of words."""

    words: list[str]


@app.post("/most_similar_words", response_model=WordsResponse)
def get_most_similar_words(word_request: WordRequest):
    """Get the most similar words to a given word."""
    logging.info("Creating Chroma client...")
    chroma_client = chromadb.HttpClient(host=os.environ["CHROMA_HOST"], port=8000)
    collection = chroma_client.get_collection(COLLECTION_NAME)
    res = collection.query(query_texts=[word_request.word], n_results=5)
    documents = res["documents"]

    print("yooo", documents[0])

    return {"words": documents[0]}


@app.post("/vector_db")
def post_vector_db():
    """Fill Chroma with all English words and their embeddings."""
    english_words = get_english_words()
    english_words = english_words[:N_WORDS]

    embeddings_model = embedding_functions.HuggingFaceEmbeddingFunction(
        api_key=os.environ["HUGGINGFACEHUB_API_TOKEN"],
        model_name="sentence-transformers/all-MiniLM-l6-v2",
    )

    logging.info("Creating Chroma client...")
    chroma_client = get_vector_db_chroma_client()

    logging.info("Creating collection...")
    collection = chroma_client.get_or_create_collection("english_words", embedding_function=embeddings_model)

    logging.info("Adding documents to collection...")
    collection.add(
        documents=english_words,
        ids=english_words,
    )
    return {"message": "Chroma filled"}


@app.get("/vector_db")
def get_vector_db():
    """Get the collection's documents."""
    logging.info("Creating Chroma client...")
    chroma_client = get_vector_db_chroma_client()
    collection = chroma_client.get_collection("english_words")
    return {"documents": collection.get()}


@app.get("/vector_db_health")
def get_vector_db_health():
    """Check the health of the vector database."""
    return {"vector_db_status": requests.get(f"http://{os.environ['CHROMA_HOST']}:8000/api/v1/heartbeat").status_code}
