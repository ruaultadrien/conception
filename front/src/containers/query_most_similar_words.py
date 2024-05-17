"""Streamlit container to query most similar words."""

import logging

import requests
import streamlit as st


def query_most_similar_words_container(backend_url: str, backend_port: str):
    """Streamlit container to query most similar words."""
    # Query space
    st.write("---")
    st.header("Query most similar words")
    # Input text with streamlit
    query_word = st.text_input("Enter a word to explore...")

    st.info("We only use a subset of the English dictionnary so far, results might not be of good quality.")

    logging.info("Querying collection...")
    res = requests.post(f"{backend_url}:{backend_port}/most_similar_words", json={"word": query_word}, timeout=120)

    st.write(res.status_code)
    if res.status_code == 200:  # noqa: PLR2004
        st.write(res.json())
    else:
        st.error("Could not query most similar words.")
