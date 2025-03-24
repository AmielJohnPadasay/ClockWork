from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from PySide6.QtUiTools import QUiLoader
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()

        # Load the main login window
        self.login_window = loader.load("log_in_main.ui", self)
        self.setCentralWidget(self.login_window)

        # Load the create login window
        self.create_login_window = loader.load("Create_Login.ui", self)

        # Find the button to switch to the create login window
        self.switch_button = self.login_window.findChild(QPushButton, "pushButton")
        if self.switch_button:
            self.switch_button.clicked.connect(self.show_create_login)

    def show_create_login(self):
        self.create_login_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())