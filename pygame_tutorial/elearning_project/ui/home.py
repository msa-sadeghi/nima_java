import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ui.lesson_selector import show_lessons

def show_home(frame, on_select_lesson, on_back):
    for widget in frame.winfo_children():
        widget.destroy()

    ttk.Label(frame, text="لطفا یک درس را انتخاب کنید",
             style="TLabel").pack(pady=10)
    

    subjects = ["فیزیک", "شیمی", "زیست",  "ریاضی"]
    for subject in subjects:
        ttk.Button(frame, text=subject,
                   width=20,
                   bootstyle=(INFO, OUTLINE),
                   command = lambda s= subject:show_lessons(frame, s, on_select_lesson, on_back)
                   ).pack(pady=5)