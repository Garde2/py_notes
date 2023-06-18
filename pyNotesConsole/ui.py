import Note


def create_note(number):
    title = check_len_text_input(
        input("Название заметки: "), number)
    body = check_len_text_input(
        input("Содержание: "), number)
    return Note.Note(title=title, body=body)


def menu():
    print("\nNotes. Выберите действие:\n\n1 - вывод всех заметок из файла\n2 - добавление заметки\n3 - удаление заметки\n4 - редактирование заметки\n5 - все заметки по дате\n6 - заметка id\n7 - выход\n\n: ")


def check_len_text_input(text, n):
    while len(text) <= n:
        print(f'Текст должен быть больше {n} символов\n')
        text = input('Введите тескт: ')
    else:
        return text


def goodbuy():
    print("Приходите к нам еще =). До новых встреч!")