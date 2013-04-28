
class Task:

    def __init__(self, content, duedate, priority):
        self.content = content
        self.duedate = duedate
        self.priority = priority
        self.completed = 0

    def toJSON(self):
        return self.__dict__