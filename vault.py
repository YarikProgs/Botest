from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow
from design4 import Ui_MainWindow
import urllib.request
from xml.dom import minidom
import sys
from PySide6.QtGui import QPixmap

url = "http://www.cbr.ru/scripts/XML_daily.asp"

webFile = urllib.request.urlopen(url)
data = webFile.read()

UrlSplit = url.split("/")[-1]
ExtSplit = UrlSplit.split(".")[1]
FileName = UrlSplit.replace(ExtSplit, "xml")
webFile.close()

doc = minidom.parse(FileName)
currency = doc.getElementsByTagName("Valute")


class Vault(QMainWindow):

    def __init__(self):
        super(Vault, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.vault1.activated.connect(self.change_pic1)
        self.ui.vault2.activated.connect(self.change_pic2)
        self.ui.btn_generate.clicked.connect(self.change)

        for rate in currency:
            charcode = rate.getElementsByTagName("CharCode")[0]
            value = rate.getElementsByTagName("Value")[0]

            if charcode.firstChild.data == 'USD': self.usd_rub = value.firstChild.data
            if charcode.firstChild.data == 'EUR': self.eur_rub = value.firstChild.data

        self.usd_rub = float(self.usd_rub.replace(',', '.'))
        self.eur_rub = float(self.eur_rub.replace(',', '.'))
        self.rub_rub = 1

        self.usd_eur = 1 / self.usd_rub * self.eur_rub
        self.rub_eur = 1 / self.eur_rub
        self.eur_eur = 1

        self.rub_usd = 1 / self.usd_rub
        self.eur_usd = 1 / self.usd_eur
        self.usd_usd = 1

    def change(self, text):
        self.ui.out1.setText(self.ui.out1.toPlainText().replace(',', '.'))
        if self.ui.vault1.currentIndex() == 0:
            if self.ui.vault2.currentIndex() == 0: self.ui.out2.setText(str(self.nums_count(self.rub_rub*float(
                self.ui.out1.toPlainText()), 4)))
            if self.ui.vault2.currentIndex() == 1: self.ui.out2.setText(str(self.nums_count(self.rub_usd*float(
                self.ui.out1.toPlainText()), 4)))
            if self.ui.vault2.currentIndex() == 2: self.ui.out2.setText(str(self.nums_count(self.rub_eur*float(
                self.ui.out1.toPlainText()), 4)))
        if self.ui.vault1.currentIndex() == 1:
            if self.ui.vault2.currentIndex() == 0: self.ui.out2.setText(str(self.nums_count(self.usd_rub*float(
                self.ui.out1.toPlainText()), 4)))
            if self.ui.vault2.currentIndex() == 1: self.ui.out2.setText(str(self.nums_count(self.usd_usd*float(
                self.ui.out1.toPlainText()), 4)))
            if self.ui.vault2.currentIndex() == 2: self.ui.out2.setText(str(self.nums_count(self.usd_eur*float(
                self.ui.out1.toPlainText()), 4)))
        if self.ui.vault1.currentIndex() == 2:
            if self.ui.vault2.currentIndex() == 0: self.ui.out2.setText(str(self.nums_count(self.eur_rub*float(
                self.ui.out1.toPlainText()), 4)))
            if self.ui.vault2.currentIndex() == 1: self.ui.out2.setText(str(self.nums_count(self.eur_usd*float(
                self.ui.out1.toPlainText()), 4)))
            if self.ui.vault2.currentIndex() == 2: self.ui.out2.setText(str(self.nums_count(self.eur_eur*float(
                self.ui.out1.toPlainText()), 4)))

    def change_pic1(self, text):
        if text == 0: self.ui.pic1.setPixmap(QPixmap('icons/rub.png'))
        if text == 1: self.ui.pic1.setPixmap(QPixmap('icons/dollar.png'))
        if text == 2: self.ui.pic1.setPixmap(QPixmap('icons/euro.png'))

    def change_pic2(self, text):
        if text == 0: self.ui.pic2.setPixmap(QPixmap('icons/rub.png'))
        if text == 1: self.ui.pic2.setPixmap(QPixmap('icons/dollar.png'))
        if text == 2: self.ui.pic2.setPixmap(QPixmap('icons/euro.png'))

    def nums_count(self, num: float, digits=0):
        return float(f"{num:.{digits}f}")


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    w = Vault()
    w.show()
    sys.exit(app.exec())
