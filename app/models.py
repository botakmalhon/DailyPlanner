import json
import os



# ====== МОДЕЛЬ ======
class Task:
    def __init__(self, name, aura, done=False):
        self.name = name
        self.aura = aura
        self.done = done

    def __str__(self):
        done_status = "✓" if self.done else "✗"
        return f"[{done_status}] {self.name}, Аура: {self.aura}"


class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, aura, done = False):
        self.tasks.append(Task(name, aura, done))

    def delete_task(self, name):
        for task in self.tasks:
            if task.name.lower() == name.lower():
                self.tasks.remove(task)
                return True
        return False

    def DoTask(self, index):
        index = index - 1
        if 0 <= index and index < len(self.tasks):
            self.tasks[index].done = True
            return True
        return False
    def get_all_tasks(self):
        return self.tasks

    def sort_by_aura(self, descending=False):
        self.tasks.sort(key=lambda t: t.aura, reverse=descending)

    def save_to_file(self, filename="tasks.json"):
        data = [{"name": t.name, "aura": t.aura, "done": t.done}
                for t in self.tasks]
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def load_from_file(self, filename="tasks.json"):
        if not os.path.exists(filename):
            return
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.tasks = [
            Task(item["name"], item["aura"], item.get("done"))
            for item in data
        ]
