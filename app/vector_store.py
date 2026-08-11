import chromadb

client=chromadb.PersistentClient(path='chroma_db')
collection=client.get_or_create_collection(name='knowledge_base')

def add_documents(chunks,embeddings,document_name):
    ids=[f'{document_name}_{i}' for i in range(len(chunks))]
    collection.add(ids=ids,documents=chunks,embeddings=embeddings.tolist())

def search(query_embedding,n_results=3):
    results=collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=n_results
    )

    return results

