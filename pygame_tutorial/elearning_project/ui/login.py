import ttkbootstrap as ttk
from tkinter import messagebox
from .user_manager import add_user, check_user
import os
import json

HISTORY_FILE = "login_history.json"


def load_history():
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return {"usernames": [], "passwords": []}
    return {"usernames": [], "passwords": []}


def save_history(username, password):
    history = load_history()

    if username not in history["usernames"]:
        history["usernames"].insert(0, username)
    else:
        history["usernames"].remove(username)
        history["usernames"].insert(0, username)
    history["passwords"].remove(password)
    history["passwords"].insert(0, password)
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f)


def on_keyrelease(c, history):
    print(c.keysym)
    if not c.widget.get():
        return
    for item in history["usernames"]:
        if item.lower().startswith(c.widget.get().lower()) and c.keysym != "BackSpace":
            c.widget.delete(0, "end")
            c.widget.insert(0, item)
            break


def show_login(frame, on_login):
    for widget in frame.winfo_children():
        widget.destroy()
    history = load_history()
    ttk.Label(frame, text="نام کاربری", style="TLabel").pack(pady=10)
    username_var = ttk.StringVar()
    usernameEntry = ttk.Entry(frame, textvariable=username_var, style="TEntry")
    usernameEntry.pack(pady=10)
    usernameEntry.bind(
        "<KeyRelease>", lambda c=username_var.get(): on_keyrelease(c, history)
    )
    ttk.Label(frame, text="کلمه عبور", style="TLabel").pack(pady=10)
    password_var = ttk.StringVar()
    ttk.Entry(frame, textvariable=password_var, style="TEntry").pack(pady=10)

    def login_user():
        username = username_var.get()
        password = password_var.get()
        if check_user(username, password):
            on_login(username)
            save_history(username, password)
        else:
            messagebox.showerror("خطا", "نام کاربری یا کلمه عبور صحیح نمی باشد")

    def register_user():
        username = username_var.get()
        password = password_var.get()

        if add_user(username, password):
            messagebox.showinfo("ثبت نام موفق", "کاربر با موفقیت ایجاد شد")
        else:
            messagebox.showwarning("ثبت نام ناموفق", "کاربر با موفقیت ایجاد نشد")

    ttk.Button(frame, text="ورود", command=login_user).pack(pady=5)
    ttk.Button(frame, text="ثبت نام", command=register_user).pack(pady=5)
