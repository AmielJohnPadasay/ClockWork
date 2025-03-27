# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'submit_taskhGmlPb.ui'
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
    QLineEdit, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_SubmitTask(object):
    def setupUi(self, SubmitTask):
        if not SubmitTask.objectName():
            SubmitTask.setObjectName(u"SubmitTask")
        SubmitTask.resize(451, 358)
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setPointSize(11)
        SubmitTask.setFont(font)
        self.gridLayout = QGridLayout(SubmitTask)
        self.gridLayout.setObjectName(u"gridLayout")
        self.member_dest_box = QGroupBox(SubmitTask)
        self.member_dest_box.setObjectName(u"member_dest_box")
        self.gridLayout_3 = QGridLayout(self.member_dest_box)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.members_list = QListWidget(self.member_dest_box)
        self.members_list.setObjectName(u"members_list")
        self.members_list.setMinimumSize(QSize(0, 100))

        self.gridLayout_3.addWidget(self.members_list, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.member_dest_box, 1, 0, 1, 3)

        self.horizontalSpacer = QSpacerItem(268, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.submit_btn = QPushButton(SubmitTask)
        self.submit_btn.setObjectName(u"submit_btn")

        self.gridLayout.addWidget(self.submit_btn, 2, 1, 1, 1)

        self.cancel_btn = QPushButton(SubmitTask)
        self.cancel_btn.setObjectName(u"cancel_btn")

        self.gridLayout.addWidget(self.cancel_btn, 2, 2, 1, 1)

        self.link_requirement_box = QGroupBox(SubmitTask)
        self.link_requirement_box.setObjectName(u"link_requirement_box")
        self.gridLayout_2 = QGridLayout(self.link_requirement_box)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.link_requirement_edit = QLineEdit(self.link_requirement_box)
        self.link_requirement_edit.setObjectName(u"link_requirement_edit")

        self.gridLayout_2.addWidget(self.link_requirement_edit, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.link_requirement_box, 0, 0, 1, 3)


        self.retranslateUi(SubmitTask)

        QMetaObject.connectSlotsByName(SubmitTask)
    # setupUi

    def retranslateUi(self, SubmitTask):
        SubmitTask.setWindowTitle(QCoreApplication.translate("SubmitTask", u"Submit Task", None))
        self.member_dest_box.setTitle(QCoreApplication.translate("SubmitTask", u"Member Destination", None))
        self.submit_btn.setText(QCoreApplication.translate("SubmitTask", u"Submit", None))
        self.cancel_btn.setText(QCoreApplication.translate("SubmitTask", u"Cancel", None))
        self.link_requirement_box.setTitle(QCoreApplication.translate("SubmitTask", u"Link of the Requirement", None))
    # retranslateUi

