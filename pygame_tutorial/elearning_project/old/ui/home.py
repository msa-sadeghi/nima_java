import tkinter as tk
from .lesson_selector import show_lessons
def show_home(frame, on_select_lesson):

    tk.Label(frame, text="لطفا یک درس را انتخاب کنید", 
             bg= "lightblue",
             fg= "purple",
             font=("ZahraRoosta", 14)).pack()

    subjects = ["فیزیک", "شیمی", "زیست",  "ریاضی"]
    for subject in subjects:
        tk.Button(frame, text=subject,
                   width=20,
                   font=("ZahraRoosta", 12),
                   command = lambda s= subject:show_lessons(frame, s, on_select_lesson, None)
                   ).pack(pady=5)