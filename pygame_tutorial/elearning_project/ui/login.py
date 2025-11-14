import ttkbootstrap as ttk
from tkinter import messagebox
from .user_manager import add_user, check_user

def show_login(frame, on_login):
    for widget in frame.winfo_children():
        widget.destroy()

    ttk.Label(frame, text="نام کاربری",
             style="TLabel").pack(pady=10)
    username_var = ttk.StringVar()
    ttk.Entry(frame, textvariable=username_var,
             style="TEntry").pack(pady=10)
    ttk.Label(frame, text="کلمه عبور",
             style="TLabel").pack(pady=10)
    password_var = ttk.StringVar()
    ttk.Entry(frame, textvariable=password_var,
             style="TEntry").pack(pady=10)
    
    def login_user():
        username = username_var.get()
        password = password_var.get()
        if check_user(username, password):
            on_login(username)
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
