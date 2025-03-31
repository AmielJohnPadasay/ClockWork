import sys
from PySide6.QtWidgets import QApplication, QWidget, QStackedWidget, QComboBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, Qt

class MainApp:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.loader = QUiLoader()
        self.current_dashboard = None

        # Starting UIs
        self.login_window = self.loader.load("log_in_main.ui", None)
        self.create_account_window = self.loader.load("Create_Login.ui", None)
        self.dashboard_window = self.loader.load("dashboard.ui", None)
        self.dashboard_manager_window = self.loader.load("dashboard_manager.ui", None)
        self.dashboard_employee_window = self.loader.load("dashboard_employee.ui", None)

        # Dialogs
        self.add_member_window = self.loader.load("add_member.ui", None)
        self.add_member_window.setWindowModality(Qt.ApplicationModal)
        
        self.add_reminder_window = self.loader.load("add_reminder.ui", None)
        self.add_reminder_window.setWindowModality(Qt.ApplicationModal)
        
        self.assign_task_window = self.loader.load("assign_task.ui", None)
        self.assign_task_window.setWindowModality(Qt.ApplicationModal)
        
        self.create_group_window = self.loader.load("create_group.ui", None)
        self.create_group_window.setWindowModality(Qt.ApplicationModal)
        
        self.join_group_window = self.loader.load("join_group.ui", None)
        self.join_group_window.setWindowModality(Qt.ApplicationModal)
        
        self.group_members_window = self.loader.load("group_members.ui", None)
        self.group_members_window.setWindowModality(Qt.ApplicationModal)
        
        self.remove_member_window = self.loader.load("remove_member.ui", None)
        self.remove_member_window.setWindowModality(Qt.ApplicationModal)
        
        self.submit_task_window = self.loader.load("submit_task.ui", None)
        self.submit_task_window.setWindowModality(Qt.ApplicationModal)
        
        self.validate_task_window = self.loader.load("validate_task.ui", None)
        self.validate_task_window.setWindowModality(Qt.ApplicationModal)

        self.profile_window = self.loader.load("profile.ui", None)
        self.profile_window.setWindowModality(Qt.ApplicationModal)

        self.edit_profile_window = self.loader.load("edit_profile.ui", None)
        self.edit_profile_window.setWindowModality(Qt.ApplicationModal)

        self.select_role_window = self.loader.load("select_role.ui", None)
        self.select_role_window.setWindowModality(Qt.ApplicationModal)

        self.supervisor_fingerprint_window = self.loader.load("supervisor_fingerprint.ui", None)
        self.supervisor_fingerprint_window.setWindowModality(Qt.ApplicationModal)

        # Connection of Buttons
        # Log-In Page
        self.role_combo_box = self.create_account_window.findChild(QComboBox, "role_combo_box")

        self.change_into_log_in_button = self.create_account_window.findChild(QWidget, "change_into_log_in_button")
        if self.change_into_log_in_button:
            self.change_into_log_in_button.clicked.connect(self.show_login)

        self.change_into_change_account_button = self.login_window.findChild(QWidget, "create_account_log_in_button_2")
        if self.change_into_change_account_button:
            self.change_into_change_account_button.clicked.connect(self.create_account)

        self.create_account_button = self.create_account_window.findChild(QWidget, "create_account_button")
        if self.create_account_button:
            self.create_account_button.clicked.connect(self.show_login) # To be changed to create account function

        self.login_button = self.login_window.findChild(QWidget, "log_in_button")
        if self.login_button:
            self.login_button.clicked.connect(self.load_dashboard)
        
        self.log_out_button = self.dashboard_window.findChild(QWidget, "log_out_btn")
        if self.log_out_button:
            self.log_out_button.clicked.connect(self.log_out)

    def load_dashboard(self):
        self.role = self.role_combo_box.currentText()

        # Map roles to UI files
        dashboard_files = {
            "Supervisor": "dashboard.ui",
            "Manager": "dashboard_manager_new.ui",
            "Employee": "dashboard_employee_new.ui"
        }

        ui_file_path = dashboard_files.get(self.role)

        if ui_file_path:
            self.open_dashboard(ui_file_path)

    def open_dashboard(self, ui_file_path):
        # Load and display the correct dashboard
        self.loader = QUiLoader()
        ui_file = QFile(ui_file_path)
        if ui_file.open(QFile.ReadOnly):
            self.current_dashboard = self.loader.load(ui_file, None)  # Store the dashboard instance
            self.current_dashboard.show()
            self.login_window.hide()
            ui_file.close()
            if self.role == "Supervisor":
                self.setup_supervisor_dashboard()
            elif self.role == "Manager":
                self.setup_manager_dashboard()
            elif self.role == "Employee":
                self.setup_employee_dashboard()

    #Supervisor's Menu
    def setup_supervisor_dashboard(self):
        self.log_out_button = self.current_dashboard.findChild(QWidget, "log_out_btn")
        if self.log_out_button:
            self.log_out_button.clicked.connect(self.log_out)

        self.stacked_supervisor = self.current_dashboard.findChild(QStackedWidget, "stacked_Supervisor")
        self.dashboard_btn = self.current_dashboard.findChild(QWidget, "dashboard_btn")
        if self.dashboard_btn:
            self.dashboard_btn.clicked.connect(lambda: self.stacked_supervisor.setCurrentIndex(0))
            
        self.activity_log_btn = self.current_dashboard.findChild(QWidget, "activity_log_btn")
        if self.activity_log_btn:
            self.activity_log_btn.clicked.connect(lambda: self.stacked_supervisor.setCurrentIndex(1))
            
        self.calendar_btn = self.current_dashboard.findChild(QWidget, "calendar_btn")
        if self.calendar_btn:
            self.calendar_btn.clicked.connect(lambda: self.stacked_supervisor.setCurrentIndex(2))

        self.add_reminder_button = self.current_dashboard.findChild(QWidget, "add_reminder_button")
        if self.add_reminder_button:
            self.add_reminder_button.clicked.connect(self.show_add_reminder)
            
        self.group_btn = self.current_dashboard.findChild(QWidget, "groups_btn")
        if self.group_btn:
            self.group_btn.clicked.connect(lambda: self.stacked_supervisor.setCurrentIndex(3))

        self.user_roles_btn = self.current_dashboard.findChild(QWidget, "user_roles_btn")
        if self.user_roles_btn:
            self.user_roles_btn.clicked.connect(lambda: self.stacked_supervisor.setCurrentIndex(4))

        self.change_role_btn = self.current_dashboard.findChild(QWidget, "change_role_btn")
        if self.change_role_btn:
            self.change_role_btn.clicked.connect(self.show_select_role)

        self.group_members_btn = self.current_dashboard.findChild(QWidget, "check_group_members_button")
        if self.group_members_btn:
            self.group_members_btn.clicked.connect(self.show_group_members)

        self.create_group_btn = self.current_dashboard.findChild(QWidget, "create_group_button")
        if self.create_group_btn:
            self.create_group_btn.clicked.connect(self.create_group)

        self.validate_btn = self.current_dashboard.findChild(QWidget, "validatetask_btn")
        if self.validate_btn:
            self.validate_btn.clicked.connect(self.validate_task)

        self.profile_btn = self.current_dashboard.findChild(QWidget, "profile_button")
        if self.profile_btn:
            self.profile_btn.clicked.connect(self.show_profile)

    def show_add_reminder(self):
        self.add_reminder_window.show()

    def show_group_members(self):
        self.group_members_window.show()
        
        self.add_member_btn = self.group_members_window.findChild(QWidget, "add_member_btn")
        if self.add_member_btn:
            self.add_member_btn.clicked.connect(self.add_member)

    def add_member(self):
        self.add_member_window.show()

    def create_group(self):
        self.create_group_window.show()

    def validate_task(self):
        self.validate_task_window.show()

    def show_profile(self):
        self.profile_window.show()

        self.edit_profile_btn = self.profile_window.findChild(QWidget, "edit_profile_btn")
        if self.edit_profile_btn:
            self.edit_profile_btn.clicked.connect(self.show_edit_profile)

    def show_edit_profile(self):
        self.edit_profile_window.show()

    def show_select_role(self):
        self.select_role_window.show()

    #Manager's Menu
    def setup_manager_dashboard(self):
        self.log_out_button = self.current_dashboard.findChild(QWidget, "log_out_btn")
        if self.log_out_button:
            self.log_out_button.clicked.connect(self.log_out)

        self.stacked_Manager = self.current_dashboard.findChild(QStackedWidget, "stacked_Manager")

        self.dashboard_btn_manager = self.current_dashboard.findChild(QWidget, "dashboard_btn")
        if self.dashboard_btn_manager:
            self.dashboard_btn_manager.clicked.connect(lambda: self.stacked_Manager.setCurrentIndex(0))
            
        self.activity_log_btn_manager = self.current_dashboard.findChild(QWidget, "activity_log_btn")
        if self.activity_log_btn_manager:
            self.activity_log_btn_manager.clicked.connect(lambda: self.stacked_Manager.setCurrentIndex(1))
            
        self.calendar_btn_manager = self.current_dashboard.findChild(QWidget, "calendar_btn")
        if self.calendar_btn_manager:
            self.calendar_btn_manager.clicked.connect(lambda: self.stacked_Manager.setCurrentIndex(2))
        
        self.group_btn_manager = self.current_dashboard.findChild(QWidget, "groups_btn")
        if self.group_btn_manager:
            self.group_btn_manager.clicked.connect(lambda: self.stacked_Manager.setCurrentIndex(3))

        self.assign_task_button = self.current_dashboard.findChild(QWidget, "assigntask_btn")
        if self.assign_task_button:
            self.assign_task_button.clicked.connect(self.show_assign_task)

        self.add_reminder_button = self.current_dashboard.findChild(QWidget, "add_reminder_button")
        if self.add_reminder_button:
            self.add_reminder_button.clicked.connect(self.show_add_reminder)

        self.group_members_btn = self.current_dashboard.findChild(QWidget, "check_group_members_button")
        if self.group_members_btn:
            self.group_members_btn.clicked.connect(self.show_group_members)

        self.profile_btn = self.current_dashboard.findChild(QWidget, "profile_button")
        if self.profile_btn:
            self.profile_btn.clicked.connect(self.show_profile)

    def show_assign_task(self):
        self.assign_task_window.show()

    def setup_employee_dashboard(self):
        self.log_out_button = self.current_dashboard.findChild(QWidget, "log_out_btn")
        if self.log_out_button:
            self.log_out_button.clicked.connect(self.log_out)

        self.stacked_Employee = self.current_dashboard.findChild(QStackedWidget, "stacked_Employee")

        self.dashboard_btn_employee = self.current_dashboard.findChild(QWidget, "dashboard_btn")
        if self.dashboard_btn_employee:
            self.dashboard_btn_employee.clicked.connect(lambda: self.stacked_Employee.setCurrentIndex(0))

        self.calendar_btn_employee = self.current_dashboard.findChild(QWidget, "calendar_btn")
        if self.calendar_btn_employee:
            self.calendar_btn_employee.clicked.connect(lambda: self.stacked_Employee.setCurrentIndex(1))

        self.group_btn_employee = self.current_dashboard.findChild(QWidget, "group_btn")
        if self.group_btn_employee:
            self.group_btn_employee.clicked.connect(lambda: self.stacked_Employee.setCurrentIndex(2))

        self.add_reminder_button = self.current_dashboard.findChild(QWidget, "add_reminder_button")
        if self.add_reminder_button:
            self.add_reminder_button.clicked.connect(self.show_add_reminder)

        self.submit_task_button = self.current_dashboard.findChild(QWidget, "submit_task_btn")
        if self.submit_task_button:
            self.submit_task_button.clicked.connect(self.show_submit_task)
        
        self.join_group_button = self.current_dashboard.findChild(QWidget, "join_group_button")
        if self.join_group_button:
            self.join_group_button.clicked.connect(self.show_join_group)
        
        self.group_members_btn = self.current_dashboard.findChild(QWidget, "check_group_members_button")
        if self.group_members_btn:
            self.group_members_btn.clicked.connect(self.show_group_members)

        self.profile_btn = self.current_dashboard.findChild(QWidget, "profile_button")
        if self.profile_btn:
            self.profile_btn.clicked.connect(self.show_profile)

    def show_submit_task(self):
        self.submit_task_window.show()

    def show_join_group(self):
        self.join_group_window.show()

    def create_account(self):
        self.create_account_window.show()
        self.login_window.hide()

    def show_login(self):
        self.login_window.show()
        self.create_account_window.hide()
    
    def log_out(self):
        self.login_window.show()
        self.current_dashboard.hide()

    def run(self):
        self.login_window.show()
        sys.exit(self.app.exec())

if __name__ == "__main__":
    main_app = MainApp()
    main_app.run()