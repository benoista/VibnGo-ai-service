import os

import httpx
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from src.vectorizer import create_user_vector

load_dotenv()

OLLAMA_HOST = os.getenv("OLLAMA_HOST")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")

app = FastAPI(title="VibnGo AI Service")


class ChatRequest(BaseModel):
    prompt: str

class ProfileRequest(BaseModel):
    responses: dict[int, str]


@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/profile/vector")
def create_profile_vector(request: ProfileRequest):
    vector = create_user_vector(request.responses)

    return {
        "vector": vector
    }

@app.post("/chat")
async def chat(request: ChatRequest):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{OLLAMA_HOST}/api/generate",
            json={"model": OLLAMA_MODEL, "prompt": request.prompt, "stream": False},
            timeout=60.0,
        )
        response.raise_for_status()
        return response.json()
