"""Streamlit app declaration."""

import os

import logging

import requests
import streamlit as st


def app() -> None:
    """Streamlit app."""
    st.title("Conception")
    st.header("Vector Database state")
    
    # health check on the vector database
    res = requests.get(f"http://{os.environ['BACKEND_HOST']}:8888/vector_db_health")
    st.metric("Vector database health code", res.json()["vector_db_status"])
        
    
    # Retrive the number of documents in the collection
    res = requests.get(f"http://{os.environ['BACKEND_HOST']}:8888/vector_db")
    if res.status_code == 200:
        st.metric("Number of documents in the collection:", len(res.json()["documents"]["ids"]))
    else:
        st.error("Could not query vector database.")

    if st.button("POST vector database"):
        requests.post(f"http://{os.environ['BACKEND_HOST']}:8888/vector_db", timeout=120)

    # Query space
    st.write("---")
    st.header("Query most similar words")
    # Input text with streamlit
    query_word = st.text_input("Enter a word to explore...")

    st.info("We only use a subset of the English dictionnary so far, results might not be of good quality.")

    logging.info("Querying collection...")
    res = requests.post(
        f"http://{os.environ['BACKEND_HOST']}:8888/most_similar_words", json={"word": query_word}, timeout=120
    )

    st.write(res.status_code)
    if res.status_code == 200:
        st.write(res.json())
    else:
        st.error("Could not query most similar words.")

