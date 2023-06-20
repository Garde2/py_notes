import function as f
import ui


def run():
    input_from_user = ""
    while input_from_user != "quit":
        ui.menu()
        input_from_user = input().strip()
        if input_from_user == "all":
            f.show("all")
        if input_from_user == "add":
            f.add()
        if input_from_user == "delete":
            f.show("all")
            f.id_edit_del_show("delete")
        if input_from_user == "edit":
            f.show("all")
            f.id_edit_del_show("edit")
        if input_from_user == "date":
            f.show("date")
        if input_from_user == "id":
            f.show("id")
            f.id_edit_del_show("show")
        if input_from_user == "quit":
            ui.goodbuy()
            break