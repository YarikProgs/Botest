# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QSizePolicy,
    QTextEdit, QWidget)
import files2_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(350, 600)
        icon = QIcon()
        icon.addFile(u":/icons/robot.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget {\n"
"	color: white;\n"
"	background-color: #121212;\n"
"	font-family: Rubik;\n"
"	font-size: 12pt;\n"
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
        self.btn_days = QPushButton(self.centralwidget)
        self.btn_days.setObjectName(u"btn_days")
        self.btn_days.setGeometry(QRect(10, 10, 111, 111))
        self.btn_days.setStyleSheet(u"QPushButton {\n"
"	background-color: #FF0033;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #CC3336;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #FF3333;\n"
"}")
        self.btn_calc = QPushButton(self.centralwidget)
        self.btn_calc.setObjectName(u"btn_calc")
        self.btn_calc.setGeometry(QRect(120, 10, 111, 111))
        self.btn_calc.setStyleSheet(u"QPushButton {\n"
"	background-color: #0099FF;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #00CCFF;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #3366CC;\n"
"}")
        self.btn_form = QPushButton(self.centralwidget)
        self.btn_form.setObjectName(u"btn_form")
        self.btn_form.setGeometry(QRect(230, 10, 111, 111))
        self.btn_form.setStyleSheet(u"QPushButton {\n"
"	background-color: #FF9900;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #FF9933;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #FF6600;\n"
"}")
        self.btn_music = QPushButton(self.centralwidget)
        self.btn_music.setObjectName(u"btn_music")
        self.btn_music.setGeometry(QRect(10, 120, 111, 111))
        self.btn_music.setStyleSheet(u"QPushButton {\n"
"	background-color: #33FFCC;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #00CC99;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #00FF99;\n"
"}")
        self.btn_exit = QPushButton(self.centralwidget)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setGeometry(QRect(230, 120, 111, 111))
        self.btn_exit.setStyleSheet(u"QPushButton {\n"
"	background-color: #FF0033;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #CC3336;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #FF3333;\n"
"}")
        self.btn_money = QPushButton(self.centralwidget)
        self.btn_money.setObjectName(u"btn_money")
        self.btn_money.setGeometry(QRect(120, 120, 111, 111))
        self.btn_money.setStyleSheet(u"QPushButton {\n"
"	background-color:#00FF00;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #009900;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #99FF66;\n"
"}")
        self.btn_hello = QPushButton(self.centralwidget)
        self.btn_hello.setObjectName(u"btn_hello")
        self.btn_hello.setGeometry(QRect(10, 230, 111, 111))
        self.btn_hello.setStyleSheet(u"QPushButton {\n"
"	background-color: #FF9900;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #FF9933;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #FF6600;\n"
"}")
        self.btn_yumor = QPushButton(self.centralwidget)
        self.btn_yumor.setObjectName(u"btn_yumor")
        self.btn_yumor.setGeometry(QRect(230, 230, 111, 111))
        self.btn_yumor.setStyleSheet(u"QPushButton {\n"
"	background-color: #0099FF;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #00CCFF;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #3366CC;\n"
"}")
        self.output = QTextEdit(self.centralwidget)
        self.output.setObjectName(u"output")
        self.output.setGeometry(QRect(10, 350, 330, 241))
        self.output.setStyleSheet(u"QTextEdit {\n"
"	color: white;\n"
"	background-color: #131313;\n"
"}")
        self.output.setReadOnly(True)
        self.btn_clear = QPushButton(self.centralwidget)
        self.btn_clear.setObjectName(u"btn_clear")
        self.btn_clear.setGeometry(QRect(120, 230, 111, 111))
        self.btn_clear.setStyleSheet(u"QPushButton {\n"
"	background-color:#CCFFCC;\n"
"	border: none;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #FFFFCC;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #FFCC99;\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Botest", None))
        self.btn_days.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043b\u0435\u043d\u0434\u0430\u0440\u044c", None))
        self.btn_calc.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043b\u044c\u043a\u0443\u043b\u044f\u0442\u043e\u0440", None))
        self.btn_form.setText(QCoreApplication.translate("MainWindow", u"\u0424\u043e\u0440\u043c\u0430\u0442\u0435\u0440", None))
        self.btn_music.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0443\u0437\u044b\u043a\u0430", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.btn_money.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0443\u0440\u0441 \u0432\u0430\u043b\u044e\u0442", None))
        self.btn_hello.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u0432\u0435\u0442", None))
        self.btn_yumor.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043d\u0435\u043a\u0442\u043e\u0434", None))
        self.btn_clear.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
    # retranslateUi

