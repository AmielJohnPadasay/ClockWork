# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'group_membersAlOBGf.ui'
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
    QHeaderView, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_GroupMembers(object):
    def setupUi(self, GroupMembers):
        if not GroupMembers.objectName():
            GroupMembers.setObjectName(u"GroupMembers")
        GroupMembers.resize(468, 346)
        font = QFont()
        font.setFamilies([u"Verdana"])
        GroupMembers.setFont(font)
        self.gridLayout_2 = QGridLayout(GroupMembers)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer = QSpacerItem(97, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.add_member_btn = QPushButton(GroupMembers)
        self.add_member_btn.setObjectName(u"add_member_btn")

        self.gridLayout_2.addWidget(self.add_member_btn, 1, 1, 1, 1)

        self.remove_member_btn = QPushButton(GroupMembers)
        self.remove_member_btn.setObjectName(u"remove_member_btn")

        self.gridLayout_2.addWidget(self.remove_member_btn, 1, 2, 1, 1)

        self.cancel_btn = QPushButton(GroupMembers)
        self.cancel_btn.setObjectName(u"cancel_btn")

        self.gridLayout_2.addWidget(self.cancel_btn, 1, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(97, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 4, 1, 1)

        self.group_members_box = QGroupBox(GroupMembers)
        self.group_members_box.setObjectName(u"group_members_box")
        self.gridLayout = QGridLayout(self.group_members_box)
        self.gridLayout.setObjectName(u"gridLayout")
        self.members_table = QTableWidget(self.group_members_box)
        if (self.members_table.columnCount() < 2):
            self.members_table.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.members_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.members_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.members_table.rowCount() < 3):
            self.members_table.setRowCount(3)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.members_table.setItem(0, 0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.members_table.setItem(0, 1, __qtablewidgetitem3)
        self.members_table.setObjectName(u"members_table")
        self.members_table.setWordWrap(False)
        self.members_table.horizontalHeader().setCascadingSectionResizes(False)
        self.members_table.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.members_table.horizontalHeader().setStretchLastSection(True)

        self.gridLayout.addWidget(self.members_table, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.group_members_box, 0, 0, 1, 5)


        self.retranslateUi(GroupMembers)

        QMetaObject.connectSlotsByName(GroupMembers)
    # setupUi

    def retranslateUi(self, GroupMembers):
        GroupMembers.setWindowTitle(QCoreApplication.translate("GroupMembers", u"Group Members", None))
        self.add_member_btn.setText(QCoreApplication.translate("GroupMembers", u"Add Member", None))
        self.remove_member_btn.setText(QCoreApplication.translate("GroupMembers", u"Remove Member", None))
        self.cancel_btn.setText(QCoreApplication.translate("GroupMembers", u"Cancel", None))
        self.group_members_box.setTitle(QCoreApplication.translate("GroupMembers", u"Group Members", None))
        ___qtablewidgetitem = self.members_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("GroupMembers", u"Name", None));
        ___qtablewidgetitem1 = self.members_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("GroupMembers", u"Email", None));

        __sortingEnabled = self.members_table.isSortingEnabled()
        self.members_table.setSortingEnabled(False)
        self.members_table.setSortingEnabled(__sortingEnabled)

    # retranslateUi

