import json
import os

USERS_FILE = "data/users.json"


def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
        
    return {}

def add_user(username, password):
    users = load_users()
    if username in users:
        return False
    users[username] = {'password':password}
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=4)
    return True

def check_user(username, password):
    users= load_users()
    return username in users and users[username]['password'] ==  password
