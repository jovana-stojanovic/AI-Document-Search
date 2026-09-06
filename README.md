# AI Document Search — RAG System

An AI-powered document search system that uses **Retrieval-Augmented Generation (RAG)** to answer questions based on information retrieved from PDF documents.

The project combines **PDF processing, text chunking, semantic embeddings, vector search, Google's Gemini API, FastAPI, and a web frontend** to retrieve relevant information and generate contextual answers.

## Features

* Extract text from PDF documents
* Split documents into smaller text chunks
* Generate semantic embeddings using Sentence Transformers
* Store embeddings in ChromaDB
* Perform semantic similarity search
* Retrieve relevant document chunks
* Generate answers using Google Gemini
* Display the source document used for the answer
* Ask multiple questions in a single terminal session
* Provide a REST API using FastAPI
* Provide a web interface using HTML, CSS, and JavaScript
* Send questions from the frontend to the FastAPI backend
* Display answers and source documents in the web interface
* Indicate when the requested information is not available in the documents

## Technologies

* **Python**
* **PyPDF** — PDF text extraction
* **Sentence Transformers** — semantic text embeddings
* **ChromaDB** — vector database and similarity search
* **Google Gemini API** — answer generation
* **python-dotenv** — environment variable management
* **FastAPI** — REST API backend
* **Uvicorn** — ASGI server for running the FastAPI application
* **HTML, CSS, JavaScript** — web frontend

## Project Structure

```text
AI-Document-Search/
├── app/
│   ├── loader.py
│   ├── chunker.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── rag.py
│   ├── api.py
│   └── schemas.py
├── data/
│   └── documents/
│       ├── deep_learning.pdf
│       ├── seq2seq_attention.pdf
│       └── word_vectors.pdf
├── frontend/
│   ├── index.html
│   ├── styles.css
│   └── app.js
├── tests/
├── index.py
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Documents

The current knowledge base contains three PDF documents related to deep learning and natural language processing:

* `deep_learning.pdf`
* `seq2seq_attention.pdf`
* `word_vectors.pdf`

## RAG Pipeline

### 1. Document Loading

PDF documents are loaded using PyPDF and their text is extracted page by page.

### 2. Text Chunking

The extracted text is divided into smaller overlapping chunks.

The current configuration uses a chunk size of **1000 characters** with an overlap of **200 characters**.

The overlap helps preserve context between neighboring chunks.

### 3. Embeddings

Each document chunk is converted into a numerical vector using the **`all-MiniLM-L6-v2`** Sentence Transformer model.

These vectors capture the semantic meaning of the text and allow similar questions and document sections to be matched.

### 4. Vector Storage

The generated embeddings, text chunks, and document identifiers are stored in **ChromaDB**.

Each chunk receives an identifier containing the document name and chunk number.

### 5. Retrieval

When a user asks a question, the question is converted into an embedding.

ChromaDB searches for the most semantically similar document chunks and returns the top three results.

### 6. Generation

The retrieved chunks are combined into a context together with the user's question.

This context is then sent to Gemini, which generates the final answer.

### 7. Source Attribution

The application extracts the document name from the retrieved chunk ID and displays it together with the generated answer.

## REST API

The RAG functionality is exposed through a REST API built with **FastAPI**.

The main endpoint is:

```text
POST /ask
```

It accepts a JSON request containing a question:

```json
{
  "question": "What is attention?"
}
```

The API processes the question using the existing RAG pipeline and returns the generated answer together with the source documents:

```json
{
  "answer": "Based on the provided documents, attention ...",
  "sources": [
    "seq2seq_attention"
  ]
}
```

FastAPI also provides interactive API documentation at:

```text
http://127.0.0.1:8000/docs
```

The `/docs` page can be used to test the API directly from the browser.

## Web Frontend

The project also includes a standalone web frontend built with **HTML, CSS, and vanilla JavaScript**.

The frontend allows users to:

* Enter a question
* Send the question to the FastAPI backend
* Display the generated answer
* Display the source documents
* See loading and error states

The frontend communicates with the backend using the REST API:

```text
Frontend
   ↓
POST /ask
   ↓
FastAPI
   ↓
RAG pipeline
   ↓
ChromaDB + Gemini
   ↓
JSON response
   ↓
Frontend
```

The frontend files are located in:

```text
frontend/
├── index.html
├── styles.css
└── app.js
```

## Example

### Web Application

The user can enter a question such as:

```text
What is attention?
```

The application returns an answer based only on the information retrieved from the available documents and displays the supporting source:

```text
Answer

Based on the provided documents, attention (in the context
of translation) can be thought of as "alignment"...

Sources

- seq2seq_attention
```

If the requested information is not available in the documents, the system indicates that it could not find the answer in the provided documents.

### Terminal Application

The original terminal interface is still available:

```text
AI Document Search

Type 'exit' to stop.

You: what is attention

Gemini:

Based on the provided context, attention is a mechanism
that learns to assign significance to different parts of
the input for each step of the output.

Source: seq2seq_attention.pdf
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/jovana-stojanovic/AI-Document-Search
cd ai-document-search
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Gemini API

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

The API key is loaded from the environment and is not included in the repository.

## Running the Application

Before using the application, the documents need to be processed and added to ChromaDB.

### 1. Index the documents

Run:

```powershell
python index.py
```

This processes all PDF documents from the `data/documents/` folder, creates embeddings, and stores them in ChromaDB.

This step only needs to be performed when the document collection is created or updated.

### 2. Start the FastAPI server

Run:

```powershell
uvicorn app.api:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Interactive API documentation is available at:

```text
http://127.0.0.1:8000/docs
```

### 3. Open the web frontend

Open:

```text
frontend/index.html
```

in a web browser.

Make sure the FastAPI server is running before using the frontend.

The frontend sends questions to:

```text
http://127.0.0.1:8000/ask
```

### 4. Run the terminal application

The original terminal interface can still be used independently:

```powershell
python main.py
```

The application runs as an interactive terminal chatbot.

You can ask multiple questions during the same session.

To close the application, type:

```text
exit
```

## Application Architecture

The project consists of several layers:

```text
                    Web Browser
                         |
                         | HTTP POST /ask
                         v
              +---------------------+
              |       FastAPI       |
              |      app/api.py     |
              +---------------------+
                         |
                         v
              +---------------------+
              |    RAG Pipeline     |
              |      rag.py         |
              +---------------------+
                    /          \
                   v            v
              ChromaDB        Gemini
             Retrieval      Generation
```

The FastAPI layer exposes the existing RAG functionality through HTTP, while the frontend provides a user-friendly interface for interacting with the API.
