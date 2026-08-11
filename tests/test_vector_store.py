import os
from app.loader import load_pdf
from app.chunker import split_text
from app.embeddings import create_embeddings
from app.vector_store import add_documents

documents_folder='data/documents'

for filename in os.listdir(documents_folder):
    
    pdf_path = os.path.join(documents_folder,filename)
    text = load_pdf(pdf_path)
    chunks = split_text(text)
    embeddings = create_embeddings(chunks)
    document_name = os.path.splitext(filename)[0]
    add_documents(chunks, embeddings,document_name)

print("All Documents successfully added to ChromaDB!")