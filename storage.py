import json
import os

DATA_DIR = "data"

def save_data(username, data):
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(f"{DATA_DIR}/{username}.json", "w") as f:
        json.dump(data, f, indent=4)

def load_data(username):
    path = f"{DATA_DIR}/{username}.json"
    if os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f)
    return {"expenses": []}