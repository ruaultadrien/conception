"""Streamlit app declaration."""

import logging
import os


import requests
import streamlit as st

from src.utils import resolve_url_from_environment
from src.containers.query_most_similar_words import query_most_similar_words_container
from src.containers.vector_db import vector_db_container

# Set up logging
logging.basicConfig(level=logging.INFO)


def app() -> None:
    """Streamlit app."""
    st.title("Conception")
    st.header("Vector Database state")

    # health check on the vector database
    backend_url = resolve_url_from_environment(os.environ["BACKEND_HOST"])
    request_url = f"{backend_url}:8888/vector_db_health"
    logging.info(f"Checking the health of the vector database at {request_url}")
    res = requests.get(request_url)
    vector_db_is_up = res.json()["vector_db_is_up"]
    if vector_db_is_up:
        message = "Vector database is up."
        logging.info(message)
        st.write(message)
    else:
        message = "Vector database is down."
        logging.info(message)
        st.error(message)

    if vector_db_is_up:
        vector_db_container()
        query_most_similar_words_container()
