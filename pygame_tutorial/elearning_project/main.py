import tkinter as tk
import ttkbootstrap as ttk
from ui.home import show_home
from ui.login import show_login
import os

def go_back():
        show_home(frame, on_select_lesson, go_back, go_home)
def go_home():
        show_home(frame, on_select_lesson,go_back, go_home)

def on_select_lesson(frame, subject):
        pass
        # print(f"lesson{subject}")

        

root = ttk.Window(themename="vapor")

style = ttk.Style()
style.configure('TButton',font=("B Nazanin", 14, "bold")) 
style.configure('TLabel',font=("B Nazanin", 14, "bold")) 
style.configure('TEntry',font=("B Nazanin", 14, "bold")) 
style.configure('My.TMenubutton',font=("B Nazanin", 14, "bold")) 
root.title("برنامه آموزشی هوشمند")
root.geometry("500x400")
if os.path.exists("./icon.ico"):
        root.iconbitmap(default="./icon.ico")

frame = tk.Frame(root)
# frame.configure(bg="lightblue")
frame.pack(expand=True, fill="both")



def on_login(username):
        show_home(frame,username, on_select_lesson, go_back, go_home)

show_login(frame, on_login)


root.mainloop()
