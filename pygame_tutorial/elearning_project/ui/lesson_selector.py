import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from data.lesson_data import lessons

def show_chapter_content(frame, subject, chapter, on_back):
    for widget in  frame.winfo_children():
        widget.destroy()
    content = lessons[subject][chapter].get("content", "محتوایی برای این فصل وجود ندارد")

    ttk.Label(frame, text=f"{chapter}", style="TLabel").pack(pady=10)
    ttk.Label(frame, text=f"{content}", style="TLabel", wraplength=400, justify='right').pack(pady=10)
   
    ttk.Button(frame, text="بازگشت",bootstyle=(INFO, OUTLINE),
                command=lambda : show_lessons(frame, subject, None, on_back)).pack(pady=10)


def show_lessons(frame, subject, on_select_lesson, on_back):
    for widget in  frame.winfo_children():
        widget.destroy()

    ttk.Label(frame, text=f"فصل های درس {subject}",style="TLabel").pack(pady=10)
    for chapter in lessons.get(subject):
        print("chapter is", chapter)
        ttk.Button(frame, text=chapter, bootstyle=(INFO, OUTLINE),
                   command=lambda c=chapter : show_chapter_content(frame, subject, c, on_back)).pack(pady=10)
    if on_back:
        ttk.Button(frame, text="بازگشت",bootstyle=(INFO, OUTLINE), command=on_back).pack(pady=10)