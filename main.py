from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import Qt, QTimer
import sys 
import datetime

def aplic():
    app = QApplication(sys.argv)
    okno = Window()

    okno.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    aplic()

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init_()

        self.setWindowTitle("Notes")
        self.setGeomertry(400,400,600,300)

        self.text_data = QtWidgets.QLabel(self)
        self.text_data.setText("Выберите дату: ")
        self.text_data.adjustSize()
        self.text_data.move(10,52)

        self.text_time = QtWidgets.QLabel(self)
        self.text_time.setText ("Выбурите время: ")
        self.text_time.adjustSize()
        self.text_time.move(10,103)

        self.data = QtWidgets.QDateEdit(self)
        self.data.move(100,50)
        self.data.adjustSize()

        self.time = QtWidgets.QTimeEdit(self)
        self.time.move(110,100)
        self.time.adjustSize()

        self.sobati = QtWidgets.QLineEdit(self)
        self.sobati.setGeometry(100,150,160,30)
        self.sobati.adjustSize()
        self.sobati.setPlaceHolderText("Введите событие: ")

        self.knopka = QtWidgets.QPushButtons(self)
        self.knopka.move(210,80)
        self.knopka.setText("Готово!")
        self.knopka.adjustSize()

        