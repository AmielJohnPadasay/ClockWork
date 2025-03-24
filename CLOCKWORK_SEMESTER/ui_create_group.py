# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_groupBPVmiU.ui'
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
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)

class Ui_Create_Group(object):
    def setupUi(self, Create_Group):
        if not Create_Group.objectName():
            Create_Group.setObjectName(u"Create_Group")
        Create_Group.resize(439, 336)
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setPointSize(12)
        Create_Group.setFont(font)
        self.gridLayout_2 = QGridLayout(Create_Group)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton = QPushButton(Create_Group)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_2.addWidget(self.pushButton, 1, 2, 1, 1)

        self.groupBox = QGroupBox(Create_Group)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.listWidget = QListWidget(self.groupBox)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMinimumSize(QSize(150, 0))

        self.gridLayout.addWidget(self.listWidget, 3, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 3)

        self.horizontalSpacer = QSpacerItem(208, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.pushButton_2 = QPushButton(Create_Group)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_2.addWidget(self.pushButton_2, 1, 1, 1, 1)


        self.retranslateUi(Create_Group)

        QMetaObject.connectSlotsByName(Create_Group)
    # setupUi

    def retranslateUi(self, Create_Group):
        Create_Group.setWindowTitle(QCoreApplication.translate("Create_Group", u"Create Group", None))
        self.pushButton.setText(QCoreApplication.translate("Create_Group", u"Cancel", None))
        self.groupBox.setTitle(QCoreApplication.translate("Create_Group", u"Group Details", None))
        self.label.setText(QCoreApplication.translate("Create_Group", u"Group Name", None))
        self.label_2.setText(QCoreApplication.translate("Create_Group", u"Group Members", None))
        self.pushButton_2.setText(QCoreApplication.translate("Create_Group", u"OK", None))
    # retranslateUi

