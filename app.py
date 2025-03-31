import random
import nltk
import datetime
from flask import Flask, request, jsonify
from nltk.tokenize import word_tokenize

app = Flask(__name__)

# In-memory chat history (user_id -> list of message dicts)
chat_history = {}

def log_message(user_id, user_input, response):
    """Logs chat history to a file"""
    with open("chat_log.txt", "a") as log_file:
        log_file.write(f"{datetime.datetime.now()} | User {user_id}: {user_input} | Assistant: {response}\n")

@app.route('/chat', methods=['POST'])
def chat():
    print("Received a request to /chat")  # Debug: Confirm request received
    data = request.json
    print(f"Request data: {data}")  # Debug: See the incoming data
    user_input = data.get('message')
    user_id = data.get('user_id', 'default_user')
    print(f"User input: {user_input}, User ID: {user_id}")  # Debug: Confirm parsing

    # Initialize history for this user if not present
    if user_id not in chat_history:
        chat_history[user_id] = []

    response = generate_response(user_input, chat_history[user_id])
    
    # Store the interaction in history (limit to last 5 for simplicity)
    chat_history[user_id].append({"input": user_input, "response": response, "timestamp": str(datetime.datetime.now())})
    if len(chat_history[user_id]) > 5:
        chat_history[user_id].pop(0)  # Keep only the last 5
    print(f"Chat history for {user_id}: {chat_history[user_id]}")  # Debug: Show history
    
    log_message(user_id, user_input, response)
    
    return jsonify({'response': response})

def generate_response(user_input, history):
    user_input = user_input.lower()
    tokens = word_tokenize(user_input)

    greetings = ["hello", "hi", "hey"]
    farewell = ["bye", "goodbye", "see you"]
    thanks = ["thank you", "thanks"]

    # Check history for context (example: if user mentioned "tired" before)
    for past_msg in history:
        if "tired" in past_msg["input"].lower():
            if "what should i do" in user_input:
                return "You mentioned being tired earlier—how about a quick break?"

    # Existing basic responses
    if any(word in tokens for word in greetings):
        return random.choice(["Hello!", "Hi there!", "Hey! How can I help?"])
    elif any(word in tokens for word in farewell):
        return random.choice(["Goodbye!", "See you later!", "Take care!"])
    elif any(word in tokens for word in thanks):
        return random.choice(["You're welcome!", "No problem!", "Glad to help!"])
    else:
        return "I'm not sure how to respond to that yet."

if __name__ == '__main__':
    nltk.download('punkt')  # Ensure NLTK data is downloaded
    app.run(debug=True)