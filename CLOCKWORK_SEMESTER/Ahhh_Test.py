import sys
import mysql.connector # Need to be created tomorrow why not NOW!!!?
import pymongo
import datetime
from mysql.connector import errorcode as err
from PySide6.QtWidgets import (QApplication, QWidget, QStackedWidget, QComboBox, QLineEdit, QTableWidget, 
                               QTableWidgetItem, QRadioButton, QDateEdit, QListWidget, QTimeEdit, QTextEdit, QTextBrowser)
from PySide6.QtWidgets import QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QMainWindow, QDialog
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, Qt
from PySide6.QtWidgets import QMessageBox

email = "a@gmail.com"
password = "22222222"
first_name = "Amiel"
last_name = "Padasay"
middle_initial = "R."
suffix = ""
role = "Supervisor"
birthdate = "2004-09-18"
sex = "Male"

manager_email = "b@yahoo.com"
manager_password = "33333333"
manager_first_name = "John"
manager_last_name = "Doe"
manager_middle_initial = "D."
manager_suffix = ""
manager_role = "Manager"
manager_birthdate = "2005-09-18"
manager_sex = "Male"

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

task_name_container = []
task_requirement_container = []
task_description_container = []
task_priority_level_container = []
task_due_date_container = []
task_due_time_container = []
task_assigned_to_container = []
task_status_container = []

email_container.append(email)
email_container.append(manager_email)
password_container.append(password)
password_container.append(manager_password)
first_name_container.append(first_name)
first_name_container.append(manager_first_name)
last_name_container.append(last_name)
last_name_container.append(manager_last_name)
middle_initial_container.append(middle_initial)
middle_initial_container.append(manager_middle_initial)
role_container.append(role)
role_container.append(manager_role)
s_container.append(sex)
s_container.append(manager_sex)
suffix_container.append(suffix)
suffix_container.append(manager_suffix)
birthdate_container.append(birthdate)
birthdate_container.append(manager_birthdate)

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

        self.submit_file_task_window = self.loader.load("submit_files_task.ui", None)
        self.submit_file_task_window.setWindowModality(Qt.ApplicationModal)
        
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

        # Inputs for user credentials
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
        
        # Check if others edit has text
        elif self.others_radio_btn.isChecked() and not self.others_edit.text():
            empty_others_msg_box = QMessageBox()
            empty_others_msg_box.setIcon(QMessageBox.Warning)
            empty_others_msg_box.setWindowTitle("Empty Others Field")
            empty_others_msg_box.setText("Please fill in the Others field.")
            empty_others_msg_box.exec()
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

        #Ensure that the create account edit credentials are empty

        self.email_edit.setText("")
        self.last_name_edit.setText("")
        self.first_name_edit.setText("")
        self.middle_init_edit.setText("")
        self.suffix_combobox.setCurrentIndex(0)
        self.password_edit.setText("")
        self.confirm_password_edit.setText("")
        self.birthdate_edit.setDate(datetime.date.today())

        account_created_msg_box = QMessageBox()
        account_created_msg_box.setIcon(QMessageBox.Information)
        account_created_msg_box.setWindowTitle("Account Created")
        account_created_msg_box.setText("Account created successfully!")
        account_created_msg_box.exec()

        self.create_account_window.hide()
        self.setup_login_page()

    def load_dashboard(self):
        #To be removed
        global email
        global password
        global manager_email
        global manager_password


        global email_container
        global password_container
        global role_container
        self.email = self.email_lineedit.text()
        self.password = self.password_lineedit.text()

        # Map roles to UI files
        dashboard_files = {
                "Supervisor": "dashboard_updated.ui",
                "Manager": "dashboard_manager_updated.ui",
                "Employee": "dashboard_employee_new.ui"
            }
        # Password and email validation
        if self.email in email_container:
            index = email_container.index(self.email)

        if self.password == password_container[index]:
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
            return

    def open_dashboard(self, ui_file_path):
        #Global variables to be removed
        global email
        global password

        global email_container
        global password_container
        global role_container

        self.email = self.email_lineedit.text()
        self.password = self.password_lineedit.text()

        ui_file = QFile(ui_file_path)
        if ui_file.open(QFile.ReadOnly):
            index = email_container.index(self.email)
            self.role = role_container[index]
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

        self.user_table = self.current_dashboard.findChild(QTableWidget, "users_table")
        if self.user_table:
            self.user_table.setRowCount(4)
            self.user_table.setColumnCount(3)

            self.user_table.setHorizontalHeaderLabels(["Name", "Email", "Role"])
            self.user_table.setVerticalHeaderLabels([])

            # Populate the table with data from temporary containers
            for i in range(len(email_container)):
                self.user_table.insertRow(i)
                self.user_table.setItem(i, 0, QTableWidgetItem(first_name_container[i] + " " + last_name_container[i]))
                self.user_table.setItem(i, 1, QTableWidgetItem(email_container[i]))
                self.user_table.setItem(i, 2, QTableWidgetItem(role_container[i]))

        self.log_out_button = self.current_dashboard.findChild(QWidget, "log_out_btn")
        if self.log_out_button:
            self.log_out_button.clicked.connect(self.log_out)

        self.stacked_supervisor = self.current_dashboard.findChild(QStackedWidget, "stacked_Supervisor")

        self.stacked_supervisor.setCurrentIndex(0)

        self.currenttask_table = self.current_dashboard.findChild(QTableWidget, "currenttask_table")
        if self.currenttask_table:
            self.currenttask_table.setColumnCount(6)
            self.currenttask_table.setHorizontalHeaderLabels(["Task", "Requirement", "Priority Level", "Status", "Assigned To", "Due Date"])
            self.currenttask_table.setVerticalHeaderLabels([])

        #Connect the tasks' temp storage
        for i in range(len(task_name_container)):
            self.currenttask_table.insertRow(i)
            self.currenttask_table.setItem(i, 0, QTableWidgetItem(task_name_container[i]))
            self.currenttask_table.setItem(i, 1, QTableWidgetItem(task_requirement_container[i]))
            self.currenttask_table.setItem(i, 2, QTableWidgetItem(task_priority_level_container[i]))
            self.currenttask_table.setItem(i, 3, QTableWidgetItem(task_status_container[i]))
            self.currenttask_table.setItem(i, 4, QTableWidgetItem(", ".join(task_assigned_to_container[i]) if isinstance(task_assigned_to_container[i], set) else task_assigned_to_container[i]))
            self.currenttask_table.setItem(i, 5, QTableWidgetItem(task_due_date_container[i] + " " + task_due_time_container[i]))

        self.pendingtask_table = self.current_dashboard.findChild(QTableWidget, "pendingtasks_table")
        if self.pendingtask_table:
            self.pendingtask_table.setColumnCount(6)
            self.pendingtask_table.setHorizontalHeaderLabels(["Task", "Requirement", "Priority Level", "Status", "Assigned To", "Due Date"])
            self.pendingtask_table.setVerticalHeaderLabels([])

        #Connect the tasks' temp storage
        for i in range(len(task_name_container)):
            self.pendingtask_table.insertRow(i)
            self.pendingtask_table.setItem(i, 0, QTableWidgetItem(task_name_container[i]))
            self.pendingtask_table.setItem(i, 1, QTableWidgetItem(task_requirement_container[i]))
            self.pendingtask_table.setItem(i, 2, QTableWidgetItem(task_priority_level_container[i]))
            self.pendingtask_table.setItem(i, 3, QTableWidgetItem(task_status_container[i]))
            self.pendingtask_table.setItem(i, 4, QTableWidgetItem(", ".join(task_assigned_to_container[i]) if isinstance(task_assigned_to_container[i], set) else task_assigned_to_container[i]))
            self.pendingtask_table.setItem(i, 5, QTableWidgetItem(task_due_date_container[i] + " " + task_due_time_container[i]))

        self.completedtask_table = self.current_dashboard.findChild(QTableWidget, "completedtask_table")    

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
        global first_name_container
        global last_name_container
        global email_container
        global role_container
        global s_container
        global birthdate_container
        global suffix_container
        global middle_initial_container

        self.profile_window.show()

        self.edit_profile_btn = self.profile_window.findChild(QWidget, "edit_profile_btn")
        if self.edit_profile_btn:
            self.edit_profile_btn.clicked.connect(self.show_edit_profile)

        # Make the labels have their name, role, email, sex and birthdate according to their index
        self.email = self.email_lineedit.text()
        self.password = self.password_lineedit.text()
        if self.email in email_container and self.password in password_container:    
            index = email_container.index(self.email)

            self.name_label = self.profile_window.findChild(QLabel, "name_label")
            if self.name_label:
                self.name_label.setText((f"Name: {first_name_container[index]} {last_name_container[index]}"))

            self.role_label = self.profile_window.findChild(QLabel, "role_label")
            if self.role_label:
                self.role_label.setText((f"Role: {role_container[index]}"))

            self.age_and_sex_label = self.profile_window.findChild(QLabel, "age_and_sex_Label")
            if self.age_and_sex_label:
                self.age_and_sex_label.setText((f"Age: {self.calculate_age(birthdate_container[index])} years old\n\nSex: {s_container[index]}"))
            
            self.email_label = self.profile_window.findChild(QLabel, "email_label_2")
            if self.email_label:
                self.email_label.setText((f"{email_container[index]}"))

            self.birthdate_label = self.profile_window.findChild(QLabel, "birthdate_label_2")
            if self.birthdate_label:
                self.birthdate_label.setText((f"{birthdate_container[index]}"))


    def calculate_age(self, birthdate):
        birthdate = datetime.datetime.strptime(birthdate, "%Y-%m-%d").date()
        today = datetime.date.today()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return age    


    def show_edit_profile(self):
        global first_name_container
        global last_name_container
        global email_container
        global role_container
        global s_container
        global birthdate_container
        global suffix_container
        global middle_initial_container

        self.edit_profile_window.show()

        #Connection of widgets
        self.edit_first_name = self.edit_profile_window.findChild(QLineEdit, "new_first_name_edit")
        self.edit_last_name = self.edit_profile_window.findChild(QLineEdit, "new_last_name_edit")
        self.edit_middle_initial = self.edit_profile_window.findChild(QLineEdit, "new_middle_initial_edit")
        self.edit_suffix = self.edit_profile_window.findChild(QComboBox, "suffix_combobox")
        self.edit_suffix.setCurrentIndex(0)

        self.new_male_radio = self.edit_profile_window.findChild(QRadioButton, "new_male_radio")
        self.new_female_radio = self.edit_profile_window.findChild(QRadioButton, "new_female_radio")
        self.new_others_radio = self.edit_profile_window.findChild(QRadioButton, "new_others_radio")
        
        self.new_others_edit = self.edit_profile_window.findChild(QLineEdit, "new_others_edit")
        self.new_others_edit.setPlaceholderText("Please specify")
        self.new_others_edit.setEnabled(False)

        if self.new_others_radio:
            self.new_others_radio.toggled.connect(lambda: self.new_others_edit.setEnabled(self.new_others_radio.isChecked()))
        if self.new_male_radio:
            self.new_male_radio.toggled.connect(lambda: self.new_others_edit.setEnabled(False))
        if self.new_female_radio:
            self.new_female_radio.toggled.connect(lambda: self.new_others_edit.setEnabled(False))

        self.edit_birthdate = self.edit_profile_window.findChild(QDateEdit, "new_birthdate_edit")
        self.edit_birthdate.setDisplayFormat("yyyy-MM-dd")
        self.edit_birthdate.setCalendarPopup(True)

        self.email = self.email_lineedit.text()

        if self.email in email_container:
            index = email_container.index(self.email)
            self.edit_first_name.setText(first_name_container[index])
            self.edit_last_name.setText(last_name_container[index])
            self.edit_middle_initial.setText(middle_initial_container[index])
            self.edit_suffix.setCurrentText(suffix_container[index])
            self.edit_birthdate.setDate(datetime.datetime.strptime(birthdate_container[index], "%Y-%m-%d").date())

            self.sex = s_container[index].strip().lower()
            if self.sex == "male":
                self.new_male_radio.setChecked(True)
                self.new_female_radio.setChecked(False)
                if self.new_others_radio:
                    self.new_others_radio.setChecked(False)
                    self.new_others_edit.clear()

            elif self.sex == "female":
                self.new_male_radio.setChecked(False)
                self.new_female_radio.setChecked(True)
                if self.new_others_radio:
                    self.new_others_radio.setChecked(False)
                    self.new_others_edit.clear()

            elif self.sex:  # Handle non-empty, non-standard values
                if self.new_others_radio:
                    self.new_others_radio.setChecked(True)
                    self.new_others_edit.setText(s_container[index])

        self.save_changes_button = self.edit_profile_window.findChild(QPushButton, "save_changes_btn")
        self.cancel_btn = self.edit_profile_window.findChild(QPushButton, "new_cancel_btn")
        
        if self.save_changes_button:
            self.save_changes_button.clicked.connect(self.save_changes_with_profile)

        if self.cancel_btn:
            self.cancel_btn.clicked.connect(self.edit_profile_window.close)
            self.show_profile()

    def save_changes_with_profile(self):
        save_change_msg_box = QMessageBox()
        save_change_msg_box.setIcon(QMessageBox.Warning)
        save_change_msg_box.setWindowTitle("Confirmation")
        save_change_msg_box.setText("Are you sure you want to edit your profile?")
        save_change_msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        save_change_msg_box.setDefaultButton(QMessageBox.No)
        save_change_msg_box.setEscapeButton(QMessageBox.No)
        save_change_msg_box.setModal(True)
        save_change_msg_box.setWindowModality(Qt.ApplicationModal)

        result = save_change_msg_box.exec()
            
        if result == QMessageBox.Yes: # To be continued
            index = email_container.index(self.email)
            new_first_name = self.edit_first_name.text()
            new_last_name = self.edit_last_name.text()
            new_middle_initial = self.edit_middle_initial.text()
            new_suffix = self.edit_suffix.currentText()
            new_birthdate = self.edit_birthdate.text()

            first_name_container[index] = new_first_name
            last_name_container[index] = new_last_name
            middle_initial_container[index] = new_middle_initial
            suffix_container[index] = new_suffix
            birthdate_container[index] = new_birthdate

            if self.new_male_radio.isChecked():
                new_s = "Male"
            elif self.new_female_radio.isChecked():
                new_s = "Female"
            elif self.new_others_radio.isChecked():
                if self.new_others_edit:
                    new_s = self.new_others_edit.text()
            s_container[index] = new_s

            self.edit_profile_window.close()
            self.show_profile()
            return

        elif result == QMessageBox.No:
            save_change_msg_box.close()
            self.show_edit_profile()

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
            # Connect the button to the save_role_changes method
            self.save_changes_button.clicked.connect(self.save_role_changes)

        self.cancel_button = self.select_role_window.findChild(QWidget, "cancel_btn")
        if self.cancel_button:
            self.cancel_button.clicked.connect(self.select_role_window.hide)

    def save_role_changes(self):
        global role_container
        global first_name_container
        global last_name_container
        global email_container

        change_role_msg_box = QMessageBox()
        change_role_msg_box.setIcon(QMessageBox.Warning)
        change_role_msg_box.setWindowTitle("Confirmation")
        change_role_msg_box.setText("Are you sure you want to change the role?")
        change_role_msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        change_role_msg_box.setDefaultButton(QMessageBox.No)
        change_role_msg_box.setEscapeButton(QMessageBox.No)
        change_role_msg_box.setModal(True)
        change_role_msg_box.setWindowModality(Qt.ApplicationModal)

        # Overwrite change in role container according to its index

        result = change_role_msg_box.exec()
            
        if result == QMessageBox.Yes:
            selected_row = self.user_table.currentRow()
            if selected_row != -1:  # Ensure a row is selected
                name_item = self.user_table.item(selected_row, 0)
                role_item = self.user_table.item(selected_row, 2)

            if name_item and role_item:
                name = name_item.text()
                role = role_item.text()

            # Connect to role_container to change role
            if self.supervisor_radio_btn.isChecked():
                new_role = "Supervisor"
            elif self.manager_radio_btn.isChecked():
                new_role = "Manager"
            elif self.employee_radio_btn.isChecked():
                new_role = "Employee"
            role_container[selected_row] = new_role

            # Update the role in the table
            if role_item:
                role_item.setText(new_role)
                self.select_role_window.hide() 
                change_role_msg_box.close()

        elif result == QMessageBox.No:
            change_role_msg_box.close()
            self.show_select_role()

    #Manager's Menu
    def setup_manager_dashboard(self):
        self.log_out_button = self.current_dashboard.findChild(QWidget, "log_out_btn")
        if self.log_out_button:
            self.log_out_button.clicked.connect(self.log_out)

        self.stacked_Manager = self.current_dashboard.findChild(QStackedWidget, "stacked_Manager")

        self.stacked_Manager.setCurrentIndex(0)

        self.currenttask_table = self.current_dashboard.findChild(QTableWidget, "currenttask_table")
        self.currenttask_table.setColumnCount(6)
        self.currenttask_table.setHorizontalHeaderLabels(["Task", "Requirement", "Priority Level", "Status", "Assigned To", "Due Date"])

        self.pendingtask_table = self.current_dashboard.findChild(QTableWidget, "pendingtasks_table")
        self.pendingtask_table.setColumnCount(6)
        self.pendingtask_table.setHorizontalHeaderLabels(["Task", "Requirement", "Priority Level", "Status", "Assigned To", "Due Date"])

        self.completedtask_table = self.current_dashboard.findChild(QTableWidget, "completedtasks_table")
        self.completedtask_table.setColumnCount(6)
        self.completedtask_table.setHorizontalHeaderLabels(["Task", "Requirement", "Priority Level", "Status", "Assigned To", "Due Date"])

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

    def show_assign_task(self): # Next function to be created
        global email_container
        global first_name_container
        global last_name_container
    
        self.assign_task_window.show()

        # Inputs for assigning tasks
        self.task_name_edit = self.assign_task_window.findChild(QLineEdit, "taskname_edit")
        self.task_description_edit = self.assign_task_window.findChild(QTextEdit, "taskreq_edit")

        self.prioritylevel_combobox = self.assign_task_window.findChild(QComboBox, "prioritylevel_combobox")
        self.prioritylevel_combobox.setCurrentIndex(0)

        self.search_bar_assign = self.assign_task_window.findChild(QLineEdit, "search_bar_assign")

        # Replace the list widget with a table widget
        self.assign_member_group_table = self.assign_task_window.findChild(QTableWidget, "assign_member_group_list")
        self.assign_member_group_table.setRowCount(len(email_container))
        self.assign_member_group_table.setColumnCount(2)
        self.assign_member_group_table.setHorizontalHeaderLabels(["", "Name"])

        # Populate the table with data
        for i in range(len(email_container)):
            #Create the first column with checkboxes
            checkbox_item = QTableWidgetItem()
            checkbox_item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
            checkbox_item.setCheckState(Qt.Unchecked)
            self.assign_member_group_table.setItem(i, 0, checkbox_item)
            # Create the second column with names and emails
            self.assign_member_group_table.setItem(i, 1, QTableWidgetItem(first_name_container[i] + " " + last_name_container[i]))
            self.assign_member_group_table.setItem(i, 2, QTableWidgetItem(email_container[i]))

        # Enable multi-row selection
        self.assign_member_group_table.itemChanged.connect(self.handle_checkbox_change)

        self.file_radio_btn = self.assign_task_window.findChild(QRadioButton, "file_radio")
        self.weblink_radio_btn = self.assign_task_window.findChild(QRadioButton, "weblink_radio")
        self.file_radio_btn.setChecked(False)
        self.weblink_radio_btn.setChecked(True)

        self.due_date_edit = self.assign_task_window.findChild(QDateEdit, "duedateEdit")
        self.due_date_edit.setDisplayFormat("yyyy-MM-dd")
        self.due_date_edit.setCalendarPopup(True)
        self.due_date_edit.setDate(datetime.date.today())
        self.due_time_edit = self.assign_task_window.findChild(QTimeEdit, "duetimeEdit")
        self.due_time_edit.setDisplayFormat("HH:mm")
        self.due_time_edit.setTime(datetime.time(0, 0))

        self.ok_button = self.assign_task_window.findChild(QWidget, "ok_btn")
        if self.ok_button:
            self.ok_button.clicked.connect(self.confirm_task)

        self.cancel_button = self.assign_task_window.findChild(QWidget, "cancel_btn")
        if self.cancel_button:
            self.cancel_button.clicked.connect(self.assign_task_window.hide)

    def handle_checkbox_change(self, item):
        if item.column() == 0 and item.checkState() == Qt.Checked:
            for col in range(self.assign_member_group_table.columnCount()):
                self.assign_member_group_table.item(item.row(), col).setSelected(True)
        elif item.column() == 0 and item.checkState() == Qt.Unchecked:
            for col in range(self.assign_member_group_table.columnCount()):
                self.assign_member_group_table.item(item.row(), col).setSelected(False)

    def confirm_task(self):
        # Get the task name and description
        if not self.task_name_edit.text() or not self.task_description_edit.toPlainText():
            empty_msg_box = QMessageBox()
            empty_msg_box.setIcon(QMessageBox.Warning)
            empty_msg_box.setWindowTitle("Empty Fields")
            empty_msg_box.setText("Please fill in all fields.")
            empty_msg_box.exec()
            return
        
        # Confirm the selected rows from the table
        selected_rows = self.assign_member_group_table.selectedItems()
        if not selected_rows:
            no_selection_msg_box = QMessageBox()
            no_selection_msg_box.setIcon(QMessageBox.Warning)
            no_selection_msg_box.setWindowTitle("No Selection")
            no_selection_msg_box.setText("Please select at least one member.")
            no_selection_msg_box.exec()
            return
        
        # Check if due date is past the current date
        due_date = self.due_date_edit.date()
        due_time = self.due_time_edit.time()
        due_datetime = datetime.datetime(due_date.year(), due_date.month(), due_date.day(), due_time.hour(), due_time.minute())
        if due_datetime < datetime.datetime.now():
            past_due_msg_box = QMessageBox()
            past_due_msg_box.setIcon(QMessageBox.Warning)
            past_due_msg_box.setWindowTitle("Invalid Due Date")
            past_due_msg_box.setText("Due date cannot be in the past.")
            past_due_msg_box.exec()
            return

        # Get the selected members' names
        selected_names = set()
        for row in range(self.assign_member_group_table.rowCount()):
            checkbox_item = self.assign_member_group_table.item(row, 0)
            if checkbox_item and checkbox_item.checkState() == Qt.Checked:
                name_item = self.assign_member_group_table.item(row, 1)
                if name_item is not None:
                    name_text = name_item.text()
                    if name_text:
                        selected_names.add(name_text)

        # Do something with the selected emails (e.g., assign tasks)
        print("Selected Names: ", selected_names)

        # If all validations are completed
        self.finalize_create_task()

    def finalize_create_task(self):
        global task_name_container
        global task_requirement_container
        global task_description_container
        global task_priority_level_container
        global task_due_date_container
        global task_due_time_container
        global task_assigned_to_container
        global task_status_container

        #Confirmation message box
        confirm_msg_box = QMessageBox()
        confirm_msg_box.setIcon(QMessageBox.Warning)
        confirm_msg_box.setWindowTitle("Confirmation")
        confirm_msg_box.setText("Are you sure you want to assign this task?")
        confirm_msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        confirm_msg_box.setDefaultButton(QMessageBox.No)
        confirm_msg_box.setEscapeButton(QMessageBox.No)
        confirm_msg_box.setModal(True)
        confirm_msg_box.setWindowModality(Qt.ApplicationModal)

        task_result = confirm_msg_box.exec()
        if task_result == QMessageBox.Yes:
            new_task_name = self.task_name_edit.text()
            new_task_description = self.task_description_edit.toPlainText()
            new_task_requirement = ""
            new_task_priority_level = self.prioritylevel_combobox.currentText()
            new_task_due_date = self.due_date_edit.text()
            new_task_due_time = self.due_time_edit.text()
            new_task_assigned_to = set()
            new_task_status = "Pending"

            # Connect to the currenttask_table and pendingtask_table to add the task
            self.currenttask_table.insertRow(self.currenttask_table.rowCount())
            self.currenttask_table.setHorizontalHeaderLabels(["Task", "Requirement", "Priority Level", "Status", "Assigned To", "Due Date"])

            self.currenttask_table.setItem(self.currenttask_table.rowCount() - 1, 0, QTableWidgetItem(new_task_name))

            if self.file_radio_btn.isChecked():
                new_task_requirement = "File"
                self.currenttask_table.setItem(self.currenttask_table.rowCount() - 1, 1, QTableWidgetItem(new_task_requirement))
            elif self.weblink_radio_btn.isChecked():
                new_task_requirement = "Web Link"
                self.currenttask_table.setItem(self.currenttask_table.rowCount() - 1, 1, QTableWidgetItem(new_task_requirement))

            self.currenttask_table.setItem(self.currenttask_table.rowCount() - 1, 2, QTableWidgetItem(new_task_priority_level))
            self.currenttask_table.setItem(self.currenttask_table.rowCount() - 1, 3, QTableWidgetItem(new_task_status))
            # Collect the names of the selected members
            for row in range(self.assign_member_group_table.rowCount()):
                checkbox_item = self.assign_member_group_table.item(row, 0)
                if checkbox_item and checkbox_item.checkState() == Qt.Checked:
                    name_item = self.assign_member_group_table.item(row, 1)
                    if name_item:
                        new_task_assigned_to.add(name_item.text())

            # Update the table with the assigned names
            self.currenttask_table.setItem(self.currenttask_table.rowCount() - 1, 4, QTableWidgetItem(", ".join(new_task_assigned_to)))
            self.currenttask_table.setItem(self.currenttask_table.rowCount() - 1, 5, QTableWidgetItem(new_task_due_date + " " + new_task_due_time))

            # Same for pendingtask_table
            self.pendingtask_table.insertRow(self.pendingtask_table.rowCount())
            self.pendingtask_table.setHorizontalHeaderLabels(["Task", "Requirement", "Priority Level", "Status", "Assigned To", "Due Date"])

            self.pendingtask_table.setItem(self.pendingtask_table.rowCount() - 1, 0, QTableWidgetItem(new_task_name))

            if self.file_radio_btn.isChecked():
                new_task_requirement = "File"
                self.pendingtask_table.setItem(self.pendingtask_table.rowCount() - 1, 1, QTableWidgetItem(new_task_requirement))
            elif self.weblink_radio_btn.isChecked():
                new_task_requirement = "Web Link"
                self.pendingtask_table.setItem(self.pendingtask_table.rowCount() - 1, 1, QTableWidgetItem(new_task_requirement))

            self.pendingtask_table.setItem(self.pendingtask_table.rowCount() - 1, 2, QTableWidgetItem(new_task_priority_level))
            self.pendingtask_table.setItem(self.pendingtask_table.rowCount() - 1, 3, QTableWidgetItem(new_task_status))

            # Collect the names of the selected members
            for row in range(self.assign_member_group_table.rowCount()):
                checkbox_item = self.assign_member_group_table.item(row, 0)
                if checkbox_item and checkbox_item.checkState() == Qt.Checked:
                    name_item = self.assign_member_group_table.item(row, 1)
                    if name_item:
                        new_task_assigned_to.add(name_item.text())

            self.pendingtask_table.setItem(self.pendingtask_table.rowCount() - 1, 4, QTableWidgetItem(", ".join(new_task_assigned_to)))
            self.pendingtask_table.setItem(self.pendingtask_table.rowCount() - 1, 5, QTableWidgetItem(new_task_due_date + " " + new_task_due_time))
            
            # Clear the input fields
            self.task_name_edit.setText("")
            self.task_description_edit.setPlainText("")
            self.due_date_edit.setDate(datetime.date.today())
            self.due_time_edit.setTime(datetime.datetime.now().time())
            self.prioritylevel_combobox.setCurrentIndex(0)
            self.file_radio_btn.setChecked(False)
            self.weblink_radio_btn.setChecked(True)
            self.search_bar_assign.setText("")

            # Append data to temporary containers
            task_name_container.append(new_task_name)
            task_requirement_container.append(new_task_requirement)
            task_description_container.append(new_task_description)
            task_priority_level_container.append(new_task_priority_level)
            task_due_date_container.append(new_task_due_date)
            task_due_time_container.append(new_task_due_time)
            task_assigned_to_container.append(new_task_assigned_to)
            task_status_container.append(new_task_status)

            # Close the assign task window
            self.assign_task_window.hide()
            confirm_msg_box.close()

        elif task_result == QMessageBox.No:
            confirm_msg_box.close()
            self.show_assign_task()
            return

    def setup_employee_dashboard(self):
        self.log_out_button = self.current_dashboard.findChild(QWidget, "log_out_btn")
        if self.log_out_button:
            self.log_out_button.clicked.connect(self.log_out)

        self.stacked_Employee = self.current_dashboard.findChild(QStackedWidget, "stacked_Employee")

        self.stacked_Employee.setCurrentIndex(0)

        self.currenttask_table = self.current_dashboard.findChild(QTableWidget, "calendartask_table")
        if self.currenttask_table:
            self.currenttask_table.setColumnCount(6)
            self.currenttask_table.setHorizontalHeaderLabels(["Task", "Requirement", "Priority Level", "Status", "Assigned To", "Due Date"])
            self.currenttask_table.setVerticalHeaderLabels([])

        #Connect the tasks' temp storage
        for i in range(len(task_name_container)):
            self.currenttask_table.insertRow(i)
            self.currenttask_table.setItem(i, 0, QTableWidgetItem(task_name_container[i]))
            self.currenttask_table.setItem(i, 1, QTableWidgetItem(task_requirement_container[i]))
            self.currenttask_table.setItem(i, 2, QTableWidgetItem(task_priority_level_container[i]))
            self.currenttask_table.setItem(i, 3, QTableWidgetItem(task_status_container[i]))
            self.currenttask_table.setItem(i, 4, QTableWidgetItem(", ".join(task_assigned_to_container[i]) if isinstance(task_assigned_to_container[i], set) else task_assigned_to_container[i]))
            self.currenttask_table.setItem(i, 5, QTableWidgetItem(task_due_date_container[i] + " " + task_due_time_container[i]))


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

    def show_submit_task(self): #Next function to be created  
        selected_row = self.currenttask_table.currentRow()
        if selected_row != -1:  # Ensure a row is selected
            item = self.currenttask_table.item(selected_row, 1)
            if item and item.text() == "Web Link":
                self.submit_task()
            elif item and item.text() == "File":
                self.submit_file_task()
        else:
            no_selection_msg_box = QMessageBox()
            no_selection_msg_box.setIcon(QMessageBox.Warning)
            no_selection_msg_box.setWindowTitle("No Selection")
            no_selection_msg_box.setText("Please select a task to submit.")
            no_selection_msg_box.exec()
            return
    
    def submit_task(self):
        self.submit_task_window.show()

        selected_row = self.currenttask_table.currentRow()

        # Connection of widgets
        self.submit_name_task = self.submit_task_window.findChild(QLabel, "name_task_label_input")
        self.submit_req_task = self.submit_task_window.findChild(QLabel, "req_task_label_input")
        self.submit_prioritylevel = self.submit_task_window.findChild(QLabel, "prioritylevel_label_input")
        self.submit_description_task = self.submit_task_window.findChild(QTextBrowser, "task_description_box")
        self.submit_due_date_task = self.submit_task_window.findChild(QLabel, "duedate_label_input")
        self.submit_btn = self.submit_task_window.findChild(QPushButton, "submit_btn")
        self.cancel_btn = self.submit_task_window.findChild(QPushButton, "cancel_btn")
        self.link_requirement_edit = self.submit_task_window.findChild(QLineEdit, "link_requirement_edit")

        submit_index = selected_row

        # Connection to task storage
        if self.submit_name_task:
            self.submit_name_task.setText(task_name_container[submit_index])
        if self.submit_req_task:
            self.submit_req_task.setText(task_requirement_container[submit_index])
        if self.submit_prioritylevel:
            self.submit_prioritylevel.setText(task_priority_level_container[submit_index])
        if self.submit_description_task:
            self.submit_description_task.setText(task_description_container[submit_index])
        if self.submit_due_date_task:
            self.submit_due_date_task.setText(task_due_date_container[submit_index])

        # Buttons
        if self.submit_btn:
            self.submit_btn.clicked.connect(self.confirm_submit_task)
        if self.cancel_btn:
            self.cancel_btn.clicked.connect(self.submit_task_window.close)
            self.setup_employee_dashboard()

    def confirm_submit_task(self):
        # Message box
        confirm_msg_box = QMessageBox()
        confirm_msg_box.setIcon(QMessageBox.Warning)
        confirm_msg_box.setWindowTitle("Confirmation")
        confirm_msg_box.setText("Are you sure you want to assign this task?")
        confirm_msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        confirm_msg_box.setDefaultButton(QMessageBox.No)
        confirm_msg_box.setEscapeButton(QMessageBox.No)
        confirm_msg_box.setModal(True)
        confirm_msg_box.setWindowModality(Qt.ApplicationModal)

        submit_result = confirm_msg_box.exec()

        if submit_result == QMessageBox.Yes:
            pass # Needed More LISTS (Temporary)

    def submit_file_task(self):
        self.submit_file_task_window.show()
        # Get the task name and description
        if not self.task_name_edit.text() or not self.task_description_edit.toPlainText():
            empty_msg_box = QMessageBox()
            empty_msg_box.setIcon(QMessageBox.Warning)
            empty_msg_box.setWindowTitle("Empty Fields")
            empty_msg_box.setText("Please fill in all fields.")
            empty_msg_box.exec()
            return

        # Confirm the selected rows from the table
        selected_rows = self.currenttask_table.selectedItems()
        if not selected_rows:
            no_selection_msg_box = QMessageBox()
            no_selection_msg_box.setIcon(QMessageBox.Warning)
            no_selection_msg_box.setWindowTitle("No Selection")
            no_selection_msg_box.setText("Please select at least one task.")
            no_selection_msg_box.exec()
            return

    def show_join_group(self): # To be removed
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