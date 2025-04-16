import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtUiTools import QUiLoader

class MainApp:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.loader = QUiLoader()

        # UIs
        self.login_window = self.loader.load("Log-In-Page.ui", None)
        self.log_in_part_2_window = self.loader.load("log_in_part_2.ui", None)
        self.dashboard_window = self.loader.load("main_dashboard.ui", None)
        self.create_group_window = self.loader.load("create_group.ui", None)
        self.group_dashboard_window = self.loader.load("dashboard.ui", None)
        self.activity_log_window = self.loader.load("activity_log.ui", None)
        self.group_members_window = self.loader.load("group_members.ui", None)
        self.add_member_window = self.loader.load("add_member.ui", None)
        self.remove_member_window = self.loader.load("remove_member.ui", None)
        self.group_settings_window = self.loader.load("group_settings.ui", None)
        self.task_window = self.loader.load("Task-Window.ui", None)
        self.assign_task_window = self.loader.load("assign_task.ui", None)
        self.remove_task_window = self.loader.load("remove_task.ui", None)
        self.submit_task_window = self.loader.load("submit_task.ui", None)
        self.validate_task_window = self.loader.load("validate_task.ui", None)
        self.supervisor_password_window = self.loader.load("supervisor_password.ui", None)


        #COnnection of buttons

        
        self.login_button = self.login_window.findChild(QWidget, "create_account_log_in_button")
        if self.login_button:
            self.login_button.clicked.connect(self.show_login_part_2)

        self.change_into_log_in_button = self.log_in_part_2_window.findChild(QWidget, "create_account_log_in_button_2")
        if self.change_into_log_in_button:
            self.change_into_log_in_button.clicked.connect(self.show_login)

        self.change_into_log_in_part_2_button = self.login_window.findChild(QWidget, "change_into_log_in_button")
        if self.change_into_log_in_part_2_button:
            self.change_into_log_in_part_2_button.clicked.connect(self.show_login_part_2)

        self.log_in_part_2_window_button = self.log_in_part_2_window.findChild(QWidget, "create_account_log_in_button")
        if self.log_in_part_2_window_button:
            self.log_in_part_2_window_button.clicked.connect(self.show_dashboard)

        self.log_out_button = self.dashboard_window.findChild(QWidget, "pushButton_2")
        if self.log_out_button:
            self.log_out_button.clicked.connect(self.log_out)

        self.create_group_button = self.dashboard_window.findChild(QWidget, "create_group_btn")
        if self.create_group_button:
            self.create_group_button.clicked.connect(self.show_create_group)

        self.cancel_back_to_main_dashboard_button = self.create_group_window.findChild(QWidget, "pushButton")
        if self.cancel_back_to_main_dashboard_button:
            self.cancel_back_to_main_dashboard_button.clicked.connect(self.cancel_back_to_main_dashboard)

        self.access_to_group_dashboard_button = self.create_group_window.findChild(QWidget, "pushButton_2")
        if self.access_to_group_dashboard_button:
            self.access_to_group_dashboard_button.clicked.connect(self.access_to_group_dashboard)

        self.back_to_main_dashboard_button = self.group_dashboard_window.findChild(QWidget, "back_to_main_dashboard_btn")
        if self.back_to_main_dashboard_button:
            self.back_to_main_dashboard_button.clicked.connect(self.back_to_main_dashboard)

        self.access_activity_log_button = self.group_dashboard_window.findChild(QWidget, "activity_log_btn")
        if self.access_activity_log_button:
            self.access_activity_log_button.clicked.connect(self.access_activity_log)

        self.close_activity_log_button = self.activity_log_window.findChild(QWidget, "OK_btn")
        if self.close_activity_log_button:
            self.close_activity_log_button.clicked.connect(self.close_activity_log)

        self.access_group_members_button = self.group_dashboard_window.findChild(QWidget, "group_members_btn")
        if self.access_group_members_button:
            self.access_group_members_button.clicked.connect(self.access_group_members)

        self.add_members_button = self.group_members_window.findChild(QWidget, "add_member_btn")
        if self.add_members_button:
            self.add_members_button.clicked.connect(self.add_member_window.show)

        self.close_add_member_button = self.add_member_window.findChild(QWidget, "cancel_btn")
        if self.close_add_member_button:
            self.close_add_member_button.clicked.connect(self.add_member_window.close)

        self.remove_member_button = self.group_members_window.findChild(QWidget, "remove_member_btn")
        if self.remove_member_button:
            self.remove_member_button.clicked.connect(self.remove_member_window.show)

        self.close_remove_member_button = self.remove_member_window.findChild(QWidget, "cancel_btn")
        if self.close_remove_member_button:
            self.close_remove_member_button.clicked.connect(self.remove_member_window.close)

        self.close_group_members_button = self.group_members_window.findChild(QWidget, "cancel_btn")
        if self.close_group_members_button:
            self.close_group_members_button.clicked.connect(self.close_group_members)

        self.group_settings_button = self.group_dashboard_window.findChild(QWidget, "group_settings_btn")
        if self.group_settings_button:
            self.group_settings_button.clicked.connect(self.group_settings_window.show)

        self.close_group_settings_button = self.group_settings_window.findChild(QWidget, "cancel_btn")
        if self.close_group_settings_button:
            self.close_group_settings_button.clicked.connect(self.group_settings_window.close)

        # Make a calendar's day a button
        self.access_task_window_button = self.group_dashboard_window.findChild(QWidget, "Task_Calendar")
        if self.access_task_window_button:
            self.access_task_window_button.clicked.connect(self.on_day_clicked)
            self.last_click_date = None

        self.assign_task_window_button = self.task_window.findChild(QWidget, "assigntask_btn")
        if self.assign_task_window_button:
            self.assign_task_window_button.clicked.connect(self.assign_task_window.show)

        self.close_assign_task_window_button = self.assign_task_window.findChild(QWidget, "cancel_btn")
        if self.close_assign_task_window_button:
            self.close_assign_task_window_button.clicked.connect(self.assign_task_window.close)

        self.remove_task_window_button = self.task_window.findChild(QWidget, "removetask_btn")
        if self.remove_task_window_button:
            self.remove_task_window_button.clicked.connect(self.remove_task_window.show)

        self.close_remove_task_window_button = self.remove_task_window.findChild(QWidget, "cancel_btn")
        if self.close_remove_task_window_button:
            self.close_remove_task_window_button.clicked.connect(self.remove_task_window.close)

        self.submit_task_window_button = self.task_window.findChild(QWidget, "submit_task_btn")
        if self.submit_task_window_button:
            self.submit_task_window_button.clicked.connect(self.submit_task_window.show)

        self.close_submit_task_window_button = self.submit_task_window.findChild(QWidget, "cancel_btn")
        if self.close_submit_task_window_button:
            self.close_submit_task_window_button.clicked.connect(self.submit_task_window.close)

        self.close_task_window_button = self.task_window.findChild(QWidget, "cancel_btn")
        if self.close_task_window_button:
            self.close_task_window_button.clicked.connect(self.task_window.close)

    def on_day_clicked(self, date):
        if self.last_click_date == date:
            self.show_task_window()
        else:
            self.last_click_date = date

    def show_login(self):
        self.log_in_part_2_window.close()
        self.login_window.show()

    def show_login_part_2(self):
        self.login_window.close()
        self.log_in_part_2_window.show()

    def show_dashboard(self):
        self.log_in_part_2_window.close()
        self.dashboard_window.show()

    def log_out(self):
        self.dashboard_window.close()
        self.log_in_part_2_window.show()

    def show_create_group(self):
        self.create_group_window.show()

    def cancel_back_to_main_dashboard(self):
        self.create_group_window.close()
        self.dashboard_window.show()

    def access_to_group_dashboard(self):
        self.create_group_window.close()
        self.dashboard_window.close()
        self.group_dashboard_window.show()

    def access_activity_log(self):
        self.group_dashboard_window.close()
        self.activity_log_window.show()

    def close_activity_log(self):
        self.activity_log_window.close()
        self.group_dashboard_window.show()

    def access_group_members(self):
        self.group_members_window.show()

    def close_group_members(self):
        self.group_members_window.close()

    def show_task_window(self):
        self.task_window.show()

    def back_to_main_dashboard(self):
        self.group_dashboard_window.close()
        self.dashboard_window.show()

    def run(self):
        self.log_in_part_2_window.show()
        sys.exit(self.app.exec())

if __name__ == "__main__":
    main_app = MainApp()
    main_app.run()