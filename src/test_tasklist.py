import unittest
import tempfile
import task
from tasklist import TaskList
import os
import time

class TestTaskList(unittest.TestCase):

    def setUp(self):
        self.workingD = tempfile.mkdtemp()

    def test_create_destroy(self):
        name = "test1"

        tl = TaskList(name, self.workingD)
        tl.save()

        assert os.path.exists(os.path.join(self.workingD, name + ".tsk"))

        tl.destroy()

        assert not os.path.exists(os.path.join(self.workingD, name + ".tsk"))

    def test_save_load(self):
        name = "test2"
        tsk1 = task.Task("Do something", 1367144289 , 0)
        tsk2 = task.Task("Do something else", 1367144288 , 0)
        tsk3 = task.Task("A completed task", 13671442887, 0)

        before = TaskList(name, self.workingD)
        before.add(tsk1)
        before.add(tsk2)

        before.add(tsk3)
        before.complete(2)

        before.save()

        after = TaskList(name, self.workingD)
        assert after.active() == 2
        assert after.completed() == 1
        
        assert after.activetasks[0].equals(before.activetasks[0])
        assert after.activetasks[1].equals(before.activetasks[1])

        assert after.completedtasks[0].equals(before.completedtasks[0])

        before.destroy()

    def test_active_sort(self):
        name = "test3"
        
        tl = TaskList(name, self.workingD)

        tsk1 = task.Task("Task with early due date and priority 0", 1367144200 , 0)
        tsk2 = task.Task("Task with later due date and priority 0", 1367144210 , 0)

        tl.add(tsk1)
        tl.add(tsk2)

        assert tl.activetasks[0].equals(tsk1)

        tsk3 = task.Task("Task with earlier due date and priority 0", 1367144100 , 0)

        tl.add(tsk3)

        assert tl.activetasks[0].equals(tsk3)

        tsk4 = task.Task("Task with the same due date and higher priority", 1367144100, 1)
        
        tl.add(tsk4)

        assert tl.activetasks[0].equals(tsk4)






if __name__ == '__main__':
    unittest.main()