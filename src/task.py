
class Task:

    def __init__(self, content, duedate, priority, completed=0):
        self.content = content
        self.duedate = duedate
        self.priority = priority
        self.completed = completed

    def toJSON(self):
        return self.__dict__

    def equals(self, othertask):
        return self.content == othertask.content \
            and self.duedate == othertask.duedate \
            and self.priority == othertask.priority \
            and self.completed == othertask.completed


def fromJSON(dictionary):
    c = dictionary['content']
    d = dictionary['duedate']
    p = dictionary['priority']
    t = dictionary['completed']
    return Task(c,d,p,t)