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

## Author
- **Logen** ([GitHub](https://github.com/Logen))
