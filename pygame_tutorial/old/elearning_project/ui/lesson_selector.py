import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import Messagebox
from data.lesson_data import lessons
import os
import webbrowser
import tkVideoPlayer
from ui.score_manager import save_scores, load_scores

def play_video(video_path):
    os.startfile(os.path.abspath(video_path))

def open_pdf(pdf_path):
    if pdf_path and os.path.exists(pdf_path):
        webbrowser.open_new(pdf_path)
    else:
        print("file not exists")


def show_chapter_content(frame,username, subject, chapter, on_back, on_home):
    for widget in  frame.winfo_children():
        widget.destroy()
    content = lessons[subject][chapter].get("content", "محتوایی برای این فصل وجود ندارد")
    icon_path = lessons[subject][chapter].get("icon")
    video_path = lessons[subject][chapter].get("video")
    pdf_path = lessons[subject][chapter].get("pdf")
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
    #     videoplayer = tkVideoPlayer.TkinterVideo(master=frame, scaled=True)
    #     videoplayer.load(video_path)
    #     videoplayer.pack(pady=5)
    #     videoplayer.play()
    if pdf_path:
        ttk.Button(frame, text="بازکردن پی دی اف",bootstyle=(INFO, OUTLINE), width=20,
                command=lambda : open_pdf(pdf_path)).pack(pady=10)
        

    ttk.Label(frame, text="امتیاز به  این فصل").pack(pady=5)

    score_var = ttk.IntVar(value=0)
    score_label = ttk.Label(frame, text=f"امتیاز:{score_var.get()}")
    score_label.pack(pady=5)

    def update_label(value):
        score_label.config(text=f"امتیاز:{score_var.get()}")

    ttk.Scale(frame, from_=0, to=5, orient="horizontal", variable=score_var,\
               command=update_label).pack(pady=5)
    
    def save_score(username):
        save_scores(username,  subject, chapter, score_var.get())
        Messagebox.show_info(f"امتیاز{score_var.get()}","ثبت امتیاز")

    ttk.Button(frame, text="ثبت امتیاز",bootstyle=(INFO, OUTLINE), width=20,
                command=lambda :save_score(username)).pack(pady=10)
    ttk.Button(frame, text="بازگشت",bootstyle=(INFO, OUTLINE), width=20,
                command=lambda : show_lessons(frame,username, subject, None, on_back, on_home)).pack(pady=10)
    ttk.Button(frame, text="خانه",bootstyle=(INFO, OUTLINE), width=20,
                command=on_home).pack(pady=10)


def show_lessons(frame,username, subject, on_select_lesson, on_back,on_home):
    for widget in  frame.winfo_children():
        widget.destroy()

    ttk.Label(frame, text=f"فصل های درس {subject}",style="TLabel").pack(pady=10)
    for chapter in lessons.get(subject):
        ttk.Button(frame, text=chapter, bootstyle=(INFO, OUTLINE), width=20,
                   command=lambda c=chapter : show_chapter_content(frame,username, subject, c, on_back, on_home)).pack(pady=10)
    if on_back:
        ttk.Button(frame, text="بازگشت",bootstyle=(INFO, OUTLINE), command=on_back).pack(pady=10)
    
    # ttk.Button(frame, text="خانه",bootstyle=(INFO, OUTLINE), command=on_home).pack(pady=10)