from app.loader import load_pdf
from app.chunker import split_text

pdf_path="./data/documents/deep_learning.pdf"
text=load_pdf(pdf_path)
chunks=split_text(text)

print('Number of chunks:', len(chunks))
print(chunks[0])
