import matplotlib.pyplot as plt
import tkinter as tk
from ui.score_manager import load_scores


def show_progress_chart(frame, username, on_back):
    for widget in frame.get_winfo_children():
        widget.destroy()
    scores = load_scores(username)
    subjects = list(scores.keys())
