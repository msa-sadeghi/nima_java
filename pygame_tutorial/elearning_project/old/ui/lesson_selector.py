import tkinter as tk
from data.lession_data import lessons

def show_lessons(frame,username, subject, on_select_lesson, on_back):
    for widget in frame.winfo_children():
        widget.destroy()
    tk.Label(frame, text=f"فصل های درس {subject}", 
             bg= "lightblue",
             fg= "purple",
             font=("ZahraRoosta", 14)).pack()
    
    on_select_lesson(frame, subject)
    