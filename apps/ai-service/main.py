import os
import httpx
from src.traveler_profiles import TRAVELER_PROFILES
from src.questionnaire import QUESTIONS
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from src.vectorizer import create_user_vector
from src.similarity import find_traveler_profile

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
    traveler_profile = find_traveler_profile(vector)

    return {
        "vector": vector,
        "traveler_profile": traveler_profile
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

@app.get("/profiles")
def get_traveler_profiles():
    return [
        {
            "code": profile_code,
            "name": profile_data["name"],
            "description": profile_data["description"]
        }
        for profile_code, profile_data in TRAVELER_PROFILES.items()
    ]

@app.get("/profile/questions")
def get_profile_questions():
    return QUESTIONS