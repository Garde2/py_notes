#from tracker import *

#import sys
#app = QtWidgets.QApplication(sys.argv)
#MainWindow = QtWidgets.QMainWindow()
#ui = Ui_MainWindow()
#ui.setupUi(MainWindow)
#MainWindow.show()
#ui.label.setText("Заметки")
#sys.exit(app.exec_())

import function as f
import tracker

import pickle
from PyQt5 import uic
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QApplication
from datetime import datetime
import uuid

Form, Window = uic.loadUiType("tracker.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

title = form.plainTextEdit_2.toPlainText("Введите содержание заметки")
id = str(uuid.uuid1())[0:3]
body = form.plainTextEdit.toPlainText("Введите содержание заметки")

def save_to_file():
    global start_date, calc_date, description

    #start_date = QDate(2023, 6, 1)
    data_to_save = {"start": start_date, "end": calc_date, "desc": description}
    file1 = open("pyNotes.json", "wb")
    pickle.dump(data_to_save, file1)
    file1.close()

def read_from_file():
    global start_date, calc_date, description, now_date
    try:
        file1 = open("pyNotes.json", "rb")
        data_to_load = pickle.load(file1)
        file1.close()
        start_date = data_to_load["start"]
        calc_date = data_to_load["end"]
        description = data_to_load["desc"]
        print(start_date.toString('dd-MM-yyyy'), calc_date.toString('dd-MM-yyyy'), description)
        form.calendarWidget.setSelectedDate(calc_date)
        form.dateEdit.setDate(calc_date)
        form.plainTextEdit.setPlainText(description)
        delta_days_left = start_date.daysTo(now_date) #прошло
        delta_days_right = now_date.daysTo(calc_date) #осталось
        days_total = start_date.daysTo(calc_date)
        print(" Отслеживаем дни: ", delta_days_left, delta_days_right, days_total)
        procent = int(delta_days_left * 100 / days_total)
        print(procent)
        form.progressBar.setProperty("value", procent)

    except:
        print("Не могу прочесть файл, может, его нет? запишите что-нибудь!")


def on_click(number):
    global calc_date, description, start_date
    start_date = now_date

    calc_date = form.calendarWidget.selectedDate()
    #description = form.plainTextEdit.toPlainText()

    if tracker.self.pushButton_6.clicked.connect(on_click):
        f.show("all")
    if tracker.self.pushButton.clicked.connect(on_click):
        f.add()
    if tracker.self.pushButton_5.clicked.connect(on_click):
        f.show("all")
        f.id_edit_del_show("del")
    if tracker.self.pushButton_4.clicked.connect(on_click):
        f.show("all")
        f.id_edit_del_show('edit')
    if tracker.self.pushButton_7.clicked.connect(on_click):
        f.show('date')
    if tracker.self.pushButton_8.clicked.connect(on_click):
        f.show("id")
        f.id_edit_del_show("show")
    if tracker.self.pushButton_9.clicked.connect(on_click):
        tracker.goodbuy()

    #print(form.plainTextEdit.toPlainText())
    #print(form.dateEdit.dateTime().toString('dd-MM-yyyy'))
    #print("В процессе...!")
    # print(form.calendarWidget.selectedDate().toString('dd-MM-yyyy'))
    # date = QDate(2023, 6, 17)
    # form.calendarWidget.setSelectedDate(date)

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
now_date = form.calendarWidget.selectedDate()
calc_date = form.calendarWidget.selectedDate()
description = form.plainTextEdit.toPlainText()
read_from_file()

form.label.setText("Заметки: %s " % start_date.toString('dd-MM-yyyy'))

on_click_calendar()

app.exec_()