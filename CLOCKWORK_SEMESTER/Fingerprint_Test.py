import sys
import cv2
import numpy as np
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QFileDialog
from PySide6.QtGui import QFont, QPixmap, QImage

class FingerprintScanner:
    def __init__(self):
        self.saved_fingerprint = None

    def preprocess_fingerprint(self, image_path):
        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        blurred = cv2.GaussianBlur(img, (5,5), 0)
        _, thresh = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY_INV)
        edges = cv2.Canny(thresh, 100, 200)
        return edges

    def register_fingerprint(self, image_path):
        self.saved_fingerprint = self.preprocess_fingerprint(image_path)
        return "Fingerprint Registered Successfully!"

    def verify_fingerprint(self, image_path):
        if self.saved_fingerprint is None:
            return "No fingerprint registered."
        scanned_fingerprint = self.preprocess_fingerprint(image_path)
        if np.array_equal(self.saved_fingerprint, scanned_fingerprint):
            return "Fingerprint Matched! Access Granted."
        else:
            return "Fingerprint Mismatch! Access Denied."

class FingerprintApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.scanner = FingerprintScanner()

    def initUI(self):
        self.setWindowTitle("Fingerprint Scanner")
        self.setGeometry(100, 100, 400, 300)

        self.label = QLabel("Welcome! Register or Verify Fingerprint", self)
        self.label.setFont(QFont("Arial", 12))

        self.register_button = QPushButton("Register Fingerprint", self)
        self.register_button.clicked.connect(self.register_fingerprint)

        self.verify_button = QPushButton("Verify Fingerprint", self)
        self.verify_button.clicked.connect(self.verify_fingerprint)

        self.image_label = QLabel(self)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.register_button)
        layout.addWidget(self.verify_button)
        layout.addWidget(self.image_label)
        self.setLayout(layout)

    def load_image(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Select Fingerprint Image", "", "Images (*.png *.jpg *.bmp)")
        return file_path

    def display_image(self, image_path):
        pixmap = QPixmap(image_path)
        self.image_label.setPixmap(pixmap)
        self.image_label.setScaledContents(True)

    def register_fingerprint(self):
        image_path = self.load_image()
        if image_path:
            self.display_image(image_path)
            message = self.scanner.register_fingerprint(image_path)
            self.label.setText(message)

    def verify_fingerprint(self):
        image_path = self.load_image()
        if image_path:
            self.display_image(image_path)
            message = self.scanner.verify_fingerprint(image_path)
            self.label.setText(message)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FingerprintApp()
    window.show()
    sys.exit(app.exec())