import pickle
from pathlib import Path

import streamlit_authenticator as stauth

noms = ("Pascale Gay", "Axel Nogue", "Moi")
identifs = ("Pascale G", "Axel N", "Ego")

passwords = ("abc123", "def789", "ihg456")

hashed_passwords = stauth.Hasher(passwords).generate()

file_path = Path(__file__).parent / "hash-dutruck.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)

