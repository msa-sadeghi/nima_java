import tkinter as tk
import os
from ui.home import show_home
def main():
    root = tk.Tk()
    root.title("برنامه آموزشی هوشمند")
    
    root.geometry("500x400")
    if os.path.exists("../icon.ico"):
        root.iconbitmap(default="../icon.ico")

    frame = tk.Frame(root)
    frame.configure(bg="lightblue")
    show_home(frame)
    frame.pack(expand=True, fill="both")
    root.mainloop()

main()