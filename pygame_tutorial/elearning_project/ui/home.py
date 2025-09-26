import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ui.lesson_selector import show_lessons
from data.lesson_data import lessons
import unicodedata

def normalize_text(text):
     text = unicodedata.normalize("NFC", text)
     text = text.replace("ی", "ي").replace("ك", "ک")
     return text.strip()



def show_home(frame, on_select_lesson, on_back, on_home):
    for widget in frame.winfo_children():
        widget.destroy()

    ttk.Label(frame, text="لطفا یک درس را انتخاب کنید",
             style="TLabel").pack(pady=10)
    search_var = tk.StringVar()
    ttk.Entry(frame, textvariable=search_var, justify="right").pack(pady=5)

    def search():
        query = search_var.get().strip()
        for widget in frame.winfo_children():
                print(widget.cget("text"))
                if isinstance(widget, ttk.Button):
                        widget.destroy()
       
        results = []

        for subject, chapters in lessons.items():
             if query in normalize_text(subject):
                  results.append(subject)
             for chapter in chapters:
                  if query in  normalize_text(chapter):
                       results.append(subject)
        results = list(set(results))

        if results:
             for subject in results:
                  ttk.Button(frame, text=subject,
                   width=20,
                   bootstyle=(INFO, OUTLINE),
                   command = lambda s= subject:show_lessons(frame, s, on_select_lesson, \
                                                            on_back, on_home)
                   ).pack(pady=5)
        else:
             ttk.Label(frame, text="موضوعی یافت نشد").pack(pady=5)
                  
        ttk.Button(frame, text="بازگشت",bootstyle=(INFO, OUTLINE), width=20,
                command=lambda : show_lessons(frame, subject, None, on_back, on_home)).pack(pady=10)
    ttk.Button(frame, text="جستجو", command=search).pack(pady=5)


    subjects = lessons.keys()
    for subject in subjects:
        ttk.Button(frame, text=subject,
                   width=20,
                   bootstyle=(INFO, OUTLINE),
                   command = lambda s= subject:show_lessons(frame, s, on_select_lesson, \
                                                            on_back, on_home)
                   ).pack(pady=5)
        
     

    