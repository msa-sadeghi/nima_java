import json
import os

SCORES_FILE = "data/scores.json"

def load_scores():
    if os.path.exists(SCORES_FILE):
        with open(SCORES_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_scores(subject, chapter, score):
    scores = load_scores()
    if subject not in scores:
        scores[subject] = {}
    scores[subject][chapter] = score
    with open(SCORES_FILE, "w", encoding="utf-8") as f:
        json.dump(scores, f)