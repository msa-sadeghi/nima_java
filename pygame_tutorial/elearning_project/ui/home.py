import tkinter as tk
from ui.lesson_selector import show_lessons

def show_home(frame, on_select_lesson, on_back):
    for widget in frame.winfo_children():
        widget.destroy()

    tk.Label(frame, text="لطفا یک درس را انتخاب کنید",
             bg="lightblue", fg="purple", font=("ZahraRoosta", 14)).pack(pady=10)
    

    subjects = ["فیزیک", "شیمی", "زیست",  "ریاضی"]
    for subject in subjects:
        tk.Button(frame, text=subject,
                   width=20,
                   font=("ZahraRoosta", 12),
                   command = lambda s= subject:show_lessons(frame, s, on_select_lesson, on_back)
                   ).pack(pady=5)