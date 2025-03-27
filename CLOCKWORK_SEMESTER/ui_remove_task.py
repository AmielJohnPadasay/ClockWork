# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'remove_taskELdqOL.ui'
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

class Ui_RemoveTask(object):
    def setupUi(self, RemoveTask):
        if not RemoveTask.objectName():
            RemoveTask.setObjectName(u"RemoveTask")
        RemoveTask.resize(456, 429)
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setPointSize(11)
        RemoveTask.setFont(font)
        self.gridLayout_2 = QGridLayout(RemoveTask)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.current_tasks_box = QGroupBox(RemoveTask)
        self.current_tasks_box.setObjectName(u"current_tasks_box")
        self.gridLayout = QGridLayout(self.current_tasks_box)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tasks_list = QListWidget(self.current_tasks_box)
        self.tasks_list.setObjectName(u"tasks_list")
        self.tasks_list.setFont(font)

        self.gridLayout.addWidget(self.tasks_list, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.current_tasks_box, 0, 0, 1, 5)

        self.horizontalSpacer = QSpacerItem(92, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.remove_btn = QPushButton(RemoveTask)
        self.remove_btn.setObjectName(u"remove_btn")

        self.gridLayout_2.addWidget(self.remove_btn, 1, 1, 1, 1)

        self.ok_btn = QPushButton(RemoveTask)
        self.ok_btn.setObjectName(u"ok_btn")

        self.gridLayout_2.addWidget(self.ok_btn, 1, 2, 1, 1)

        self.cancel_btn = QPushButton(RemoveTask)
        self.cancel_btn.setObjectName(u"cancel_btn")

        self.gridLayout_2.addWidget(self.cancel_btn, 1, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(91, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 4, 1, 1)


        self.retranslateUi(RemoveTask)

        QMetaObject.connectSlotsByName(RemoveTask)
    # setupUi

    def retranslateUi(self, RemoveTask):
        RemoveTask.setWindowTitle(QCoreApplication.translate("RemoveTask", u"Remove Task", None))
        self.current_tasks_box.setTitle(QCoreApplication.translate("RemoveTask", u"Current Tasks", None))
        self.remove_btn.setText(QCoreApplication.translate("RemoveTask", u"Remove", None))
        self.ok_btn.setText(QCoreApplication.translate("RemoveTask", u"OK", None))
        self.cancel_btn.setText(QCoreApplication.translate("RemoveTask", u"Cancel", None))
    # retranslateUi

