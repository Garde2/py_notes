# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import datetime

print(" Заметки - консольное приложение")

fileName = 'pyNotesConsole.json'
fileID = 'idNotes.txt'

date_now = datetime.datetime.now()
print(date_now)

def whatToDo():
    exit = True
    while exit == True:
        print("Введите команду: add - добавить заметку, " +
                "search - поиск заметки," +
                "edit - редактировать заметку," +
                "showall - показать все заметки," +
                "exit - выйти из приложения.")
        cmd = input("Выберите команду из списка: ")

        if cmd == "add":
            print(newNote(newNoteName(), newNoteText()))

        if cmd == "search":
            search = input("Ищем заметку: ").lower()
            printNotes(searchNote(search))

        if cmd == "edit":
            edit = input("Найдем заметку: ").lower()
            printNotes(searchNote(edit))
            smth = searchNote(edit)
            print(example(smth))

        if cmd == "exit":
            print("Приложение завершило свою работу")
            break

        else:
            print("Ошибка!Что-то введено не верно!")

def newNoteName():
    noteName = str(input("Введите название заметки: "))
    return noteName

def newNoteText():
    noteText = str(input("Введите описание события: "))
    return noteText



