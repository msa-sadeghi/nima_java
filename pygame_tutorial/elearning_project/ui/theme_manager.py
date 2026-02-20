THEMES = {
    "light": {
        "bg": "lightblue",
        "fg": "black",
        "button_bg": "white",
        "button_fg": "purple",
    },
    "dark": {
        "bg": "#2c3e50",
        "fg": "white",
        "button_bg": "#34495e",
        "button_fg": "#ecf0f1",
    },
}
current_theme = "light"


def get_theme():
    return THEMES[current_theme]


def get_theme_name():
    return current_theme


def style_frame(frame):
    t = get_theme()
    frame.configure(bg=t["bg"])


def style_label(widget):
    t = get_theme()
    widget.configure(background=t["bg"], foreground=t["fg"])


def style_button(widget):
    t = get_theme()
    widget.configure(
        background=t["button_bg"],
        foreground=t["button_fg"],
        activebackground=t["button_bg"],
        activeforeground=t["button_fg"],
    )


def set_theme(theme_name):
    global current_theme
    if theme_name in THEMES:
        current_theme = theme_name
