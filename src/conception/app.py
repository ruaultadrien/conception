"""Streamlit app declaration."""
import os

import streamlit as st
from english_words import get_english_words_set
from langchain.embeddings import HuggingFaceInferenceAPIEmbeddings
from langchain.vectorstores.chroma import Chroma


def app() -> None:
    """Streamlit app."""
    st.title("Conception")

    # Input text with streamlit
    query_word = st.text_input("Enter a word to explore...")

    english_words = list(get_english_words_set(sources=["web2"]))
    english_words = english_words[:10000]

    embeddings_model = HuggingFaceInferenceAPIEmbeddings(
        # api_key=inference_api_key,
        api_key=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
        model_name="sentence-transformers/all-MiniLM-l6-v2",
    )
    db = Chroma.from_texts(english_words, embeddings_model)

    res = db.similarity_search(query_word, k=5)

    most_similar_words = [r.page_content for r in res]
    st.write(most_similar_words)
