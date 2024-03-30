"""Streamlit app declaration."""

import os


import requests
import streamlit as st

from src.utils import resolve_url_from_environment
from src.containers.query_most_similar_words import query_most_similar_words_container
from src.containers.vector_db import vector_db_container


def app() -> None:
    """Streamlit app."""
    st.title("Conception")
    st.header("Vector Database state")

    # health check on the vector database
    backend_url = resolve_url_from_environment(os.environ["BACKEND_HOST"])
    res = requests.get(f"{backend_url}:8888/vector_db_health")
    vector_db_is_up = res.json()["vector_db_is_up"]
    if vector_db_is_up:
        st.write("Vector database is up.")
    else:
        st.error("Vector database is sick.")

    if vector_db_is_up:
        vector_db_container()
        query_most_similar_words_container()
