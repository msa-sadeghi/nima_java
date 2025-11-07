import json
import os

USERS_FILE = "data/users.json"


def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
        
    return {}