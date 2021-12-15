from design2 import Ui_MainWindow
from PySide6 import QtWidgets
from PySide6.QtWidgets import QMessageBox
import sys
import random
import calculator
import formater
import vault
import pygame
import music
import calendar_


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        pygame.init()
        pygame.mixer.init()

        self.calc = calculator.Calculator()
        self.conv = formater.Converter()
        self.vaul = vault.Vault()
        self.musi = music.Music()
        self.cale = calendar_.Calendar()

        self.hello = ['Привет', 'Привет', 'Привет', 'Прив', 'Хай', 'Privet', 'Privet', 'Privet', 'Ты каматуза?']
        self.audio_hello = [pygame.mixer.Sound("sounds/hello.mp3"), pygame.mixer.Sound("sounds/hello.mp3"),
                            pygame.mixer.Sound("sounds/hello.mp3"), pygame.mixer.Sound("sounds/hell.mp3"),
                            pygame.mixer.Sound("sounds/hi.mp3"), pygame.mixer.Sound("sounds/hello.mp3"),
                            pygame.mixer.Sound("sounds/hello.mp3"), pygame.mixer.Sound("sounds/hello.mp3"),
                            pygame.mixer.Sound("sounds/debil.mp3")]

        self.yumor = ['Колобок повесился', 'Русалка села на шпагат', 'Воздух задохнулся', 'Вода утонула']
        self.audio_yumor = [pygame.mixer.Sound("sounds/kolobok.mp3"), pygame.mixer.Sound("sounds/rusalka.mp3"),
                            pygame.mixer.Sound("sounds/air.mp3"), pygame.mixer.Sound("sounds/water.mp3")]

        self.ui.btn_calc.clicked.connect(lambda: self.start('CALC'))
        self.ui.btn_exit.clicked.connect(lambda: self.start('EXIT'))
        self.ui.btn_form.clicked.connect(lambda: self.start('CONVERTER'))
        self.ui.btn_hello.clicked.connect(lambda: self.start('HELLO'))
        self.ui.btn_yumor.clicked.connect(lambda: self.start('YUMOR'))
        self.ui.btn_clear.clicked.connect(lambda: self.start('CLEAR'))
        self.ui.btn_money.clicked.connect(lambda: self.start('MONEY'))
        self.ui.btn_music.clicked.connect(lambda: self.start('MUSIC'))
        self.ui.btn_days.clicked.connect(lambda: self.start('CALENDAR'))

    def set_text(self, text):
        self.ui.output.setText(
            self.ui.output.toPlainText() + f"\n [botest]:{text}")

    def start(self, app_) -> None:
        if app_ == "CALC":
            self.calc.show()

        if app_ == "EXIT":
            sys.exit('Goodbye.')

        if app_ == "CONVERTER":
            self.conv.show()

        if app_ == "HELLO":
            random_ = random.randint(0, len(self.hello)-1)
            self.set_text(self.hello[random_])
            self.audio_hello[random_].play()

        if app_ == "YUMOR":
            random_ = random.randint(0, len(self.yumor)-1)
            self.set_text(self.yumor[random_])
            self.audio_yumor[random_].play()

        if app_ == "CLEAR":
            self.ui.output.setText("")

        if app_ == "MONEY":
            self.vaul.show()

        if app_ == "MUSIC":
            self.musi.show()

        if app_ == "CALENDAR":
            self.cale.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(
            self, 'Вопрос', 'Вы точно хотите выйти?',
            QMessageBox.Yes, QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            self.conv.close()
            self.calc.close()
            self.musi.close()
            self.vaul.close()
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())
