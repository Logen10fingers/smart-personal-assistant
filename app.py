import random
import nltk
import datetime
from flask import Flask, request, jsonify
from nltk.tokenize import word_tokenize

app = Flask(__name__)

def log_message(user_input, response):
    """Logs chat history to a file"""
    with open("chat_log.txt", "a") as log_file:
        log_file.write(f"{datetime.datetime.now()} | User: {user_input} | Assistant: {response}\n")

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = generate_response(user_input)

    log_message(user_input, response) 
    
    return jsonify({'response': response})

def generate_response(user_input):
    user_input = user_input.lower()  # Convert to lowercase for better matching
    tokens = word_tokenize(user_input)  # Tokenize user input

    greetings = ["hello", "hi", "hey"]
    farewell = ["bye", "goodbye", "see you"]
    thanks = ["thank you", "thanks"]

    if any(word in tokens for word in greetings):  # Corrected this line
        return random.choice(["Hello!", "Hi there!", "Hey! How can I help?"])

    elif any(word in tokens for word in farewell):  # Corrected this line
        return random.choice(["Goodbye!", "See you later!", "Take care!"])

    elif any(word in tokens for word in thanks):  # Corrected this line
        return random.choice(["You're welcome!", "No problem!", "Glad to help!"])

    else:
        return "I'm not sure how to respond to that yet."

if __name__ == '__main__':
    app.run(debug=True)
