"""Streamlit app declaration."""
import logging

import requests
import streamlit as st


def app() -> None:
    """Streamlit app."""
    st.title("Conception")

    # Input text with streamlit
    query_word = st.text_input("Enter a word to explore...")

    fill_chroma()

    logging.info("Querying collection...")
    res = requests.post("http://backend:8888/most_similar_words", json={"word": query_word}, timeout=60)

    st.write(res.json())


@st.cache_data
def fill_chroma():
    """Fill Chroma with all English words and their embeddings."""
    logging.info("Filling Chroma...")
    requests.post("http://backend:8888/fill_chroma", timeout=3600)
