# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'assign_taskxBCFDw.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QDialog, QGridLayout,
    QGroupBox, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QSpacerItem,
    QTextEdit, QTimeEdit, QWidget)

class Ui_AssignTask(object):
    def setupUi(self, AssignTask):
        if not AssignTask.objectName():
            AssignTask.setObjectName(u"AssignTask")
        AssignTask.resize(506, 403)
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setPointSize(11)
        AssignTask.setFont(font)
        self.gridLayout_3 = QGridLayout(AssignTask)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.task_details_box = QGroupBox(AssignTask)
        self.task_details_box.setObjectName(u"task_details_box")
        self.gridLayout = QGridLayout(self.task_details_box)
        self.gridLayout.setObjectName(u"gridLayout")
        self.taskname_edit = QLineEdit(self.task_details_box)
        self.taskname_edit.setObjectName(u"taskname_edit")

        self.gridLayout.addWidget(self.taskname_edit, 0, 1, 1, 1)

        self.taskreq_edit = QTextEdit(self.task_details_box)
        self.taskreq_edit.setObjectName(u"taskreq_edit")

        self.gridLayout.addWidget(self.taskreq_edit, 2, 0, 1, 2)

        self.req_task_label = QLabel(self.task_details_box)
        self.req_task_label.setObjectName(u"req_task_label")

        self.gridLayout.addWidget(self.req_task_label, 1, 0, 1, 2)

        self.name_task_label = QLabel(self.task_details_box)
        self.name_task_label.setObjectName(u"name_task_label")

        self.gridLayout.addWidget(self.name_task_label, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.task_details_box, 0, 0, 1, 3)

        self.assign_task_box = QGroupBox(AssignTask)
        self.assign_task_box.setObjectName(u"assign_task_box")
        self.gridLayout_2 = QGridLayout(self.assign_task_box)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.assignmember_list = QListWidget(self.assign_task_box)
        self.assignmember_list.setObjectName(u"assignmember_list")

        self.gridLayout_2.addWidget(self.assignmember_list, 0, 1, 2, 3)

        self.assign_members_label = QLabel(self.assign_task_box)
        self.assign_members_label.setObjectName(u"assign_members_label")

        self.gridLayout_2.addWidget(self.assign_members_label, 0, 0, 1, 1)

        self.duetimeEdit = QTimeEdit(self.assign_task_box)
        self.duetimeEdit.setObjectName(u"duetimeEdit")

        self.gridLayout_2.addWidget(self.duetimeEdit, 2, 3, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.duedate_label = QLabel(self.assign_task_box)
        self.duedate_label.setObjectName(u"duedate_label")

        self.gridLayout_2.addWidget(self.duedate_label, 2, 0, 1, 1)

        self.duedateEdit = QDateEdit(self.assign_task_box)
        self.duedateEdit.setObjectName(u"duedateEdit")

        self.gridLayout_2.addWidget(self.duedateEdit, 2, 1, 1, 2)


        self.gridLayout_3.addWidget(self.assign_task_box, 1, 0, 1, 3)

        self.horizontalSpacer = QSpacerItem(323, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.ok_btn = QPushButton(AssignTask)
        self.ok_btn.setObjectName(u"ok_btn")

        self.gridLayout_3.addWidget(self.ok_btn, 2, 1, 1, 1)

        self.cancel_btn = QPushButton(AssignTask)
        self.cancel_btn.setObjectName(u"cancel_btn")

        self.gridLayout_3.addWidget(self.cancel_btn, 2, 2, 1, 1)


        self.retranslateUi(AssignTask)

        QMetaObject.connectSlotsByName(AssignTask)
    # setupUi

    def retranslateUi(self, AssignTask):
        AssignTask.setWindowTitle(QCoreApplication.translate("AssignTask", u"Assign Task", None))
        self.task_details_box.setTitle(QCoreApplication.translate("AssignTask", u"Task Details", None))
        self.req_task_label.setText(QCoreApplication.translate("AssignTask", u"Requirements of the Task", None))
        self.name_task_label.setText(QCoreApplication.translate("AssignTask", u"Name of Task", None))
        self.assign_task_box.setTitle(QCoreApplication.translate("AssignTask", u"Assign Task", None))
        self.assign_members_label.setText(QCoreApplication.translate("AssignTask", u"Assign Members", None))
        self.duedate_label.setText(QCoreApplication.translate("AssignTask", u"Due Date", None))
        self.ok_btn.setText(QCoreApplication.translate("AssignTask", u"OK", None))
        self.cancel_btn.setText(QCoreApplication.translate("AssignTask", u"Cancel", None))
    # retranslateUi

