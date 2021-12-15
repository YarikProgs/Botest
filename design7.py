# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design7.ui'
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
from PySide6.QtWidgets import (QApplication, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QTextEdit, QWidget)
import files7_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(380, 542)
        MainWindow.setMinimumSize(QSize(380, 542))
        MainWindow.setMaximumSize(QSize(380, 542))
        icon = QIcon()
        icon.addFile(u":/icons/icons/question.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget {\n"
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
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btn_youtube = QPushButton(self.centralwidget)
        self.btn_youtube.setObjectName(u"btn_youtube")
        self.btn_youtube.setGeometry(QRect(0, 0, 211, 170))
        self.btn_youtube.setMinimumSize(QSize(0, 0))
        self.btn_youtube.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: #FF0000;\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #EE204D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color:  #FC2847;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/youtube.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_youtube.setIcon(icon1)
        self.btn_youtube.setIconSize(QSize(100, 100))
        self.command_line = QTextEdit(self.centralwidget)
        self.command_line.setObjectName(u"command_line")
        self.command_line.setGeometry(QRect(10, 440, 321, 90))
        self.command_line.setReadOnly(True)
        self.btn_router = QPushButton(self.centralwidget)
        self.btn_router.setObjectName(u"btn_router")
        self.btn_router.setGeometry(QRect(210, 0, 170, 170))
        self.btn_router.setMinimumSize(QSize(0, 0))
        self.btn_router.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background-color: #33ccff;\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #00bfff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color:  #7fc7ff;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/router.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_router.setIcon(icon2)
        self.btn_router.setIconSize(QSize(100, 100))
        self.go = QPushButton(self.centralwidget)
        self.go.setObjectName(u"go")
        self.go.setGeometry(QRect(330, 470, 40, 40))
        self.go.setIcon(icon1)
        self.go.setIconSize(QSize(80, 80))
        self.admin = QLineEdit(self.centralwidget)
        self.admin.setObjectName(u"admin")
        self.admin.setGeometry(QRect(40, 230, 291, 31))
        self.admin_ = QLineEdit(self.centralwidget)
        self.admin_.setObjectName(u"admin_")
        self.admin_.setGeometry(QRect(40, 260, 291, 31))
        self.login = QPushButton(self.centralwidget)
        self.login.setObjectName(u"login")
        self.login.setGeometry(QRect(40, 290, 291, 23))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"???????????????????????????????????????????????????????", None))
        self.btn_youtube.setText("")
        self.btn_router.setText("")
        self.go.setText("")
        self.login.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0441\u0442\u0438 \u043b\u043e\u0433\u0438\u043d \u0438 \u043f\u0430\u0440\u043e\u043b\u044c.", None))
    # retranslateUi

