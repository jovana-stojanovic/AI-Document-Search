
def build_context(results):
    documents=results['documents'][0]
    context='\n'.join(documents)
    return context

def build_prompt(query,context):
    prompt=f'''
Use the following context to answer the question
Context: {context}
Question: {query}
Answer: 
'''
    return prompt

import os
from dotenv import load_dotenv
from google import genai

from app.embeddings import model
from app.vector_store import search

load_dotenv()
client=genai.Client(api_key=os.getenv('GEMINI_API_KEY'))

def ask_gemini(prompt):
    response=client.models.generate_content(model='gemini-3.6-flash',contents=prompt)
    return response.text

def ask_question(query):
    query_embedding=model.encode(query)
    results=search(query_embedding,n_results=3)
    context=build_context(results)
    prompt=build_prompt(query,context)
    answer=ask_gemini(prompt)
    document_id = results["ids"][0][0]
    document_name = document_id.rsplit("_", 1)[0]

    return answer,document_name

