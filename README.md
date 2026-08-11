# AI Document Search — RAG System

An AI-powered document search system that uses **Retrieval-Augmented Generation (RAG)** to answer questions based on information retrieved from PDF documents.

The project combines **PDF processing, text chunking, semantic embeddings, vector search, and Google's Gemini API** to retrieve relevant information and generate contextual answers.

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
* Indicate when the requested information is not available in the documents


## Technologies

* **Python**
* **PyPDF** — PDF text extraction
* **Sentence Transformers** — semantic text embeddings
* **ChromaDB** — vector database and similarity search
* **Google Gemini API** — answer generation
* **python-dotenv** — environment variable management

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

## Example

```text
AI Document Search
Type 'exit' to stop.

You: what is attention

Gemini:
Based on the provided context, attention is a mechanism
that learns to assign significance to different parts of
the input for each step of the output.

Source: seq2seq_attention.pdf

You: what are word vectors

Gemini:
Based on the provided context, word vectors are
representations of word tokens as vectors...

Source: word_vectors.pdf

You: who is Cristiano Ronaldo

Gemini:
Based on the provided context, there is no information
mentioned about Cristiano Ronaldo.


You: exit
Goodbye!
```

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
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

Before using the chatbot, the documents need to be processed and added to ChromaDB.

### 1. Index the documents

Run:

```powershell
python -m tests.test_vector_store
```

This processes all PDF documents from the `data/documents/` folder, creates embeddings, and stores them in ChromaDB.

This step only needs to be performed when the document collection is created or updated.

### 2. Start the chatbot

Run:

```powershell
python -m tests.test_rag
```

The application runs as an interactive terminal chatbot.

You can ask multiple questions during the same session.

To close the application, type:

```text
exit
```


