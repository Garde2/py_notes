# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import datetime

print(" Заметки - консольное приложение")

fileName = "pyNotesConsole.json"
fileID = "idNotes.txt"

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
            continue

        if cmd == "search":
            search = input("Ищем заметку: ").lower()
            printNote(searchNote(search))
            continue

        if cmd == "edit":
            edit = input("Найдем заметку: ").lower()
            printNote(searchNote(edit))
            srch = searchNote(edit)
            print(ifFound(srch))
            continue

        if cmd == "showall":
            printAllNotes()
            continue

        if cmd == "exit":
            print("Приложение завершило свою работу")
            break

        else:
            print("Ошибка!Что-то введено не верно!")


def newNote(noteName, key):
    with open(fileName, "a") as file:
        id = idNoteCheck() + 1
        file.write("id = " + str(id) + "; " + "Создана: " + str(date_now) + " _ " + noteName.lower() + " _ " + key.lower() + '/n')
        idWriting(id)
        return "Заметка добавлена!"

def newNoteName():
    noteName = str(input("Введите название заметки: "))
    return noteName

def newNoteText():
    noteText = str(input("Введите описание события: "))
    return noteText


def idNoteCheck():
    with open (fileID, "r") as file:
        temp = ''.join(file.readlines())
        id = int(temp)

        return id

def idWriting(id):
    with open(fileID, "w") as file:
        file.write(str(id))

def ifFound(dictionary):
    if dictionary.ger("er") == None:
        changeNote(dictionary)
        return changeNote(dictionary)

def searchNote(search):
    with open(fileName, "r") as file:
        dictionary = { }
        content = file.readlines()
        for i in range(len(content)):
            if search in content[i]:
                number = str(i)
                dictionary[number] = content[i]

        if len(dictionary) < 1:
            dictionary2 = { }
            dictionary2["er"] = "Не найдено!"
            return dictionary2

        else:
            return dictionary


def changeNote(dictionary2):
    exit == True
    while exit == True:
        selection = input("Какую строку редактируем (номер)? Или введите exit: ")

        if selection == "exit" and len(selection) == 2:
            return "Закончили!"

        if selection in dictionary2:

            print("Перезапишите заметку полностью!: ")
            newData = "_" + newNoteName() + "; " + newNoteText()

            with open(fileName, "r") as file:
                oldData = file.read()
                data = dictionary2[selection]
                if len(newData) == 0:
                    new_data = oldData.replace(data, newData + '\n')
                    new_data = new_data.lower()
                else:
                    id = idNoteCheck() + 1
                    new_data = oldData.replace(data, "id = " + str(id) + "; " + "Создано: " +
                                                str(date_now) + "; " + newData + '\n')
                    new_data = new_data.lower()
                    idWriting(id)

            with open(fileName, "w") as file:
                file.writelines(new_data)
                print("Готово!")
            continue


        elif selection not in dictionary2 and selection != "exit":
            print("Введите заново!")
        continue

def printNote(dictionary):
    for key, value in dictionary.items():
        print(f"Строка: {key}  Заметка: {value} ")

def printAllNotes():
    book = open("pyNotesConsole.json", "r")
    print(book.read())
    book.close()

whatToDo()

