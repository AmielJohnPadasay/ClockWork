import sys
from PySide6.QtWidgets import QApplication, QWidget, QCalendarWidget, QVBoxLayout, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QDate

class CalendarApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Double-Click Calendar")

        # Load Dashboard UI
        loader = QUiLoader()
        self.dashboard = loader.load("dashboard.ui")

        # Calendar Setup
        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)
        self.calendar.clicked.connect(self.on_day_clicked)

        layout = QVBoxLayout()
        layout.addWidget(self.calendar)
        self.setLayout(layout)

        self.last_click_date = None

    def on_day_clicked(self, date):
        if self.last_click_date == date:
            self.open_task_window()
        else:
            self.last_click_date = date

    def open_task_window(self):
        loader = QUiLoader()
        self.task_window = loader.load("Task-Window.ui")
        self.task_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalendarApp()
    window.show()
    sys.exit(app.exec())
