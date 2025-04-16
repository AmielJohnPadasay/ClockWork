import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout


# Main function
def main():
    app = QApplication(sys.argv)  # Create application object

    window = QWidget()  # Create main window
    window.setWindowTitle("My First PySide6 App")
    window.resize(400, 300)  # Set window size

    # Add a label
    layout = QVBoxLayout()
    label = QLabel("Hello, PySide6!")
    layout.addWidget(label)
    window.setLayout(layout)

    window.show()  # Display the window
    sys.exit(app.exec())  # Execute the application loop


if __name__ == "__main__":
    main()