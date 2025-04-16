# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'group_settingsppNcDY.ui'
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
    QWidget)

class Ui_GroupSettings(object):
    def setupUi(self, GroupSettings):
        if not GroupSettings.objectName():
            GroupSettings.setObjectName(u"GroupSettings")
        GroupSettings.resize(427, 219)
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setPointSize(11)
        GroupSettings.setFont(font)
        self.gridLayout_2 = QGridLayout(GroupSettings)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.ok_btn = QPushButton(GroupSettings)
        self.ok_btn.setObjectName(u"ok_btn")

        self.gridLayout_2.addWidget(self.ok_btn, 1, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.cancel_btn = QPushButton(GroupSettings)
        self.cancel_btn.setObjectName(u"cancel_btn")

        self.gridLayout_2.addWidget(self.cancel_btn, 1, 2, 1, 1)

        self.group_mod_box = QGroupBox(GroupSettings)
        self.group_mod_box.setObjectName(u"group_mod_box")
        self.gridLayout = QGridLayout(self.group_mod_box)
        self.gridLayout.setObjectName(u"gridLayout")
        self.delete_group_label = QLabel(self.group_mod_box)
        self.delete_group_label.setObjectName(u"delete_group_label")

        self.gridLayout.addWidget(self.delete_group_label, 0, 0, 1, 1)

        self.delete_btn = QPushButton(self.group_mod_box)
        self.delete_btn.setObjectName(u"delete_btn")

        self.gridLayout.addWidget(self.delete_btn, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.group_mod_box, 0, 0, 1, 3)


        self.retranslateUi(GroupSettings)

        QMetaObject.connectSlotsByName(GroupSettings)
    # setupUi

    def retranslateUi(self, GroupSettings):
        GroupSettings.setWindowTitle(QCoreApplication.translate("GroupSettings", u"Settings", None))
        self.ok_btn.setText(QCoreApplication.translate("GroupSettings", u"OK", None))
        self.cancel_btn.setText(QCoreApplication.translate("GroupSettings", u"Cancel", None))
        self.group_mod_box.setTitle(QCoreApplication.translate("GroupSettings", u"Group Modifications", None))
        self.delete_group_label.setText(QCoreApplication.translate("GroupSettings", u"Delete this Group", None))
        self.delete_btn.setText(QCoreApplication.translate("GroupSettings", u"Delete", None))
    # retranslateUi

