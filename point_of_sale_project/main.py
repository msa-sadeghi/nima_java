import sys
from PySide6.QtWidgets import QWidget, QApplication,QLabel,QLineEdit, QPushButton, QHBoxLayout , \
QMainWindow, QVBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(480, 320)
        self.setWindowTitle("سیستم صندوق فروش")
        title_label = QLabel("ورود به سیستم صندوق فروش")
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("نام کاربری")
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("کلمه عبور")
        self.login_button = QPushButton("ورود")
        main_layout = QHBoxLayout()
        main_layout.addWidget(title_label)
        main_layout.addWidget(self.username_input)
        main_layout.addWidget(self.password_input)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)


        
       


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
