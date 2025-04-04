import requests
import os

API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")
API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}
payload = {
    "inputs": "Tell me a joke",
    "parameters": {
        "max_length": 100,
        "min_length": 10,
        "num_return_sequences": 1
    }
}

try:
    response = requests.post(API_URL, headers=headers, json=payload)
    response.raise_for_status()
    result = response.json()
    print("API Response:", result)
except requests.exceptions.RequestException as e:
    print("Error:", e)