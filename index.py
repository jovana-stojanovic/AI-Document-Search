import os

from app.loader import load_pdf
from app.chunker import split_text
from app.embeddings import create_embeddings
from app.vector_store import add_documents


DOCUMENTS_FOLDER = "data/documents"


def index_documents():
    for filename in os.listdir(DOCUMENTS_FOLDER):

        if not filename.lower().endswith(".pdf"):
            continue

        pdf_path = os.path.join(DOCUMENTS_FOLDER, filename)

        print(f"Processing: {filename}")

        text = load_pdf(pdf_path)
        chunks = split_text(text)
        embeddings = create_embeddings(chunks)

        document_name = os.path.splitext(filename)[0]

        add_documents(
            chunks,
            embeddings,
            document_name
        )

    print("\nAll documents successfully added to ChromaDB!")


if __name__ == "__main__":
    index_documents()