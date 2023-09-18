import streamlit as st
from src.conception.constants import MODEL_ID
from sentence_transformers.util import semantic_search

from src.conception.utils import get_embeddings, query_hugging_face

def app():
    st.title("Conception")

    # Input text with streamlit
    query = st.text_input("Enter a word to explore...")

    # get english words
    english_embeddings = get_embeddings()

    query_embedding = query_hugging_face([query], MODEL_ID)

    hits = semantic_search(query_embedding, english_embeddings, top_k=5)
    st.write(hits)


    # Still need to compute the cosine similarity
    # between the query embedding and the embeddings
    # using the hugging face semantic function