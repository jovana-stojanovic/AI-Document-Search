
import os
from dotenv import load_dotenv
from google import genai

from app.embeddings import model
from app.vector_store import search

load_dotenv()
client=genai.Client(api_key=os.getenv('GEMINI_API_KEY'))

def build_context(results):
    documents=results['documents'][0]

    if not documents:
        return ""
    
    context='\n'.join(documents)
    return context

def build_prompt(query, context):
    prompt = f"""
You are an AI assistant that answers questions based only on the provided documents.
Use the following context to answer the question.
If the answer cannot be found in the context, say:
"I could not find the answer in the provided documents."

Do not use outside knowledge.

Context:
{context}

Question:
{query}

Answer:
"""
    return prompt




def ask_gemini(prompt):
    response=client.models.generate_content(model='gemini-3.6-flash',contents=prompt)
    return response.text

def get_source_documents(results):
    ids = results.get("ids", [[]])[0]
    sources=set()

    for document_id in ids:
        doc_name=document_id.rsplit('_',1)[0]
        sources.add(doc_name)

    return list(sources)

def ask_question(query):
    query_embedding=model.encode(query)
    results=search(query_embedding,n_results=3)

    context=build_context(results)

    if not context:
        return (
            "I could not find any relevant information in the "
            "provided documents.",
            []
        )

    prompt=build_prompt(query,context)
    answer=ask_gemini(prompt)

    sources=get_source_documents(results)

    return answer,sources

