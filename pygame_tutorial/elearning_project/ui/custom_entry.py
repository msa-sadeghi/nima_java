import ttkbootstrap as ttk
from tkinter import Listbox, END


class AutocompleteEntry(ttk.Entry):
    def __init__(self, parent, autocomplete_list, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.autocomplete_list = autocomplete_list
        self.filtered = []
        self.listbox = None
        self.bind("<KeyRelease>", self.on_keyrelease)
        self.bind("<Escape>", self.hide_listbox)
        # self.bind("<Down>", self.move_down)

    def on_keyrelease(self, event):
        if event.keysym in ("Up", "Down", "Return", "Escape"):
            return
        value = self.get()
        if not value:
            self.hide_listbox()
            return

        self.filtered = [
            item
            for item in self.autocomplete_list
            if item.lower().startswith(value.lower())
        ]
        self.show_listbox()

    def show_listbox(self):
        if not self.listbox:
            self.listbox = Listbox(self.parent, height=5, activestyle="none")
        self.listbox.delete(0, END)
        for item in self.filtered:
            self.listbox.insert(END, item)
        x = self.winfo_x()
        y = self.winfo_y() + self.winfo_height()
        self.listbox.place(x=x, y=y, w=self.winfo_width())

    def hide_listbox(self, event=None):
        if self.listbox:
            self.listbox.destroy()
            self.listbox = None

    def update_list(self, new_list):
        self.autocomplete_list = new_list
