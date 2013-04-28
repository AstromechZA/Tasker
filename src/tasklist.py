import os
from os import path
import task
import json
import time

class TaskList:

    def __init__(self, name, folder):

        # Name must not include the .tsk extension
        if (len(name) > 4) and (name[-3:] == ".tsk"):
            name = name[:-3]

        self.name = name
        self.path = path.join(folder, name + ".tsk")
        self.activetasks = []
        self.completedtasks = []

        self.load()

    def load(self):
        if path.exists(self.path):
            with open(self.path,'r') as f:
                l = f.readline()
                j = json.loads(l)
                ts = j['active']
                for t in ts:
                    self.activetasks.append(task.fromJSON(t))
                ts = j['completed']
                for t in ts:
                    self.completedtasks.append(task.fromJSON(t))

                self.sort()

    def save(self):
        with open(self.path, 'w') as f:
            f.write(json.dumps(self.toJSON()))

    def destroy(self):
        os.remove(self.path)

    # Add a task to the tasklist
    def add(self, task):
        self.activetasks.append(task)
        self.sort_active()

    def complete(self, index):
        t = self.activetasks.pop(index)
        t.completed = time.time()

        self.completedtasks.append(t)
        self.sort()

    def active(self):
        return len(self.activetasks)

    def completed(self):
        return len(self.completedtasks)

    def sort(self):
        self.sort_active()
        self.sort_completed()

    def sort_active(self):
        def active_comparator(t1, t2):
            if t1.duedate == t2.duedate: 
                return t2.priority - t1.priority
            return t1.duedate - t2.duedate

        self.activetasks = sorted(self.activetasks, cmp=active_comparator)

    def sort_completed(self):
        def completed_comparator(t1, t2):
            return t2.completed - t1.completed

        self.completedtasks = sorted(self.completedtasks, cmp=completed_comparator)



    



    def toJSON(self):
        return {
            'name' : self.name, 
            'active' : [t.toJSON() for t in self.activetasks], 
            'completed' : [t.toJSON() for t in self.completedtasks]
        }