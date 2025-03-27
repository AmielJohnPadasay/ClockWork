from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QCalendarWidget, QLineEdit, QPushButton, QListWidget
from PySide6.QtGui import QTextCharFormat, QColor
from PySide6.QtCore import QDate

class TaskCalendar(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the UI layout
        self.setWindowTitle("Task Calendar")
        layout = QVBoxLayout()

        # Calendar widget
        self.calendar = QCalendarWidget()
        layout.addWidget(self.calendar)

        # Task input field
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Enter task")
        layout.addWidget(self.task_input)

        # Add task button
        self.add_button = QPushButton("Add Task")
        layout.addWidget(self.add_button)

        # Task list widget
        self.task_list = QListWidget()
        layout.addWidget(self.task_list)

        # Delete task button
        self.delete_button = QPushButton("Delete Task")
        layout.addWidget(self.delete_button)

        self.setLayout(layout)

        # Store tasks with due dates
        self.tasks = {}

        # Connect buttons to functions
        self.add_button.clicked.connect(self.add_task)
        self.delete_button.clicked.connect(self.delete_task)

        # Update task list when calendar date changes
        self.calendar.selectionChanged.connect(self.update_task_list)

    def add_task(self):
        task_name = self.task_input.text()
        due_date = self.calendar.selectedDate()

        if task_name:
            # Save the task
            if due_date not in self.tasks:
                self.tasks[due_date] = []
            self.tasks[due_date].append(task_name)

            # Update task list and calendar
            self.update_task_list()
            self.mark_date(due_date)

            # Clear the input field
            self.task_input.clear()

    def delete_task(self):
        selected_item = self.task_list.currentItem()
        if selected_item:
            task_info = selected_item.text()
            date_str, task_name = task_info.split(": ", 1)
            due_date = QDate.fromString(date_str, "yyyy-MM-dd")

            # Remove the task
            if due_date in self.tasks and task_name in self.tasks[due_date]:
                self.tasks[due_date].remove(task_name)

                # Clean up if no tasks remain for the date
                if not self.tasks[due_date]:
                    del self.tasks[due_date]
                    self.clear_date_mark(due_date)

                # Update UI
                self.update_task_list()

    def update_task_list(self):
        self.task_list.clear()
        due_date = self.calendar.selectedDate()

        if due_date in self.tasks:
            for task in self.tasks[due_date]:
                self.task_list.addItem(f"{due_date.toString('yyyy-MM-dd')}: {task}")

    def mark_date(self, date):
        # Annotate and highlight the due date
        highlight = QTextCharFormat()
        highlight.setBackground(QColor("lightgreen"))
        highlight.setToolTip("Tasks available")
        self.calendar.setDateTextFormat(date, highlight)

    def clear_date_mark(self, date):
        # Clear the highlight if no tasks remain
        clear_format = QTextCharFormat()
        self.calendar.setDateTextFormat(date, clear_format)

if __name__ == "__main__":
    app = QApplication([])
    window = TaskCalendar()
    window.show()
    app.exec()