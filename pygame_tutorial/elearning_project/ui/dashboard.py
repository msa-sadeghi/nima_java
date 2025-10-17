import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ui.score_manager import load_scores

def show_dashboard(frame, on_back):
    for widget in frame.winfo_children():
        widget.destroy()

    ttk.Label(frame, text="داشبور پیشرفت").pack(pady=5)

    scores = load_scores()
    total_score = 0
    count =  0
    for subject, chapters in scores.items():
        ttk.Label(frame, text=f"درس {subject}").pack(pady=5)
        for chapter, score in chapters.items():
            ttk.Label(frame, text=f"فصل {chapter}").pack(pady=5)
            total_score += score
            count +=  1

    if count > 0:
        avg = total_score/ count
        ttk.Label(frame, text=f"میانگین کل نمره ها {avg} / 5").pack(pady=5)
    else:
        ttk.Label(frame, text=f"هنوز نمره ای ثبت نشده است").pack(pady=5)

    ttk.Button(frame, text="بازگشت",bootstyle=(INFO, OUTLINE), width=20,
                command=lambda :  on_back).pack(pady=10)

