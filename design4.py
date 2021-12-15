# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design4.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QTextEdit, QWidget)
import files4_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(350, 500)
        MainWindow.setMinimumSize(QSize(350, 500))
        MainWindow.setMaximumSize(QSize(350, 500))
        icon = QIcon()
        icon.addFile(u":/icons/icons/dollar_2.png", QSize(), QIcon.Normal, QIcon.Off)
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
        self.vault1 = QComboBox(self.centralwidget)
        self.vault1.addItem("")
        self.vault1.addItem("")
        self.vault1.addItem("")
        self.vault1.setObjectName(u"vault1")
        self.vault1.setGeometry(QRect(20, 110, 111, 40))
        self.vault2 = QComboBox(self.centralwidget)
        self.vault2.addItem("")
        self.vault2.addItem("")
        self.vault2.addItem("")
        self.vault2.setObjectName(u"vault2")
        self.vault2.setGeometry(QRect(218, 110, 111, 40))
        self.pic1 = QLabel(self.centralwidget)
        self.pic1.setObjectName(u"pic1")
        self.pic1.setGeometry(QRect(20, 15, 80, 80))
        self.pic1.setPixmap(QPixmap(u":/icons/icons/rub.png"))
        self.pic1.setScaledContents(False)
        self.pic1.setAlignment(Qt.AlignCenter)
        self.pic1.setWordWrap(False)
        self.pic2 = QLabel(self.centralwidget)
        self.pic2.setObjectName(u"pic2")
        self.pic2.setGeometry(QRect(240, 15, 80, 80))
        self.pic2.setPixmap(QPixmap(u":/icons/icons/rub.png"))
        self.btn_generate = QPushButton(self.centralwidget)
        self.btn_generate.setObjectName(u"btn_generate")
        self.btn_generate.setGeometry(QRect(139, 110, 71, 41))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_generate.setIcon(icon1)
        self.btn_generate.setIconSize(QSize(80, 80))
        self.out1 = QTextEdit(self.centralwidget)
        self.out1.setObjectName(u"out1")
        self.out1.setGeometry(QRect(20, 160, 140, 80))
        self.out1.setReadOnly(False)
        self.out2 = QTextEdit(self.centralwidget)
        self.out2.setObjectName(u"out2")
        self.out2.setGeometry(QRect(190, 160, 140, 80))
        self.out2.setReadOnly(True)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 420, 311, 61))
        font = QFont()
        font.setFamilies([u"Rubik"])
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"QLabel {\n"
"	font-size: 12pt;\n"
"	color: lightgray;\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Vault - botest", None))
        self.vault1.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0420\u0443\u0431\u043b\u044c", None))
        self.vault1.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043b\u043b\u0430\u0440", None))
        self.vault1.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0415\u0432\u0440\u043e", None))

        self.vault2.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0420\u0443\u0431\u043b\u044c", None))
        self.vault2.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043b\u043b\u0430\u0440", None))
        self.vault2.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0415\u0432\u0440\u043e", None))

        self.pic1.setText("")
        self.pic2.setText("")
        self.btn_generate.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043b\u044f \u043f\u043e\u0434\u0441\u0447\u0451\u0442\u0430 \u0432\u0430\u043b\u044e\u0442 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043b\u0441\u044f\n"
" \u0431\u0430\u043d\u043a https://cbr.ru/ \u0434\u043b\u044f \u043f\u0440\u043e\u0435\u0442\u0430 \u0438 \n"
"\u0431\u043e\u0442\u0430 botest (c) \u043e\u0442 Yarik_Prod.", None))
    # retranslateUi

