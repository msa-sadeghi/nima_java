import tkinter as tk
from tkinter import filedialog, messagebox
import ttkbootstrap as ttk
import json
from data.lesson_data import lessons


def show_admin_panel(frame):
    for widget in frame.winfo_children():
        widget.destroy()

    ttk.Label(frame, text="پنل مدیریت محتوا").pack(pady=10)

    ttk.Label(frame, text="درس جدید").pack(pady=5)
    subject_var = ttk.StringVar()
    ttk.Entry(frame, textvariable=subject_var, justify="right").pack(pady=5)

    ttk.Label(frame, text="فصل جدید").pack(pady=5)
    chapter_var = ttk.StringVar()
    ttk.Entry(frame, textvariable=chapter_var, justify="right").pack(pady=5)

    ttk.Text(frame, text="متن توضیحی").pack(pady=5)
    context_text = ttk.Text(frame, height=5, width=40)
    context_text.pack(pady=5)

    video_path_var = ttk.StringVar()

    def select_video():
        path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4;*.avi")])
        if path:
            video_path_var.set(path)

    ttk.Button(
        frame, text="انتخاب ویدئو", command=select_video
    ).pack(pady=5)

    pdf_path_var = ttk.StringVar()
    def select_pdf():
        path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if path:
            pdf_path_var.set(path)

    ttk.Button(
        frame, text="انتخاب PDF", command=select_pdf
    ).pack(pady=5)


    def save_content():
        subject = subject_var.get().strip()
        chapter = chapter_var.get().strip()
        content = context_text.get()
        video = video_path_var.get()
        pdf = pdf_path_var.get()

        if not subject or not chapter:
            messagebox.showerror("خطا","نام درس و فصل الزامی است")
            return
        
        if subject not in lessons:
            lessons[subject] = {}
        lessons[subject][chapter] =  {
            "content": content,
            "video" : video,
            "pdf" : pdf
        }
        with open("data/lesson_data.py", "w", encoding="utf-8") as f:
            f.write("lessons = " + json.dumps(lessons))

        messagebox.showinfo("موفقیت", f"فصل{chapter} به درس {subject} اضافه شد")

    

    ttk.Button(
        frame, text="ذخیره محتوا", command=save_content
    ).pack(pady=5)