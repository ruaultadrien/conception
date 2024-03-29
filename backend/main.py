"""Main module for the backend FastAPI application."""
import logging
import os

import chromadb
from chromadb.utils import embedding_functions
from fastapi import FastAPI
from pydantic import BaseModel
from src.constants import N_WORDS
from src.utils import get_english_words

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
    chroma_client = chromadb.HttpClient(host="chroma", port=8000)
    collection = chroma_client.get_collection("english_words")
    res = collection.query(query_texts=[word_request.word], n_results=5)
    documents = res["documents"]

    print("yooo", documents[0])

    return {"words": documents[0]}


@app.post("/fill_chroma")
def fill_chroma_with_all_english_words():
    """Fill Chroma with all English words and their embeddings."""
    english_words = get_english_words()
    english_words = english_words[:N_WORDS]

    embeddings_model = embedding_functions.HuggingFaceEmbeddingFunction(
        api_key=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
        model_name="sentence-transformers/all-MiniLM-l6-v2",
    )

    logging.info("Creating Chroma client...")
    chroma_client = chromadb.HttpClient(host=os.environ["CHROMA_HOST"], port=8000)

    logging.info("Creating collection...")
    collection = chroma_client.get_or_create_collection("english_words", embedding_function=embeddings_model)

    logging.info("Adding documents to collection...")
    collection.add(
        documents=english_words,
        ids=english_words,
    )
    return {"message": "Chroma filled"}
