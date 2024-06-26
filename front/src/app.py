"""Streamlit app declaration."""

import logging
import os

import streamlit as st

from src.containers.query_most_similar_words import query_most_similar_words_container
from src.utils import resolve_backend_port_from_environment, resolve_url_from_environment

# Set up logging
logging.basicConfig(level=logging.INFO)


def app() -> None:
    """Streamlit app."""
    backend_url = resolve_url_from_environment(os.environ["BACKEND_HOST"])
    backend_port = resolve_backend_port_from_environment()

    st.title("Conception")

    query_most_similar_words_container(backend_url, backend_port)
