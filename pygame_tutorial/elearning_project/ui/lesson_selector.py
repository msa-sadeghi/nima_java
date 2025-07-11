import tkinter as tk
from data.lession_data import lessons

def show_lessons(frame, subject, on_select_lesson, on_back):
    tk.Label(frame, text=f"فصل های درس {subject}", 
             bg= "lightblue",
             fg= "purple",
             font=("ZahraRoosta", 14)).pack()