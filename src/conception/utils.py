import requests
import os

def query_hugging_face(texts: list[str], model_id:str):
    api_url, headers = get_api_urls_and_headers(model_id)
    response = requests.post(api_url, headers=headers, json={"inputs": texts, "options":{"wait_for_model":True}})
    return response.json()

def get_api_urls_and_headers(model_id)-> tuple[str, dict]:
    api_url = f"https://api-inference.huggingface.co/pipeline/feature-extraction/{model_id}"
    headers = {"Authorization": f"Bearer {os.environ['HF_TOKEN']}"}
    return api_url, headers