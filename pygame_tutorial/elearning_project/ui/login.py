import ttkbootstrap as ttk
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
        pass
    def register_user():
        pass

    ttk.Button(frame, text="ورود", command=login_user).pack(pady=5)
    ttk.Button(frame, text="ثبت نام", command=register_user).pack(pady=5)
