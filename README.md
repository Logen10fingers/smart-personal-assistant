# Smart Personal Assistant

A **Smart Personal Assistant** built to provide conversational support, growing in complexity and functionality over time. This project combines a Flask backend, a Next.js frontend, and features like context-aware responses and chat logging, making it a practical tool for learning full-stack development and AI integration.

## Features

- **Flask Backend**:
  - RESTful API with a `/chat` endpoint to handle user messages.
  - In-memory chat history to enable context-aware responses (e.g., remembers if you say "I’m tired" and suggests a break when you ask "What should I do?").
  - Logs conversations to `chat_log.txt` for persistence.
  - Uses NLTK for basic natural language processing (e.g., tokenizing user input for keyword matching).

- **Next.js Frontend**:
  - A responsive chat UI built with React and styled with Tailwind CSS.
  - Connects to the Flask backend to send user messages and display responses.

- **Context Awareness**:
  - Tracks conversation history per user (using `user_id`) and uses it to generate smarter responses.
  - Example: If you say "I’m tired" and later ask "What should I do?", the assistant responds with "You mentioned being tired earlier—how about a quick break?"

- **Development Tools**:
  - Debug print statements in the backend to trace chat history and request flow.
  - Local development environment set up for both frontend and backend.

## Project Structure

smart-personal-assistant/
├── app.py              # Flask backend with /chat endpoint and context logic
├── chat_log.txt        # Logs of user-assistant conversations
├── frontend/           # Next.js frontend directory
│   ├── pages/          # React pages (e.g., chat interface)
│   ├── styles/         # Tailwind CSS styles
│   └── package.json    # Frontend dependencies
├── README.md           # Project documentation (you’re reading it!)
└── requirements.txt    # Python dependencies (e.g., Flask, NLTK)

## Setup and Installation

### Prerequisites
- **Python 3.13.1** (or compatible version)
- **Node.js** (for the Next.js frontend)
- **Git** (to clone the repository)

### Backend Setup
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Logen/smart-personal-assistant.git
   cd smart-personal-assistant

Set Up a Virtual Environment (optional but recommended):
bash

python -m venv env
.\env\Scripts\activate  # On Windows

Install Python Dependencies:
bash

pip install -r requirements.txt

If requirements.txt doesn’t exist yet, install manually:
bash

pip install flask nltk

Run the Flask Backend:
bash

python app.py

The backend will run on http://127.0.0.1:5000.

Frontend Setup
Navigate to the Frontend Directory:
bash

cd frontend

Install Node.js Dependencies:
bash

npm install

Run the Next.js Frontend:
bash

npm run dev

The frontend will run on http://localhost:3000.

Testing the Application
Start Both Servers:
Run the Flask backend (python app.py) in one terminal.

Run the Next.js frontend (npm run dev) in another terminal.

Access the Chat Interface:
Open http://localhost:3000 in your browser to see the chat UI.

Send messages to the assistant and see responses.

Test with Postman (Optional):
Send POST requests to http://127.0.0.1:5000/chat:
Example 1: {"message": "I’m tired", "user_id": "user1"}

Example 2: {"message": "What should I do?", "user_id": "user1"}

Check chat_log.txt for logged conversations.

Current Progress
Completed:
Flask backend with a /chat endpoint.

Next.js frontend with a basic chat UI using Tailwind CSS.

Context-aware responses using in-memory chat history.

Chat logging to a file (chat_log.txt).

Debug prints for troubleshooting chat history and request flow.

Next Steps:
Integrate Google’s Gemini API to enhance response generation.

Improve the frontend UI/UX.

Add persistent storage for chat history (e.g., database).

Contributing
This is a learning project, but contributions are welcome! Feel free to fork the repository, make improvements, and submit a pull request.
License
This project is licensed under the MIT License—see the LICENSE file for details (if applicable).
Author
Logen (GitHub)

