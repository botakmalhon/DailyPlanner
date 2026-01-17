
# ====== КОНТРОЛЛЕР ======
class TaskListController:
    
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.model.load_from_file(filename="../data/tasks.json")
        self.view.show_message("Задачи загружены из файла.")
        

    def add_task(self):
        name = self.view.ask_task_name("Введите название задачи: ")
        aura = self.view.ask_task_aura()
        self.model.add_task(name, aura)
        self.view.show_message("Задача добавлена!")

    def show_tasks(self):
        self.view.show_tasks(self.model.get_all_tasks())

    def DoTask(self):
        number = self.view.ask_task_num("Введите nomer задачи: ")
        if self.model.DoTask(number):
            self.view.show_message("Задача vipolnena!")
        else:
            self.view.show_message("Задача не найдена!")

    def delete_task(self):
        name = self.view.ask_task_name("Введите название задачи для удаления: ")
        if self.model.delete_task(name):
            self.view.show_message("Задача удалена!")
        else:
            self.view.show_message("Задача не найдена!")

    def sort_tasks(self):
        choice = self.view.ask_sort_order()
        if choice == "1":
            self.model.sort_by_aura(False)
            self.view.show_message("Сортировка по возрастанию выполнена.")
        elif choice == "2":
            self.model.sort_by_aura(True)
            self.view.show_message("Сортировка по убыванию выполнена.")
        else:
            self.view.show_message("Неверный выбор.")

    def run(self):
        while True:
            self.view.show_menu()
            choice = input("Выберите действие: ")

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.show_tasks()
            elif choice == "3":
                self.DoTask()
            elif choice == "4":
                self.delete_task()    
            elif choice == "5":
                self.sort_tasks()
            elif choice == "6":
                self.model.save_to_file(filename="../data/tasks.json")
                self.view.show_message("Задачи сохранены. Выход из программы.")
                break
            else:
                self.view.show_message("Неверная команда!")
    