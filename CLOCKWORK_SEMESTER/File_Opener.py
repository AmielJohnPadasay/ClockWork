from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel, QHBoxLayout, QFrame
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QIcon
import sys
import os

class FileDropWidget(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.setFrameStyle(QFrame.StyledPanel | QFrame.Raised)
        self.setStyleSheet("background-color: #f0f0f0; border: 2px dashed #aaa;")
        self.setMinimumHeight(80)

        self.icon_label = QLabel()
        self.icon_label.setFixedSize(48, 48)

        self.name_label = QLabel("Drop a file here or use Browse")
        self.name_label.setStyleSheet("font-size: 14px;")

        layout = QHBoxLayout()
        layout.addWidget(self.icon_label)
        layout.addWidget(self.name_label)
        layout.addStretch()
        self.setLayout(layout)

    def set_file(self, file_path):
        if os.path.isfile(file_path):
            icon = QIcon(file_path)
            pixmap = icon.pixmap(48, 48)
            if pixmap.isNull():
                # Use a generic icon if no specific icon found
                pixmap = QPixmap(48, 48)
                pixmap.fill(Qt.lightGray)
            self.icon_label.setPixmap(pixmap)
            self.name_label.setText(os.path.basename(file_path))
            self.setToolTip(file_path)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dragMoveEvent(self, event):
        event.acceptProposedAction()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            urls = event.mimeData().urls()
            if urls:
                file_path = urls[0].toLocalFile()
                self.set_file(file_path)

class FileSelector(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Selector with Drag-and-Drop & Icon Preview")

        self.layout = QVBoxLayout()

        self.file_widget = FileDropWidget(self)
        self.layout.addWidget(self.file_widget)

        self.browse_button = QPushButton("Browse File")
        self.browse_button.clicked.connect(self.open_file_dialog)
        self.layout.addWidget(self.browse_button)

        self.setLayout(self.layout)

    def open_file_dialog(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File")
        if file_path:
            self.file_widget.set_file(file_path)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileSelector()
    window.resize(500, 150)
    window.show()
    sys.exit(app.exec())