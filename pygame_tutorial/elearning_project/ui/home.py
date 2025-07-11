import tkinter as tk

def show_home(frame):

    tk.Label(frame, text="لطفا یک درس را انتخاب کنید", 
             bg= "lightblue",
             fg= "purple",
             font=("ZahraRoosta", 14)).pack()

    subjects = ["فیزیک", "شیمی", "زیست",  "ریاضی"]
    for subject in subjects:
        tk.Button(frame, text=subject,
                   width=20,
                   font=("ZahraRoosta", 12),
                #    command=
                   ).pack(pady=5)