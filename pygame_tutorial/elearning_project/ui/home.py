import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ui.lesson_selector import show_lessons, show_chapter_content
from data.lesson_data import lessons
import unicodedata
from .dashboard import show_dashboard
from ui.score_manager import load_scores
from ui.theme_manager import (
    style_frame,
    style_label,
    style_button,
    set_theme,
    get_theme_name,
)
from ui.admin_panel import show_admin_panel
import json
from ui.progress_chart import show_progress_chart


def normalize_text(text):
    text = unicodedata.normalize("NFC", text)
    text = text.replace("ی", "ي").replace("ك", "ک")
    return text.strip()


def show_home(frame, username, on_select_lesson, on_back, on_home):
    for widget in frame.winfo_children():
        widget.destroy()
    style_frame(frame)

    def toggle_theme():
        name = get_theme_name()
        if name == "light":
            set_theme("dark")
        elif name == "dark":
            set_theme("light")
        show_home(
            frame,
            username,
            on_select_lesson,
            lambda: on_back(username),
            lambda: on_home(username),
        )

    theme_btn = ttk.Button(
        frame,
        text="تغییر تم",
        width=20,
        bootstyle=(INFO, OUTLINE),
        command=toggle_theme,
    )
    theme_btn.pack(pady=5)
    title = ttk.Label(frame, text="لطفا یک درس را انتخاب کنید", style="TLabel")
    title.pack(pady=10)
    style_label(title)
    search_var = tk.StringVar()
    ttk.Entry(frame, textvariable=search_var, justify="right").pack(pady=5)
    filter_var = tk.StringVar(value="درس")
    option_menu = ttk.OptionMenu(frame, filter_var, "درس", "فصل", "درس")
    option_menu.config(style="My.TMenubutton")
    menu = option_menu["menu"]
    menu.config(font=("B Nazanin", 13, "bold"))
    option_menu.pack(pady=5)

    def search():
        for widget in frame.winfo_children():
            if isinstance(widget, ttk.Label):
                widget.destroy()
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
                    if query in normalize_text(chapter):
                        results.append((subject, chapter))
        results = list(set(results))
        if results:
            for item in results:
                if isinstance(item, str):
                    ttk.Button(
                        frame,
                        text=item,
                        width=20,
                        bootstyle=(INFO, OUTLINE),
                        command=lambda s=item: show_lessons(
                            frame, username, s, on_select_lesson, on_back, on_home
                        ),
                    ).pack(pady=5)
                else:
                    subject, chapter = item
                    ttk.Button(
                        frame,
                        text=f"{chapter} ({subject})",
                        width=20,
                        bootstyle=(INFO, OUTLINE),
                        command=lambda s=subject, c=chapter: show_chapter_content(
                            frame, username, s, c, on_back, on_home
                        ),
                    ).pack(pady=5)

        else:

            ttk.Label(frame, text="موضوعی یافت نشد").pack(pady=5)

            ttk.Button(frame, text="جستجو", command=search).pack(pady=5)
            ttk.Button(
                frame, text="خانه", bootstyle=(INFO, OUTLINE), width=20, command=on_home
            ).pack(pady=10)

    ttk.Button(frame, text="جستجو", command=search).pack(pady=5)

    subjects = lessons.keys()
    for subject in subjects:
        ttk.Button(
            frame,
            text=subject,
            width=20,
            bootstyle=(INFO, OUTLINE),
            command=lambda s=subject: show_lessons(
                frame, username, s, on_select_lesson, on_back, on_home
            ),
        ).pack(pady=5)

    ttk.Button(
        frame,
        text="داشبورد پیشرفت",
        bootstyle=(INFO, OUTLINE),
        command=lambda: show_dashboard(frame, username, on_back),
    ).pack(pady=5)
    ttk.Button(
        frame,
        text="نمودار پیشرفت",
        bootstyle=(INFO, OUTLINE),
        command=lambda: show_progress_chart(frame, username, on_back),
    ).pack(pady=5)
    with open("data/users.json", "r", encoding="utf-8") as f:

        is_admin = json.load(f)
    if is_admin[username]["is_admin"]:

        ttk.Button(
            frame,
            text="مدیریت محتوا",
            bootstyle=(INFO, OUTLINE),
            command=lambda: show_admin_panel(frame),
        ).pack(pady=5)
