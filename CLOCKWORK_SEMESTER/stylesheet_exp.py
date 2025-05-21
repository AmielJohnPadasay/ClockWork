from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
import sys

app = QApplication(sys.argv)

# Main window
window = QWidget()
window.setWindowTitle("Hard-coded Stylesheet Example")

# Create button
button = QPushButton("Click Me")

# Apply hard-coded stylesheet
button.setStyleSheet("""
    QPushButton {
        background-color: #3498db;
        color: white;
        font-size: 16px;
        padding: 10px;
        border-radius: 5px;
    }
    QPushButton:hover {
        background-color: #2980b9;
    }
""")

# Layout
layout = QVBoxLayout()
layout.addWidget(button)
window.setLayout(layout)

# Show window
window.show()
sys.exit(app.exec())