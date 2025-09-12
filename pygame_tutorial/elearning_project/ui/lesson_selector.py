import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from data.lesson_data import lessons
import os

def play_video(video_path):
    os.startfile(os.path.abspath(video_path))

def show_chapter_content(frame, subject, chapter, on_back, on_home):
    for widget in  frame.winfo_children():
        widget.destroy()
    content = lessons[subject][chapter].get("content", "محتوایی برای این فصل وجود ندارد")
    icon_path = lessons[subject][chapter].get("icon")
    video_path = lessons[subject][chapter].get("video")
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
    if video_path:
        ttk.Button(frame, text="Play",bootstyle=(INFO, OUTLINE), width=20,
                command=lambda : play_video(video_path)).pack(pady=10)

    ttk.Button(frame, text="بازگشت",bootstyle=(INFO, OUTLINE), width=20,
                command=lambda : show_lessons(frame, subject, None, on_back, on_home)).pack(pady=10)
    ttk.Button(frame, text="خانه",bootstyle=(INFO, OUTLINE), width=20,
                command=on_home).pack(pady=10)


def show_lessons(frame, subject, on_select_lesson, on_back,on_home):
    for widget in  frame.winfo_children():
        widget.destroy()

    ttk.Label(frame, text=f"فصل های درس {subject}",style="TLabel").pack(pady=10)
    for chapter in lessons.get(subject):
        ttk.Button(frame, text=chapter, bootstyle=(INFO, OUTLINE), width=20,
                   command=lambda c=chapter : show_chapter_content(frame, subject, c, on_back, on_home)).pack(pady=10)
    if on_back:
        ttk.Button(frame, text="بازگشت",bootstyle=(INFO, OUTLINE), command=on_back).pack(pady=10)
    
    # ttk.Button(frame, text="خانه",bootstyle=(INFO, OUTLINE), command=on_home).pack(pady=10)