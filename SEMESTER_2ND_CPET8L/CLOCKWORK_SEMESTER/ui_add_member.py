# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_memberMFEiEL.ui'
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

class Ui_MemberAddition(object):
    def setupUi(self, MemberAddition):
        if not MemberAddition.objectName():
            MemberAddition.setObjectName(u"MemberAddition")
        MemberAddition.resize(516, 356)
        MemberAddition.setMinimumSize(QSize(200, 150))
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setPointSize(11)
        MemberAddition.setFont(font)
        self.gridLayout_2 = QGridLayout(MemberAddition)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.users_box = QGroupBox(MemberAddition)
        self.users_box.setObjectName(u"users_box")
        self.gridLayout = QGridLayout(self.users_box)
        self.gridLayout.setObjectName(u"gridLayout")
        self.users_list = QListWidget(self.users_box)
        self.users_list.setObjectName(u"users_list")

        self.gridLayout.addWidget(self.users_list, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.users_box, 0, 0, 1, 5)

        self.horizontalSpacer = QSpacerItem(119, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.add_btn = QPushButton(MemberAddition)
        self.add_btn.setObjectName(u"add_btn")

        self.gridLayout_2.addWidget(self.add_btn, 1, 1, 1, 1)

        self.ok_btn = QPushButton(MemberAddition)
        self.ok_btn.setObjectName(u"ok_btn")

        self.gridLayout_2.addWidget(self.ok_btn, 1, 2, 1, 1)

        self.cancel_btn = QPushButton(MemberAddition)
        self.cancel_btn.setObjectName(u"cancel_btn")

        self.gridLayout_2.addWidget(self.cancel_btn, 1, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(119, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 4, 1, 1)


        self.retranslateUi(MemberAddition)

        QMetaObject.connectSlotsByName(MemberAddition)
    # setupUi

    def retranslateUi(self, MemberAddition):
        MemberAddition.setWindowTitle(QCoreApplication.translate("MemberAddition", u"Member Addition", None))
        self.users_box.setTitle(QCoreApplication.translate("MemberAddition", u"Users", None))
        self.add_btn.setText(QCoreApplication.translate("MemberAddition", u"Add", None))
        self.ok_btn.setText(QCoreApplication.translate("MemberAddition", u"OK", None))
        self.cancel_btn.setText(QCoreApplication.translate("MemberAddition", u"Cancel", None))
    # retranslateUi

