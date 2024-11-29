#Basic class to manage and interact withg To Do Lists, every task its also a to do list, because they can be completed and have your own sub tasks to
class Todolist():
    def __init__(self, name):
        self.name = name
        self.tasks = []
        self.completed = False

    def addTask(self, new_task: str):
        self.tasks.append(Todolist(new_task))

    def removeTask(self, task_id):
        self.tasks.pop(task_id)

    def showSubTasks(self):
        for item in self.tasks:
            print(item.name)
        
