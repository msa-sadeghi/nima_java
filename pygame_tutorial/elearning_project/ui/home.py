import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ui.lesson_selector import show_lessons, show_chapter_content
from data.lesson_data import lessons
import unicodedata
from .dashboard import show_dashboard

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
    filter_var = tk.StringVar(value='درس')
    option_menu = ttk.OptionMenu(frame, filter_var,"درس", "فصل", "درس")
    option_menu.config(style='My.TMenubutton')
    menu = option_menu["menu"]
    menu.config(font=("B Nazanin", 13, "bold"))
    option_menu.pack(pady=5)
    def search():
        query = search_var.get().strip()
        filter_type = filter_var.get()
        for widget in frame.winfo_children():
                if isinstance(widget, ttk.Button):
                        widget.destroy()
        results = []
        if filter_type == normalize_text("درس"):
             for subject in lessons:
                  if query in normalize_text(subject):
                       results.append(subject)
        elif filter_type == "فصل":     
          for subject, chapters in lessons.items():
               for chapter in chapters:
                    if query in  normalize_text(chapter):
                         results.append((subject, chapter))
        results = list(set(results))
        if results:
             for item in results:
                  if isinstance(item, str):
                         ttk.Button(frame, text=item,
                         width=20,
                         bootstyle=(INFO, OUTLINE),
                         command = lambda s= item:show_lessons(frame, s, on_select_lesson, \
                                                                      on_back, on_home)
                         ).pack(pady=5)
                  else:
                       subject, chapter = item
                       ttk.Button(frame, text=f"{chapter} ({subject})",
                       width=20,
                       bootstyle=(INFO, OUTLINE),
                       command = lambda s= subject, c= chapter:show_chapter_content(frame, s, c, \
                                                                    on_back, on_home)
                       ).pack(pady=5)

        else:
             ttk.Label(frame, text="موضوعی یافت نشد").pack(pady=5)
                  
     #    ttk.Button(frame, text="بازگشت",bootstyle=(INFO, OUTLINE), width=20,
     #            command=lambda : show_lessons(frame, subject, None, on_back, on_home)).pack(pady=10)
             ttk.Button(frame, text="خانه",bootstyle=(INFO, OUTLINE), width=20,
                command=on_home).pack(pady=10)
    ttk.Button(frame, text="جستجو", command=search).pack(pady=5)


    subjects = lessons.keys()
    for subject in subjects:
        ttk.Button(frame, text=subject,
                   width=20,
                   bootstyle=(INFO, OUTLINE),
                   command = lambda s= subject:show_lessons(frame, s, on_select_lesson, \
                                                            on_back, on_home)
                   ).pack(pady=5)
        

    ttk.Button(frame, text="داشبورد پیشرفت",bootstyle=(INFO, OUTLINE),
                   command = lambda : show_dashboard(frame, lambda :  show_home(frame, on_select_lesson, \
                                                                                 on_back, on_home))).pack(pady=5)
        
     

    