import tkinter as tk
import os
from ui.home import show_home
from data.lession_data import lessons
def on_select_lesson(frame, subject):
    all_lessons = lessons[subject]
    for l in all_lessons:
        tk.Button(frame, text=l, font=("ZahraRoosta", 14)).pack(pady=10)


def main():
    root = tk.Tk()
    root.title("برنامه آموزشی هوشمند")
    
    root.geometry("500x400")
    if os.path.exists("../icon.ico"):
        root.iconbitmap(default="../icon.ico")

    frame = tk.Frame(root)
    frame.configure(bg="lightblue")
    
    show_home(frame, on_select_lesson)
    frame.pack(expand=True, fill="both")
    root.mainloop()

main()