from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import QuestionRequest
from app.rag import ask_question

app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post('/ask')
def ask(request:QuestionRequest):
    answer,sources= ask_question(request.question)
    return {
        'answer':answer,
        'sources':sources
    }
