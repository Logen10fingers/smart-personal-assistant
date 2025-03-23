import random
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = generate_response(user_input)
    return jsonify({'response': response})

def generate_response(user_input):
    user_input = user_input.lower()  # Convert to lowercase for better matching

    greetings = ["hello", "hi", "hey"]
    farewell = ["bye", "goodbye", "see you"]
    thanks = ["thank you", "thanks"]

    if any(word in user_input for word in greetings):
        return random.choice(["Hello!", "Hi there!", "Hey! How can I help?"])

    elif any(word in user_input for word in farewell):
        return random.choice(["Goodbye!", "See you later!", "Take care!"])

    elif any(word in user_input for word in thanks):
        return random.choice(["You're welcome!", "No problem!", "Glad to help!"])

    else:
        return "I'm not sure how to respond to that yet."

if __name__ == '__main__':
    app.run(debug=True)