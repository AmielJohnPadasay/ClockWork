from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QTableWidget, QTableWidgetItem
)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
import sys

class TableTestApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Table Widget Test")
        self.resize(800, 600)

        # Load the UI
        loader = QUiLoader()
        ui_file = QFile("dashboard.ui")
        ui_file.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file, self)
        ui_file.close()

        # Layout to hold UI and buttons
        layout = QVBoxLayout(self)
        layout.addWidget(self.ui)

        # Add control buttons
        self.btn_add_row = QPushButton("Add Row to All Tables")
        self.btn_add_column = QPushButton("Add Column to All Tables")
        layout.addWidget(self.btn_add_row)
        layout.addWidget(self.btn_add_column)

        # Connect buttons
        self.btn_add_row.clicked.connect(self.add_rows_to_tables)
        self.btn_add_column.clicked.connect(self.add_columns_to_tables)

    def add_rows_to_tables(self):
        table_names = ["tableWidget", "reminder_table", "user_roles_table"]
        for name in table_names:
            table = self.ui.findChild(QTableWidget, name)
            if table:
                row = table.rowCount()
                table.insertRow(row)
                for col in range(table.columnCount()):
                    table.setItem(row, col, QTableWidgetItem(f"{name} R{row+1}C{col+1}"))

    def add_columns_to_tables(self):
        table_names = ["tableWidget", "reminder_table", "user_roles_table"]
        for name in table_names:
            table = self.ui.findChild(QTableWidget, name)
            if table:
                col = table.columnCount()
                table.insertColumn(col)
                for row in range(table.rowCount()):
                    table.setItem(row, col, QTableWidgetItem(f"{name} R{row+1}C{col+1}"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TableTestApp()
    window.show()
    sys.exit(app.exec())