import requests
import streamlit as st

import logging


def vector_db_container(backend_url:str, backend_port:str):
    st.header("Vector Database state")

    # health check on the vector database

    request_url = f"{backend_url}:{backend_port}/vector_db_health"
    logging.info(f"Checking the health of the vector database at {request_url}")
    res = requests.get(request_url)
    vector_db_is_up = res.json()["vector_db_is_up"]
    if vector_db_is_up:
        message = "Vector database is up."
        logging.info(message)
        st.info(message)
    else:
        message = "Vector database is down."
        logging.info(message)
        st.error(message)


    if vector_db_is_up:
        # Retrieve the number of documents in the collection
        request_url = f"{backend_url}:{backend_port}/vector_db"
        logging.info(f"Get documents with this url: {request_url}")
        res = requests.get(request_url)
        if res.status_code == 200:
            st.metric("Number of documents in the collection:", len(res.json()["documents"]["ids"]))
        else:
            st.error("Could not query vector database.")

        if st.button("POST vector database"):
            requests.post(request_url, timeout=120)
    
    return vector_db_is_up
