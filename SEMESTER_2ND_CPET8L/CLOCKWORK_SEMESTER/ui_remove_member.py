# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'remove_memberEaYkDc.ui'
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

class Ui_MemberRemoval(object):
    def setupUi(self, MemberRemoval):
        if not MemberRemoval.objectName():
            MemberRemoval.setObjectName(u"MemberRemoval")
        MemberRemoval.resize(452, 445)
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setPointSize(10)
        MemberRemoval.setFont(font)
        self.gridLayout_2 = QGridLayout(MemberRemoval)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer = QSpacerItem(130, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.remove_btn = QPushButton(MemberRemoval)
        self.remove_btn.setObjectName(u"remove_btn")

        self.gridLayout_2.addWidget(self.remove_btn, 1, 1, 1, 1)

        self.ok_btn = QPushButton(MemberRemoval)
        self.ok_btn.setObjectName(u"ok_btn")

        self.gridLayout_2.addWidget(self.ok_btn, 1, 2, 1, 1)

        self.cancel_btn = QPushButton(MemberRemoval)
        self.cancel_btn.setObjectName(u"cancel_btn")

        self.gridLayout_2.addWidget(self.cancel_btn, 1, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(130, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 4, 1, 1)

        self.group_members_box = QGroupBox(MemberRemoval)
        self.group_members_box.setObjectName(u"group_members_box")
        self.gridLayout = QGridLayout(self.group_members_box)
        self.gridLayout.setObjectName(u"gridLayout")
        self.members_list = QListWidget(self.group_members_box)
        self.members_list.setObjectName(u"members_list")

        self.gridLayout.addWidget(self.members_list, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.group_members_box, 0, 0, 1, 5)


        self.retranslateUi(MemberRemoval)

        QMetaObject.connectSlotsByName(MemberRemoval)
    # setupUi

    def retranslateUi(self, MemberRemoval):
        MemberRemoval.setWindowTitle(QCoreApplication.translate("MemberRemoval", u"Member Removal", None))
        self.remove_btn.setText(QCoreApplication.translate("MemberRemoval", u"Remove", None))
        self.ok_btn.setText(QCoreApplication.translate("MemberRemoval", u"OK", None))
        self.cancel_btn.setText(QCoreApplication.translate("MemberRemoval", u"Cancel", None))
        self.group_members_box.setTitle(QCoreApplication.translate("MemberRemoval", u"Group Members", None))
    # retranslateUi

