import tkinter as tk
from data.lesson_data import lessons
def show_lessons(frame, subject, on_select_lesson, on_back):
    for widget in  frame.winfo_children():
        widget.destroy()

    tk.Label(frame, text=f"فصل های درس {subject}",
             bg="lightblue", fg="purple", font=("ZahraRoosta", 14)).pack(pady=10)
    
    if on_back:
        tk.Button(frame, text="بازکشت",font=("ZahraRoosta", 12), command=on_back).pack(pady=10)

    for chapter in lessons.get(subject):

        tk.Button(frame, text=chapter, font=("ZahraRoosta", 12)).pack(pady=10)