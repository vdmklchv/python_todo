import todo_manager as tdm


if __name__ == '__main__':
    manager = tdm.TodoManager()
    manager.load_todos('todos.txt')
    options = {"1": manager.list_todos, "2": manager.add_todo}
    while True:
        action = input('1 - list, 2 - add, q - quit: ')
        if action == 'q':
            manager.save_todos('todos.txt')
            print('Saved')
            break
        if action == '2':
            name = input('name: ')
            date = input('date: ')
            args = (name, date)
        else:
            args = ()

        try:
            options[action](*args)
        except KeyError:
            print('No such command')
