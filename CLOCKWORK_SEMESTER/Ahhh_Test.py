import sys
import mysql.connector
import datetime
import webbrowser # For browsing online links
from mysql.connector import errorcode as err
from PySide6.QtWidgets import (QApplication, QWidget, QStackedWidget, QComboBox, QLineEdit, QTableWidget,
                               QTableWidgetItem, QRadioButton, QDateEdit, QTabWidget, QTimeEdit,
                               QTextEdit, QTextBrowser, QProgressBar)
from PySide6.QtWidgets import QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QMainWindow, QDialog, QFileDialog, QCalendarWidget
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, Qt, QDate, QTimer
from PySide6.QtWidgets import QMessageBox, QTableWidgetSelectionRange
from PySide6.QtGui import QColor, QPainter
from pyzkfp import ZKFP2
from PySide6.QtCharts import QChart, QChartView, QPieSeries
import time  # Import the time module for sleep function

email = "amiel.padasay004@gmail.com"
password = "amiel2004"
first_name = "Amiel John"
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

employee_email = "q@gmail.com"
employee_password = "12345678"
employee_first_name = "Quincy"
employee_last_name = "Domingo"
employee_middle_initial = "Q."
employee_suffix = ""
employee_role = "Employee"
employee_birthdate = "2004-12-29"
employee_sex = "Male"

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

completed_task_name_container = []
completed_task_requirement_container = []
completed_task_description_container = []
completed_task_priority_level_container = []
completed_task_due_date_container = []
completed_task_due_time_container = []
completed_task_assigned_to_container = []
completed_task_status_container = []

completed_task_link_container = []

email_container.append(email)
email_container.append(manager_email)
email_container.append(employee_email)

password_container.append(password)
password_container.append(manager_password)
password_container.append(employee_password)

first_name_container.append(first_name)
first_name_container.append(manager_first_name)
first_name_container.append(employee_first_name)

last_name_container.append(last_name)
last_name_container.append(manager_last_name)
last_name_container.append(employee_last_name)

middle_initial_container.append(middle_initial)
middle_initial_container.append(manager_middle_initial)
middle_initial_container.append(employee_middle_initial)

role_container.append(role)
role_container.append(manager_role)
role_container.append(employee_role)

s_container.append(sex)
s_container.append(manager_sex)
s_container.append(employee_sex)

suffix_container.append(suffix)
suffix_container.append(manager_suffix)
suffix_container.append(employee_suffix)

birthdate_container.append(birthdate)
birthdate_container.append(manager_birthdate)
birthdate_container.append(employee_birthdate)

class Clockwork_Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="amiel_2004"  # Pads_2004120 amiel_2004
        )
        self.mycursor = self.conn.cursor()
        self.initialize_database()

    def errorDisplay(self, errno, sqlstate, msg):
        print(f"Error Code: {errno}, SQL State: {sqlstate}, Message: {msg}")

    def initialize_database(self):
        try:
            # Create the database if it doesn't exist
            self.mycursor.execute("CREATE DATABASE IF NOT EXISTS ClockWork")
            self.conn.database = "ClockWork"  # Switch to the newly created database
            print("Database initialized successfully.")
        except mysql.connector.Error as err:
            self.errorDisplay(err.errno, err.sqlstate, err.msg)

    def create_users_info_table(self):
        try:
            self.mycursor.execute("""
                CREATE TABLE IF NOT EXISTS Users_Info(
                    user_id INT AUTO_INCREMENT PRIMARY KEY, 
                    username VARCHAR(255) NOT NULL, 
                    email VARCHAR(255) NOT NULL, 
                    password VARCHAR(255) NOT NULL,
                    birthdate DATE NOT NULL, 
                    role VARCHAR(50) NOT NULL, 
                    first_name VARCHAR(100) NOT NULL, 
                    last_name VARCHAR(100) NOT NULL, 
                    middle_initial VARCHAR(10),
                    suffix VARCHAR(10), 
                    sex VARCHAR(20) NOT NULL, 
                    fingerprint MEDIUMBLOB, 
                    task_id INT
                )
            """)
            print("Users_Info table created successfully.")
        except mysql.connector.Error as err:
            self.errorDisplay(err.errno, err.sqlstate, err.msg)

    def create_task_storage_table(self):
        try:
            self.mycursor.execute("""
                CREATE TABLE IF NOT EXISTS Task_Storage(
                    task_id INT AUTO_INCREMENT PRIMARY KEY, 
                    task_name VARCHAR(255) NOT NULL, 
                    task_description VARCHAR(1000) NOT NULL,
                    task_requirement VARCHAR(50) NOT NULL,
                    submitted_link VARCHAR(1000),
                    submitted_file LONGBLOB, 
                    due_date_time DATETIME NOT NULL, 
                    priority_level VARCHAR(50) NOT NULL, 
                    status VARCHAR(50) NOT NULL, 
                    submitted_date_time DATETIME, 
                    group_members VARCHAR(255) NOT NULL,
                    user_id INT
                )
            """)
            print("Task_Storage table created successfully.")
        except mysql.connector.Error as err:
            self.errorDisplay(err.errno, err.sqlstate, err.msg)

    def create_account_to_db(self, email, password, first_name, last_name, middle_initial, suffix, birthdate, sex, role):
        try:
            # Check if the email already exists in the database
            check_query = "SELECT email FROM Users_Info WHERE email = %s"
            self.mycursor.execute(check_query, (email,))
            result = self.mycursor.fetchone()
            if result:
                print("Error: An account with this email already exists.")
                return "Duplicate email detected. Account not added."

            # Normalize the email to lowercase and names to uppercase
            email = email.lower()
            first_name = first_name.upper()
            last_name = last_name.upper()
            middle_initial = middle_initial.upper()

            query = """
                INSERT INTO Users_Info (username, email, password, birthdate, role, first_name, last_name, middle_initial, suffix, sex)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = (
                f"{first_name} {last_name}",  # username
                email,
                password,
                birthdate,
                role,
                first_name,
                last_name,
                middle_initial,
                suffix,
                sex
            )
            self.mycursor.execute(query, values)
            self.conn.commit()
            print("Account successfully added to the database.")
        except mysql.connector.Error as err:
            self.errorDisplay(err.errno, err.sqlstate, err.msg)

DB = Clockwork_Database()
DB.create_users_info_table()
DB.create_task_storage_table()
DB.create_account_to_db(email, password, first_name, last_name, middle_initial, suffix, birthdate, sex, role)
DB.create_account_to_db(manager_email, manager_password, manager_first_name, manager_last_name, manager_middle_initial, manager_suffix, manager_birthdate, manager_sex, manager_role)
DB.create_account_to_db(employee_email, employee_password, employee_first_name, employee_last_name, employee_middle_initial, employee_suffix, employee_birthdate, employee_sex, employee_role)

class MainApp:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.loader = QUiLoader()
        self.current_dashboard = None
        self.create_foreign_key_relationship()

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

        self.log_in_with_fingerprint()

        self.log_in_credentials_btn = self.login_window.findChild(QWidget, "log_in_credentials_btn")
        if self.log_in_credentials_btn:
            self.log_in_credentials_btn.clicked.connect(lambda: self.log_in_stacked.setCurrentIndex(0))

        self.log_in_fingerprint_btn = self.login_window.findChild(QWidget, "log_in_fingerprint_btn")
        if self.log_in_fingerprint_btn:
            self.log_in_fingerprint_btn.clicked.connect(self.log_in_with_fingerprint)

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

    def log_in_with_fingerprint(self):
        try:
            self.log_in_stacked.setCurrentIndex(1)
            self.fingerprint_scanner = ZKFP2()
            self.fingerprint_scanner.Init()
            self.fingerprint_scanner.OpenDevice(0)
            self.fingerprint_scanner.Light("green")

            self.timer = QTimer()
            self.timer.timeout.connect(self.check_fingerprint_for_login)
            self.timer.start(100)  # Check every 100 milliseconds

        except ImportError:
            QMessageBox.critical(None, "Error", "ZKFP2 library is not installed or available.")
            return
        except Exception as e:
            QMessageBox.critical(None, "Error", f"An error occurred while initializing the fingerprint scanner: {str(e)}")
            return

    def check_fingerprint_for_login(self):
        try:
            if not hasattr(self, 'fingerprint_scanner') or not self.fingerprint_scanner:
                QMessageBox.critical(None, "Error", "Fingerprint scanner is not initialized.")
                return

            capture = self.fingerprint_scanner.AcquireFingerprint()
            if capture:
                tmp, _ = capture
                print(f"Fingerprint captured: {tmp}")  # Debugging log

                # Fetch all fingerprints from the database
                query = "SELECT email, username, password, fingerprint FROM Users_Info WHERE fingerprint IS NOT NULL"
                DB.mycursor.execute(query)
                results = DB.mycursor.fetchall()
                if results:
                    for email, username, password, fingerprint_blob in results:
                        if fingerprint_blob:
                            # Convert fingerprint_blob (bytes) to list of ints for DBMatch
                            db_template = list(fingerprint_blob)
                            # DBMatch expects two templates: enrolled and captured
                            if self.fingerprint_scanner.DBMatch(db_template, tmp) > 0:
                                if hasattr(self, 'timer') and self.timer:
                                    self.timer.stop()
                                if hasattr(self, 'fingerprint_scanner') and self.fingerprint_scanner:
                                    self.fingerprint_scanner.CloseDevice()
                                    self.fingerprint_scanner.Terminate()
                                    self.fingerprint_scanner = None
                                QMessageBox.information(None, "Login Successful", f"Welcome, {username}!")
                                self.email_lineedit.setText(email)
                                self.password_lineedit.setText(password)
                                self.load_dashboard()
                                return
                    # If no match found after checking all fingerprints
                    QMessageBox.warning(None, "Login Failed", "Fingerprint not recognized. Please try again.")
                # Only close the scanner after all matching attempts
                if hasattr(self, 'timer') and self.timer:
                    self.timer.stop()
                if hasattr(self, 'fingerprint_scanner') and self.fingerprint_scanner:
                    self.fingerprint_scanner.CloseDevice()
                    self.fingerprint_scanner.Terminate()
                    self.fingerprint_scanner = None

        except Exception as e:
            print(f"Error during fingerprint login: {str(e)}")  # Debugging log
            QMessageBox.critical(None, "Error", f"An error occurred during fingerprint login: {str(e)}")
            if hasattr(self, 'timer') and self.timer:
                self.timer.stop()
            if hasattr(self, 'fingerprint_scanner') and self.fingerprint_scanner:
                self.fingerprint_scanner.CloseDevice()
                self.fingerprint_scanner.Terminate()
                self.fingerprint_scanner = None
            return

    def setup_create_account_page(self):
        # Stop fingerprint scanner and timer if running
        if hasattr(self, 'timer') and self.timer:
            self.timer.stop()
            self.timer = None
        if hasattr(self, 'fingerprint_scanner') and self.fingerprint_scanner:
            try:
                self.fingerprint_scanner.CloseDevice()
                self.fingerprint_scanner.Terminate()
            except Exception:
                pass
            self.fingerprint_scanner = None

        self.create_account_window.setWindowTitle("Create Account")
        self.create_account_window.show()
        self.login_window.hide()

        # Inputs for user credentials
        self.email_edit = self.create_account_window.findChild(QLineEdit, "email_edit")
        self.email_edit.setMaxLength(255)

        self.last_name_edit = self.create_account_window.findChild(QLineEdit, "last_name_edit")
        self.last_name_edit.setMaxLength(100)

        self.first_name_edit = self.create_account_window.findChild(QLineEdit, "first_name_edit")
        self.first_name_edit.setMaxLength(100)

        self.middle_init_edit = self.create_account_window.findChild(QLineEdit, "middle_initial_edit")
        self.middle_init_edit.setMaxLength(10)

        self.suffix_combobox = self.create_account_window.findChild(QComboBox, "suffix_combobox")
        self.suffix_combobox.setCurrentIndex(0)

        self.birthdate_edit = self.create_account_window.findChild(QDateEdit, "birthdate_edit")

        #For sex radio buttons
        self.male_radio_btn = self.create_account_window.findChild(QRadioButton, "male_radio")
        self.male_radio_btn.setChecked(True)
        self.female_radio_btn = self.create_account_window.findChild(QRadioButton, "female_radio")
        
        self.others_radio_btn = self.create_account_window.findChild(QRadioButton, "others_radio")
        self.others_edit = self.create_account_window.findChild(QLineEdit, "others_edit")
        self.others_edit.setMaxLength(20)
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
        self.password_edit.setMaxLength(255)

        self.confirm_password_edit = self.create_account_window.findChild(QLineEdit, "confirm_password_edit")
        self.confirm_password_edit.setEchoMode(QLineEdit.Password)
        self.confirm_password_edit.setMaxLength(255)

        #Ensure that the create account edit credentials are empty

        self.email_edit.setText("")
        self.last_name_edit.setText("")
        self.first_name_edit.setText("")
        self.middle_init_edit.setText("")
        self.suffix_combobox.setCurrentIndex(0)
        self.password_edit.setText("")
        self.confirm_password_edit.setText("")
        self.birthdate_edit.setDate(datetime.date.today())

        self.change_into_log_in_button = self.create_account_window.findChild(QWidget, "change_into_log_in_button")
        if self.change_into_log_in_button:
            self.change_into_log_in_button.clicked.connect(self.show_login)

        self.create_account_button = self.create_account_window.findChild(QWidget, "create_account_button")

        if self.create_account_button:
            self.create_account_button.clicked.connect(self.validate_create_account)

    def validate_create_account(self):
        # Error handling for empty fields
        if not self.email_edit.text() or not self.last_name_edit.text() or not self.first_name_edit.text() or not self.password_edit.text() or not self.confirm_password_edit.text():
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
        
        # Check if birthdate makes the user's age above or equal to 18 years old.
        elif (datetime.date.today() - self.birthdate_edit.date().toPython()).days // 365 < 18:
            underage_msg_box = QMessageBox()
            underage_msg_box.setIcon(QMessageBox.Warning)
            underage_msg_box.setWindowTitle("Invalid Age")
            underage_msg_box.setText("You must be at least 18 years old to create an account.")
            underage_msg_box.exec()
            return

        # Check if the email already exists in the official database
        try:
            query = "SELECT email FROM Users_Info WHERE email = %s"
            DB.mycursor.execute(query, (self.email_edit.text(),))
            result = DB.mycursor.fetchone()
            if result:
                email_exists_msg_box = QMessageBox()
                email_exists_msg_box.setIcon(QMessageBox.Warning)
                email_exists_msg_box.setWindowTitle("Email Already Exists")
                email_exists_msg_box.setText("This email is already registered.")
                email_exists_msg_box.exec()
                return
            
        except mysql.connector.Error as err:
            error_msg_box = QMessageBox()
            error_msg_box.setIcon(QMessageBox.Critical)
            error_msg_box.setWindowTitle("Database Error")
            error_msg_box.setText(f"An error occurred while checking the email: {err.msg}")
            error_msg_box.exec()
            return

        # If all validations pass, store the account into the database
        self.store_into_database()

    def open_login(self):
        self.register_fingerprint_window.hide()
        self.show_login()
       
    def register_fingerprint(self):
        try:
            if self.register_fingerprint_window:
                self.register_fingerprint_window.show()
                # Set the "x" button (close event) to open the login window
                self.register_fingerprint_window.closeEvent = lambda event: (self.open_login(), event.accept())
            else:
                QMessageBox.critical(None, "Error", "Fingerprint registration window could not be loaded.")
                return

            self.skip_btn = self.register_fingerprint_window.findChild(QWidget, "skip_btn")
            if self.skip_btn:
                self.skip_btn.clicked.connect(self.open_login)
            else:
                QMessageBox.warning(None, "Error", "Skip button not found in the fingerprint window.")
                return

            self.cancel_btn = self.register_fingerprint_window.findChild(QWidget, "cancel_btn")
            if self.cancel_btn:
                self.cancel_btn.clicked.connect(self.open_login)
            else:
                QMessageBox.warning(None, "Error", "Cancel button not found in the fingerprint window.")
                return

            try:

                self.fingerprint_scanner = ZKFP2()
                self.fingerprint_scanner.Init()
                self.fingerprint_scanner.OpenDevice(0)
                self.fingerprint_scanner.Light("green")

                self.templates = []
                self.register = True

            except ImportError:
                QMessageBox.critical(None, "Error", "ZKFP2 library is not installed or available.")
                self.register_fingerprint_window.hide()
                return
            
            self.progress_bar = self.register_fingerprint_window.findChild(QProgressBar, "progress_bar")
            if self.progress_bar:
                self.progress_bar.setValue(0)
                self.progress_bar.setMaximum(3)

            self.timer = QTimer()
            self.timer.timeout.connect(self.check_fingerprint_scanner)
            self.timer.start(100)  # Check every 100 milliseconds

        except Exception as e:
            print(f"Error during fingerprint registration: {str(e)}")  # Debugging log
            QMessageBox.critical(None, "Error", f"An error occurred during fingerprint registration: {str(e)}")
            self.register_fingerprint_window.hide()
            self.open_login()
            return
        
    def check_fingerprint_scanner(self):
        try:
            self.email = self.email_edit.text()
            if not self.fingerprint_scanner:
                QMessageBox.critical(None, "Error", "Fingerprint scanner is not initialized.")
                self.register_fingerprint_window.hide()
                self.timer.stop()
                return
        
            capture = self.fingerprint_scanner.AcquireFingerprint()
            if capture:
                tmp, _ = capture
                if tmp:
                    print(f"Fingerprint captured: {tmp}")  # Debugging log
                    # Add logic to process the fingerprint data
                    if not self.templates or all(self.fingerprint_scanner.DBMatch(template, tmp) <= 0 for template in self.templates):
                        self.templates.append(tmp)
                        print(f"Fingerprint template added. Total templates: {len(self.templates)}")
                        if len(self.templates) >= 3:
                            self.timer.stop()
                            QMessageBox.information(None, "Success", "Fingerprint registration completed successfully.")
                            self.register_fingerprint_window.hide()
                            return tmp  # Return the local variable 'tmp' to make it accessible
                else:
                    print("No valid fingerprint data captured.")
        
                if len(self.templates) < 3:
                    if not self.templates or self.fingerprint_scanner.DBMatch(self.templates[-1], tmp) > 0:
                        self.fingerprint_scanner.Light("green")
                        self.templates.append(tmp)
        
                        # Update progress bar in the GUI
                        if self.progress_bar:
                            self.progress_bar.setValue(len(self.templates))
        
                            try:
                                query = """
                                            UPDATE Users_Info
                                            SET fingerprint = %s
                                            WHERE email = %s
                                    """
                                fingerprint_blob = bytes(tmp)  # Convert 'tmp' to binary format
                                if self.email:
                                    DB.mycursor.execute(query, (fingerprint_blob, self.email))
                                    DB.conn.commit()
                                else:
                                    print("Error: Email is not defined or not set.")
        
                            except mysql.connector.Error as db_err:
                                QMessageBox.critical(None, "Database Error", f"Failed to save fingerprint: {db_err.msg}")
        
                        # Stop the timer and complete registration if 3 fingerprints are captured
                        if len(self.templates) >= 3:
                            self.timer.stop()
                            QMessageBox.information(None, "Success", "Fingerprint registration completed successfully.")
                            self.register_fingerprint_window.hide()
                            self.open_login()
        
        except Exception as e:
                print(f"Error during fingerprint registration: {str(e)}")  # Debugging log
                QMessageBox.critical(None, "Error", f"An error occurred during fingerprint registration: {str(e)}")
                self.register_fingerprint_window.hide()
                self.timer.stop()
                self.open_login()
                return

    def store_into_database(self):
        self.register_fingerprint_window.hide()

        new_email = self.email_edit.text()
        new_password = self.password_edit.text()
        new_first_name = self.first_name_edit.text()
        new_last_name = self.last_name_edit.text()
        new_middle_initial = self.middle_init_edit.text()
        new_suffix = self.suffix_combobox.currentText()

        if new_suffix == "-select-":
            new_suffix = ""

        new_birthdate = self.birthdate_edit.text()

        if self.male_radio_btn.isChecked():
            selected_s = "Male"
        elif self.female_radio_btn.isChecked():
            selected_s = "Female"
        elif self.others_radio_btn.isChecked():
            selected_s = self.others_edit.text()

        # Append data to temporary containers
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

        # Insert the new account into the official database
        try:
            DB.create_account_to_db(
                email=new_email,
                password=new_password,
                first_name=new_first_name,
                last_name=new_last_name,
                middle_initial=new_middle_initial,
                suffix=new_suffix,
                birthdate=new_birthdate,
                sex=selected_s,
                role="Employee"
            )
        except mysql.connector.Error as err:
            error_msg_box = QMessageBox()
            error_msg_box.setIcon(QMessageBox.Critical)
            error_msg_box.setWindowTitle("Database Error")
            error_msg_box.setText(f"An error occurred while storing the account: {err.msg}")
            error_msg_box.exec()

        account_created_msg_box = QMessageBox()
        account_created_msg_box.setIcon(QMessageBox.Information)
        account_created_msg_box.setWindowTitle("Account Created")
        account_created_msg_box.setText("Account created successfully!")
        account_created_msg_box.exec()

        self.register_fingerprint()

        self.create_account_window.hide() # The reason for recursive message box?

    def load_dashboard(self):
        self.email = self.email_lineedit.text()
        self.password = self.password_lineedit.text()

        # Map roles to UI files
        dashboard_files = {
            "Supervisor": "dashboard_updated.ui",
            "Manager": "dashboard_manager_updated.ui",
            "Employee": "dashboard_employee_updated.ui"
        }

        try:
            # Query the database to check if the email and password match
            query = "SELECT role FROM Users_Info WHERE email = %s AND password = %s"
            DB.mycursor.execute(query, (self.email, self.password))
            result = DB.mycursor.fetchone()

            if result:
                self.role = result[0]
                ui_file_path = dashboard_files.get(self.role)

                if ui_file_path:
                    self.open_dashboard(ui_file_path)
            else:
                # Show login failed message if no match is found
                login_failed_msg_box = QMessageBox()
                login_failed_msg_box.setIcon(QMessageBox.Warning)
                login_failed_msg_box.setWindowTitle("Login Failed")
                login_failed_msg_box.setText("Invalid email or password. Please try again.")
                login_failed_msg_box.exec()
                return

        except mysql.connector.Error as err:
            # Handle database connection errors
            error_msg_box = QMessageBox()
            error_msg_box.setIcon(QMessageBox.Critical)
            error_msg_box.setWindowTitle("Database Error")
            error_msg_box.setText(f"An error occurred while connecting to the database: {err.msg}")
            error_msg_box.exec()
            return

    def open_dashboard(self, ui_file_path):
        self.email = self.email_lineedit.text()
        self.password = self.password_lineedit.text()

        try:
            # Query the database to get the role of the user
            query = "SELECT role FROM Users_Info WHERE email = %s AND password = %s"
            DB.mycursor.execute(query, (self.email, self.password))
            result = DB.mycursor.fetchone()

            if result:
                self.role = result[0]  # Extract the role from the query result
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
            else:
                # Show error message if no matching user is found
                error_msg_box = QMessageBox()
                error_msg_box.setIcon(QMessageBox.Warning)
                error_msg_box.setWindowTitle("Login Failed")
                error_msg_box.setText("Invalid email or password. Please try again.")
                error_msg_box.exec()

        except mysql.connector.Error as err:
            # Handle database connection errors
            error_msg_box = QMessageBox()
            error_msg_box.setIcon(QMessageBox.Critical)
            error_msg_box.setWindowTitle("Database Error")
            error_msg_box.setText(f"An error occurred while connecting to the database: {err.msg}")
            error_msg_box.exec()

    #Supervisor's Menu
    def setup_supervisor_dashboard(self):

        # Fetch data from Users_Info table
        try:
            query = "SELECT first_name, last_name, email, role FROM Users_Info"
            DB.mycursor.execute(query)
            users_info = DB.mycursor.fetchall()
        except mysql.connector.Error as err:
            QMessageBox.critical(self.current_dashboard, "Database Error", f"An error occurred while fetching user data: {err.msg}")
            return

        self.user_table = self.current_dashboard.findChild(QTableWidget, "users_table")
        if self.user_table:
            self.user_table.setRowCount(len(users_info))
            self.user_table.setColumnCount(3)
            self.user_table.setHorizontalHeaderLabels(["Name", "Email", "Role"])
            self.user_table.setVerticalHeaderLabels([])

            # Populate the table with data from the database
            for i, (first_name, last_name, email, role) in enumerate(users_info):
                self.user_table.setItem(i, 0, QTableWidgetItem(f"{first_name} {last_name}"))
                self.user_table.setItem(i, 1, QTableWidgetItem(email))
                self.user_table.setItem(i, 2, QTableWidgetItem(role))

        # Fetch data from Task_Storage table
        try:
            query = "SELECT task_name, task_requirement, priority_level, status, group_members, due_date_time FROM Task_Storage"
            DB.mycursor.execute(query)
            tasks_info = DB.mycursor.fetchall()
        except mysql.connector.Error as err:
            QMessageBox.critical(self.current_dashboard, "Database Error", f"An error occurred while fetching task data: {err.msg}")
            return

        self.currenttask_table = self.current_dashboard.findChild(QTableWidget, "currenttask_table")
        if self.currenttask_table:
            current_tasks = [task for task in tasks_info if task[3] in ["Pending", "Completed - Not Validated"]]  # Filter tasks with status "Pending"
            self.currenttask_table.setRowCount(len(current_tasks))
            self.currenttask_table.setColumnCount(6)
            self.currenttask_table.setHorizontalHeaderLabels(["Task", "Requirement", "Priority Level", "Status", "Assigned To", "Due Date"])

            for i, (task_name, task_requirement, priority_level, status, group_members, due_date_time) in enumerate(current_tasks):
                self.currenttask_table.setItem(i, 0, QTableWidgetItem(task_name))
                self.currenttask_table.setItem(i, 1, QTableWidgetItem(task_requirement))
                self.currenttask_table.setItem(i, 2, QTableWidgetItem(priority_level))
                self.currenttask_table.setItem(i, 3, QTableWidgetItem(status))
                self.currenttask_table.setItem(i, 4, QTableWidgetItem(group_members))
                self.currenttask_table.setItem(i, 5, QTableWidgetItem(str(due_date_time)))

        # Similar setup for pending and completed task tables
        self.pendingtask_table = self.current_dashboard.findChild(QTableWidget, "pendingtasks_table")
        self.completedtask_table = self.current_dashboard.findChild(QTableWidget, "completedtasks_table")

        if self.pendingtask_table:
            pending_tasks = [task for task in tasks_info if task[3] in "Pending"]  # Filter tasks with status "Pending"
            self.pendingtask_table.setRowCount(len(pending_tasks))
            self.pendingtask_table.setColumnCount(6)
            self.pendingtask_table.setHorizontalHeaderLabels(["Task", "Requirement", "Priority Level", "Status", "Assigned To", "Due Date"])

            for i, (task_name, task_requirement, priority_level, status, group_members, due_date_time) in enumerate(pending_tasks):
                if status == "Pending":
                    self.pendingtask_table.setItem(i, 0, QTableWidgetItem(task_name))
                    self.pendingtask_table.setItem(i, 1, QTableWidgetItem(task_requirement))
                    self.pendingtask_table.setItem(i, 2, QTableWidgetItem(priority_level))
                    self.pendingtask_table.setItem(i, 3, QTableWidgetItem(status))
                    self.pendingtask_table.setItem(i, 4, QTableWidgetItem(group_members))
                    self.pendingtask_table.setItem(i, 5, QTableWidgetItem(str(due_date_time)))

        if self.completedtask_table:
            completed_tasks = [task for task in tasks_info if task[3] in ["Completed - Not Validated", "Completed - Validated"]]  # Filter tasks with completed status
            self.completedtask_table.setRowCount(len(completed_tasks))
            self.completedtask_table.setColumnCount(6)
            self.completedtask_table.setHorizontalHeaderLabels(["Task", "Requirement", "Priority Level", "Status", "Assigned To", "Due Date"])

            for i, (task_name, task_requirement, priority_level, status, group_members, due_date_time) in enumerate(completed_tasks):
                if status.startswith("Completed"):
                    self.completedtask_table.setItem(i, 0, QTableWidgetItem(task_name))
                    self.completedtask_table.setItem(i, 1, QTableWidgetItem(task_requirement))
                    self.completedtask_table.setItem(i, 2, QTableWidgetItem(priority_level))
                    self.completedtask_table.setItem(i, 3, QTableWidgetItem(status))
                    self.completedtask_table.setItem(i, 4, QTableWidgetItem(group_members))
                    self.completedtask_table.setItem(i, 5, QTableWidgetItem(str(due_date_time)))

        # Connect buttons and other UI elements as before
        self.stacked_supervisor = self.current_dashboard.findChild(QStackedWidget, "stacked_Supervisor")

        self.stacked_supervisor.setCurrentIndex(0)

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

        self.number_tasks_label = self.current_dashboard.findChild(QLabel, "number_tasks_label")
        if self.number_tasks_label:
            self.update_task_count()

        self.search_bar_tasks = self.current_dashboard.findChild(QLineEdit, "search_bar_tasks")
        self.search_btn = self.current_dashboard.findChild(QPushButton, "search_btn")
        
        if self.search_btn:
            self.search_btn.clicked.connect(self.search_tasks)

        self.search_bar_users = self.current_dashboard.findChild(QLineEdit, "search_bar_users")

        self.search_user_btn = self.current_dashboard.findChild(QPushButton, "search_user_btn")
        if self.search_user_btn:
            self.search_user_btn.clicked.connect(self.search_users)

        self.task_calendar = self.current_dashboard.findChild(QCalendarWidget, "Task_Calendar_2")
        if self.task_calendar:
            self.color_code_calendar_by_priority()

        self.task_calendar_2 = self.current_dashboard.findChild(QCalendarWidget, "Task_Calendar")
        if self.task_calendar_2:
            self.task_calendar_2.selectionChanged.connect(self.show_tasks_for_selected_date)
            self.color_code_calendar_by_priority_2()

        # Call the function to display the pie chart
        self.show_task_completion_pie_chart()

        self.change_role_btn = self.current_dashboard.findChild(QWidget, "change_role_btn")
        if self.change_role_btn:
            self.change_role_btn.clicked.connect(self.show_select_role_with_data)

        self.validate_btn = self.current_dashboard.findChild(QWidget, "validatetask_btn")
        if self.validate_btn:
            self.validate_btn.clicked.connect(self.validate_task)

        self.profile_btn = self.current_dashboard.findChild(QWidget, "profile_button")
        if self.profile_btn:
            self.profile_btn.clicked.connect(self.show_profile)

        self.log_out_button = self.current_dashboard.findChild(QWidget, "log_out_btn")
        if self.log_out_button:
            self.log_out_button.clicked.connect(self.log_out)

        self.validate_btn = self.current_dashboard.findChild(QWidget, "validatetask_btn")
        self.task_tab = self.current_dashboard.findChild(QTabWidget, "task_tab")
        if self.task_tab:
            self.task_tab.currentChanged.connect(self.update_validate_btn_visibility)
            self.update_validate_btn_visibility(self.task_tab.currentIndex())
        else:
            print("Error: task_tab not found.")

    def show_task_completion_pie_chart(self):
        # Fetch task completion data from the database
        try:
            query = """
                        SELECT status, COUNT(*) as count
                        FROM Task_Storage
                        GROUP BY status
                    """
            DB.mycursor.execute(query)
            task_data = DB.mycursor.fetchall()

            # Check if there is any data in Task_Storage
            if not task_data:
                # If no data, create a QLabel and add it to the group box
                self.task_completion_groupbox = self.current_dashboard.findChild(QWidget, "task_completion_groupbox")
                if self.task_completion_groupbox:
                    layout = QVBoxLayout(self.task_completion_groupbox)
                    no_data_label = QLabel("No task data available.")
                    no_data_label.setAlignment(Qt.AlignCenter)
                    layout.addWidget(no_data_label)
                    self.task_completion_groupbox.setLayout(layout)
                return

            # Create a pie series
            self.series = QPieSeries()
            for status, count in task_data:
                self.series.append(f"{status} ({count})", count)

            # Create a chart and add the series
            self.chart = QChart()
            self.chart.addSeries(self.series)
            self.chart.setTitle("Task Completion Status")
            self.chart.legend().setVisible(True)
            self.chart.legend().setAlignment(Qt.AlignBottom)

            # Create a chart view and set it in the group box
            self.chart_view = QChartView(self.chart)
            self.chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)
            self.chart_view.setMinimumSize(400, 300)  # Set a larger minimum size for the chart

            # Find the group box and add the chart view
            self.task_completion_groupbox = self.current_dashboard.findChild(QWidget, "task_completion_groupbox")
            if self.task_completion_groupbox:
                layout = QVBoxLayout(self.task_completion_groupbox)
                layout.addWidget(self.chart_view)
                self.task_completion_groupbox.setLayout(layout)

        except mysql.connector.Error as err:
            QMessageBox.critical(self.current_dashboard, "Database Error", f"An error occurred while fetching task data: {err.msg}")


    def search_tasks(self):
        search_text = self.search_bar_tasks.text().strip().lower()
        if self.pendingtask_table:
            for row in range(self.pendingtask_table.rowCount()):
                match_found = False
                for col in range(self.pendingtask_table.columnCount()):
                    item = self.pendingtask_table.item(row, col)
                    if item and search_text in item.text().strip().lower():
                        match_found = True
                        break
                self.pendingtask_table.setRowHidden(row, not match_found)

        if self.completedtask_table:
            for row in range(self.completedtask_table.rowCount()):
                match_found = False
                for col in range(self.completedtask_table.columnCount()):
                    item = self.completedtask_table.item(row, col)
                    if item and search_text in item.text().strip().lower():
                        match_found = True
                        break
                self.completedtask_table.setRowHidden(row, not match_found)
    
    def search_users(self):
        search_text = self.search_bar_users.text().strip().lower()
        if self.user_table:
            for row in range(self.user_table.rowCount()):
                match_found = False
                for col in range(self.user_table.columnCount()):
                    item = self.user_table.item(row, col)
                    if item and search_text in item.text().strip().lower():
                        match_found = True
                        break
                self.user_table.setRowHidden(row, not match_found)

    def update_task_count(self):
        try:
            query = "SELECT COUNT(*) FROM Task_Storage"
            DB.mycursor.execute(query)
            result = DB.mycursor.fetchone()
            if result:
                self.number_tasks_label.setText(f"Total Tasks: {result[0]}")
            else:
                self.number_tasks_label.setText("Total Tasks: 0")
        except mysql.connector.Error as err:
            QMessageBox.critical(self.current_dashboard, "Database Error", f"An error occurred while fetching task count: {err.msg}")
    
    def update_validate_btn_visibility(self, index):
        if self.validate_btn:
            if index == 1:
                self.validate_btn.hide()
            elif index == 0:
                self.validate_btn.show()

    def open_link_browser(self):
        link = self.link_submitted_input.text()
        if link and link != "No link available":
            webbrowser.open(link)
        else:
            no_link_msg_box = QMessageBox()
            no_link_msg_box.setIcon(QMessageBox.Warning)
            no_link_msg_box.setWindowTitle("No Link Provided")
            no_link_msg_box.setText("No link is available to open.")
            no_link_msg_box.exec()

    def validate_task(self):
        self.validate_task_window.show()

        # Connection of widgets
        self.validate_name_task = self.validate_task_window.findChild(QLabel, "taskname_label")
        self.validate_req_task = self.validate_task_window.findChild(QLabel, "req_task_label_input")
        self.validate_prioritylevel = self.validate_task_window.findChild(QLabel, "prioritylevel_label_input")
        self.validate_description_task = self.validate_task_window.findChild(QTextBrowser, "des_task_view")
        self.validate_due_date_task = self.validate_task_window.findChild(QLabel, "duedate_label_input")
        self.link_submitted_input = self.validate_task_window.findChild(QLabel, "link_submitted_input")
        self.link_submitted_label = self.validate_task_window.findChild(QLabel, "link_submitted_label")
        self.download_file_btn = self.validate_task_window.findChild(QPushButton, "download_file_btn")
        self.open_link_btn = self.validate_task_window.findChild(QPushButton, "openlink_btn")
        self._validate_btn = self.validate_task_window.findChild(QPushButton, "validate_task_btn")
        self.cancel_btn = self.validate_task_window.findChild(QPushButton, "cancel_btn")

        selected_row = self.completedtask_table.currentRow()

        if selected_row != -1:  # Ensure a row is selected
            try:
                # Fetch the task details from the database
                query = """
                    SELECT task_name, task_requirement, priority_level, task_description, due_date_time, submitted_link, submitted_file
                    FROM Task_Storage
                    WHERE status = 'Completed - Not Validated'
                    LIMIT 1 OFFSET %s
                """
                DB.mycursor.execute(query, (selected_row,))
                result = DB.mycursor.fetchone()

                if result:
                    task_name, task_requirement, priority_level, task_description, due_date_time, submitted_link, submitted_file = result
                    if self.validate_name_task:
                        self.validate_name_task.setText(task_name)
                    if self.validate_req_task:
                        self.validate_req_task.setText(task_requirement)
                    if self.validate_prioritylevel:
                        self.validate_prioritylevel.setText(priority_level)
                    if self.validate_description_task:
                        self.validate_description_task.setText(task_description)
                    if self.validate_due_date_task:
                        self.validate_due_date_task.setText(str(due_date_time))

                    # Handle task requirement type
                    if task_requirement == "Web Link":
                        if self.link_submitted_label:
                            self.link_submitted_label.setText("Link Submitted:")
                        if self.link_submitted_input:
                            self.link_submitted_input.setText(submitted_link if submitted_link else "No link available")
                        if self.open_link_btn:
                            self.open_link_btn.show()
                            self.open_link_btn.clicked.connect(self.open_link_browser)
                        if self.download_file_btn:
                            self.download_file_btn.hide()

                    elif task_requirement == "File":
                        if self.link_submitted_label:
                            self.link_submitted_label.setText("File Submitted:")
                        if self.link_submitted_input:
                            self.link_submitted_input.setText(submitted_file.name if hasattr(submitted_file, 'name') else (submitted_file if isinstance(submitted_file, str) else "Submitted File"))
                        if self.download_file_btn:
                            self.download_file_btn.show()
                            self.download_file_btn.clicked.connect(self.download_file)
                        if self.open_link_btn:
                            self.open_link_btn.hide()
                    else:
                        if self.link_submitted_input:
                            self.link_submitted_input.setText("No submission available")
                        if self.download_file_btn:
                            self.download_file_btn.hide()
                        if self.open_link_btn:
                            self.open_link_btn.hide()
                else:
                    QMessageBox.warning(self.validate_task_window, "Error", "Task not found in the database.")
            except mysql.connector.Error as err:
                QMessageBox.critical(self.validate_task_window, "Database Error", f"An error occurred while fetching task details: {err.msg}")
        else:
            QMessageBox.warning(self.validate_task_window, "Error", "No task selected.")

        # Buttons
        if self._validate_btn:
            self._validate_btn.clicked.connect(self.confirm_validate_task)
        if self.cancel_btn:
            self.cancel_btn.clicked.connect(self.validate_task_window.close)

    def download_file(self): # Need to read file type
        selected_row = self.completedtask_table.currentRow()
        validate_index = selected_row

        try:
            # Fetch the submitted file and its name from the database
            query = """
                SELECT submitted_file, task_name
                FROM Task_Storage
                WHERE status = 'Completed - Not Validated'
                LIMIT %s, 1
            """
            DB.mycursor.execute(query, (validate_index,))
            result = DB.mycursor.fetchone()

            if result and result[0]:
                file_data = result[0]
                task_name = result[1]

                # Use QFileDialog to save the file
                file_dialog = QFileDialog()
                suggested_name = f"{task_name}"
                save_path, _ = file_dialog.getSaveFileName(self.validate_task_window, "Save File", suggested_name, "All Files (*)")

                if save_path:
                    with open(save_path, "wb") as file:
                        file.write(file_data)
                    QMessageBox.information(self.validate_task_window, "File Downloaded", f"The file has been successfully downloaded as {suggested_name}.")
                else:
                    QMessageBox.warning(self.validate_task_window, "Download Cancelled", "The file download was cancelled.")
            else:
                QMessageBox.warning(self.validate_task_window, "Error", "No file available for download.")
        except mysql.connector.Error as err:
            QMessageBox.critical(self.validate_task_window, "Database Error", f"An error occurred: {err.msg}")
        except Exception as e:
            QMessageBox.critical(self.validate_task_window, "Error", f"An unexpected error occurred: {str(e)}")

    def confirm_validate_task(self):
        selected_row = self.completedtask_table.currentRow()
        validate_index = selected_row

        valid_msg_box = QMessageBox()
        valid_msg_box.setIcon(QMessageBox.Warning)
        valid_msg_box.setWindowTitle("Confirmation")
        valid_msg_box.setText("Are you sure you want to validate this task?")
        valid_msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        valid_msg_box.setDefaultButton(QMessageBox.No)
        valid_msg_box.setEscapeButton(QMessageBox.No)
        valid_msg_box.setModal(True)
        valid_msg_box.setWindowModality(Qt.ApplicationModal)

        valid_result = valid_msg_box.exec()

        if valid_result == QMessageBox.Yes:
            try:
                # Update the task status in the database
                # Fetch the task_name first to avoid subquery issues
                fetch_task_query = """
                    SELECT task_name
                    FROM Task_Storage
                    WHERE status = 'Completed - Not Validated'
                    LIMIT %s, 1
                """
                DB.mycursor.execute(fetch_task_query, (validate_index,))
                task_name_result = DB.mycursor.fetchone()

                if task_name_result:
                    task_name = task_name_result[0]
                    update_query = """
                        UPDATE Task_Storage
                        SET status = %s
                        WHERE task_name = %s
                    """
                DB.mycursor.execute(update_query, ("Completed - Validated", task_name))
                DB.conn.commit()

                # Update the status in the completed task table
                self.completedtask_table.setItem(validate_index, 3, QTableWidgetItem("Completed - Validated"))

                # Show success message
                success_msg_box = QMessageBox()
                success_msg_box.setIcon(QMessageBox.Information)
                success_msg_box.setWindowTitle("Task Validated")
                success_msg_box.setText("The task has been successfully validated.")
                success_msg_box.exec()

                self.validate_task_window.close()
                self.setup_supervisor_dashboard() # Last Change

            except mysql.connector.Error as err:
                error_msg_box = QMessageBox()
                error_msg_box.setIcon(QMessageBox.Critical)
                error_msg_box.setWindowTitle("Database Error")
                error_msg_box.setText(f"An error occurred while validating the task: {err.msg}")
                error_msg_box.exec()
        
        elif valid_result == QMessageBox.No:
            valid_msg_box.close()
            self.validate_task()

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

        self.register_fingerprint_btn = self.profile_window.findChild(QPushButton, "register_fingerprint_btn")
        if self.register_fingerprint_btn:
            self.register_fingerprint_btn.setText("Change Fingerprint")
            self.register_fingerprint_btn.clicked.connect(self.change_fingerprint)

        self.edit_profile_btn = self.profile_window.findChild(QWidget, "edit_profile_btn")
        if self.edit_profile_btn:
            self.edit_profile_btn.clicked.connect(self.show_edit_profile)

        # Make the labels have their name, role, email, sex and birthdate according to their index
        self.email = self.email_lineedit.text()
        self.password = self.password_lineedit.text()

        try:
            # Query the database to get the user's credentials
            query = """
                SELECT first_name, last_name, middle_initial, suffix, role, sex, birthdate, email
                FROM Users_Info
                WHERE email = %s AND password = %s
            """
            DB.mycursor.execute(query, (self.email, self.password))
            result = DB.mycursor.fetchone()

            if result:
                first_name, last_name, middle_initial, suffix, role, sex, birthdate, email = result

                self.name_label = self.profile_window.findChild(QLabel, "name_label")
                if self.name_label:
                    self.name_label.setText(f"Name: {first_name} {middle_initial or ''} {last_name} {suffix or ''}")

                self.role_label = self.profile_window.findChild(QLabel, "role_label")
                if self.role_label:
                    self.role_label.setText(f"Role: {role}")

                self.age_and_sex_label = self.profile_window.findChild(QLabel, "age_and_sex_Label")
                if self.age_and_sex_label:
                    self.age_and_sex_label.setText(f"Age: {self.calculate_age(birthdate)} years old\n\nSex: {sex}")

                self.email_label = self.profile_window.findChild(QLabel, "email_label_2")
                if self.email_label:
                    self.email_label.setText(email)

                self.birthdate_label = self.profile_window.findChild(QLabel, "birthdate_label_2")
                if self.birthdate_label:
                    self.birthdate_label.setText(str(birthdate))
            else:
                error_msg_box = QMessageBox()
                error_msg_box.setIcon(QMessageBox.Warning)
                error_msg_box.setWindowTitle("Error")
                error_msg_box.setText("User credentials not found in the database.")
                error_msg_box.exec()

        except mysql.connector.Error as err:
            error_msg_box = QMessageBox()
            error_msg_box.setIcon(QMessageBox.Critical)
            error_msg_box.setWindowTitle("Database Error")
            error_msg_box.setText(f"An error occurred while fetching user credentials: {err.msg}")
            error_msg_box.exec()

    def calculate_age(self, birthdate):
        if isinstance(birthdate, str):
            birthdate = datetime.datetime.strptime(birthdate, "%Y-%m-%d").date()
        today = datetime.date.today()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return age    

    def show_edit_profile(self):
        self.edit_profile_window.show()

        # Connection of widgets
        self.edit_first_name = self.edit_profile_window.findChild(QLineEdit, "new_first_name_edit")
        self.edit_first_name.setMaxLength(100)

        self.edit_last_name = self.edit_profile_window.findChild(QLineEdit, "new_last_name_edit")
        self.edit_last_name.setMaxLength(100)

        self.edit_middle_initial = self.edit_profile_window.findChild(QLineEdit, "new_middle_initial_edit")
        self.edit_middle_initial.setMaxLength(10)

        self.edit_suffix = self.edit_profile_window.findChild(QComboBox, "suffix_combobox")
        self.edit_suffix.setCurrentIndex(0)

        self.new_male_radio = self.edit_profile_window.findChild(QRadioButton, "new_male_radio")
        self.new_female_radio = self.edit_profile_window.findChild(QRadioButton, "new_female_radio")
        self.new_others_radio = self.edit_profile_window.findChild(QRadioButton, "new_others_radio")
        
        self.new_others_edit = self.edit_profile_window.findChild(QLineEdit, "new_others_edit")
        self.new_others_edit.setMaxLength(20)
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

        try:
            # Query the database to fetch user information
            query = """
                SELECT first_name, last_name, middle_initial, suffix, sex, birthdate
                FROM Users_Info
                WHERE email = %s
            """
            DB.mycursor.execute(query, (self.email,))
            result = DB.mycursor.fetchone()

            if result:
                first_name, last_name, middle_initial, suffix, sex, birthdate = result
                self.edit_first_name.setText(first_name)
                self.edit_last_name.setText(last_name)
                self.edit_middle_initial.setText(middle_initial)
                self.edit_suffix.setCurrentText(suffix if suffix else "-select-")
                
                if isinstance(birthdate, str):
                    try:
                        parsed_date = datetime.datetime.strptime(birthdate.strip(), "%Y-%m-%d").date()
                        self.edit_birthdate.setDate(QDate(parsed_date.year, parsed_date.month, parsed_date.day))
                    except ValueError:
                        QMessageBox.warning(self.edit_profile_window, "Invalid Date Format", "The birthdate format is invalid. Setting to today's date.")
                        self.edit_birthdate.setDate(QDate.currentDate())

                elif isinstance(birthdate, datetime.date):
                    self.edit_birthdate.setDate(QDate(birthdate.year, birthdate.month, birthdate.day))

                elif isinstance(birthdate, datetime.datetime):
                    self.edit_birthdate.setDate(QDate(birthdate.year, birthdate.month, birthdate.day))

                else:
                    QMessageBox.warning(self.edit_profile_window, "Missing Birthdate", "The birthdate is missing or invalid. Setting to today's date.")
                    self.edit_birthdate.setDate(QDate.currentDate())

                sex = sex.strip().lower()
                if sex == "male":
                    self.new_male_radio.setChecked(True)
                    self.new_female_radio.setChecked(False)
                    if self.new_others_radio:
                        self.new_others_radio.setChecked(False)
                        self.new_others_edit.clear()
                elif sex == "female":
                    self.new_male_radio.setChecked(False)
                    self.new_female_radio.setChecked(True)
                    if self.new_others_radio:
                        self.new_others_radio.setChecked(False)
                        self.new_others_edit.clear()
                elif sex:  # Handle non-empty, non-standard values
                    if self.new_others_radio:
                        self.new_others_radio.setChecked(True)
                        self.new_others_edit.setText(sex)
            else:
                QMessageBox.warning(self.edit_profile_window, "Error", "User data not found in the database.")

        except mysql.connector.Error as err:
            QMessageBox.critical(self.edit_profile_window, "Database Error", f"An error occurred: {err.msg}")

        self.save_changes_button = self.edit_profile_window.findChild(QPushButton, "save_changes_btn")
        self.cancel_btn = self.edit_profile_window.findChild(QPushButton, "new_cancel_btn")
        
        if self.save_changes_button:
            self.save_changes_button.clicked.connect(self.save_changes_with_profile)

        if self.cancel_btn:
            self.cancel_btn.clicked.connect(self.edit_profile_window.close)

    def save_changes_with_profile(self):

        if not self.edit_first_name.text().strip() or not self.edit_last_name.text().strip():
            empty_fields_msg_box = QMessageBox()
            empty_fields_msg_box.setIcon(QMessageBox.Warning)
            empty_fields_msg_box.setWindowTitle("Empty Fields")
            empty_fields_msg_box.setText("First Name and Last Name cannot be empty.")
            empty_fields_msg_box.exec()
            return

        if self.new_others_radio.isChecked():
            if self.new_others_edit.text().strip() == "":
                others_empty_msg_box = QMessageBox()
                others_empty_msg_box.setIcon(QMessageBox.Warning)
                others_empty_msg_box.setWindowTitle("Empty Field")
                others_empty_msg_box.setText("Please enter your credentials on Others.")
                others_empty_msg_box.exec()
                return

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

        if result == QMessageBox.Yes:
            try:
                index = email_container.index(self.email)
                new_first_name = self.edit_first_name.text()
                new_last_name = self.edit_last_name.text()
                new_middle_initial = self.edit_middle_initial.text()
                new_suffix = self.edit_suffix.currentText()
                new_birthdate = self.edit_birthdate.text()

                if self.new_male_radio.isChecked():
                    new_s = "Male"
                elif self.new_female_radio.isChecked():
                    new_s = "Female"
                elif self.new_others_radio.isChecked():
                    if self.new_others_edit:
                        new_s = self.new_others_edit.text()

                # Update temporary containers 
                # Keep an eye
                first_name_container[index] = new_first_name
                last_name_container[index] = new_last_name
                middle_initial_container[index] = new_middle_initial
                suffix_container[index] = new_suffix
                birthdate_container[index] = new_birthdate
                s_container[index] = new_s

                # Update the official database
                update_query = """
                    UPDATE Users_Info
                    SET first_name = %s, last_name = %s, middle_initial = %s, suffix = %s, birthdate = %s, sex = %s
                    WHERE email = %s
                """
                update_values = (
                    new_first_name,
                    new_last_name,
                    new_middle_initial,
                    new_suffix if new_suffix != "-select-" else "",
                    new_birthdate,
                    new_s,
                    self.email
                )
                DB.mycursor.execute(update_query, update_values)
                DB.conn.commit()

                # Close the edit profile window and refresh the profile view
                self.edit_profile_window.close()
                self.show_profile()

                # Show success message
                success_msg_box = QMessageBox()
                success_msg_box.setIcon(QMessageBox.Information)
                success_msg_box.setWindowTitle("Profile Updated")
                success_msg_box.setText("Your profile has been successfully updated.")
                success_msg_box.exec()

            except mysql.connector.Error as err:
                error_msg_box = QMessageBox()
                error_msg_box.setIcon(QMessageBox.Critical)
                error_msg_box.setWindowTitle("Database Error")
                error_msg_box.setText(f"An error occurred while updating your profile: {err.msg}")
                error_msg_box.exec()

        elif result == QMessageBox.No:
            save_change_msg_box.close()
            self.show_edit_profile()

    def change_fingerprint(self):
        try:
            if self.register_fingerprint_window:
                self.register_fingerprint_window.show()
            else:
                QMessageBox.critical(None, "Error", "Fingerprint change window could not be loaded.")
                return

            self.skip_btn = self.register_fingerprint_window.findChild(QWidget, "skip_btn")
            if self.skip_btn:
                self.skip_btn.clicked.connect(self.register_fingerprint_window.close)

            else:
                QMessageBox.warning(None, "Error", "Skip button not found in the fingerprint window.")
                return

            self.cancel_btn = self.register_fingerprint_window.findChild(QWidget, "cancel_btn")
            if self.cancel_btn:
                self.cancel_btn.clicked.connect(self.register_fingerprint_window.close)
            else:
                QMessageBox.warning(None, "Error", "Cancel button not found in the fingerprint window.")
                return

            self.register_fingerprint_window.setWindowTitle("Change Fingerprint")
            instruction_label = self.register_fingerprint_window.findChild(QLabel, "label")
            if instruction_label:
                instruction_label.setText("Please put your finger to the scanner to change your fingerprint.")

            try:
                self.fingerprint_scanner = ZKFP2()
                self.fingerprint_scanner.Init()
                self.fingerprint_scanner.OpenDevice(0)
                self.fingerprint_scanner.Light("green")

                self.templates = []
                self.register = True

            except ImportError:
                QMessageBox.critical(None, "Error", "ZKFP2 library is not installed or available.")
                self.register_fingerprint_window.hide()
                return

            self.progress_bar = self.register_fingerprint_window.findChild(QProgressBar, "progress_bar")
            if self.progress_bar:
                self.progress_bar.setValue(0)
                self.progress_bar.setMaximum(3)

            self.timer = QTimer()
            self.timer.timeout.connect(self.check_fingerprint_scanner_for_change)
            self.timer.start(100)  # Check every 100 milliseconds

        except Exception as e:
            print(f"Error during fingerprint change: {str(e)}")  # Debugging log
            QMessageBox.critical(None, "Error", f"An error occurred during fingerprint change: {str(e)}")
            self.register_fingerprint_window.hide()
            return

    def check_fingerprint_scanner_for_change(self):
        try:
            self.email = self.email_edit.text()
            if not self.fingerprint_scanner:
                QMessageBox.critical(None, "Error", "Fingerprint scanner is not initialized.")
                self.register_fingerprint_window.hide()
                self.timer.stop()
                return

            capture = self.fingerprint_scanner.AcquireFingerprint()
            if capture:
                tmp, _ = capture
                if tmp:  # Ensure tmp is not None or empty
                    print(f"Fingerprint captured: {tmp}")  # Debugging log

                    if len(self.templates) < 3:
                        if not self.templates or self.fingerprint_scanner.DBMatch(self.templates[-1], tmp) > 0:
                            self.fingerprint_scanner.Light("green")
                            self.templates.append(tmp)

                # Update progress bar in the GUI
                if self.progress_bar:
                    self.progress_bar.setValue(len(self.templates))

                try:
                    query = """
                        UPDATE Users_Info
                        SET fingerprint = %s
                        WHERE email = %s
                    """
                    fingerprint_blob = bytes(tmp)  # Convert 'tmp' to binary format

                    if self.email:
                        DB.mycursor.execute(query, (fingerprint_blob, self.email))
                        DB.conn.commit()
                    else:
                        print("Error: Email is not defined or not set.")

                except mysql.connector.Error as db_err:
                    QMessageBox.critical(None, "Database Error", f"Failed to save fingerprint: {db_err.msg}")

                # Stop the timer and complete registration if 3 fingerprints are captured
                if len(self.templates) >= 3:
                    self.timer.stop()
                    QMessageBox.information(None, "Success", "Fingerprint change completed successfully.")
                    self.register_fingerprint_window.hide()

        except Exception as e:
            print(f"Error during fingerprint change: {str(e)}")  # Debugging log
            QMessageBox.critical(None, "Error", f"An error occurred during fingerprint change: {str(e)}")
            self.register_fingerprint_window.hide()
            self.timer.stop()
            return

    def show_select_role_with_data(self): # Update the database with role changes
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

        if self.name != "AMIEL JOHN PADASAY":
            self.show_select_role()
        else:  
            no_change_msg_box = QMessageBox()
            no_change_msg_box.setIcon(QMessageBox.Warning)
            no_change_msg_box.setWindowTitle("Invalid Action")
            no_change_msg_box.setText("You cannot change the role of this user.")
            no_change_msg_box.exec()
            self.select_role_window.hide()

    def save_role_changes(self): # Save role changes to the database

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
                email_item = self.user_table.item(selected_row, 1)

            if name_item and role_item and email_item:
                name = name_item.text()
                role = role_item.text()
                email = email_item.text()

            # Determine the new role based on the selected radio button
            if self.supervisor_radio_btn.isChecked():
                new_role = "Supervisor"
            elif self.manager_radio_btn.isChecked():
                new_role = "Manager"
            elif self.employee_radio_btn.isChecked():
                new_role = "Employee"
            else:
                new_role = role  # Default to the current role if no selection is made

            # Update the role in the table
            if role_item:
                role_item.setText(new_role)

            # Update the role in the database
            try:
                update_query = """
                    UPDATE Users_Info
                    SET role = %s
                    WHERE email = %s
                """
                DB.mycursor.execute(update_query, (new_role, email))
                DB.conn.commit()

                # Show success message
                success_msg_box = QMessageBox()
                success_msg_box.setIcon(QMessageBox.Information)
                success_msg_box.setWindowTitle("Role Updated")
                success_msg_box.setText(f"The role of {name} has been successfully updated to {new_role}.")
                success_msg_box.exec()

            except mysql.connector.Error as err:
                error_msg_box = QMessageBox()
                error_msg_box.setIcon(QMessageBox.Critical)
                error_msg_box.setWindowTitle("Database Error")
                error_msg_box.setText(f"An error occurred while updating the role: {err.msg}")
                error_msg_box.exec()

            self.select_role_window.hide()

        elif result == QMessageBox.No:
            change_role_msg_box.close()

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

    #Manager's Menu
    def setup_manager_dashboard(self):
    
        self.log_out_button = self.current_dashboard.findChild(QWidget, "log_out_btn")
        if self.log_out_button:
            self.log_out_button.clicked.connect(self.log_out)

        self.stacked_Manager = self.current_dashboard.findChild(QStackedWidget, "stacked_Manager")

        self.stacked_Manager.setCurrentIndex(0)

        # Fetch data from Task_Storage table for current and pending tasks
        try:
            query = """
                SELECT task_name, task_requirement, priority_level, status, group_members, due_date_time
                FROM Task_Storage
            """
            DB.mycursor.execute(query)
            tasks_info = DB.mycursor.fetchall()
        except mysql.connector.Error as err:
            QMessageBox.critical(self.current_dashboard, "Database Error", f"An error occurred while fetching task data: {err.msg}")
            return

        self.pendingtask_table = self.current_dashboard.findChild(QTableWidget, "pendingtasks_table")
        if self.pendingtask_table:
            pending_tasks = [task for task in tasks_info if task[3] in "Pending"]  # Filter tasks with status "Pending"
            self.pendingtask_table.setRowCount(len(pending_tasks))
            self.pendingtask_table.setColumnCount(6)
            self.pendingtask_table.setHorizontalHeaderLabels(["Task", "Requirement", "Priority Level", "Status", "Assigned To", "Due Date"])

            for i, (task_name, task_requirement, priority_level, status, group_members, due_date_time) in enumerate(pending_tasks):
                self.pendingtask_table.setItem(i, 0, QTableWidgetItem(task_name))
                self.pendingtask_table.setItem(i, 1, QTableWidgetItem(task_requirement))
                self.pendingtask_table.setItem(i, 2, QTableWidgetItem(priority_level))
                self.pendingtask_table.setItem(i, 3, QTableWidgetItem(status))
                self.pendingtask_table.setItem(i, 4, QTableWidgetItem(group_members))
                self.pendingtask_table.setItem(i, 5, QTableWidgetItem(str(due_date_time)))

        # Fetch data from Task_Storage table for current and pending tasks
        try:
            query = """
                SELECT task_name, task_requirement, priority_level, status, group_members, due_date_time
                FROM Task_Storage
            """
            DB.mycursor.execute(query)
            tasks_info = DB.mycursor.fetchall()
        except mysql.connector.Error as err:
            QMessageBox.critical(self.current_dashboard, "Database Error", f"An error occurred while fetching task data: {err.msg}")
            return

        self.currenttask_table = self.current_dashboard.findChild(QTableWidget, "currenttask_table")
        if self.currenttask_table:
            current_tasks = [task for task in tasks_info if task[3] in ["Pending", "Completed - Not Validated"]]  # Filter tasks with status "Pending"
            self.currenttask_table.setRowCount(len(current_tasks))
            self.currenttask_table.setColumnCount(6)
            self.currenttask_table.setHorizontalHeaderLabels(["Task", "Requirement", "Priority Level", "Status", "Assigned To", "Due Date"])

            for i, (task_name, task_requirement, priority_level, status, group_members, due_date_time) in enumerate(current_tasks):
                self.currenttask_table.setItem(i, 0, QTableWidgetItem(task_name))
                self.currenttask_table.setItem(i, 1, QTableWidgetItem(task_requirement))
                self.currenttask_table.setItem(i, 2, QTableWidgetItem(priority_level))
                self.currenttask_table.setItem(i, 3, QTableWidgetItem(status))
                self.currenttask_table.setItem(i, 4, QTableWidgetItem(group_members))
                self.currenttask_table.setItem(i, 5, QTableWidgetItem(str(due_date_time)))

        # Fetch data from Task_Storage table for completed tasks
        try:
            query = """
                SELECT task_name, task_requirement, priority_level, status, group_members, due_date_time
                FROM Task_Storage
                WHERE status LIKE 'Completed%'
            """
            DB.mycursor.execute(query)
            completed_tasks_info = DB.mycursor.fetchall()
        
        except mysql.connector.Error as err:
            QMessageBox.critical(self.current_dashboard, "Database Error", f"An error occurred while fetching completed task data: {err.msg}")
            return

        self.completedtask_table = self.current_dashboard.findChild(QTableWidget, "completedtasks_table")
        if self.completedtask_table:
            completed_tasks = [task for task in completed_tasks_info if task[3] in ["Completed - Not Validated", "Completed - Validated"]]  # Filter tasks with status "Pending"
            self.completedtask_table.setRowCount(len(completed_tasks))
            self.completedtask_table.setColumnCount(6)
            self.completedtask_table.setHorizontalHeaderLabels(["Task", "Requirement", "Priority Level", "Status", "Assigned To", "Due Date"])

            for i, (task_name, task_requirement, priority_level, status, group_members, due_date_time) in enumerate(completed_tasks):
                self.completedtask_table.setItem(i, 0, QTableWidgetItem(task_name))
                self.completedtask_table.setItem(i, 1, QTableWidgetItem(task_requirement))
                self.completedtask_table.setItem(i, 2, QTableWidgetItem(priority_level))
                self.completedtask_table.setItem(i, 3, QTableWidgetItem(status))
                self.completedtask_table.setItem(i, 4, QTableWidgetItem(group_members))
                self.completedtask_table.setItem(i, 5, QTableWidgetItem(str(due_date_time)))

        self.dashboard_btn_manager = self.current_dashboard.findChild(QWidget, "dashboard_btn")
        if self.dashboard_btn_manager:
            self.dashboard_btn_manager.clicked.connect(lambda: self.stacked_Manager.setCurrentIndex(0))
            
        self.activity_log_btn_manager = self.current_dashboard.findChild(QWidget, "activity_log_btn")
        if self.activity_log_btn_manager:
            self.activity_log_btn_manager.clicked.connect(lambda: self.stacked_Manager.setCurrentIndex(1))
            
        self.calendar_btn_manager = self.current_dashboard.findChild(QWidget, "calendar_btn")
        if self.calendar_btn_manager:
            self.calendar_btn_manager.clicked.connect(lambda: self.stacked_Manager.setCurrentIndex(2))

        self.number_tasks_label = self.current_dashboard.findChild(QLabel, "number_tasks_label")
        if self.number_tasks_label:
            self.update_task_count()

        self.task_calendar = self.current_dashboard.findChild(QCalendarWidget, "Task_Calendar_2")
        if self.task_calendar:
            self.color_code_calendar_by_priority()

        self.task_calendar_2 = self.current_dashboard.findChild(QCalendarWidget, "Task_Calendar")
        if self.task_calendar_2:
            self.task_calendar_2.selectionChanged.connect(self.show_tasks_for_selected_date)
            self.color_code_calendar_by_priority_2()
        
        self.show_task_completion_pie_chart()

        self.search_bar_tasks = self.current_dashboard.findChild(QLineEdit, "search_bar_tasks")

        self.search_btn = self.current_dashboard.findChild(QPushButton, "search_btn")
        if self.search_btn:
            self.search_btn.clicked.connect(self.search_tasks)

        # Assign Task
        self.assign_task_button = self.current_dashboard.findChild(QWidget, "assigntask_btn")
        if self.assign_task_button:
            self.assign_task_button.clicked.connect(self.show_assign_task)

        # Remove task button connection
        self.remove_task_button = self.current_dashboard.findChild(QWidget, "removetask_btn")
        if self.remove_task_button:
            self.remove_task_button.clicked.connect(self.remove_task)

        self.profile_btn = self.current_dashboard.findChild(QWidget, "profile_button")
        if self.profile_btn:
            self.profile_btn.clicked.connect(self.show_profile)

        self.log_out_button = self.dashboard_window.findChild(QWidget, "log_out_btn")
        if self.log_out_button:
            self.log_out_button.clicked.connect(self.log_out)

    def color_code_calendar_by_priority(self):
        try:
            # Fetch all tasks with their due dates and priority levels
            query = """
            SELECT due_date_time, priority_level
            FROM Task_Storage
            """
            DB.mycursor.execute(query)
            tasks_info = DB.mycursor.fetchall()

            # Iterate through tasks and color-code the calendar
            for due_date_time, priority_level in tasks_info:
                if due_date_time:
                    due_date = due_date_time.date()
                    calendar_date = QDate(due_date.year, due_date.month, due_date.day)

                # Determine the color based on priority level
                if priority_level.lower() == "low":
                    color = QColor("green")
                elif priority_level.lower() == "medium":
                    color = QColor("yellow")
                elif priority_level.lower() == "high":
                    color = QColor("red")
                else:
                    color = QColor("white")  # Default color for unknown priority

                # Highlight the date on the calendar
                format = self.task_calendar.dateTextFormat(calendar_date)
                format.setBackground(color)
                self.task_calendar.setDateTextFormat(calendar_date, format)

        except mysql.connector.Error as err:
            QMessageBox.critical(self.current_dashboard, "Database Error", f"An error occurred while fetching tasks: {err.msg}")

    def color_code_calendar_by_priority_2(self):
        try:
            # Fetch all tasks with their due dates and priority levels
            query = """
            SELECT due_date_time, priority_level
            FROM Task_Storage
            """
            DB.mycursor.execute(query)
            tasks_info = DB.mycursor.fetchall()

            # Iterate through tasks and color-code the calendar
            for due_date_time, priority_level in tasks_info:
                if due_date_time:
                    due_date = due_date_time.date()
                    calendar_date = QDate(due_date.year, due_date.month, due_date.day)

                # Determine the color based on priority level
                if priority_level.lower() == "low":
                    color = QColor("green")
                elif priority_level.lower() == "medium":
                    color = QColor("yellow")
                elif priority_level.lower() == "high":
                    color = QColor("red")
                else:
                    color = QColor("white")  # Default color for unknown priority

                # Highlight the date on the calendar
                format = self.task_calendar_2.dateTextFormat(calendar_date)
                format.setBackground(color)
                self.task_calendar_2.setDateTextFormat(calendar_date, format)

        except mysql.connector.Error as err:
            QMessageBox.critical(self.current_dashboard, "Database Error", f"An error occurred while fetching tasks: {err.msg}")

    def show_tasks_for_selected_date(self):
        selected_date = self.task_calendar_2.selectedDate().toString("yyyy-MM-dd")
        try:
            # Fetch tasks for the selected date from the database
            query = """
            SELECT task_name, task_requirement, priority_level, status, group_members, due_date_time
            FROM Task_Storage
            WHERE DATE(due_date_time) = %s
            """
            DB.mycursor.execute(query, (selected_date,))
            tasks_info = DB.mycursor.fetchall()

            # Find the table widget for displaying tasks
            self.calendar_task_table = self.current_dashboard.findChild(QTableWidget, "calendartask_table")
            if self.calendar_task_table:
                self.calendar_task_table.setRowCount(len(tasks_info))
                self.calendar_task_table.setColumnCount(6)
                self.calendar_task_table.setHorizontalHeaderLabels(["Task", "Requirement", "Priority Level", "Status", "Assigned To", "Due Date"])
                self.calendar_task_table.setVerticalHeaderLabels([])

            # Populate the table with tasks for the selected date
            for i, (task_name, task_requirement, priority_level, status, group_members, due_date_time) in enumerate(tasks_info):
                self.calendar_task_table.setItem(i, 0, QTableWidgetItem(task_name))
                self.calendar_task_table.setItem(i, 1, QTableWidgetItem(task_requirement))
                self.calendar_task_table.setItem(i, 2, QTableWidgetItem(priority_level))
                self.calendar_task_table.setItem(i, 3, QTableWidgetItem(status))
                self.calendar_task_table.setItem(i, 4, QTableWidgetItem(group_members))
                self.calendar_task_table.setItem(i, 5, QTableWidgetItem(str(due_date_time)))

        except mysql.connector.Error as err:
            QMessageBox.critical(self.current_dashboard, "Database Error", f"An error occurred while fetching tasks: {err.msg}")

    def show_assign_task(self): # Created line edit limits
        global email_container
        global first_name_container
        global last_name_container
    
        self.assign_task_window.show()

        # Resize the window to be larger
        self.assign_task_window.resize(800, 600)  # Set width to 800 and height to 600

        # Center the window on the screen
        screen_geometry = QApplication.primaryScreen().geometry()
        window_geometry = self.assign_task_window.geometry()
        x = (screen_geometry.width() - window_geometry.width()) // 2
        y = (screen_geometry.height() - window_geometry.height()) // 2
        self.assign_task_window.move(x, y)

        # Inputs for assigning tasks
        self.task_name_edit = self.assign_task_window.findChild(QLineEdit, "taskname_edit")
        self.task_name_edit.setMaxLength(255)        

        self.task_description_edit = self.assign_task_window.findChild(QTextEdit, "taskreq_edit")
        self.task_description_edit.textChanged.connect(self.limit_task_description_length)

        self.prioritylevel_combobox = self.assign_task_window.findChild(QComboBox, "prioritylevel_combobox")
        self.prioritylevel_combobox.setCurrentIndex(0)

        # Connect the search bar's textChanged signal to this method
        self.search_bar_assign = self.assign_task_window.findChild(QLineEdit, "search_bar_assign")
        if self.search_bar_assign:
            self.search_bar_assign.textChanged.connect(self.search_assign)

        # Replace the list widget with a table widget
        self.assign_member_group_table = self.assign_task_window.findChild(QTableWidget, "assign_member_group_list")
        self.assign_member_group_table.setRowCount(len(email_container))
        self.assign_member_group_table.setColumnCount(2)
        self.assign_member_group_table.setHorizontalHeaderLabels(["", "Name"])

        # Fetch only employees from the database
        try:
            query = """
            SELECT first_name, last_name, email
            FROM Users_Info
            WHERE role = 'Employee'
            """
            DB.mycursor.execute(query)
            employees = DB.mycursor.fetchall()

            # Populate the table with employee data
            self.assign_member_group_table.setRowCount(len(employees))

            for i, (first_name, last_name, email) in enumerate(employees):
                # Create the first column with checkboxes
                checkbox_item = QTableWidgetItem()
                checkbox_item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
                checkbox_item.setCheckState(Qt.Unchecked)
                self.assign_member_group_table.setItem(i, 0, checkbox_item)
                # Create the second column with names and emails
                self.assign_member_group_table.setItem(i, 1, QTableWidgetItem(f"{first_name} {last_name}"))
                self.assign_member_group_table.setItem(i, 2, QTableWidgetItem(email))

        except mysql.connector.Error as err:
            QMessageBox.critical(self.assign_task_window, "Database Error", f"An error occurred while fetching employees: {err.msg}")

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

    def limit_task_description_length(self):
        max_length = 1000
        current_text = self.task_description_edit.toPlainText()
        if len(current_text) > max_length:
            self.task_description_edit.blockSignals(True)
            self.task_description_edit.setPlainText(current_text[:max_length])
            self.task_description_edit.blockSignals(False)
            cursor = self.task_description_edit.textCursor()
            cursor.movePosition(cursor.End)
            self.task_description_edit.setTextCursor(cursor)

    def search_assign(self):
        if not self.assign_member_group_table:
            return  # Exit if the table is not initialized

        search_text = self.search_bar_assign.text().strip().lower()

        if self.assign_member_group_table:
            for row in range(self.assign_member_group_table.rowCount()):
                match_found = False
                for col in range(self.assign_member_group_table.columnCount()):
                    item = self.assign_member_group_table.item(row, col)
                    if item and search_text in item.text().strip().lower():
                        match_found = True
                        break
                self.assign_member_group_table.setRowHidden(row, not match_found)

    def handle_checkbox_change(self, item):
        if item.column() == 0 and item.checkState() == Qt.Checked:
            for col in range(self.assign_member_group_table.columnCount()):
                self.assign_member_group_table.item(item.row(), col).setSelected(True)
        elif item.column() == 0 and item.checkState() == Qt.Unchecked:
            for col in range(self.assign_member_group_table.columnCount()):
                self.assign_member_group_table.setRangeSelected(QTableWidgetSelectionRange(item.row(), 0, item.row(), self.assign_member_group_table.columnCount() - 1), False)

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

    def assign_task_to_db(self, task_name, task_description, task_requirement, task_priority_level, task_due_date, task_due_time, task_assigned_to, task_status):
            try:
                # Insert the task into the Task_Storage table
                insert_query = """
                    INSERT INTO Task_Storage (task_name, task_description, task_requirement, due_date_time, priority_level, status, group_members)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
                due_date_time = f"{task_due_date} {task_due_time}"
                group_members = ", ".join(task_assigned_to) if isinstance(task_assigned_to, (set, list)) else task_assigned_to
                DB.mycursor.execute(insert_query, (task_name, task_description, task_requirement, due_date_time, task_priority_level, task_status, group_members))
                DB.conn.commit()
                print("Task successfully assigned and stored in the database.")
            except mysql.connector.Error as err:
                error_msg_box = QMessageBox()
                error_msg_box.setIcon(QMessageBox.Critical)
                error_msg_box.setWindowTitle("Database Error")
                error_msg_box.setText(f"An error occurred while assigning the task: {err.msg}")
                error_msg_box.exec()

    def remove_task_from_db(self, task_name):
            try:
                # Remove the task from the Task_Storage table
                delete_query = "DELETE FROM Task_Storage WHERE task_name = %s"
                DB.mycursor.execute(delete_query, (task_name,))
                DB.conn.commit()
                print("Task successfully removed from the database.")
            except mysql.connector.Error as err:
                error_msg_box = QMessageBox()
                error_msg_box.setIcon(QMessageBox.Critical)
                error_msg_box.setWindowTitle("Database Error")
                error_msg_box.setText(f"An error occurred while removing the task: {err.msg}")
                error_msg_box.exec()

    def finalize_create_task(self):
            global task_name_container
            global task_requirement_container
            global task_description_container
            global task_priority_level_container
            global task_due_date_container
            global task_due_time_container
            global task_assigned_to_container
            global task_status_container

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
                new_task_requirement = "File" if self.file_radio_btn.isChecked() else "Web Link"
                new_task_priority_level = self.prioritylevel_combobox.currentText()
                new_task_due_date = self.due_date_edit.text()
                new_task_due_time = self.due_time_edit.text()
                new_task_assigned_to = set()
                new_task_status = "Pending"

                for row in range(self.assign_member_group_table.rowCount()):
                    checkbox_item = self.assign_member_group_table.item(row, 0)
                    if checkbox_item and checkbox_item.checkState() == Qt.Checked:
                        name_item = self.assign_member_group_table.item(row, 1)
                        if name_item:
                            new_task_assigned_to.add(name_item.text())

                #Insert the new task directly into the database
                self.assign_task_to_db(new_task_name, new_task_description, new_task_requirement, new_task_priority_level, new_task_due_date, new_task_due_time, new_task_assigned_to, new_task_status)

                #Refresh the current task table
                self.currenttask_table = self.current_dashboard.findChild(QTableWidget, "currenttask_table")
                self.currenttask_table.setRowCount(0)

                try:
                    query = """
                        SELECT task_name, task_requirement, priority_level, status, group_members, due_date_time
                        FROM Task_Storage
                    """
                    DB.mycursor.execute(query)
                    tasks_info = DB.mycursor.fetchall()

                    self.currenttask_table.setColumnCount(6)
                    self.currenttask_table.setHorizontalHeaderLabels(["Task", "Requirement", "Priority Level", "Status", "Assigned To", "Due Date"])

                    for i, (task_name, task_requirement, priority_level, status, group_members, due_date_time) in enumerate(tasks_info):
                        self.currenttask_table.insertRow(i)
                        self.currenttask_table.setItem(i, 0, QTableWidgetItem(task_name))
                        self.currenttask_table.setItem(i, 1, QTableWidgetItem(task_requirement))
                        self.currenttask_table.setItem(i, 2, QTableWidgetItem(priority_level))
                        self.currenttask_table.setItem(i, 3, QTableWidgetItem(status))
                        self.currenttask_table.setItem(i, 4, QTableWidgetItem(group_members))
                        self.currenttask_table.setItem(i, 5, QTableWidgetItem(str(due_date_time)))

                except mysql.connector.Error as err:
                    QMessageBox.critical(self.current_dashboard, "Database Error", f"An error occurred while refreshing tasks: {err.msg}")

                # Refresh the pending task table
                self.pendingtask_table = self.current_dashboard.findChild(QTableWidget, "pendingtasks_table")
                self.pendingtask_table.setRowCount(0)

                try:
                    pending_tasks = [task for task in tasks_info if task[3] == "Pending"]

                    self.pendingtask_table.setColumnCount(6)
                    self.pendingtask_table.setHorizontalHeaderLabels(["Task", "Requirement", "Priority Level", "Status", "Assigned To", "Due Date"])

                    for i, (task_name, task_requirement, priority_level, status, group_members, due_date_time) in enumerate(pending_tasks):
                        self.pendingtask_table.insertRow(i)
                        self.pendingtask_table.setItem(i, 0, QTableWidgetItem(task_name))
                        self.pendingtask_table.setItem(i, 1, QTableWidgetItem(task_requirement))
                        self.pendingtask_table.setItem(i, 2, QTableWidgetItem(priority_level))
                        self.pendingtask_table.setItem(i, 3, QTableWidgetItem(status))
                        self.pendingtask_table.setItem(i, 4, QTableWidgetItem(group_members))
                        self.pendingtask_table.setItem(i, 5, QTableWidgetItem(str(due_date_time)))

                except mysql.connector.Error as err:
                    QMessageBox.critical(self.current_dashboard, "Database Error", f"An error occurred while refreshing pending tasks: {err.msg}")

                self.task_name_edit.setText("")
                self.task_description_edit.setPlainText("")
                self.due_date_edit.setDate(datetime.date.today())
                self.due_time_edit.setTime(datetime.datetime.now().time())
                self.prioritylevel_combobox.setCurrentIndex(0)
                self.file_radio_btn.setChecked(False)
                self.weblink_radio_btn.setChecked(True)
                self.search_bar_assign.setText("")

                self.assign_task_window.hide()
                confirm_msg_box.close()

            elif task_result == QMessageBox.No:
                confirm_msg_box.close()
                self.show_assign_task()
                return

    def remove_task(self):
            selected_row = self.pendingtask_table.currentRow()
            remove_index = selected_row

            if selected_row != -1:
                remove_task_msg_box = QMessageBox()
                remove_task_msg_box.setIcon(QMessageBox.Warning)
                remove_task_msg_box.setWindowTitle("Confirmation")
                remove_task_msg_box.setText("Are you sure you want to remove this task?")
                remove_task_msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                remove_task_msg_box.setDefaultButton(QMessageBox.No)
                remove_task_msg_box.setEscapeButton(QMessageBox.No)
                remove_task_msg_box.setModal(True)
                remove_task_msg_box.setWindowModality(Qt.ApplicationModal)

                remove_result = remove_task_msg_box.exec()

                if remove_result == QMessageBox.Yes:
                    # Remove the task from the database
                    task_name = self.pendingtask_table.item(remove_index, 0).text()
                    self.remove_task_from_db(task_name)

                    # Refresh the current task table
                    self.currenttask_table.setRowCount(0)
                    try:
                        query = """
                            SELECT task_name, task_requirement, priority_level, status, group_members, due_date_time
                            FROM Task_Storage
                        """
                        DB.mycursor.execute(query)
                        tasks_info = DB.mycursor.fetchall()

                        self.currenttask_table.setColumnCount(6)
                        self.currenttask_table.setHorizontalHeaderLabels(["Task", "Requirement", "Priority Level", "Status", "Assigned To", "Due Date"])

                        for i, (task_name, task_requirement, priority_level, status, group_members, due_date_time) in enumerate(tasks_info):
                            self.currenttask_table.insertRow(i)
                            self.currenttask_table.setItem(i, 0, QTableWidgetItem(task_name))
                            self.currenttask_table.setItem(i, 1, QTableWidgetItem(task_requirement))
                            self.currenttask_table.setItem(i, 2, QTableWidgetItem(priority_level))
                            self.currenttask_table.setItem(i, 3, QTableWidgetItem(status))
                            self.currenttask_table.setItem(i, 4, QTableWidgetItem(group_members))
                            self.currenttask_table.setItem(i, 5, QTableWidgetItem(str(due_date_time)))

                    except mysql.connector.Error as err:
                        QMessageBox.critical(self.current_dashboard, "Database Error", f"An error occurred while refreshing tasks: {err.msg}")

                    # Refresh the pending task table
                    self.pendingtask_table.setRowCount(0)
                    try:
                        pending_tasks = [task for task in tasks_info if task[3] == "Pending"]

                        self.pendingtask_table.setColumnCount(6)
                        self.pendingtask_table.setHorizontalHeaderLabels(["Task", "Requirement", "Priority Level", "Status", "Assigned To", "Due Date"])

                        for i, (task_name, task_requirement, priority_level, status, group_members, due_date_time) in enumerate(pending_tasks):
                            self.pendingtask_table.insertRow(i)
                            self.pendingtask_table.setItem(i, 0, QTableWidgetItem(task_name))
                            self.pendingtask_table.setItem(i, 1, QTableWidgetItem(task_requirement))
                            self.pendingtask_table.setItem(i, 2, QTableWidgetItem(priority_level))
                            self.pendingtask_table.setItem(i, 3, QTableWidgetItem(status))
                            self.pendingtask_table.setItem(i, 4, QTableWidgetItem(group_members))
                            self.pendingtask_table.setItem(i, 5, QTableWidgetItem(str(due_date_time)))

                    except mysql.connector.Error as err:
                        QMessageBox.critical(self.current_dashboard, "Database Error", f"An error occurred while refreshing pending tasks: {err.msg}")

                elif remove_result == QMessageBox.No:
                    remove_task_msg_box.close()
                    self.setup_manager_dashboard()

            else:
                no_selection_msg_box = QMessageBox()
                no_selection_msg_box.setIcon(QMessageBox.Warning)
                no_selection_msg_box.setWindowTitle("No Selection")
                no_selection_msg_box.setText("Please select a task to remove.")
                no_selection_msg_box.exec()
                return

    #Employee Menu
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

        # Fetch tasks assigned to the employee from the database
        try:
            query = """
                SELECT task_name, task_requirement, priority_level, status, group_members, due_date_time
                FROM Task_Storage
            """
            DB.mycursor.execute(query)
            tasks_info = DB.mycursor.fetchall()
            current_tasks = [task for task in tasks_info if task[3] in ["Pending", "Completed - Not Validated"]]  # Filter tasks with statuses

            # Populate the table with data from the database
            for i, (task_name, task_requirement, priority_level, status, group_members, due_date_time) in enumerate(current_tasks):
                    self.currenttask_table.setItem(i, 0, QTableWidgetItem(task_name))
                    self.currenttask_table.setItem(i, 1, QTableWidgetItem(task_requirement))
                    self.currenttask_table.setItem(i, 2, QTableWidgetItem(priority_level))
                    self.currenttask_table.setItem(i, 3, QTableWidgetItem(status))
                    self.currenttask_table.setItem(i, 4, QTableWidgetItem(group_members))
                    self.currenttask_table.setItem(i, 5, QTableWidgetItem(str(due_date_time)))

        except mysql.connector.Error as err:
            QMessageBox.critical(self.current_dashboard, "Database Error", f"An error occurred while fetching tasks: {err.msg}")

        self.dashboard_btn_employee = self.current_dashboard.findChild(QWidget, "dashboard_btn")
        if self.dashboard_btn_employee:
            self.dashboard_btn_employee.clicked.connect(lambda: self.stacked_Employee.setCurrentIndex(0))

        self.calendar_btn_employee = self.current_dashboard.findChild(QWidget, "calendar_btn")
        if self.calendar_btn_employee:
            self.calendar_btn_employee.clicked.connect(lambda: self.stacked_Employee.setCurrentIndex(1))

        self.task_calendar = self.current_dashboard.findChild(QCalendarWidget, "Task_Calendar_2")
        if self.task_calendar:
            self.color_code_calendar_by_priority()

        self.task_calendar_2 = self.current_dashboard.findChild(QCalendarWidget, "Task_Calendar")
        if self.task_calendar_2:
            self.color_code_calendar_by_priority_2()

        self.show_task_completion_pie_chart()

        self.submit_task_button = self.current_dashboard.findChild(QWidget, "submit_task_btn")
        if self.submit_task_button:
            self.submit_task_button.clicked.connect(self.show_submit_task)

        self.profile_btn = self.current_dashboard.findChild(QWidget, "profile_button")
        if self.profile_btn:
            self.profile_btn.clicked.connect(self.show_profile)

    def show_submit_task(self):  
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

        # Connection of widgets
        self.submit_name_task = self.submit_task_window.findChild(QLabel, "name_task_label_input")
        self.submit_req_task = self.submit_task_window.findChild(QLabel, "req_task_label_input")
        self.submit_prioritylevel = self.submit_task_window.findChild(QLabel, "prioritylevel_label_input")
        self.submit_description_task = self.submit_task_window.findChild(QTextBrowser, "task_description_box")
        self.submit_due_date_task = self.submit_task_window.findChild(QLabel, "duedate_label_input")
        self.submit_btn = self.submit_task_window.findChild(QPushButton, "submit_btn")
        self.cancel_btn = self.submit_task_window.findChild(QPushButton, "cancel_btn")

        self.link_requirement_edit = self.submit_task_window.findChild(QLineEdit, "link_requirement_edit")
        self.link_requirement_edit.setMaxLength(1000)

        selected_row = self.currenttask_table.currentRow() 
        submit_index = selected_row

        try:
            # Fetch the task details from the database
            query = """
            SELECT task_name, task_requirement, priority_level, task_description, due_date_time
            FROM Task_Storage
            WHERE status = 'Pending'
            LIMIT %s, 1
            """
            DB.mycursor.execute(query, (int(submit_index),))
            result = DB.mycursor.fetchone()

            if result:
                task_name, task_requirement, priority_level, task_description, due_date_time = result
                if self.submit_name_task:
                    self.submit_name_task.setText(task_name)
                if self.submit_req_task:
                    self.submit_req_task.setText(task_requirement)
                if self.submit_prioritylevel:
                    self.submit_prioritylevel.setText(priority_level)
                if self.submit_description_task:
                    self.submit_description_task.setText(task_description)
                if self.submit_due_date_task:
                    self.submit_due_date_task.setText(str(due_date_time))
            else:
                QMessageBox.warning(self.submit_task_window, "Error", "Task not found in the database.")
        except mysql.connector.Error as err:
            QMessageBox.critical(self.submit_task_window, "Database Error", f"An error occurred while fetching task details: {err.msg}")
    
        # Buttons
        if self.submit_btn:
            self.submit_btn.clicked.connect(lambda: self.confirm_submit_task_to_db(submit_index))
        if self.cancel_btn:
            self.cancel_btn.clicked.connect(self.submit_task_window.close)

    def confirm_submit_task_to_db(self, submit_index):
        if self.link_requirement_edit and self.link_requirement_edit.text().strip():

            # Check if the link starts with "https://"
            if not self.link_requirement_edit.text().startswith("https://"):
                invalid_link_msg_box = QMessageBox()
                invalid_link_msg_box.setIcon(QMessageBox.Warning)
                invalid_link_msg_box.setWindowTitle("Invalid Link")
                invalid_link_msg_box.setText("The link must start with 'https://'. Please enter a valid link.")
                invalid_link_msg_box.exec()
                return

            # Message box
            confirm_msg_box = QMessageBox()
            confirm_msg_box.setIcon(QMessageBox.Warning)
            confirm_msg_box.setWindowTitle("Confirmation")
            confirm_msg_box.setText("Do you want to submit this task?")
            confirm_msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            confirm_msg_box.setDefaultButton(QMessageBox.No)
            confirm_msg_box.setEscapeButton(QMessageBox.No)
            confirm_msg_box.setModal(True)
            confirm_msg_box.setWindowModality(Qt.ApplicationModal)

            submit_result = confirm_msg_box.exec()

            if submit_result == QMessageBox.Yes:
                try:
                    # Update the task status and insert the submitted link into the database
                    update_query = """
                        UPDATE Task_Storage
                        SET submitted_link = %s, status = %s, submitted_date_time = NOW()
                        WHERE task_name = %s
                    """
                    # Ensure task_name_container is defined and populated
                    global task_name_container
                    if 'task_name_container' not in globals() or not task_name_container:
                        DB.mycursor.execute("SELECT task_name FROM Task_Storage")
                        task_name_container = [task[0] for task in DB.mycursor.fetchall()]

                    DB.mycursor.execute(update_query, (
                        self.link_requirement_edit.text(),
                        "Completed - Not Validated",
                        task_name_container[submit_index]
                    ))
                    DB.conn.commit()

                    # Update the task in the current task table
                    self.currenttask_table.setItem(submit_index, 3, QTableWidgetItem("Completed - Not Validated"))

                    # Close the submit task window
                    self.submit_task_window.close()

                    # Show success message
                    success_msg_box = QMessageBox()
                    success_msg_box.setIcon(QMessageBox.Information)
                    success_msg_box.setWindowTitle("Task Submitted")
                    success_msg_box.setText("Task has been successfully submitted.")
                    success_msg_box.exec()

                    # Clear the link requirement edit
                    self.link_requirement_edit.setText("")

                except mysql.connector.Error as err:
                    error_msg_box = QMessageBox()
                    error_msg_box.setIcon(QMessageBox.Critical)
                    error_msg_box.setWindowTitle("Database Error")
                    error_msg_box.setText(f"An error occurred while submitting the task: {err.msg}")
                    error_msg_box.exec()

            elif submit_result == QMessageBox.No:
                confirm_msg_box.close()
                return

        else:
            no_link_msg_box = QMessageBox()
            no_link_msg_box.setIcon(QMessageBox.Warning)
            no_link_msg_box.setWindowTitle("No Link Entered")
            no_link_msg_box.setText("Please enter the link you are going to submit.")
            no_link_msg_box.exec()
            return

    def submit_file_task(self):
        self.submit_file_task_window.show()

        # Connection of widgets
        self.submit_file_name_task = self.submit_file_task_window.findChild(QLabel, "name_task_label_input")
        self.submit_file_req_task = self.submit_file_task_window.findChild(QLabel, "req_task_label_input")
        self.submit_file_prioritylevel = self.submit_file_task_window.findChild(QLabel, "prioritylevel_label_input")
        self.submit_file_description_task = self.submit_file_task_window.findChild(QTextBrowser, "task_description_box")
        self.submit_file_due_date_task = self.submit_file_task_window.findChild(QLabel, "duedate_label_2")
        self.submit_file_btn = self.submit_file_task_window.findChild(QPushButton, "submit_btn")
        self.submit_file_cancel_btn = self.submit_file_task_window.findChild(QPushButton, "cancel_btn")

        self.file_path_edit = self.submit_file_task_window.findChild(QLineEdit, "file_path_edit")
        self.file_path_edit.setMaxLength(1000)

        self.browse_file_btn = self.submit_file_task_window.findChild(QPushButton, "browse_file_btn")

        selected_row = self.currenttask_table.currentRow()

        # Fetch task details from the database
        try:
            query = """
                SELECT task_name, task_requirement, priority_level, task_description, due_date_time
                FROM Task_Storage
                WHERE status = 'Pending'
                LIMIT %s, 1
            """
            DB.mycursor.execute(query, (selected_row,))
            result = DB.mycursor.fetchone()

            if result:
                task_name, task_requirement, priority_level, task_description, due_date_time = result
                if self.submit_file_name_task:
                    self.submit_file_name_task.setText(task_name)
                if self.submit_file_req_task:
                    self.submit_file_req_task.setText(task_requirement)
                if self.submit_file_prioritylevel:
                    self.submit_file_prioritylevel.setText(priority_level)
                if self.submit_file_description_task:
                    self.submit_file_description_task.setText(task_description)
                if self.submit_file_due_date_task:
                    self.submit_file_due_date_task.setText(str(due_date_time))
            else:
                QMessageBox.warning(self.submit_file_task_window, "Error", "Task not found in the database.")
        except mysql.connector.Error as err:
            QMessageBox.critical(self.submit_file_task_window, "Database Error", f"An error occurred while fetching task details: {err.msg}")

        # Connect browse button to open file dialog
        if self.browse_file_btn:
            self.browse_file_btn.clicked.connect(self.browse_file)

        # Connect submit button to confirm submission
        if self.submit_file_btn:
            self.submit_file_btn.clicked.connect(lambda: self.confirm_submit_file_task(selected_row))

        # Connect cancel button to close the window
        if self.submit_file_cancel_btn:
            self.submit_file_cancel_btn.clicked.connect(self.submit_file_task_window.close)

    def browse_file(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self.submit_file_task_window, "Select File", "", "All Files (*)")
        if file_path:
            self.file_path_edit.setText(file_path)
            # Read the file data and store it temporarily
            with open(file_path, "rb") as file:
                self.selected_file_data = file.read()

    def confirm_submit_file_task(self, selected_row):
        if hasattr(self, 'selected_file_data') and self.selected_file_data:
            submit_index = selected_row

            # Message box
            confirm_msg_box = QMessageBox()
            confirm_msg_box.setIcon(QMessageBox.Warning)
            confirm_msg_box.setWindowTitle("Confirmation")
            confirm_msg_box.setText("Do you want to submit this task?")
            confirm_msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            confirm_msg_box.setDefaultButton(QMessageBox.No)
            confirm_msg_box.setEscapeButton(QMessageBox.No)
            confirm_msg_box.setModal(True)
            confirm_msg_box.setWindowModality(Qt.ApplicationModal)

            submit_result = confirm_msg_box.exec()

            if submit_result == QMessageBox.Yes:
                try:
                    # Update the task status and insert the submitted file data
                    update_query = """
                        UPDATE Task_Storage
                        SET submitted_file = %s, status = %s, submitted_date_time = NOW()
                        WHERE task_name = %s
                    """
                    # Ensure task_name_container is defined and populated
                    global task_name_container
                    if 'task_name_container' not in globals() or not task_name_container:
                        DB.mycursor.execute("SELECT task_name FROM Task_Storage")
                        task_name_container = [task[0] for task in DB.mycursor.fetchall()]

                    DB.mycursor.execute(update_query, (
                        self.selected_file_data,
                        "Completed - Not Validated",
                        task_name_container[submit_index]
                    ))
                    DB.conn.commit()

                    # Update the task in the current task table
                    self.currenttask_table.setItem(submit_index, 3, QTableWidgetItem("Completed - Not Validated"))

                    # Close the submit task window
                    self.submit_file_task_window.close()

                    # Show success message
                    success_msg_box = QMessageBox()
                    success_msg_box.setIcon(QMessageBox.Information)
                    success_msg_box.setWindowTitle("Task Submitted")
                    success_msg_box.setText("Task has been successfully submitted.")
                    success_msg_box.exec()

                    # Clear the file data
                    self.selected_file_data = None
                    self.file_path_edit.setText("")

                except Exception as e:
                    error_msg_box = QMessageBox()
                    error_msg_box.setIcon(QMessageBox.Critical)
                    error_msg_box.setWindowTitle("Error")
                    error_msg_box.setText(f"An error occurred while submitting the task: {str(e)}")
                    error_msg_box.exec()

            elif submit_result == QMessageBox.No:
                confirm_msg_box.close()
                self.submit_file_task()

        else:
            no_file_msg_box = QMessageBox()
            no_file_msg_box.setIcon(QMessageBox.Warning)
            no_file_msg_box.setWindowTitle("No File Selected")
            no_file_msg_box.setText("Please select a file to submit.")
            no_file_msg_box.exec()
            self.submit_file_task()
            return

    def create_foreign_key_relationship(self):
        try:
            # Ensure the foreign key constraint is added only if it doesn't already exist
            check_foreign_key_query = """
                SELECT CONSTRAINT_NAME
                FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
                WHERE TABLE_NAME = 'Task_Storage' AND CONSTRAINT_NAME = 'fk_user_id';
            """
            DB.mycursor.execute(check_foreign_key_query)
            result = DB.mycursor.fetchone()

            if not result:
                # Add foreign key constraints to link Task_Storage and Users_Info tables
                add_foreign_key_query = """
                    ALTER TABLE Task_Storage
                    ADD CONSTRAINT fk_user_id
                    FOREIGN KEY (user_id)
                    REFERENCES Users_Info(user_id)
                    ON DELETE CASCADE
                    ON UPDATE CASCADE;
                """
                DB.mycursor.execute(add_foreign_key_query)
                DB.conn.commit()
                print("Foreign key relationship successfully created.")
            else:
                print("Foreign key relationship already exists.")

        except mysql.connector.Error as err:
            print(f"An error occurred while creating the foreign key relationship: {err.msg}")

    def show_join_group(self): # To be removed
        self.join_group_window.show()

    def show_login(self):
        self.login_window.show()
        self.create_account_window.hide()
        self.setup_login_page()
    
    def log_out(self):
        self.current_dashboard.hide()
        self.login_window.show()
        self.setup_login_page()
        self.log_in_stacked.setCurrentIndex(1)

        self.email_lineedit.setText("")
        self.password_lineedit.setText("")

    def run(self):
        self.login_window.show()
        sys.exit(self.app.exec())

if __name__ == "__main__":
    main_app = MainApp()
    main_app.run()