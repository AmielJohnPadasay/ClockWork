from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QComboBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

class DashboardAccess(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the UI for user selection
        self.setWindowTitle("Dashboard Access")
        layout = QVBoxLayout()

        # Role selection
        self.role_label = QLabel("Select your role:")
        layout.addWidget(self.role_label)

        self.role_selector = QComboBox()
        self.role_selector.addItems(["Supervisor", "Manager", "Employee"])
        layout.addWidget(self.role_selector)

        # Login button
        self.login_button = QPushButton("Access Dashboard")
        layout.addWidget(self.login_button)

        self.setLayout(layout)

        # Connect login button
        self.login_button.clicked.connect(self.load_dashboard)

    def load_dashboard(self):
        role = self.role_selector.currentText()

        # Map roles to UI files
        dashboard_files = {
            "Supervisor": "dashboard.ui",
            "Manager": "dashboard_manager_new.ui",
            "Employee": "dashboard_employee_new.ui"
        }

        ui_file_path = dashboard_files.get(role)

        if ui_file_path:
            self.open_dashboard(ui_file_path)

    def open_dashboard(self, ui_file_path):
        # Load and display the correct dashboard
        loader = QUiLoader()
        ui_file = QFile(ui_file_path)
        if ui_file.open(QFile.ReadOnly):
            dashboard = loader.load(ui_file, self)
            ui_file.close()
            dashboard.show()

if __name__ == "__main__":
    app = QApplication([])
    window = DashboardAccess()
    window.show()
    app.exec()