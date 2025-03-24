# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'validate_taskyeJGuk.ui'
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
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTextBrowser, QWidget)

class Ui_ValidateTask(object):
    def setupUi(self, ValidateTask):
        if not ValidateTask.objectName():
            ValidateTask.setObjectName(u"ValidateTask")
        ValidateTask.resize(432, 368)
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setPointSize(11)
        ValidateTask.setFont(font)
        self.gridLayout_2 = QGridLayout(ValidateTask)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.cancel_btn = QPushButton(ValidateTask)
        self.cancel_btn.setObjectName(u"cancel_btn")

        self.gridLayout_2.addWidget(self.cancel_btn, 1, 3, 1, 1)

        self.openlink_btn = QPushButton(ValidateTask)
        self.openlink_btn.setObjectName(u"openlink_btn")

        self.gridLayout_2.addWidget(self.openlink_btn, 1, 2, 1, 1)

        self.validate_task_btn = QPushButton(ValidateTask)
        self.validate_task_btn.setObjectName(u"validate_task_btn")

        self.gridLayout_2.addWidget(self.validate_task_btn, 1, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(63, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 1, 4, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(62, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.submitted_task_box = QGroupBox(ValidateTask)
        self.submitted_task_box.setObjectName(u"submitted_task_box")
        self.gridLayout = QGridLayout(self.submitted_task_box)
        self.gridLayout.setObjectName(u"gridLayout")
        self.name_task_label = QLabel(self.submitted_task_box)
        self.name_task_label.setObjectName(u"name_task_label")

        self.gridLayout.addWidget(self.name_task_label, 0, 0, 1, 1)

        self.taskname_label = QLabel(self.submitted_task_box)
        self.taskname_label.setObjectName(u"taskname_label")

        self.gridLayout.addWidget(self.taskname_label, 0, 1, 1, 2)

        self.name_task_label_2 = QLabel(self.submitted_task_box)
        self.name_task_label_2.setObjectName(u"name_task_label_2")

        self.gridLayout.addWidget(self.name_task_label_2, 1, 0, 1, 2)

        self.horizontalSpacer_4 = QSpacerItem(197, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 1, 2, 1, 1)

        self.reqtask_view = QTextBrowser(self.submitted_task_box)
        self.reqtask_view.setObjectName(u"reqtask_view")
        self.reqtask_view.setMinimumSize(QSize(0, 90))

        self.gridLayout.addWidget(self.reqtask_view, 2, 0, 1, 3)

        self.link_submitted_label = QLabel(self.submitted_task_box)
        self.link_submitted_label.setObjectName(u"link_submitted_label")

        self.gridLayout.addWidget(self.link_submitted_label, 3, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(247, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 3, 1, 1, 2)

        self.link_submitted_view = QTextBrowser(self.submitted_task_box)
        self.link_submitted_view.setObjectName(u"link_submitted_view")
        self.link_submitted_view.setMinimumSize(QSize(0, 90))

        self.gridLayout.addWidget(self.link_submitted_view, 4, 0, 1, 3)


        self.gridLayout_2.addWidget(self.submitted_task_box, 0, 0, 1, 5)


        self.retranslateUi(ValidateTask)

        QMetaObject.connectSlotsByName(ValidateTask)
    # setupUi

    def retranslateUi(self, ValidateTask):
        ValidateTask.setWindowTitle(QCoreApplication.translate("ValidateTask", u"Validate Task", None))
        self.cancel_btn.setText(QCoreApplication.translate("ValidateTask", u"Cancel", None))
        self.openlink_btn.setText(QCoreApplication.translate("ValidateTask", u"Open Link", None))
        self.validate_task_btn.setText(QCoreApplication.translate("ValidateTask", u"Validate Task", None))
        self.submitted_task_box.setTitle(QCoreApplication.translate("ValidateTask", u"Submitted Task", None))
        self.name_task_label.setText(QCoreApplication.translate("ValidateTask", u"Name of the Task:", None))
        self.taskname_label.setText(QCoreApplication.translate("ValidateTask", u"TaskName", None))
        self.name_task_label_2.setText(QCoreApplication.translate("ValidateTask", u"Requirement of the Task:", None))
        self.link_submitted_label.setText(QCoreApplication.translate("ValidateTask", u"Link Submitted:", None))
    # retranslateUi

