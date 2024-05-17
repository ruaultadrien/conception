"""Main module for the backend FastAPI application."""

import logging
import os
from http.client import HTTPException

import requests
from fastapi import BackgroundTasks, FastAPI
from pydantic import BaseModel

from src import vector_db
from src.constants import COLLECTION_NAME
from src.utils import (
    resolve_http_or_https_from_environment,
)
from src.vector_db_clients import ChromaClient

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
    chroma_client = ChromaClient()
    most_similar_words = chroma_client.get_most_similar_words(word_request.word)

    return {"words": most_similar_words}


@app.post("/vector_db")
def post_vector_db(background_tasks: BackgroundTasks):
    """Fill Chroma with all English words and their embeddings."""
    background_tasks.add_task(vector_db.post_data)
    return {"message": "Chroma DB filling in the background."}


@app.get("/vector_db")
def get_vector_db():
    """Get the collection's documents."""
    logging.info("Creating Chroma client...")
    vector_db_is_up = get_vector_db_health()["vector_db_is_up"]

    if not vector_db_is_up:
        raise HTTPException(status_code=500, detail="Vector database is down.")

    chroma_client = ChromaClient()
    try:
        collection = chroma_client.chroma_client.get_collection(COLLECTION_NAME)
    except ValueError:
        raise HTTPException(
            status_code=500, detail=f"Collection {COLLECTION_NAME} not found. Call POST /vector_db to create it."
        )
    return {"documents": collection.get()}


@app.get("/vector_db_health")
def get_vector_db_health():
    """Check the health of the vector database."""
    chroma_url = resolve_http_or_https_from_environment(os.environ["CHROMA_HOST"])
    chroma_port = ChromaClient._resolve_chroma_port_from_environment()
    request_url = f"{chroma_url}:{chroma_port}/api/v1/heartbeat"
    logging.info(f"Checking the health of the vector database at {request_url}")
    res = requests.get(request_url, timeout=5)
    vector_db_is_up = res.status_code == 200  # noqa: PLR2004
    return {"vector_db_is_up": vector_db_is_up}
