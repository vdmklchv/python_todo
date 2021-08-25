import uuid


class Todo:
    def __init__(self, name, due_date):
        self.name = name
        self.uuid = uuid.uuid1()
        self.due_date = due_date
        self.done = False

    def toggle_done(self):
        self.done = not self.done

    def change_due_date(self, new_date):
        self.due_date = new_date

    def rename(self, new_name):
        self.name = new_name
