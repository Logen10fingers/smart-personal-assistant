import random
import nltk
import datetime
from flask import Flask, request, jsonify
from nltk.tokenize import word_tokenize
from dotenv import load_dotenv
import os
import requests
import time

load_dotenv()
HUGGINGFACE_API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")
print(f"Hugging Face API Token: {HUGGINGFACE_API_TOKEN}")

app = Flask(__name__)

chat_history = {}

def log_message(user_id, user_input, response):
    with open("chat_log.txt", "a") as log_file:
        log_file.write(f"{datetime.datetime.now()} | User {user_id}: {user_input} | Assistant: {response}\n")

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get('message')
    user_id = data.get('user_id', 'default_user')

    if user_id not in chat_history:
        chat_history[user_id] = []

    response = generate_response(user_input, chat_history[user_id])
    
    chat_history[user_id].append({"input": user_input, "response": response, "timestamp": str(datetime.datetime.now())})
    if len(chat_history[user_id]) > 5:
        chat_history[user_id].pop(0)
    
    log_message(user_id, user_input, response)
    
    return jsonify({'response': response})

def generate_response(user_input, history):
    user_input_lower = user_input.lower()
    tokens = word_tokenize(user_input_lower)

    greetings = ["hello", "hi", "hey"]
    farewell = ["bye", "goodbye", "see you"]
    thanks = ["thank you", "thanks"]

    for past_msg in history:
        if "tired" in past_msg["input"].lower():
            if "what should i do" in user_input_lower:
                return "You mentioned being tired earlier—how about a quick break?"

    if any(word in tokens for word in greetings):
        return random.choice(["Hello!", "Hi there!", "Hey! How can I help?"])
    elif any(word in tokens for word in farewell):
        return random.choice(["Goodbye!", "See you later!", "Take care!"])
    elif any(word in tokens for word in thanks):
        return random.choice(["You're welcome!", "No problem!", "Glad to help!"])
    else:
        API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
        headers = {
            "Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"
        }
        payload = {
            "inputs": user_input,
            "parameters": {
                "max_length": 50,
                "num_return_sequences": 1
            }
        }

        for attempt in range(3):
            try:
                response = requests.post(API_URL, headers=headers, json=payload)
                response.raise_for_status()
                result = response.json()
                print(f"Hugging Face API Response: {result}")
                if isinstance(result, list) and len(result) > 0 and "generated_text" in result[0]:
                    generated_text = result[0]["generated_text"].strip()
                    # Check if the response is just the input repeated (ignoring case and minor formatting)
                    if generated_text.lower().replace("’", "'").replace(" ", "") == user_input_lower.replace("’", "'").replace(" ", ""):
                        print("API response is the same as the input.")
                        return "I'm not sure how to respond to that yet."
                    return generated_text
                else:
                    print("Hugging Face API returned an unexpected response format.")
                    return "I'm not sure how to respond to that yet."
            except requests.exceptions.RequestException as e:
                print(f"Error calling Hugging Face API (attempt {attempt + 1}/3): {e}")
                if attempt < 2:
                    time.sleep(2)
                continue
        return "I'm sorry, I couldn't generate a response right now."

if __name__ == '__main__':
    nltk.download('punkt')
    app.run(debug=True)