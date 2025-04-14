# modular_main_app.py (extended)

import sys
import datetime
from PySide6.QtWidgets import (QApplication, QWidget, QStackedWidget, QLineEdit, QComboBox, QDateEdit,
                               QRadioButton, QMessageBox, QTableWidget, QTableWidgetItem, QTextEdit, QTimeEdit)
from PySide6.QtCore import QFile, Qt
from PySide6.QtUiTools import QUiLoader

# --- Data Container Class ---
class UserData:
    email = ["a@gmail.com", "b@yahoo.com"]
    password = ["22222222", "33333333"]
    first_name = ["Amiel", "John"]
    last_name = ["Padasay", "Doe"]
    middle_initial = ["R.", "D."]
    suffix = ["", ""]
    birthdate = ["2004-09-18", "2005-09-18"]
    sex = ["Male", "Male"]
    role = ["Supervisor", "Manager"]

    task_name = []
    task_requirement = []
    task_description = []
    task_priority_level = []
    task_due_date = []
    task_due_time = []
    task_assigned_to = []
    task_status = []


# --- Login and Account Creation ---
class LoginManager:
    def __init__(self, main_app):
        self.main = main_app
        self.login_window = self.main.loader.load("log_in_main.ui")
        self.create_account_window = self.main.loader.load("Create_Login.ui")
        self.register_fingerprint_window = self.main.loader.load("register_fingerprint.ui")
        self.setup_login_ui()

    def setup_login_ui(self):
        self.login_window.show()
        self.log_in_stacked = self.login_window.findChild(QStackedWidget, "log_in_stacked")
        self.log_in_stacked.setCurrentIndex(1)

        self.email_input = self.login_window.findChild(QLineEdit, "email_lineEdit")
        self.password_input = self.login_window.findChild(QLineEdit, "password_lineEdit")
        self.password_input.setEchoMode(QLineEdit.Password)

        credentials_btn = self.login_window.findChild(QWidget, "log_in_credentials_btn")
        if credentials_btn:
            credentials_btn.clicked.connect(lambda: self.log_in_stacked.setCurrentIndex(0))

        fingerprint_btn = self.login_window.findChild(QWidget, "log_in_fingerprint_btn")
        if fingerprint_btn:
            fingerprint_btn.clicked.connect(lambda: self.log_in_stacked.setCurrentIndex(1))

        login_btn = self.login_window.findChild(QWidget, "log_in_button")
        if login_btn:
            login_btn.clicked.connect(self.login)

        switch_btn = self.login_window.findChild(QWidget, "create_account_log_in_button_2")
        if switch_btn:
            switch_btn.clicked.connect(self.show_create_account)

    def login(self):
        email = self.email_input.text()
        password = self.password_input.text()

        if email in UserData.email:
            index = UserData.email.index(email)
            if password == UserData.password[index]:
                role = UserData.role[index]
                self.main.load_dashboard(role)
                self.login_window.hide()
                return

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Login Failed")
        msg.setText("Invalid email or password.")
        msg.exec()

    def show_create_account(self):
        self.login_window.hide()
        self.create_account_window.show()
        # Hook up validation button later


# --- Dashboard Manager ---
class DashboardManager:
    def __init__(self, main_app):
        self.main = main_app

    def load_dashboard(self, role):
        file_map = {
            "Supervisor": "dashboard_updated.ui",
            "Manager": "dashboard_manager_updated.ui",
            "Employee": "dashboard_employee_new.ui"
        }
        ui_file = QFile(file_map[role])
        if ui_file.open(QFile.ReadOnly):
            dashboard_ui = self.main.loader.load(ui_file, None)
            self.main.current_dashboard = dashboard_ui
            dashboard_ui.show()
            ui_file.close()

            if role == "Supervisor":
                SupervisorDashboard(self.main, dashboard_ui)
            elif role == "Manager":
                ManagerDashboard(self.main, dashboard_ui)
            elif role == "Employee":
                EmployeeDashboard(self.main, dashboard_ui)


# --- Supervisor Dashboard ---
class SupervisorDashboard:
    def __init__(self, main, dashboard):
        self.main = main
        self.dashboard = dashboard
        self.user_table = self.dashboard.findChild(QTableWidget, "users_table")
        self.populate_users()

    def populate_users(self):
        self.user_table.setColumnCount(3)
        self.user_table.setHorizontalHeaderLabels(["Name", "Email", "Role"])
        self.user_table.setRowCount(len(UserData.email))
        for i in range(len(UserData.email)):
            self.user_table.setItem(i, 0, QTableWidgetItem(f"{UserData.first_name[i]} {UserData.last_name[i]}"))
            self.user_table.setItem(i, 1, QTableWidgetItem(UserData.email[i]))
            self.user_table.setItem(i, 2, QTableWidgetItem(UserData.role[i]))


# --- Manager Dashboard ---
class ManagerDashboard:
    def __init__(self, main, dashboard):
        self.main = main
        self.dashboard = dashboard
        # Hook Manager-specific logic here


# --- Employee Dashboard ---
class EmployeeDashboard:
    def __init__(self, main, dashboard):
        self.main = main
        self.dashboard = dashboard
        # Hook Employee-specific logic here


# --- Main App Class ---
class MainApp:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.loader = QUiLoader()
        self.current_dashboard = None

        self.login_manager = LoginManager(self)
        self.dashboard_manager = DashboardManager(self)

    def load_dashboard(self, role):
        self.dashboard_manager.load_dashboard(role)

    def run(self):
        self.login_manager.login_window.show()
        sys.exit(self.app.exec())


if __name__ == "__main__":
    MainApp().run()
