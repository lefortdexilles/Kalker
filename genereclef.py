import pickle
from pathlib import Path

import streamlit_authenticator as stauth

names = ["Pascale Gay", "Axel Nogue", "Moi"]
usernames = ["Pascale G", "Axel N", "Ego"]

passwords = ["abc123", "def789", "ihg456"]

hashed_password = stauth.Hasher(passwords).generate()

file_path = Path(__file__).parent / "hash-dutruc.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_password, file)

