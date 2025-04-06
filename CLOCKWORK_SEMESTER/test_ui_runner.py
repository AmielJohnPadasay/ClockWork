from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTableWidget
from PySide6.QtWidgets import QTableWidgetItem
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
import sys

class TestUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Test UI with Table Manager")
        self.resize(800, 600)

        loader = QUiLoader()
        ui_file = QFile("test_ui.ui")
        ui_file.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file, self)
        ui_file.close()

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.ui)

        self.reminder_table = self.ui.findChild(QTableWidget, "reminder_table")
        self.reminder_table.setRowCount(0)
        self.reminder_table.setColumnCount(0)
        if not self.reminder_table:
            raise RuntimeError("QTableWidget with object name 'reminder_table' not found in test_ui.ui")
        
        self.layout.addWidget(self.reminder_table)

        btn_row = QPushButton("Add Row to reminder_table")
        btn_col = QPushButton("Add Column to reminder_table")

        btn_row.clicked.connect(lambda: add_row_to_table(self, "reminder_table"))
        btn_col.clicked.connect(lambda: add_column_to_table(self, "reminder_table"))

        self.layout.addWidget(btn_row)
        self.layout.addWidget(btn_col)

def connect_table_signals(ui, table_name, add_row_button_name, add_column_button_name):
    """
    Connects signals for adding rows and columns to the specified QTableWidget in the loaded UI.

    :param ui: The loaded UI object (from QUiLoader or uic)
    :param table_name: The objectName of the QTableWidget
    :param add_row_button_name: The objectName of the button to add rows
    :param add_column_button_name: The objectName of the button to add columns
    """
    add_row_button = ui.findChild(QPushButton, add_row_button_name)
    add_column_button = ui.findChild(QPushButton, add_column_button_name)
    table = ui.findChild(QTableWidget, "reminder_table")

    if add_row_button and table:
        add_row_button.clicked.connect(lambda: add_row_to_table(ui, table_name))
    if add_column_button and table:
        add_column_button.clicked.connect(lambda: add_column_to_table(ui, table_name))

def add_row_to_table(ui, table_name):
    """
    Adds a row to the specified QTableWidget in the loaded UI.
    
    :param ui: The loaded UI object (from QUiLoader or uic)
    :param table_name: The objectName of the QTableWidget
    """
    table = ui.findChild(QTableWidget, table_name)
    if table:
        row_position = table.rowCount()
        table.insertRow(row_position)

def add_column_to_table(ui, table_name):
    """
    Adds a column to the specified QTableWidget in the loaded UI.
    
    :param ui: The loaded UI object (from QUiLoader or uic)
    :param table_name: The objectName of the QTableWidget
    """
    table = ui.findChild(QTableWidget, table_name)
    if table:
        col_position = table.columnCount()
        table.insertColumn(col_position)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TestUI()
    window.show()
    sys.exit(app.exec())
