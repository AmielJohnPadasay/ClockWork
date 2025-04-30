# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'activity_loggHvTwg.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHeaderView, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_ActivityLog(object):
    def setupUi(self, ActivityLog):
        if not ActivityLog.objectName():
            ActivityLog.setObjectName(u"ActivityLog")
        ActivityLog.resize(494, 510)
        font = QFont()
        font.setFamilies([u"Verdana"])
        ActivityLog.setFont(font)
        self.centralwidget = QWidget(ActivityLog)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.members_percent_box = QGroupBox(self.centralwidget)
        self.members_percent_box.setObjectName(u"members_percent_box")
        self.gridLayout = QGridLayout(self.members_percent_box)
        self.gridLayout.setObjectName(u"gridLayout")
        self.table_member_percent = QTableWidget(self.members_percent_box)
        if (self.table_member_percent.columnCount() < 2):
            self.table_member_percent.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_member_percent.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_member_percent.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.table_member_percent.rowCount() < 3):
            self.table_member_percent.setRowCount(3)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_member_percent.setItem(0, 1, __qtablewidgetitem2)
        self.table_member_percent.setObjectName(u"table_member_percent")
        self.table_member_percent.setMinimumSize(QSize(200, 150))
        self.table_member_percent.horizontalHeader().setStretchLastSection(True)
        self.table_member_percent.verticalHeader().setCascadingSectionResizes(True)
        self.table_member_percent.verticalHeader().setStretchLastSection(False)

        self.gridLayout.addWidget(self.table_member_percent, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.members_percent_box, 0, 0, 1, 3)

        self.productivity_rate_box = QGroupBox(self.centralwidget)
        self.productivity_rate_box.setObjectName(u"productivity_rate_box")
        self.productivity_rate_box.setMinimumSize(QSize(0, 0))
        self.gridLayout_2 = QGridLayout(self.productivity_rate_box)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.line_graph = QLabel(self.productivity_rate_box)
        self.line_graph.setObjectName(u"line_graph")
        self.line_graph.setMinimumSize(QSize(300, 170))
        self.line_graph.setFrameShape(QFrame.Shape.Box)
        self.line_graph.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.line_graph, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.productivity_rate_box, 1, 0, 1, 3)

        self.OK_btn = QPushButton(self.centralwidget)
        self.OK_btn.setObjectName(u"OK_btn")

        self.gridLayout_3.addWidget(self.OK_btn, 3, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 3, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 3, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 2, 1, 1, 1)

        ActivityLog.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ActivityLog)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 494, 21))
        ActivityLog.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ActivityLog)
        self.statusbar.setObjectName(u"statusbar")
        ActivityLog.setStatusBar(self.statusbar)

        self.retranslateUi(ActivityLog)

        QMetaObject.connectSlotsByName(ActivityLog)
    # setupUi

    def retranslateUi(self, ActivityLog):
        ActivityLog.setWindowTitle(QCoreApplication.translate("ActivityLog", u"Activity Log", None))
        self.members_percent_box.setTitle(QCoreApplication.translate("ActivityLog", u"Member's Percentage of Submission", None))
        ___qtablewidgetitem = self.table_member_percent.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ActivityLog", u"Name", None));
        ___qtablewidgetitem1 = self.table_member_percent.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ActivityLog", u"Percentage of Submission", None));

        __sortingEnabled = self.table_member_percent.isSortingEnabled()
        self.table_member_percent.setSortingEnabled(False)
        self.table_member_percent.setSortingEnabled(__sortingEnabled)

        self.productivity_rate_box.setTitle(QCoreApplication.translate("ActivityLog", u"Productivity Rate", None))
        self.line_graph.setText(QCoreApplication.translate("ActivityLog", u"Line Graph", None))
        self.OK_btn.setText(QCoreApplication.translate("ActivityLog", u"OK", None))
    # retranslateUi

