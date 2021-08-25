import datetime
import json
from Todo import Todo


class TodoManager:
    def __init__(self):
        self.todos = []

    def save_todos(self, file):
        with open(file, 'w') as f:
            json.dump(self.todos, f)

    def load_todos(self, file):
        with open(file, 'r') as f:
            try:
                self.todos = json.load(f)
            except json.decoder.JSONDecodeError:
                self.todos = []

    def add_todo(self, name, date):
        try:
            datetime.datetime.strptime(date, '%d-%m-%Y')
        except ValueError:
            print('Date format incorrect. Should be dd-mm-YYYY')
            return

        new_todo = Todo(name, date)

        self.todos.append({
            'uuid': str(new_todo.uuid),
            'name': new_todo.name,
            'due_date': new_todo.due_date,
            'is_done': new_todo.done
        })

    def list_todos(self):
        if len(self.todos) > 0:
            print('Name'.ljust(20), 'UUID'.ljust(40), 'Due Date')
            print('=' * 80)
            for todo in self.todos:
                print(todo['name'].ljust(20), todo['uuid'].ljust(40), todo['due_date'])
            print('\n')
        else:
            print('No todos to display')