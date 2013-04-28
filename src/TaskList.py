from os import path
from Task import Task
import json

class TaskList:

    def __init__(self, name, folder):

        # Name must not include the .tsk extension
        if (len(name) > 4) and (name[-3:] == ".tsk"):
            name = name[:-3]

        self.name = name
        self.path = path.join(folder, name + ".tsk")
        self.tasks = []

    def loadList(self):
        if not path.exists(self.path):
            self.tasks = []
        else:
            with open(self.path,'r') as f:
                l = f.readline()
                self.tasks = json.loads(l)
                print l

    def saveList(self):
        with open(self.path, 'w') as f:
            f.write(json.dumps(self.toJSON()))

    # Add a task to the tasklist
    def addTask(self, content, due=None, priority=None):
        t = Task(content, due, priority)
        self.tasks.append(t)

        self.saveList()


    def listTasks(self):
        # first get all uncompleted tasks
        # sort by priority & due date

        # get completed tasks
        # sort by date completed
        # append

        # print





    def toJSON(self):
        tasks_as_json = [t.toJSON() for t in self.tasks]
        return {'name':self.name, 'tasks':tasks_as_json}