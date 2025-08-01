import tkinter as tk

def my_function(message):
    output_label.config({'text':message + " "+ my_input.get()})


root = tk.Tk()

my_input = tk.Entry(root)
my_input.pack()
message = "salaam"
my_button = tk.Button(root, text="کلیک کن", command=lambda m = message:my_function(m))
my_button.pack()

output_label = tk.Label(root, text="")
output_label.pack()

root.mainloop()