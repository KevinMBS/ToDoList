class Todolist():
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def addTask(self, new_task):
        self.tasks.append(new_task)

    def removeTask(self, task_id):
        self.tasks.pop(task_id)
