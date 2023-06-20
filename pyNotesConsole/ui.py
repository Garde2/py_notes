import Note


def create_note(number):
    title = check_len_text_input(
        input("Название заметки: "), number)
    body = check_len_text_input(
        input("Содержание: "), number)
    return Note.Note(title=title, body=body)


def menu():
    print("\nNotes.Выберите действие:\n\n")
    print("all - Вывод всех заметок из файла\n add - Добавление заметки\ndelete - Удаление заметки\nedit - Редактирование заметки\ndate - Все заметки по дате\nid - заметка по id\nquit - Выход\n\n: ")


def check_len_text_input(text, n):
    while len(text) <= n:
        print(f'Текст должен быть больше {n} символов\n')
        text = input('Введите тескт: ')
    else:
        return text


def goodbuy():
    print("Приходите к нам еще =). До новых встреч!")