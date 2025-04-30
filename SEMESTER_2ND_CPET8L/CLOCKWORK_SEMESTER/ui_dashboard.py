# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboardppHMSV.ui'
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QFrame, QGridLayout,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QWidget)

class Ui_Group_Dashboard(object):
    def setupUi(self, Group_Dashboard):
        if not Group_Dashboard.objectName():
            Group_Dashboard.setObjectName(u"Group_Dashboard")
        Group_Dashboard.resize(555, 529)
        font = QFont()
        font.setFamilies([u"Verdana"])
        Group_Dashboard.setFont(font)
        Group_Dashboard.setAutoFillBackground(False)
        self.centralwidget = QWidget(Group_Dashboard)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.logo = QLabel(self.centralwidget)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(100, 50))
        self.logo.setFrameShape(QFrame.Shape.Box)
        self.logo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.logo, 0, 0, 1, 2)

        self.horizontalSpacer = QSpacerItem(594, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.account_btn = QPushButton(self.centralwidget)
        self.account_btn.setObjectName(u"account_btn")
        self.account_btn.setMinimumSize(QSize(80, 50))
        self.account_btn.setMaximumSize(QSize(50, 50))
        self.account_btn.setStyleSheet(u"")

        self.gridLayout.addWidget(self.account_btn, 0, 3, 1, 1)

        self.btns_frame = QFrame(self.centralwidget)
        self.btns_frame.setObjectName(u"btns_frame")
        self.btns_frame.setMaximumSize(QSize(16777215, 16777215))
        self.btns_frame.setStyleSheet(u"")
        self.btns_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.btns_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.btns_frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.activity_log_btn = QPushButton(self.btns_frame)
        self.activity_log_btn.setObjectName(u"activity_log_btn")
        self.activity_log_btn.setMinimumSize(QSize(80, 50))
        self.activity_log_btn.setMaximumSize(QSize(50, 50))

        self.gridLayout_2.addWidget(self.activity_log_btn, 0, 0, 1, 1)

        self.group_members_btn = QPushButton(self.btns_frame)
        self.group_members_btn.setObjectName(u"group_members_btn")
        self.group_members_btn.setMinimumSize(QSize(80, 50))
        self.group_members_btn.setMaximumSize(QSize(50, 50))

        self.gridLayout_2.addWidget(self.group_members_btn, 1, 0, 1, 1)

        self.back_to_main_dashboard_btn = QPushButton(self.btns_frame)
        self.back_to_main_dashboard_btn.setObjectName(u"back_to_main_dashboard_btn")
        self.back_to_main_dashboard_btn.setMinimumSize(QSize(80, 50))
        self.back_to_main_dashboard_btn.setMaximumSize(QSize(50, 50))

        self.gridLayout_2.addWidget(self.back_to_main_dashboard_btn, 3, 0, 1, 1)

        self.group_settings_btn = QPushButton(self.btns_frame)
        self.group_settings_btn.setObjectName(u"group_settings_btn")
        self.group_settings_btn.setMinimumSize(QSize(80, 50))
        self.group_settings_btn.setMaximumSize(QSize(50, 50))

        self.gridLayout_2.addWidget(self.group_settings_btn, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.btns_frame, 1, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(573, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 2, 0, 1, 4)

        self.Task_Calendar = QCalendarWidget(self.centralwidget)
        self.Task_Calendar.setObjectName(u"Task_Calendar")

        self.gridLayout.addWidget(self.Task_Calendar, 1, 2, 1, 2)

        Group_Dashboard.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Group_Dashboard)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 555, 21))
        Group_Dashboard.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Group_Dashboard)
        self.statusbar.setObjectName(u"statusbar")
        Group_Dashboard.setStatusBar(self.statusbar)

        self.retranslateUi(Group_Dashboard)

        QMetaObject.connectSlotsByName(Group_Dashboard)
    # setupUi

    def retranslateUi(self, Group_Dashboard):
        Group_Dashboard.setWindowTitle(QCoreApplication.translate("Group_Dashboard", u"Group Dashboard", None))
        self.logo.setText(QCoreApplication.translate("Group_Dashboard", u"Logo", None))
#if QT_CONFIG(tooltip)
        self.account_btn.setToolTip(QCoreApplication.translate("Group_Dashboard", u"Account", None))
#endif // QT_CONFIG(tooltip)
        self.account_btn.setText(QCoreApplication.translate("Group_Dashboard", u"Account", None))
#if QT_CONFIG(tooltip)
        self.activity_log_btn.setToolTip(QCoreApplication.translate("Group_Dashboard", u"Activity Log", None))
#endif // QT_CONFIG(tooltip)
        self.activity_log_btn.setText(QCoreApplication.translate("Group_Dashboard", u"Activity Log", None))
#if QT_CONFIG(tooltip)
        self.group_members_btn.setToolTip(QCoreApplication.translate("Group_Dashboard", u"Group Members", None))
#endif // QT_CONFIG(tooltip)
        self.group_members_btn.setText(QCoreApplication.translate("Group_Dashboard", u"Group Members", None))
#if QT_CONFIG(tooltip)
        self.back_to_main_dashboard_btn.setToolTip(QCoreApplication.translate("Group_Dashboard", u"Back to Main Dashboard", None))
#endif // QT_CONFIG(tooltip)
        self.back_to_main_dashboard_btn.setText(QCoreApplication.translate("Group_Dashboard", u"Back to Main Dashboard", None))
#if QT_CONFIG(tooltip)
        self.group_settings_btn.setToolTip(QCoreApplication.translate("Group_Dashboard", u"Group Settings", None))
#endif // QT_CONFIG(tooltip)
        self.group_settings_btn.setText(QCoreApplication.translate("Group_Dashboard", u"Group Settings", None))
    # retranslateUi

