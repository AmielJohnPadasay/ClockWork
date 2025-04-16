# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_dashboardupPaMm.ui'
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
    QMainWindow, QMenuBar, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStatusBar, QWidget)

class Ui_MainDashboard(object):
    def setupUi(self, MainDashboard):
        if not MainDashboard.objectName():
            MainDashboard.setObjectName(u"MainDashboard")
        MainDashboard.resize(563, 465)
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setPointSize(11)
        MainDashboard.setFont(font)
        MainDashboard.setStyleSheet(u"")
        self.centralwidget = QWidget(MainDashboard)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.logo = QLabel(self.centralwidget)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(150, 0))
        self.logo.setFrameShape(QFrame.Shape.Box)

        self.gridLayout_2.addWidget(self.logo, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(318, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 1, 1, 2)

        self.account_btn = QPushButton(self.centralwidget)
        self.account_btn.setObjectName(u"account_btn")
        self.account_btn.setMinimumSize(QSize(80, 50))
        self.account_btn.setMaximumSize(QSize(50, 50))
        self.account_btn.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.account_btn, 0, 3, 1, 1)

        self.groups_container = QScrollArea(self.centralwidget)
        self.groups_container.setObjectName(u"groups_container")
        self.groups_container.setMinimumSize(QSize(300, 0))
        self.groups_container.setStyleSheet(u"")
        self.groups_container.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 543, 310))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.create_group_btn = QPushButton(self.scrollAreaWidgetContents)
        self.create_group_btn.setObjectName(u"create_group_btn")
        self.create_group_btn.setMinimumSize(QSize(260, 100))

        self.gridLayout.addWidget(self.create_group_btn, 0, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(318, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 0, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 69, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 1, 1, 1, 1)

        self.groups_container.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.groups_container, 1, 0, 1, 4)

        self.horizontalSpacer_2 = QSpacerItem(374, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 2, 0, 1, 2)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_2.addWidget(self.pushButton_2, 2, 2, 1, 1)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_2.addWidget(self.pushButton, 2, 3, 1, 1)

        MainDashboard.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainDashboard)
        self.statusbar.setObjectName(u"statusbar")
        MainDashboard.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainDashboard)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 563, 24))
        MainDashboard.setMenuBar(self.menubar)

        self.retranslateUi(MainDashboard)

        QMetaObject.connectSlotsByName(MainDashboard)
    # setupUi

    def retranslateUi(self, MainDashboard):
        MainDashboard.setWindowTitle(QCoreApplication.translate("MainDashboard", u"Dashboard", None))
        self.logo.setText(QCoreApplication.translate("MainDashboard", u"Logo", None))
        self.account_btn.setText(QCoreApplication.translate("MainDashboard", u"Account", None))
        self.create_group_btn.setText(QCoreApplication.translate("MainDashboard", u"Create Group", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainDashboard", u"Log-Out", None))
        self.pushButton.setText(QCoreApplication.translate("MainDashboard", u"Quit", None))
    # retranslateUi

