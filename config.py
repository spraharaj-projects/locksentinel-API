from pydantic import BaseSettings
import os


class Settings(BaseSettings):
    HF_TOKEN: str = os.environ.get("HF_TOKEN")
    REPO_ID: str = "hf-supreetpraharaj/rfc_locksentinel"
    MODEL: str = "rfc_password_checker_model.pkl"
    VECTORIZER: str = "rfc_password_vectorizer.pkl"


settings = Settings()
