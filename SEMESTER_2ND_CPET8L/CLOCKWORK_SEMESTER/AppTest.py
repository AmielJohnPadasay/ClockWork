import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtUiTools import QUiLoader

# Function to load .ui file
def load_ui(file_path):
    loader = QUiLoader()
    ui = loader.load(file_path, None)
    if not ui:
        print(f"Failed to load UI file: {file_path}")
        sys.exit(1)
    return ui

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Load and show the UI
    window = load_ui("Log-In-Page.ui")
    window.show()

    sys.exit(app.exec())