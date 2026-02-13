THEMES =  {
    "light":{
        "bg":"lightblue",
        "fg":'black',
        'button_bg':'white',
        'button_fg':'purple',
    },
    "dark":{
        "bg":"#2c3e50",
        "fg":'white',
        'button_bg':'#34495e',
        'button_fg':'#ecf0f1',
    }
}
current_theme = "light"
def get_theme():
    return THEMES[current_theme]
def set_theme(theme_name):
    global current_theme
    if theme_name in THEMES:
        current_theme = theme_name