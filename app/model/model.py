import gzip
import pickle
import joblib
from pathlib import Path
import gdown

__version__ = "0.1.0"

BASE_DIR = Path(__file__).resolve(strict=True).parent


classifier_file = Path(BASE_DIR) / "rfc_password_checker_model.pkl.gz"
vectorizer_file = Path(BASE_DIR) / "rfc_password_vectorizer.pkl"

if not classifier_file.exists():
    gdown.download(id="1SlTJXDdAIeNytQEWAPZM8ppDeb6p5Yik", output=str(classifier_file))

if not vectorizer_file.exists():
    gdown.download(id="1_ghLdOogqIVaTlNdwuCKrPGjj_SdditJ", output=str(vectorizer_file))

with gzip.open(classifier_file, "rb") as f:
    classifier = pickle.load(f)

with open(vectorizer_file, "rb") as f:
    vectorizer = joblib.load(f)


def predict_pipeline(password):
    password_numercial = vectorizer.transform([password]).toarray()
    strength = classifier.predict(password_numercial)
    return strength
