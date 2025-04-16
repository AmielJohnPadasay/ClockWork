# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'supervisor_passwordlNtXNf.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_Sup_Password(object):
    def setupUi(self, Sup_Password):
        if not Sup_Password.objectName():
            Sup_Password.setObjectName(u"Sup_Password")
        Sup_Password.resize(270, 230)
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setPointSize(11)
        Sup_Password.setFont(font)
        self.gridLayout = QGridLayout(Sup_Password)
        self.gridLayout.setObjectName(u"gridLayout")
        self.cancel_btn = QPushButton(Sup_Password)
        self.cancel_btn.setObjectName(u"cancel_btn")

        self.gridLayout.addWidget(self.cancel_btn, 2, 2, 1, 1)

        self.ok_btn = QPushButton(Sup_Password)
        self.ok_btn.setObjectName(u"ok_btn")

        self.gridLayout.addWidget(self.ok_btn, 2, 1, 1, 1)

        self.password_input = QLineEdit(Sup_Password)
        self.password_input.setObjectName(u"password_input")

        self.gridLayout.addWidget(self.password_input, 0, 1, 1, 2)

        self.password_label = QLabel(Sup_Password)
        self.password_label.setObjectName(u"password_label")

        self.gridLayout.addWidget(self.password_label, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 3, 0, 1, 3)


        self.retranslateUi(Sup_Password)

        QMetaObject.connectSlotsByName(Sup_Password)
    # setupUi

    def retranslateUi(self, Sup_Password):
        Sup_Password.setWindowTitle(QCoreApplication.translate("Sup_Password", u"Password", None))
        self.cancel_btn.setText(QCoreApplication.translate("Sup_Password", u"Cancel", None))
        self.ok_btn.setText(QCoreApplication.translate("Sup_Password", u"OK", None))
        self.password_label.setText(QCoreApplication.translate("Sup_Password", u"Password:", None))
    # retranslateUi

