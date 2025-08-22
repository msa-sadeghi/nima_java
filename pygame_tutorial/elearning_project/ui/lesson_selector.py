import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from data.lesson_data import lessons

def show_chapter_content(frame, subject, chapter, on_back):
    for widget in  frame.winfo_children():
        widget.destroy()
    content = lessons[subject][chapter].get("content", "محتوایی برای این فصل وجود ندارد")
    icon_path = lessons[subject][chapter].get("icon")
    ttk.Label(frame, text=f"{chapter}", style="TLabel").pack(pady=10)
    if icon_path:
        try:
            icon = tk.PhotoImage(file=icon_path)
            icon = icon.subsample(5,5)
        except Exception as e:
            print(e)
    if icon:

        label = ttk.Label(frame, text=f"{content}", style="TLabel", 
                          wraplength=400, justify='right', image=icon,compound=RIGHT)
        label.image = icon
        label.pack(pady=10)
   
    ttk.Button(frame, text="بازگشت",bootstyle=(INFO, OUTLINE),
                command=lambda : show_lessons(frame, subject, None, on_back)).pack(pady=10)


def show_lessons(frame, subject, on_select_lesson, on_back):
    for widget in  frame.winfo_children():
        widget.destroy()

    ttk.Label(frame, text=f"فصل های درس {subject}",style="TLabel").pack(pady=10)
    for chapter in lessons.get(subject):
        ttk.Button(frame, text=chapter, bootstyle=(INFO, OUTLINE),
                   command=lambda c=chapter : show_chapter_content(frame, subject, c, on_back)).pack(pady=10)
    if on_back:
        ttk.Button(frame, text="بازگشت",bootstyle=(INFO, OUTLINE), command=on_back).pack(pady=10)