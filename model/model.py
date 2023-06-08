import gzip
import pickle
import joblib
from pathlib import Path

__version__ = "0.1.0"

BASE_DIR = Path(__file__).resolve(strict=True).parent

with gzip.open(f"{BASE_DIR}/rfc_password_checker_model.plk.gz", "rb") as f:
    classifier = pickle.load(f)

with open(f"{BASE_DIR}/rfc_password_vectorizer.plk", "rb") as f:
    vectorizer = joblib.load(f)


def predict_pipeline(password):
    password_numercial = vectorizer.transform([password]).toarray()
    strength = classifier.predict(data)
