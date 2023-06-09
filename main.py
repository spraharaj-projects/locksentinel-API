from fastapi import FastAPI
from pydantic import BaseModel
from app.model.model import predict_pipeline
from app.model.model import __version__ as model_version
from config import settings
from huggingface_hub import login

app = FastAPI()

login(settings.HF_TOKEN)


class PasswordIn(BaseModel):
    password: str


class PredictionOut(BaseModel):
    strength: int


@app.get("/")
def home():
    return {
        "heath_check": "OK",
        "model_version": model_version
    }


@app.post("/check", response_model=PredictionOut)
def predict(payload: PasswordIn):
    strength = predict_pipeline(payload.password)
    return {"strength": strength}
