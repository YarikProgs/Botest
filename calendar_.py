from PySide6.QtWidgets import QApplication, QDialog, QCalendarWidget, QLabel
from design6 import Ui_Dialog


class Calendar(QDialog):
    def __init__(self):
        super(Calendar, self).__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.calendar = self.findChild(QCalendarWidget, "calendarWidget")
        self.label = self.findChild(QLabel, "label")


if __name__ == "__main__":
    print('Вам надо запустить main.py! Это рут файл.')
    input()