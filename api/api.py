import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from rag_app.services.retriever import retrieve_relevant_chunks
from rag_app.services.generator import generate_answer

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class QuestionRequest(BaseModel):
    question: str

@app.post("/ask")
def ask(body: QuestionRequest):
    chunks = retrieve_relevant_chunks(body.question)
    answer = generate_answer(body.question, chunks)
    return {"answer": answer}
