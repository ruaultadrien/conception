"""Entrypoint of the application."""

import streamlit as st

from constants import MODEL_ID
from english_words import get_english_words_set
import logging

from utils import query_hugging_face

logging.getLogger().setLevel(logging.INFO)


def main():
    st.title("Conception")
    
    # Input text with streamlit
    query = st.text_input("Enter a word to explore...")

    # get english words
    embeddings = get_embeddings()

    query_embedding = query_hugging_face([query], MODEL_ID)

    # Still need to compute the cosine similarity
    # between the query embedding and the embeddings
    # using the hugging face semantic function
    

@st.cache
def get_embeddings():
    english_words = get_english_words_set(sources=['web2'])
    embeddings = query_hugging_face(list(english_words), MODEL_ID)
    return embeddings



if __name__ == "__main__":
    main()