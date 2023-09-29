"""Utils for conception package."""
import streamlit as st
import os

import requests
from english_words import get_english_words_set
from src.conception.constants import MODEL_ID


def query_hugging_face(texts: list[str], model_id: str) -> dict:
    """Query Hugging Face API for feature extraction."""
    api_url, headers = get_api_urls_and_headers(model_id)
    response = requests.post(api_url, headers=headers, json={"inputs": texts, "options": {"wait_for_model": True}})
    return response.json()


def get_api_urls_and_headers(model_id) -> tuple[str, dict]:
    """Get API URL and headers for Hugging Face API."""
    api_url = f"https://api-inference.huggingface.co/pipeline/feature-extraction/{model_id}"
    headers = {"Authorization": f"Bearer {os.environ['HF_TOKEN']}"}
    return api_url, headers

@st.cache_data
def get_embeddings():
    english_words = get_english_words_set(sources=["web2"])
    embeddings = query_hugging_face(list(english_words), MODEL_ID)
    return embeddings