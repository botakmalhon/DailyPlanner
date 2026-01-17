
# ====== VIEW ======
class TaskListView:
    def __init__(self):
        pass
        
    def show_tasks(self, tasks):
        if not tasks:
            print("Список задач пуст.")
        else:
            print("\nВаши задачи:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")


    def ask_task_name(self, message):
        return input(message)

    def ask_task_num(self, message):
        return int(input(message))

    def ask_task_aura(self):
        while True:
            try:
                return int(input("Введите ауру задачи: "))
            except ValueError:
                print("Введите число!")

    

    def ask_sort_order(self):
        print("\nКак сортировать по ауре?")
        print("1. По возрастанию")
        print("2. По убыванию")
        return input("Ваш выбор: ")

    def show_message(self, message):
        print(message)

    def show_menu(self):
        print("\n===== МЕНЮ =====")
        print("1. Добавить задачу")
        print("2. Посмотреть задачи")
        print("3. do tasks")
        print("4. Удалить задачу")
        print("5. Сортировать по ауре")
        print("6. ВЫХОД")
