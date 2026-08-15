from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from backend.retrieval import retrieve_answer


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "Medical RAG API is running"
    }


@app.post("/ask")
def ask_question(request: QuestionRequest):
    answer = retrieve_answer(request.question)

    return {
        "answer": answer
    }