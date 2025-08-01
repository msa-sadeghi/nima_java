import tkinter as tk
from ui.home import show_home
import os

def go_back():
        show_home(frame, on_select_lesson, go_back)

def on_select_lesson(frame, subject):
        print(f"lesson{subject}")


root = tk.Tk()
root.title("برنامه آموزشی هوشمند")
root.geometry("500x400")
if os.path.exists("./icon.ico"):
        root.iconbitmap(default="./icon.ico")

frame = tk.Frame(root)
frame.configure(bg="lightblue")
frame.pack(expand=True, fill="both")

show_home(frame, on_select_lesson, go_back)


root.mainloop()
