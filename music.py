import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtGui import QPixmap
from design5 import Ui_MainWindow
import pygame


pygame.mixer.init()


class Music(QMainWindow):
    def __init__(self):
        super(Music, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_open.clicked.connect(self.open_file)
        self.ui.btn_play.clicked.connect(self.play)
        self.ui.btn_right_10.clicked.connect(self.right)
        self.ui.btn_left_10.clicked.connect(self.left)
        self.ui.volume_slider.valueChanged.connect(self.change)
        self.ui.btn_pause.clicked.connect(self.pause)

        self.c = 0
        self.oops = pygame.mixer.Sound('sounds/oops.mp3')
        self.files = []

    def open_file(self):
        try:
            self.files.append(pygame.mixer.Sound(QFileDialog.getOpenFileName(self, 'Открыть', '/home')[0]))
        except FileNotFoundError or FileExistsError as error:
            print(f'Man, INPUT THE CORRECT FILE PLEASE!!!!!!11 {error}')

    def left(self):
        try:
            self.files[::-1][1].play()
        except IndexError:
            pass

    def right(self):
        self.oops.play()

    def play(self):
        try:
            self.files[::-1][0].play()
        except pygame.error as error:
            print(f'Yo, import the MUSIC below! {error}')
        except AttributeError as error:
            print(f'Yo, import the music below! {error}')
        except IndexError as error:
            print(f"Yo, IMPORT the music below! {error}")
        except TypeError as error:
            print(f'Rerun program, theres many errors... {error}')

    def change(self, value):
        self.ui.label_2.setText(str(value+1) + '%')
        if 0 < value < 10:
            self.ui.volume.setPixmap(QPixmap('icons/volume_1.png'))
        elif 10 < value < 60:
            self.ui.volume.setPixmap(QPixmap('icons/volume_2.png'))
        elif 60 < value <= 100:
            self.ui.volume.setPixmap(QPixmap('icons/volume_3.png'))

        if len(self.files) != 0:
            for file in self.files:
                file.set_volume(value/100)

    def pause(self):
        if self.c == 0:
            pygame.mixer.pause()
            self.c += 1
        elif self.c == 1:
            pygame.mixer.unpause()
            self.c = 0
        else:
            print('pausing error')


if __name__ == '__main__':
    app = QApplication()
    w = Music()
    w.show()
    sys.exit(app.exec())
