# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design6.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QDialog, QSizePolicy,
    QVBoxLayout, QWidget)
import files6_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(634, 363)
        icon = QIcon()
        icon.addFile(u":/icons/icons/calendar.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(u"QWidget {\n"
"	color: white;\n"
"	background-color: #121212;\n"
"	font-family: Rubik;\n"
"	font-size: 16pt;\n"
"	font-weight: 600;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: transparent;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #666;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #888;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.calendarWidget = QCalendarWidget(Dialog)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setStyleSheet(u"QCalendarWidget QToolButton {\n"
"\n"
"\n"
"height:40px;\n"
"width:150px;\n"
"color:white;\n"
"font-size:20px;\n"
"icon-size:56px,56px;\n"
"background-color:black;\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QCalendarWidget  QWidget{\n"
"\n"
"alternate-background-color:rgb(128,128,128)\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"QCalendarWidget QAbstractItemView:enabled {\n"
"\n"
"\n"
"font-size:18px;\n"
"color:rgb(180,180,180);\n"
"background-color:black;\n"
"selection-background-color:rgb(64,64,64);\n"
"selection-color:rgb(0,255,0);\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")

        self.verticalLayout.addWidget(self.calendarWidget)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Calendar - botest", None))
    # retranslateUi

