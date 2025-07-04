import tkinter as tk

def my_function():
    my_label.config({'text': 'چطوری؟'})

root = tk.Tk()
root.geometry("400x300")
my_label = tk.Label(root, text="سلام", font=('arial', 32))
my_label.config({'foreground': 'red', 'background':'green'})
my_label.pack(pady=10)

my_button = tk.Button(root, text="تایید", font=('arial', 32), command=my_function)
my_button.config({'foreground': 'red', 'background':'green'})
my_button.pack()

root.mainloop()