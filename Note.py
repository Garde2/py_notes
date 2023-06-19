from datetime import datetime
import uuid
import uic
import datetime


Form = uic.loadUiType("tracker.ui")
form = Form()

class Note:

    def __init__(self, id = str(uuid.uuid1())[0:3], title = form.plainTextEdit_2.toPlainText(), body = form.plainTextEdit.toPlainText(), date=str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))):

        self.id = id
        self.title = title
        self.body = body
        self.date = date

    def get_id(self):
        return self.id

    def get_title(self):
        return self.title

    def get_body(self):
        return self.body

    def get_date(self):
        return self.date

    def set_id(self):
        self.id = str(uuid.uuid1())[0:3]

    def set_title(self, title):
        self.title = title

    def set_body(self, body):
        self.body = body

    def set_date(self):
        self.date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

    def to_string(self):
        return self.id + '; ' + self.title + '; ' + self.body + '; ' + self.date

    def map_note(self):
        return '\nID: ' + self.id + '\n' + "Название: " + self.title + '\n' + "Содержание: " + self.body + '\n' + "Дата: " + self.date