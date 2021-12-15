from PySide6 import QtWidgets
from design3 import Ui_MainWindow
from os import path
import moviepy.editor
import moviepy


class Converter(QtWidgets.QMainWindow):
    def __init__(self):
        super(Converter, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_convert.clicked.connect(self.convert)

    def convert(self):
        if path.isfile(self.ui.way_to_file.text()):
            video_path = self.ui.way_to_file.text()

            video = moviepy.editor.VideoFileClip(video_path)
            audio = video.audio

            audio_name = self.ui.way_to_newfile.text()
            audio_format = self.ui.file_format.text()
            audio.write_audiofile(f"{audio_name}.{audio_format}")
        else:
            self.ui.way_to_file.setText('')


if __name__ == '__main__':
    print('Вам надо запустить main.py! Это рут файл.')
    input()
