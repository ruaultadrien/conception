"""Streamlit app declaration."""
import os

import logging

import requests
import streamlit as st


def app() -> None:
    """Streamlit app."""
    st.title("Conception")

    # Input text with streamlit
    query_word = st.text_input("Enter a word to explore...")

    st.info("We only use a subset of the English dictionnary so far, results might not be of good quality.")

    fill_chroma()

    logging.info("Querying collection...")
    #res = requests.post("http://backend:8888/most_similar_words", json={"word": query_word}, timeout=60)
    res = requests.post(f"{os.environ['BACKEND_HOST']}:8888/most_similar_words", json={"word": query_word}, timeout=60)

    st.write(res.status_code)
    if res.status_code == 200:
        st.write(res.json())
    else:
        st.error("Could not query most similar words.")


@st.cache_data
def fill_chroma():
    """Fill Chroma with all English words and their embeddings."""
    logging.info("Filling Chroma...")
    requests.post(f"{os.environ['BACKEND_HOST']}:8888/fill_vector_db", timeout=3600)
