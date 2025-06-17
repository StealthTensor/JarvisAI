# JarvisAI

A JARVIS-inspired AI assistant built with Python, LangChain, and Ollama, featuring voice interaction and a web interface. It uses the Qwen 7B model for natural language understanding and retrieval-augmented generation to answer queries. The assistant processes user input—either via voice or text—by embedding documents into a Chroma vector database, retrieving relevant information, and generating responses through the Qwen 7B model. The web interface, powered by FastAPI, provides a sleek chat experience, while the voice mode leverages speech recognition and text-to-speech for hands-free operation. Ideal for enthusiasts interested in artificial intelligence, coding, and innovation.

## Features
- Voice interaction using speech recognition and text-to-speech.
- Web-based chat interface with a modern UI.
- Retrieval-augmented generation with LangChain and Qwen 7B model via Ollama.
- Persistent vector database using Chroma for document retrieval.
- FastAPI backend for handling chat requests.

## How It Works
1. **Document Processing**: The assistant starts by loading text data (e.g., from `data.txt`) and splitting it into chunks using LangChain’s `CharacterTextSplitter`. These chunks are embedded into a Chroma vector database using Ollama’s `nomic-embed-text` model for efficient retrieval.
2. **Query Handling**:
   - **Voice Mode**: Speech input is captured via a microphone, converted to text using the `speech_recognition` library, and processed as a query. The response is converted back to speech using `pyttsx3`.
   - **Web Mode**: Text input is sent to the FastAPI backend, which processes the query and returns a response to the frontend for display.
3. **Response Generation**: Queries are sent to the Chroma database to retrieve relevant document chunks. These chunks are passed to the Qwen 7B model (via Ollama) to generate a natural language response using retrieval-augmented generation.
4. **User Interface**: The web interface (`index.html`) offers a chat-based experience with a futuristic design, while the voice mode allows hands-free operation.

## Prerequisites
- Python 3.8+
- Ollama installed with the Qwen 7B model (`qwen:7b`) and `nomic-embed-text` for embeddings.
- Redis (optional, for caching if extended).
- PostgreSQL (optional, for user data if extended).

## Setup Instructions
1. **Clone the Repository**
   ```bash
   git clone https://github.com/StealthTensor/JarvisAI.git
   cd JarvisAI
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   If you don't have a `requirements.txt`, install the following:
   ```bash
   pip install langchain langchain-community fastapi uvicorn jinja2 speechrecognition pyttsx3 chromadb
   ```

3. **Set Up Ollama**
   - Ensure Ollama is running on `http://localhost:11434`.
   - Pull the required models:
     ```bash
     ollama pull qwen:7b
     ollama pull nomic-embed-text
     ```

4. **Run the Vector Database Setup**
   - Run `main.py` to initialize the Chroma database with `data.txt`:
     ```bash
     python main.py
     ```
   - This step creates the `db` folder for persistence.

5. **Start the Web Server**
   ```bash
   uvicorn app:app --host 0.0.0.0 --port 8000
   ```
   - Access the web interface at `http://localhost:8000`.

6. **Voice Interaction**
   - Run `main.py` separately in another terminal for voice interaction:
     ```bash
     python main.py
     ```
   - Speak to the assistant; say "exit" or "quit" to stop.

## Usage
- **Web Interface**: Open `http://localhost:8000` in your browser. Type your queries in the chat input to interact with Jarvis.
- **Voice Assistant**: Run `main.py` and speak your queries. The assistant will respond via voice.
- **Example Queries**:
  - "What is artificial intelligence?"
  - "Tell me about coding."
  - "What can you do?"

## Project Structure
- `main.py`: Core script for voice interaction and vector database setup.
- `app.py`: FastAPI backend for the web interface.
- `voice_assistant.py`: Handles speech recognition and text-to-speech.
- `index.html`: Frontend HTML for the web interface.
- `static/`: Directory for static files (e.g., CSS, images like `jarvis_logo.png`).
- `db/`: Chroma vector database for document retrieval.
- `data.txt`: Input data for the assistant.
- `langchain.env`: Environment configuration for Ollama.

## Future Improvements
- Add CSS styling for a more JARVIS-like futuristic UI (e.g., glowing effects, dark theme).
- Implement user authentication for the web interface.
- Add support for multiple languages in voice recognition.
- Integrate PostgreSQL for user data and preferences.
- Enhance error handling in voice recognition.

## Contributing
Feel free to fork this repository, submit issues, or create pull requests. Let’s make JarvisAI even smarter!

## License
This project is licensed under the MIT License.
