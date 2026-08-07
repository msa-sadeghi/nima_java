import sys
from PySide6.QtWidgets import QWidget, QApplication,QLabel,QLineEdit, QPushButton, QHBoxLayout , \
QMainWindow, QVBoxLayout, QGridLayout, QFormLayout
from PySide6.QtGui import Qt
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

        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.login_button = QPushButton("ورود")
        self.login_button.clicked.connect(self.handle_click)
        form_layout = QFormLayout()
        form_layout.addRow("نام کاربری", self.username_input)
        form_layout.addRow("کلمه عبور", self.password_input)
        main_layout = QVBoxLayout()
        main_layout.addWidget(title_label)
        main_layout.addLayout(form_layout)
        main_layout.addWidget(self.login_button)
        container = QWidget()
        container.setLayout(main_layout)


        self.setCentralWidget(container)


        
       
    def handle_click(self):
        print("hello")

def main():
    app = QApplication(sys.argv)
    app.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
