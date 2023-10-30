"""Streamlit app declaration."""
import os

import streamlit as st
import uuid
import logging
import numpy as np
from english_words import get_english_words_set
from langchain.embeddings import HuggingFaceInferenceAPIEmbeddings
from langchain.vectorstores.chroma import Chroma
from chromadb.utils import embedding_functions


import chromadb


def app() -> None:
    """Streamlit app."""
    st.title("Conception")

    # Input text with streamlit
    query_word = st.text_input("Enter a word to explore...")

    english_words = list(get_english_words_set(sources=["web2"]))
    english_words = english_words[:10000]

    embeddings_model = embedding_functions.HuggingFaceEmbeddingFunction(
        # api_key=inference_api_key,
        api_key=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
        model_name="sentence-transformers/all-MiniLM-l6-v2",
    )
    chroma_client = chromadb.HttpClient(host="chroma", port=8000)

    logging.info("Creating collection")
    collection = chroma_client.get_or_create_collection("english_words", embedding_function=embeddings_model)

    logging.info("Adding documents to collection")
    collection.add(
        documents=english_words,
        ids=[str(uuid.uuid4()) for _ in range(len(english_words))],
    )

    logging.info("Querying collection")
    res = collection.query(query_texts=[query_word], n_results=5)

    st.write(res)
