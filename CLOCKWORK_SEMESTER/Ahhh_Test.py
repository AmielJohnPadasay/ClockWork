import sys
import mysql.connector # Need to be created tomorrow
import datetime
from mysql.connector import errorcode as err
from PySide6.QtWidgets import QApplication, QWidget, QStackedWidget, QComboBox, QLineEdit, QTableWidget, QTableWidgetItem, QRadioButton, QDateEdit
from PySide6.QtWidgets import QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QMainWindow, QDialog
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, Qt
from PySide6.QtWidgets import QMessageBox

email = "a@gmail.com"
password = "22222222"
manager_email = "b@yahoo.com"
manager_password = "33333333"

#Temporary containers for user data
# These will be used to store user data temporarily before inserting into the database
email_container = []
password_container = []
first_name_container = []
last_name_container = []
middle_initial_container = []
role_container = []
s_container = []
suffix_container = []
birthdate_container = []

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

        self.register_fingerprint_window = self.loader.load("register_fingerprint.ui", None)
        self.register_fingerprint_window.setWindowModality(Qt.ApplicationModal)

        self.setup_login_page()  # Setup the login page

    # Log-In Page
    def setup_login_page(self):
        global email
        global password
        global email_container
        global password_container
        global role_container

        self.login_window.show()

        self.log_in_stacked = self.login_window.findChild(QStackedWidget, "log_in_stacked")
        self.log_in_stacked.setCurrentIndex(1)

        self.log_in_credentials_btn = self.login_window.findChild(QWidget, "log_in_credentials_btn")
        if self.log_in_credentials_btn:
            self.log_in_credentials_btn.clicked.connect(lambda: self.log_in_stacked.setCurrentIndex(0))

        self.log_in_fingerprint_btn = self.login_window.findChild(QWidget, "log_in_fingerprint_btn")
        if self.log_in_fingerprint_btn:
            self.log_in_fingerprint_btn.clicked.connect(lambda: self.log_in_stacked.setCurrentIndex(1))

        self.email_lineedit = self.login_window.findChild(QLineEdit, "email_lineEdit")

        self.password_lineedit = self.login_window.findChild(QLineEdit, "password_lineEdit")
        self.password_lineedit.setEchoMode(QLineEdit.Password)

        self.change_into_change_account_button = self.login_window.findChild(QWidget, "create_account_log_in_button_2")
        if self.change_into_change_account_button:
            self.change_into_change_account_button.clicked.connect(self.setup_create_account_page)

        self.login_button = self.login_window.findChild(QWidget, "log_in_button")
        if self.login_button:
            self.login_button.clicked.connect(self.load_dashboard)

        # Ensure the login failed message box does not appear on program start
        self.email_lineedit.textChanged.connect(lambda: None)
        self.password_lineedit.textChanged.connect(lambda: None)


    def setup_create_account_page(self):
        self.create_account_window.setWindowTitle("Create Account")
        self.create_account_window.show()
        self.login_window.hide()


        self.email_edit = self.create_account_window.findChild(QLineEdit, "email_edit")
        self.last_name_edit = self.create_account_window.findChild(QLineEdit, "last_name_edit")
        self.first_name_edit = self.create_account_window.findChild(QLineEdit, "first_name_edit")
        self.middle_init_edit = self.create_account_window.findChild(QLineEdit, "middle_initial_edit")
        self.suffix_combobox = self.create_account_window.findChild(QComboBox, "suffix_combobox")
        self.suffix_combobox.setCurrentIndex(0)
        self.birthdate_edit = self.create_account_window.findChild(QDateEdit, "birthdate_edit")

        #For sex radio buttons
        self.male_radio_btn = self.create_account_window.findChild(QRadioButton, "male_radio")
        self.male_radio_btn.setChecked(True)
        self.female_radio_btn = self.create_account_window.findChild(QRadioButton, "female_radio")
        
        self.others_radio_btn = self.create_account_window.findChild(QRadioButton, "others_radio")
        self.others_edit = self.create_account_window.findChild(QLineEdit, "others_edit")
        self.others_edit.setPlaceholderText("Please specify")

        self.others_edit.setEnabled(False)
        self.others_radio_btn.toggled.connect(lambda: self.others_edit.setEnabled(self.others_radio_btn.isChecked()))

        #For date of birth
        self.birthdate_edit.setDisplayFormat("yyyy-MM-dd")
        self.birthdate_edit.setCalendarPopup(True)
        self.birthdate_edit.setDate(datetime.date.today())

        #For passwords
        self.password_edit = self.create_account_window.findChild(QLineEdit, "password_edit")
        self.password_edit.setEchoMode(QLineEdit.Password)
        self.confirm_password_edit = self.create_account_window.findChild(QLineEdit, "confirm_password_edit")
        self.confirm_password_edit.setEchoMode(QLineEdit.Password)

        #Remove role combo box and directly set role to "Supervisor" #To be removed
        self.role = "Supervisor"

        self.change_into_log_in_button = self.create_account_window.findChild(QWidget, "change_into_log_in_button")
        if self.change_into_log_in_button:
            self.change_into_log_in_button.clicked.connect(self.show_login)

        self.create_account_button = self.create_account_window.findChild(QWidget, "create_account_button")

        if self.create_account_button:
            self.create_account_button.clicked.connect(self.validate_create_account)

    def validate_create_account(self):
        # Error handling for empty fields
        if not self.email_edit.text() or not self.last_name_edit.text() or not self.first_name_edit.text() or not self.middle_init_edit.text() or not self.password_edit.text() or not self.confirm_password_edit.text():
            empty_msg_box = QMessageBox()
            empty_msg_box.setIcon(QMessageBox.Warning)
            empty_msg_box.setWindowTitle("Empty Fields")
            empty_msg_box.setText("Please fill in all fields.")
            empty_msg_box.exec()
            return

        # Check if "@gmail.com" and "@yahoo.com" and is in the email field
        elif "@gmail.com" not in self.email_edit.text() and "@yahoo.com" not in self.email_edit.text():
            invalid_email_msg_box = QMessageBox()
            invalid_email_msg_box.setIcon(QMessageBox.Warning)
            invalid_email_msg_box.setWindowTitle("Invalid Email")
            invalid_email_msg_box.setText("Please enter a valid Gmail address.")
            invalid_email_msg_box.exec()
            return 
        
        # Check if the password is at least 8 characters long
        elif len(self.password_edit.text()) < 8:
            less_8_msg_box = QMessageBox()
            less_8_msg_box.setIcon(QMessageBox.Warning)
            less_8_msg_box.setWindowTitle("Invalid Password")
            less_8_msg_box.setText("Password must be at least 8 characters long.")
            less_8_msg_box.exec()
            return

        # Check if the password and confirm password match
        elif self.password_edit.text() != self.confirm_password_edit.text():
            not_match_msg_box = QMessageBox()
            not_match_msg_box.setIcon(QMessageBox.Warning)
            not_match_msg_box.setWindowTitle("Password Mismatch")
            not_match_msg_box.setText("Passwords do not match.")
            not_match_msg_box.exec()
            return 

        # Check if the email already exists in the database
        elif self.email_edit.text() in email_container:
            email_exists_msg_box = QMessageBox()
            email_exists_msg_box.setIcon(QMessageBox.Warning)
            email_exists_msg_box.setWindowTitle("Email Already Exists")
            email_exists_msg_box.setText("This email is already registered.")
            email_exists_msg_box.exec()
            return 

        # If all validations pass, store the account into the database
        self.register_fingerprint()
       
    def register_fingerprint(self):
        self.register_fingerprint_window.show()

        self.skip_btn = self.register_fingerprint_window.findChild(QWidget, "skip_btn")
        if self.skip_btn:
            self.skip_btn.clicked.connect(self.store_into_database)

        self.cancel_btn = self.register_fingerprint_window.findChild(QWidget, "cancel_btn")
        if self.cancel_btn:
            self.cancel_btn.clicked.connect(self.register_fingerprint_window.hide)
            return

    def store_into_database(self):
        self.register_fingerprint_window.hide()

        new_email = self.email_edit.text()
        new_password = self.password_edit.text()
        new_first_name = self.first_name_edit.text()
        new_last_name = self.last_name_edit.text()
        new_middle_initial = self.middle_init_edit.text()
        new_suffix = self.suffix_combobox.currentText()
        new_birthdate = self.birthdate_edit.text()

        if self.male_radio_btn.isChecked():
            selected_s = "Male"
        elif self.female_radio_btn.isChecked():
            selected_s = "Female"
        elif self.others_radio_btn.isChecked():
            selected_s = self.others_edit.text()

        #Append data to temporary containers
        email_container.append(new_email)
        password_container.append(new_password)
        first_name_container.append(new_first_name)
        last_name_container.append(new_last_name)
        middle_initial_container.append(new_middle_initial)
        suffix_container.append(new_suffix)
        s_container.append(selected_s)
        birthdate_container.append(new_birthdate)

        # Set role to employee
        role_container.append("Employee")

        account_created_msg_box = QMessageBox()
        account_created_msg_box.setIcon(QMessageBox.Information)
        account_created_msg_box.setWindowTitle("Account Created")
        account_created_msg_box.setText("Account created successfully!")
        account_created_msg_box.exec()

        #Ensure that the create account edit credentials are empty

        self.email_edit.setText("")
        self.last_name_edit.setText("")
        self.first_name_edit.setText("")
        self.middle_init_edit.setText("")
        self.suffix_combobox.setCurrentIndex(0)
        self.password_edit.setText("")
        self.confirm_password_edit.setText("")
        self.birthdate_edit.setDate(datetime.date.today())

        self.create_account_window.hide()
        self.setup_login_page()

    def load_dashboard(self):
        global email
        global password
        global manager_email
        global manager_password
        global email_container
        global password_container
        self.email = self.email_lineedit.text()
        self.password = self.password_lineedit.text()

        # Map roles to UI files
        dashboard_files = {
                "Supervisor": "dashboard_updated.ui",
                "Manager": "dashboard_manager_updated.ui",
                "Employee": "dashboard_employee_new.ui"
            }
        # For main supervisor role
        if self.email == email and self.password == password:
            self.role = "Supervisor"

            ui_file_path = dashboard_files.get(self.role)

            if ui_file_path:
                self.open_dashboard(ui_file_path)

        # For manager role (TBA)
        if self.email == manager_email and self.password == manager_password:
            self.role = "Manager"

            ui_file_path = dashboard_files.get(self.role)

            if ui_file_path:
                self.open_dashboard(ui_file_path)

        # For other roles
        elif self.email in email_container and self.password in password_container:
            index = email_container.index(self.email)
            self.role = role_container[index]

            ui_file_path = dashboard_files.get(self.role)

            if ui_file_path:
                self.open_dashboard(ui_file_path)
        
        else:
            login_failed_msg_box = QMessageBox()
            login_failed_msg_box.setIcon(QMessageBox.Warning)
            login_failed_msg_box.setWindowTitle("Login Failed")
            login_failed_msg_box.setText("Invalid email or password. Please try again.")
            login_failed_msg_box.exec()

    def open_dashboard(self, ui_file_path):
        global email
        global password
        self.email = self.email_lineedit.text()
        self.password = self.password_lineedit.text()

        ui_file = QFile(ui_file_path)
        if ui_file.open(QFile.ReadOnly):
            self.current_dashboard = self.loader.load(ui_file, None)  # Store the dashboard instance
            self.current_dashboard.show()
            self.login_window.hide()
            ui_file.close()
            if self.email == email and self.password == password:
                self.setup_supervisor_dashboard()
            elif self.email == manager_email and self.password == manager_password:
                self.setup_manager_dashboard()
            elif self.role == "Employee":
                self.setup_employee_dashboard()

    #Supervisor's Menu
    def setup_supervisor_dashboard(self):

        self.user_table = self.current_dashboard.findChild(QTableWidget, "users_table")
        if self.user_table:
            self.user_table.setRowCount(3)
            self.user_table.setColumnCount(3)
            self.user_table.setSelectionBehavior(QTableWidget.SelectRows)
            self.user_table.setSelectionMode(QTableWidget.SingleSelection)

            self.user_table.setHorizontalHeaderLabels(["Name", "Email", "Role"])
            self.user_table.setVerticalHeaderLabels([])

            self.user_table.setItem(0, 0, QTableWidgetItem("Amiel Padasay"))
            self.user_table.setItem(0, 1, QTableWidgetItem("amiel.padasay004@gmail.com"))
            self.user_table.setItem(0, 2, QTableWidgetItem("Supervisor"))

            self.user_table.setItem(1, 0, QTableWidgetItem("John Doe"))
            self.user_table.setItem(1, 1, QTableWidgetItem("johndoe@gmail.com"))
            self.user_table.setItem(1, 2, QTableWidgetItem("Manager"))

        self.log_out_button = self.current_dashboard.findChild(QWidget, "log_out_btn")
        if self.log_out_button:
            self.log_out_button.clicked.connect(self.log_out)

        self.stacked_supervisor = self.current_dashboard.findChild(QStackedWidget, "stacked_Supervisor")

        self.stacked_supervisor.setCurrentIndex(0)

        self.currenttask_table = self.current_dashboard.findChild(QTableWidget, "currenttask_table")
        if self.currenttask_table:
            self.currenttask_table.setRowCount(4)
            self.currenttask_table.setColumnCount(4)

            self.currenttask_table.setHorizontalHeaderLabels(["Task", "Assigned To", "Due Date", "Status"])
            self.currenttask_table.setVerticalHeaderLabels([])

        self.dashboard_btn = self.current_dashboard.findChild(QWidget, "dashboard_btn")
        if self.dashboard_btn:
            self.dashboard_btn.clicked.connect(lambda: self.stacked_supervisor.setCurrentIndex(0))
          
        self.activity_log_btn = self.current_dashboard.findChild(QWidget, "activity_log_btn")
        if self.activity_log_btn:
            self.activity_log_btn.clicked.connect(lambda: self.stacked_supervisor.setCurrentIndex(1))
            
        self.calendar_btn = self.current_dashboard.findChild(QWidget, "calendar_btn")
        if self.calendar_btn:
            self.calendar_btn.clicked.connect(lambda: self.stacked_supervisor.setCurrentIndex(2))
            
        self.user_roles_btn = self.current_dashboard.findChild(QWidget, "user_roles_btn")
        if self.user_roles_btn:
            self.user_roles_btn.clicked.connect(lambda: self.stacked_supervisor.setCurrentIndex(3))

        self.change_role_btn = self.current_dashboard.findChild(QWidget, "change_role_btn")
        if self.change_role_btn:
            self.change_role_btn.clicked.connect(self.show_select_role_with_data)

        self.validate_btn = self.current_dashboard.findChild(QWidget, "validatetask_btn")
        if self.validate_btn:
            self.validate_btn.clicked.connect(self.validate_task)

        self.profile_btn = self.current_dashboard.findChild(QWidget, "profile_button")
        if self.profile_btn:
            self.profile_btn.clicked.connect(self.show_profile)
                
        self.log_out_button = self.dashboard_window.findChild(QWidget, "log_out_btn")
        if self.log_out_button:
            self.log_out_button.clicked.connect(self.log_out)

    def validate_task(self):
        self.validate_task_window.show()

    def show_profile(self):
        self.profile_window.show()

        self.edit_profile_btn = self.profile_window.findChild(QWidget, "edit_profile_btn")
        if self.edit_profile_btn:
            self.edit_profile_btn.clicked.connect(self.show_edit_profile)

    def show_edit_profile(self):
        self.edit_profile_window.show()

    def show_select_role_with_data(self):
        selected_row = self.user_table.currentRow()
        self.name = ""
        self.role = ""
        if selected_row != -1:  # Ensure a row is selected
            name_item = self.user_table.item(selected_row, 0)
            role_item = self.user_table.item(selected_row, 2)

            if name_item and role_item:
                self.name = name_item.text()
                self.role = role_item.text()

            # Set the name and role in the change role window
            name_label = self.select_role_window.findChild(QLabel, "name_label")
            if name_label:
                name_label.setText((f"Name: {self.name}"))

            role_label = self.select_role_window.findChild(QLabel, "current_role_label")
            if role_label:
                role_label.setText((f"Current Role: {self.role}"))

        if self.name != "Amiel Padasay":
            self.show_select_role()
        else:  
            no_change_msg_box = QMessageBox()
            no_change_msg_box.setIcon(QMessageBox.Warning)
            no_change_msg_box.setWindowTitle("Invalid Action")
            no_change_msg_box.setText("You cannot change the role of this user.")
            no_change_msg_box.exec()
            self.select_role_window.hide()

    def show_select_role(self):
        self.select_role_window.show()
        
        self.role_label = self.select_role_window.findChild(QLabel, "current_role_label")
        if self.role_label:
            self.role_label.setText((f"Current Role: {self.role}"))

        self.supervisor_radio_btn = self.select_role_window.findChild(QRadioButton, "supervisor_radio")
        self.manager_radio_btn = self.select_role_window.findChild(QRadioButton, "manager_radio")
        self.employee_radio_btn = self.select_role_window.findChild(QRadioButton, "employee_radio")
        
        # Auto select the radio button based on the current role
        if self.role == "Supervisor":
            self.supervisor_radio_btn.setChecked(True)
        elif self.role == "Manager":
            self.manager_radio_btn.setChecked(True)
        elif self.role == "Employee":
            self.employee_radio_btn.setChecked(True)
    
        # Ensure the confirmation message box does not reappear
        if hasattr(self, 'confirmation_shown') and self.confirmation_shown:
            return
        self.confirmation_shown = True

        self.save_changes_button = self.select_role_window.findChild(QPushButton, "save_changes_btn")
        if self.save_changes_button:
            self.save_changes_button.clicked.connect(self.save_role_changes)

        self.cancel_button = self.select_role_window.findChild(QWidget, "cancel_btn")
        if self.cancel_button:
            self.cancel_button.clicked.connect(self.select_role_window.hide)

    def save_role_changes(self):

        change_role_msg_box = QMessageBox()
        change_role_msg_box.setIcon(QMessageBox.Warning)
        change_role_msg_box.setWindowTitle("Confirmation")
        change_role_msg_box.setText("Are you sure you want to change the role?")
        change_role_msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        change_role_msg_box.setDefaultButton(QMessageBox.No)
        change_role_msg_box.setEscapeButton(QMessageBox.No)
        change_role_msg_box.setModal(True)
        change_role_msg_box.setWindowModality(Qt.ApplicationModal)
        
        result = change_role_msg_box.exec()
            
        if result == QMessageBox.Yes:
            selected_row = self.user_table.currentRow()
            if selected_row != -1:  # Ensure a row is selected
                name_item = self.user_table.item(selected_row, 0)
                role_item = self.user_table.item(selected_row, 2)

            if name_item and role_item:
                name = name_item.text()
                role = role_item.text()

            # Get the selected radio button
            if self.supervisor_radio_btn.isChecked():
                new_role = "Supervisor"
            elif self.manager_radio_btn.isChecked():
                new_role = "Manager"
            elif self.employee_radio_btn.isChecked():
                new_role = "Employee"

            # Update the role in the table
            if role_item:
                role_item.setText(new_role)
                self.select_role_window.hide() 
                change_role_msg_box.close()

        elif result == QMessageBox.No:
            change_role_msg_box.close()

    #Manager's Menu
    def setup_manager_dashboard(self):
        self.log_out_button = self.current_dashboard.findChild(QWidget, "log_out_btn")
        if self.log_out_button:
            self.log_out_button.clicked.connect(self.log_out)

        self.stacked_Manager = self.current_dashboard.findChild(QStackedWidget, "stacked_Manager")

        self.stacked_Manager.setCurrentIndex(0)

        self.currenttask_table = self.current_dashboard.findChild(QTableWidget, "currenttask_table")
        if self.currenttask_table:
            self.currenttask_table.setRowCount(4)
            self.currenttask_table.setColumnCount(4)

            # self.currenttask_table.setHorizontalHeaderLabels(["Task", "Assigned To", "Due Date", "Status"])
            self.currenttask_table.setVerticalHeaderLabels([])

        self.dashboard_btn_manager = self.current_dashboard.findChild(QWidget, "dashboard_btn")
        if self.dashboard_btn_manager:
            self.dashboard_btn_manager.clicked.connect(lambda: self.stacked_Manager.setCurrentIndex(0))
            
        self.activity_log_btn_manager = self.current_dashboard.findChild(QWidget, "activity_log_btn")
        if self.activity_log_btn_manager:
            self.activity_log_btn_manager.clicked.connect(lambda: self.stacked_Manager.setCurrentIndex(1))
            
        self.calendar_btn_manager = self.current_dashboard.findChild(QWidget, "calendar_btn")
        if self.calendar_btn_manager:
            self.calendar_btn_manager.clicked.connect(lambda: self.stacked_Manager.setCurrentIndex(2))

        self.assign_task_button = self.current_dashboard.findChild(QWidget, "assigntask_btn")
        if self.assign_task_button:
            self.assign_task_button.clicked.connect(self.show_assign_task)

        self.profile_btn = self.current_dashboard.findChild(QWidget, "profile_button")
        if self.profile_btn:
            self.profile_btn.clicked.connect(self.show_profile)

        self.log_out_button = self.dashboard_window.findChild(QWidget, "log_out_btn")
        if self.log_out_button:
            self.log_out_button.clicked.connect(self.log_out)

    def show_assign_task(self):
        self.assign_task_window.show()

    def setup_employee_dashboard(self):
        self.log_out_button = self.current_dashboard.findChild(QWidget, "log_out_btn")
        if self.log_out_button:
            self.log_out_button.clicked.connect(self.log_out)

        self.stacked_Employee = self.current_dashboard.findChild(QStackedWidget, "stacked_Employee")

        self.stacked_Employee.setCurrentIndex(0)

        self.dashboard_btn_employee = self.current_dashboard.findChild(QWidget, "dashboard_btn")
        if self.dashboard_btn_employee:
            self.dashboard_btn_employee.clicked.connect(lambda: self.stacked_Employee.setCurrentIndex(0))

        self.calendar_btn_employee = self.current_dashboard.findChild(QWidget, "calendar_btn")
        if self.calendar_btn_employee:
            self.calendar_btn_employee.clicked.connect(lambda: self.stacked_Employee.setCurrentIndex(1))

        self.submit_task_button = self.current_dashboard.findChild(QWidget, "submit_task_btn")
        if self.submit_task_button:
            self.submit_task_button.clicked.connect(self.show_submit_task)

        self.profile_btn = self.current_dashboard.findChild(QWidget, "profile_button")
        if self.profile_btn:
            self.profile_btn.clicked.connect(self.show_profile)
                
        self.log_out_button = self.dashboard_window.findChild(QWidget, "log_out_btn")
        if self.log_out_button:
            self.log_out_button.clicked.connect(self.log_out)

    def show_submit_task(self):
        self.submit_task_window.show()

    def show_join_group(self):
        self.join_group_window.show()

    def show_login(self):
        self.login_window.show()
        self.create_account_window.hide()
    
    def log_out(self):
        self.login_window.show()
        self.log_in_stacked.setCurrentIndex(1)
        self.current_dashboard.hide()

    def run(self):
        self.login_window.show()
        sys.exit(self.app.exec())

if __name__ == "__main__":
    main_app = MainApp()
    main_app.run()