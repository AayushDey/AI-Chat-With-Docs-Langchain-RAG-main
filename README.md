# AI Chat With Docs - Langchain RAG

A Retrieval-Augmented Generation (RAG) application that allows you to chat with your markdown documents. It uses LangChain, FastAPI, ChromaDB, HuggingFace embeddings, and the Groq API for lightning-fast inference.

## Features

- **Document Ingestion**: Parse and chunk `.md` files from a designated directory (`data/books`).
- **Vector Database**: Use ChromaDB to store and retrieve document embeddings locally.
- **FastAPI Backend**: A RESTful API to query the vectorized database.
- **Web UI**: A clean HTML/CSS/JS frontend to interact with the documents easily.
- **Powered by Groq**: Uses Groq's high-performance API (`llama-3.3-70b-versatile`) for query responses.
- **HuggingFace Embeddings**: Fast local embeddings using `all-MiniLM-L6-v2`.

## Prerequisites

- Python 3.8+
- [Groq API Key](https://console.groq.com/)

## Installation

1. **Clone the repository** (if you haven't already):
   ```bash
   git clone <your-repo-url>
   cd AI-Chat-With-Docs-Langchain-RAG-main
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Mac/Linux:
   source venv/bin/activate
   ```

3. **Install the dependencies**:
   Ensure you have all the required packages installed. Since this project uses Groq and HuggingFace, make sure to install their respective Langchain integrations:
   ```bash
   pip install -r requirements.txt
   pip install langchain-groq langchain-huggingface fastapi uvicorn
   pip install "unstructured[md]"
   ```

4. **Environment Variables**:
   Create a `.env` file in the root of your project and add your Groq API key:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

## Usage

### 1. Ingest Documents

Place your markdown files (`.md`) inside the `data/books` directory. Then, generate the embeddings and populate the local Chroma vector database:

```bash
python create_database.py
```
This will create a `chroma` folder containing the indexed database.

### 2. Query via CLI (Optional)

You can test the RAG pipeline directly from the command line:

```bash
python query_data.py "What is the main topic of the documents?"
```

### 3. Run the Web Application

Start the FastAPI backend server to serve the API and the web frontend:

```bash
python app.py
```

Open your browser and navigate to `http://localhost:8000`. You can now chat with your documents using the interactive UI!

## Project Structure

- `app.py`: FastAPI server and route definitions.
- `create_database.py`: Logic to load documents, split text, create embeddings, and store them in ChromaDB.
- `query_data.py`: Logic to perform similarity search in ChromaDB and generate answers using the Groq LLM.
- `data/books/`: Directory to store source markdown files.
- `static/`: Contains the frontend assets (`index.html`, `styles.css`, `script.js`).
- `chroma/`: The local vector database directory.

## License

MIT License
