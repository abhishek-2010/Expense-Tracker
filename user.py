import json
import os

USERS_FILE = "data/users.json"

def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    return {}

def save_users(users):
    os.makedirs("data", exist_ok=True)
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)

def register(username, password):
    users = load_users()
    if username in users:
        print("Username already exists.")
        return False
    users[username] = password
    save_users(users)
    print(f"User '{username}' registered successfully!")
    return True

def login(username, password):
    users = load_users()
    if users.get(username) == password:
        print(f"Welcome back, {username}!")
        return True
    print("Invalid username or password.")
    return False