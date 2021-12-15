# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design5.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSlider, QWidget)
import files5_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 400)
        icon = QIcon()
        icon.addFile(u":/icons/icons/headphones.png", QSize(), QIcon.Normal, QIcon.Off)
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
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(49, 280, 421, 101))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_left_10 = QPushButton(self.horizontalLayoutWidget)
        self.btn_left_10.setObjectName(u"btn_left_10")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_left_10.sizePolicy().hasHeightForWidth())
        self.btn_left_10.setSizePolicy(sizePolicy)
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_left_10.setIcon(icon1)
        self.btn_left_10.setIconSize(QSize(60, 60))
        self.btn_left_10.setAutoRepeat(False)

        self.horizontalLayout.addWidget(self.btn_left_10)

        self.btn_pause = QPushButton(self.horizontalLayoutWidget)
        self.btn_pause.setObjectName(u"btn_pause")
        sizePolicy.setHeightForWidth(self.btn_pause.sizePolicy().hasHeightForWidth())
        self.btn_pause.setSizePolicy(sizePolicy)
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/pause.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_pause.setIcon(icon2)
        self.btn_pause.setIconSize(QSize(60, 60))

        self.horizontalLayout.addWidget(self.btn_pause)

        self.btn_play = QPushButton(self.horizontalLayoutWidget)
        self.btn_play.setObjectName(u"btn_play")
        sizePolicy.setHeightForWidth(self.btn_play.sizePolicy().hasHeightForWidth())
        self.btn_play.setSizePolicy(sizePolicy)
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_play.setIcon(icon3)
        self.btn_play.setIconSize(QSize(60, 60))

        self.horizontalLayout.addWidget(self.btn_play)

        self.btn_right_10 = QPushButton(self.horizontalLayoutWidget)
        self.btn_right_10.setObjectName(u"btn_right_10")
        sizePolicy.setHeightForWidth(self.btn_right_10.sizePolicy().hasHeightForWidth())
        self.btn_right_10.setSizePolicy(sizePolicy)
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/_right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_right_10.setIcon(icon4)
        self.btn_right_10.setIconSize(QSize(60, 60))

        self.horizontalLayout.addWidget(self.btn_right_10)

        self.btn_open = QPushButton(self.centralwidget)
        self.btn_open.setObjectName(u"btn_open")
        self.btn_open.setGeometry(QRect(10, 10, 101, 31))
        self.volume_slider = QSlider(self.centralwidget)
        self.volume_slider.setObjectName(u"volume_slider")
        self.volume_slider.setGeometry(QRect(460, 10, 22, 160))
        self.volume_slider.setOrientation(Qt.Vertical)
        self.volume = QLabel(self.centralwidget)
        self.volume.setObjectName(u"volume")
        self.volume.setGeometry(QRect(396, 20, 51, 51))
        self.volume.setPixmap(QPixmap(u":/icons/icons/volume_1.png"))
        self.volume.setScaledContents(True)
        self.volume.setAlignment(Qt.AlignCenter)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 70, 211, 191))
        self.label.setPixmap(QPixmap(u":/icons/icons/papug.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(386, 112, 61, 51))
        self.label_2.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Music - botest", None))
        self.btn_left_10.setText("")
        self.btn_pause.setText("")
        self.btn_play.setText("")
        self.btn_right_10.setText("")
        self.btn_open.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
        self.volume.setText("")
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"0%", None))
    # retranslateUi

