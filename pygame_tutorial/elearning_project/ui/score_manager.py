import json
import os

SCORES_FILE = "data/scores.json"

def load_scores(username=None):
    if os.path.exists(SCORES_FILE):
        try:
            with open(SCORES_FILE, "r", encoding="utf-8") as f:
                scores = json.load(f)
                if username:
                    return scores.get(username)
                return scores
        except:
            print("error")
    return {}


def save_scores(username, subject, chapter, score):
    scores = {}
    if os.path.exists(SCORES_FILE):
        with open(SCORES_FILE, "r", encoding="utf-8") as f:
                scores = json.load(f)
    if username not in scores:
        scores[username] = {}
    if subject not in scores[username]:
        scores[username] = {}
    scores[username][subject][chapter] = score
    with open(SCORES_FILE, "w", encoding="utf-8") as f:
        json.dump(scores, f)