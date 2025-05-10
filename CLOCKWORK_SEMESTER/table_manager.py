from PySide6.QtWidgets import QTableWidget, QTableWidgetItem
from PySide6.QtCore import QObject

from test_ui_runner import *

def connect_table_signals(ui, table_name, add_row_button_name, add_column_button_name):
    """
    Connects signals for adding rows and columns to the specified QTableWidget in the loaded UI.

    :param ui: The loaded UI object (from QUiLoader or uic)
    :param table_name: The objectName of the QTableWidget
    :param add_row_button_name: The objectName of the button to add rows
    :param add_column_button_name: The objectName of the button to add columns
    """
    add_row_button = ui.findChild(QObject, "btn_row")
    add_column_button = ui.findChild(QObject, "btn_col")
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
        for col in range(table.columnCount()):
            table.setItem(row_position, col, QTableWidgetItem(f"R{row_position+1} C{col+1}"))

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
        for row in range(table.rowCount()):
            table.setItem(row, col_position, QTableWidgetItem(f"R{row+1} C{col_position+1}"))
