# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Log-In-PageEshOYq.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_Create_Login(object):
    def setupUi(self, Create_Login):
        if not Create_Login.objectName():
            Create_Login.setObjectName(u"Create_Login")
        Create_Login.resize(526, 575)
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setPointSize(10)
        Create_Login.setFont(font)
        self.centralwidget = QWidget(Create_Login)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.password_label = QLabel(self.centralwidget)
        self.password_label.setObjectName(u"password_label")
        font1 = QFont()
        font1.setFamilies([u"Verdana"])
        font1.setPointSize(12)
        self.password_label.setFont(font1)

        self.gridLayout.addWidget(self.password_label, 8, 2, 1, 1)

        self.create_account_log_in_button = QPushButton(self.centralwidget)
        self.create_account_log_in_button.setObjectName(u"create_account_log_in_button")
        self.create_account_log_in_button.setFont(font1)

        self.gridLayout.addWidget(self.create_account_log_in_button, 11, 2, 1, 1)

        self.first_name_label = QLabel(self.centralwidget)
        self.first_name_label.setObjectName(u"first_name_label")
        self.first_name_label.setFont(font1)

        self.gridLayout.addWidget(self.first_name_label, 4, 2, 1, 1)

        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout.addWidget(self.lineEdit_4, 9, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 483, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 0, 13, 1)

        self.horizontalSpacer_2 = QSpacerItem(297, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 10, 2, 1, 1)

        self.email_label = QLabel(self.centralwidget)
        self.email_label.setObjectName(u"email_label")
        self.email_label.setFont(font1)

        self.gridLayout.addWidget(self.email_label, 2, 2, 1, 1)

        self.change_into_button = QPushButton(self.centralwidget)
        self.change_into_button.setObjectName(u"change_into_button")
        self.change_into_button.setFont(font1)
        self.change_into_button.setFlat(True)

        self.gridLayout.addWidget(self.change_into_button, 12, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 483, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 4, 13, 1)

        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 5, 2, 1, 1)

        self.create_new_account_label = QLabel(self.centralwidget)
        self.create_new_account_label.setObjectName(u"create_new_account_label")
        self.create_new_account_label.setFont(font1)
        self.create_new_account_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.create_new_account_label, 1, 2, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 51, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 11, 3, 2, 1)

        self.horizontalSpacer = QSpacerItem(472, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 14, 2, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 51, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 11, 1, 2, 1)

        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout.addWidget(self.lineEdit_3, 7, 2, 1, 1)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 3, 2, 1, 1)

        self.main_logo = QLabel(self.centralwidget)
        self.main_logo.setObjectName(u"main_logo")
        self.main_logo.setMinimumSize(QSize(300, 150))
        self.main_logo.setFont(font1)
        self.main_logo.setFrameShape(QFrame.Shape.Box)
        self.main_logo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.main_logo, 0, 2, 1, 1)

        self.last_name_label = QLabel(self.centralwidget)
        self.last_name_label.setObjectName(u"last_name_label")
        self.last_name_label.setFont(font1)

        self.gridLayout.addWidget(self.last_name_label, 6, 2, 1, 1)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 13, 2, 1, 1)

        Create_Login.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Create_Login)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 526, 22))
        Create_Login.setMenuBar(self.menubar)

        self.retranslateUi(Create_Login)

        QMetaObject.connectSlotsByName(Create_Login)
    # setupUi

    def retranslateUi(self, Create_Login):
        Create_Login.setWindowTitle(QCoreApplication.translate("Create_Login", u"ClockWork", None))
        self.password_label.setText(QCoreApplication.translate("Create_Login", u"Password", None))
        self.create_account_log_in_button.setText(QCoreApplication.translate("Create_Login", u"Create Account", None))
        self.first_name_label.setText(QCoreApplication.translate("Create_Login", u"First Name", None))
        self.lineEdit_4.setText("")
        self.email_label.setText(QCoreApplication.translate("Create_Login", u"Email", None))
        self.change_into_button.setText(QCoreApplication.translate("Create_Login", u"Have an account? Log-In", None))
        self.lineEdit_2.setText("")
        self.create_new_account_label.setText(QCoreApplication.translate("Create_Login", u"Create New Account", None))
        self.lineEdit_3.setText("")
        self.lineEdit.setText("")
        self.main_logo.setText(QCoreApplication.translate("Create_Login", u"Logo", None))
        self.last_name_label.setText(QCoreApplication.translate("Create_Login", u"Last Name", None))
        self.pushButton.setText(QCoreApplication.translate("Create_Login", u"Exit Program", None))
    # retranslateUi

