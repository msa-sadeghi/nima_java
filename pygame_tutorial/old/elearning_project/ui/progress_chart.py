import matplotlib.pyplot as plt
import tkinter as tk
from ui.score_manager import load_scores
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import arabic_reshaper
from bidi.algorithm import get_display


def fa(text):
    reshaped = arabic_reshaper.reshape(text)
    return get_display(reshaped)


def show_progress_chart(frame, username, on_back):
    for widget in frame.winfo_children():
        widget.destroy()
    scores = load_scores(username)
    title = tk.Label(frame, text=fa("نمودار پیشرفت تحصیلی"))
    title.pack(pady=10)

    if not scores:
        lbl = tk.Label(frame, text=fa("داده ای برای نمایش وجود ندارد"))
        lbl.pack(pady=10)
        return
    subjects = []
    for s in list(scores.keys()):
        subjects.append(fa(s))

    averages = []
    for subject, chapters in scores.items():
        total_score = 0
        count = 0
        for chapter, score in chapters.items():
            total_score += score
            count += 1

        if count > 0:
            avg = total_score / count
            averages.append(avg)

    fig, ax = plt.subplots(figsize=(6, 4))
    bars = ax.bar(subjects, averages)
    ax.set_ylabel(fa("میانگین نمره"))
    ax.set_xlabel(fa("درس "))
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=10)
