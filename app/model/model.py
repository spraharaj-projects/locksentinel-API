# import gzip
from huggingface_hub import login, hf_hub_download
import os
# import pickle
import joblib
from config import settings

# from pathlib import Path
# import gdown

__version__ = "0.1.0"

print('-----------------------------------------------------------')
print(os.environ.get('HF_TOKEN'))
print('-----------------------------------------------------------')

# BASE_DIR = Path(__file__).resolve(strict=True).parent


# classifier_file = Path(BASE_DIR) / "rfc_password_checker_model.pkl.gz"
# vectorizer_file = Path(BASE_DIR) / "rfc_password_vectorizer.pkl"

# if not classifier_file.exists():
#     gdown.download(id="1SlTJXDdAIeNytQEWAPZM8ppDeb6p5Yik", output=str(classifier_file))

# if not vectorizer_file.exists():
#     gdown.download(id="1_ghLdOogqIVaTlNdwuCKrPGjj_SdditJ", output=str(vectorizer_file))
# print(hf_hub_download(repo_id="hf-supreetpraharaj/rfc_locksentinel",
#                          filename="rfc_password_checker_model.pkl"))
classifier = joblib.load(hf_hub_download(repo_id="hf-supreetpraharaj/rfc_locksentinel",
                         filename="rfc_password_checker_model.pkl"))
vectorizer = joblib.load(hf_hub_download(repo_id="hf-supreetpraharaj/rfc_locksentinel",
                         filename="rfc_password_vectorizer.pkl"))


def predict_pipeline(password):
    password_numercial = vectorizer.transform([password]).toarray()
    strength = classifier.predict(password_numercial)
    return strength
