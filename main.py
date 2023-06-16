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
        self.knopka.clicked.connect(self.knopka_gotovo)

    def knopka_gotovo(self):
        data_txt = str(self.data.text())
        time_txt = str(self.time.text())
        sobati_txt = str(self.sobati.text())

        print("Дата: " + data_txt)
        print("Время: " + time_txt)
        print("Событие: " + sobati_txt)

        File_A = open('dataTime.txt', 'a+')
        DateTime_txt = (data_txt + " ' " + time_txt + " ' " + sobati_txt)
        Date_txt = (data_txt + " ' time ' " + sobati_txt)
        File_A.write(DateTime_txt + '\n')
        File_A.write(Date_txt + '\n')
        File_A.close()

    def proverka(self):

        date_pk = datetime.date.today()
        time_pk = datetime.datetime.now().time()
        date_pk = str(date_pk)
        time_pk = str(time_pk)
        one = date_pk[:4:]
        two = date_pk [8::]
        date_pk = date_pk[4:8:]
        date_pk = (two + date_pk + one)
        date_pk = date_pk.replace ('-', '.')

        time_pk = time_pk[:5:]

        dateTime_pk = (date_pk + " ' " + time_pk)

        print(dateTime_pk + " = нынешнее время и дата")

        date_pk = (date_pk + " ' time")

        File_R = open("dateTime.txt", "r")
        lines = File_R.readlines()
        File_R.close()
        lines = [line.rstrip() for line in lines]

        for line in lines:
            if date_pk in line:

                index_date = lines.index(line)
                del lines[index_date]

                text = line[19::]

                self.error = QtWidgets.QMessageBox(self)
                self.error.setWindowTitle("Напоминаем")
                self.error.settext(text)
                self.error.setIcon(QtWidgets.QMessageBox.Warning)
                self.error.setStandartButton(self.error.Ok|self.error.Cancel)
                self.error.exec_()

        
            if dateTime_pk in lines:

                index_dateTime = lines.index(line)
                del lines[index_dateTime]

                text = line[20::]

                self.error = QtWidgets.QMessageBox(self)
                self.error.setWindowTitle ("Напоминаем")
                self.error.setIcon(QtWidgets.QMessageBox.Warning)
                self.error.setStandardButtons(self.error.Ok|self.error.Cancel)
                self.error.exec_()

        File_R = open("dateTime.txt", "w")
        for i in lines:
            File_R.write(i + '\n')
        File_R.close() 
        
               

