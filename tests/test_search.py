from app.embeddings import model
from app.vector_store import search

query= "Deep learning is a type of machine learning that uses neural networks"
query_embedding=model.encode(query)

results=search(query_embedding,n_results=5)

for i, document in enumerate(results["documents"][0]):
    print(f"\nResult {i + 1}:")
    print(document)

print("\nDistances:")
print(results["distances"][0])
print(results)