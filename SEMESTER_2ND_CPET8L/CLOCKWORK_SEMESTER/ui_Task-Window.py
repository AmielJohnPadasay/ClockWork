# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Task-WindowKxxxsM.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QGroupBox,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_TaskWindow(object):
    def setupUi(self, TaskWindow):
        if not TaskWindow.objectName():
            TaskWindow.setObjectName(u"TaskWindow")
        TaskWindow.resize(559, 333)
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setPointSize(11)
        TaskWindow.setFont(font)
        self.gridLayout_2 = QGridLayout(TaskWindow)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer = QSpacerItem(272, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.assigntask_btn = QPushButton(TaskWindow)
        self.assigntask_btn.setObjectName(u"assigntask_btn")

        self.gridLayout_2.addWidget(self.assigntask_btn, 1, 1, 1, 1)

        self.removetask_btn = QPushButton(TaskWindow)
        self.removetask_btn.setObjectName(u"removetask_btn")

        self.gridLayout_2.addWidget(self.removetask_btn, 1, 2, 1, 1)

        self.submit_task_btn = QPushButton(TaskWindow)
        self.submit_task_btn.setObjectName(u"submit_task_btn")

        self.gridLayout_2.addWidget(self.submit_task_btn, 1, 3, 1, 1)

        self.ok_btn = QPushButton(TaskWindow)
        self.ok_btn.setObjectName(u"ok_btn")

        self.gridLayout_2.addWidget(self.ok_btn, 1, 4, 1, 1)

        self.cancel_btn = QPushButton(TaskWindow)
        self.cancel_btn.setObjectName(u"cancel_btn")

        self.gridLayout_2.addWidget(self.cancel_btn, 1, 5, 1, 1)

        self.current_tasks_box = QGroupBox(TaskWindow)
        self.current_tasks_box.setObjectName(u"current_tasks_box")
        self.gridLayout = QGridLayout(self.current_tasks_box)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tasks_list = QListWidget(self.current_tasks_box)
        self.tasks_list.setObjectName(u"tasks_list")
        self.tasks_list.setFont(font)

        self.gridLayout.addWidget(self.tasks_list, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.current_tasks_box, 0, 0, 1, 6)


        self.retranslateUi(TaskWindow)

        QMetaObject.connectSlotsByName(TaskWindow)
    # setupUi

    def retranslateUi(self, TaskWindow):
        TaskWindow.setWindowTitle(QCoreApplication.translate("TaskWindow", u"Task Window", None))
        self.assigntask_btn.setText(QCoreApplication.translate("TaskWindow", u"Assign Task", None))
        self.removetask_btn.setText(QCoreApplication.translate("TaskWindow", u"Remove Task", None))
        self.submit_task_btn.setText(QCoreApplication.translate("TaskWindow", u"Submit Task", None))
        self.ok_btn.setText(QCoreApplication.translate("TaskWindow", u"OK", None))
        self.cancel_btn.setText(QCoreApplication.translate("TaskWindow", u"Cancel", None))
        self.current_tasks_box.setTitle(QCoreApplication.translate("TaskWindow", u"Current Tasks", None))
    # retranslateUi

