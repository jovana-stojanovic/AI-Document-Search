from app.loader import load_pdf

pdf_path="./data/documents/deep_learning.pdf"
text=load_pdf(pdf_path)
print(text[:3000])
