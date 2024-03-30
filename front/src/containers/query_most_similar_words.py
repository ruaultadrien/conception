import streamlit as st
import logging
import requests
import os


def query_most_similar_words_container():
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
