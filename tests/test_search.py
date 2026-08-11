from app.embeddings import model
from app.vector_store import search

query='What is a ReLU?'
query_embedding=model.encode(query)

results=search(query_embedding,n_results=3)

for i, document in enumerate(results["documents"][0]):
    print(f"\nResult {i + 1}:")
    print(document)

print("\nDistances:")
print(results["distances"][0])
print(results)