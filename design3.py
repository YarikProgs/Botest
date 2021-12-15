# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design3.ui'
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
    QSizePolicy, QWidget)
import files3_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 236)
        MainWindow.setMinimumSize(QSize(500, 236))
        MainWindow.setMaximumSize(QSize(500, 236))
        icon = QIcon()
        icon.addFile(u":/icons/icons/upload.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget {\n"
"	color: white;\n"
"	background-color: #121212;\n"
"	font-family: Rubik;\n"
"	font-size: 14pt;\n"
"	font-weight: 600;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.way_to_file = QLineEdit(self.centralwidget)
        self.way_to_file.setObjectName(u"way_to_file")
        self.way_to_file.setGeometry(QRect(10, 10, 481, 51))
        self.file_format = QLineEdit(self.centralwidget)
        self.file_format.setObjectName(u"file_format")
        self.file_format.setGeometry(QRect(10, 70, 241, 51))
        self.way_to_newfile = QLineEdit(self.centralwidget)
        self.way_to_newfile.setObjectName(u"way_to_newfile")
        self.way_to_newfile.setGeometry(QRect(250, 70, 241, 51))
        self.btn_convert = QPushButton(self.centralwidget)
        self.btn_convert.setObjectName(u"btn_convert")
        self.btn_convert.setGeometry(QRect(144, 132, 211, 71))
        self.btn_convert.setStyleSheet(u"QPushButton {\n"
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
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Converter - botest", None))
        self.way_to_file.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c \u043a \u0444\u0430\u0439\u043b\u044e + \u0441\u0430\u043c \u0444\u0430\u0439\u043b", None))
        self.file_format.setText(QCoreApplication.translate("MainWindow", u"\u0424\u043e\u0440\u043c\u0430\u0442 \u043d\u043e\u0432\u043e\u0433\u043e \u0444\u0430\u0439\u043b\u0430", None))
        self.way_to_newfile.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043d\u043e\u0432\u043e\u0433\u043e \u0444\u0430\u0439\u043b\u0430", None))
        self.btn_convert.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0432\u0435\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c!", None))
    # retranslateUi

