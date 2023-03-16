import pickle
from pathlib import Path

import streamlit_authenticator as stauth

noms = ("PG", "AN", "Moi")
identifs = ("PG", "AN", "Ego")

passwords = ("abc335", "def788", "ihg456")

hashed_passwords = stauth.Hasher(passwords).generate()

file_path = Path(__file__).parent / "hash-dutruc.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)

