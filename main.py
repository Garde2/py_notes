#from tracker import *

#import sys
#app = QtWidgets.QApplication(sys.argv)
#MainWindow = QtWidgets.QMainWindow()
#ui = Ui_MainWindow()
#ui.setupUi(MainWindow)
#MainWindow.show()

#ui.label.setText("Заметки")

#sys.exit(app.exec_())

import pickle
from PyQt5 import uic
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QApplication

Form, Window = uic.loadUiType("tracker.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

def save_to_file():
    global start_date, calc_date, description
    data_to_save = {"start": start_date, "end": calc_date, "desc": description}
    file1 = open("dateTime.txt", "wb")
    pickle.dump(data_to_save, file1)
    file1.close()

def read_from_file():
    global start_date, calc_date, description
    try:
        file1 = open("dateTime.txt", "rb")
        data_to_load = pickle.load(file1)
        file1.close()
        start_date = data_to_load["start"]
        calc_date = data_to_load["end"]
        description = data_to_load["desc"]
        print(start_date.toString('dd-MM-yyyy'), calc_date.toString('dd-MM-yyyy'), description)
        form.calendarWidget.setSelectedDate(calc_date)
        form.dateEdit.setDate(calc_date)
        form.plainTextEdit.setPlainTexr(description)

    except:
        print("Не могу прочесть файл, может, его нет? запишите что-нибудь!")



def on_click():
    global calc_date, description
    calc_date = form.calendarWidget.selectedDate()
    description = form.plainTextEdit.toPlainText()

    #print(form.plainTextEdit.toPlainText())
    #print(form.dateEdit.dateTime().toString('dd-MM-yyyy'))
    #print("В процессе...!")

    save_to_file()
    #print(form.calendarWidget.selectedDate().toString('dd-MM-yyyy'))
    #date = QDate(2023, 6, 17)
    #form.calendarWidget.setSelectedDate(date)

def on_click_calendar():
    global start_date, calc_date
    #print(form.calendarWidget.selectedDate().toString('dd-MM-yyyy'))
    form.dateEdit.setDate(form.calendarWidget.selectedDate())
    calc_date = form.calendarWidget.selectedDate()
    delta_days = start_date.daysTo(calc_date)
    print(delta_days)
    form.label_4.setText("До наступления события осталось: %s дней" % delta_days)

def on_dateedit_change():
    global start_date, calc_date
    #print(form.dateEdit.dateTime().toString('dd-MM-yyyy'))
    form.calendarWidget.setSelectedDate(form.dateEdit.date())
    calc_date = form.dateEdit.date()
    delta_days = start_date.daysTo(calc_date)
    print(delta_days)
    form.label_4.setText("До наступления события осталось дней: %s " % delta_days)



form.pushButton.clicked.connect(on_click)
form.calendarWidget.clicked.connect(on_click_calendar)
form.dateEdit.dateChanged.connect(on_dateedit_change)

start_date = form.calendarWidget.selectedDate()
calc_date = form.calendarWidget.selectedDate()
description = form.plainTextEdit.toPlainText()
read_from_file()


form.label.setText("Заметки: %s " % start_date.toString('dd-MM-yyyy'))


on_click_calendar()



app.exec_()
