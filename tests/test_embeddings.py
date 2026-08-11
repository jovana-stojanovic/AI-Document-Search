from app.loader import load_pdf
from app.chunker import split_text
from app.embeddings import create_embeddings

text=load_pdf('./data/documents/deep_learning.pdf')
chunks=split_text(text)
embeddings=create_embeddings(chunks)

print("Number of chunks:", len(chunks))
print("Number of embeddings:", len(embeddings))
print("Embedding dimensions:", len(embeddings[0]))