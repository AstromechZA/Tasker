import os
from os import path
import task
import json
import time

import terminalsize
import colorama
from colorama import Fore, Back, Style

class TaskList:

    priorityStyles = [ Back.BLACK + Fore.WHITE, Back.BLACK + Fore.GREEN, Back.GREEN + Fore.WHITE, Back.YELLOW + Fore.WHITE, Back.RED + Fore.WHITE ]

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
                if 'active' in j:
                    ts = j['active']
                    for t in ts:
                        self.activetasks.append(task.fromJSON(t))
                if 'completed' in j:
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
            return int(t1.duedate - t2.duedate)

        self.activetasks = sorted(self.activetasks, cmp=active_comparator)

    def sort_completed(self):
        def completed_comparator(t1, t2):
            return t2.completed - t1.completed

        self.completedtasks = sorted(self.completedtasks, cmp=completed_comparator)


    def print_list(self):
        colorama.init()
        sizex, sizey = terminalsize.get_terminal_size()
        sizex-=5
        # Print active tasks
        tlen = 9+10+20+3
        clen = sizex-tlen
        fmtstr = "%(id)3s | %(content)-" + str(clen) + "s | %(due)-20s | %(priority)-10s" + Fore.RESET + Back.RESET + Style.RESET_ALL
        print Back.WHITE + Fore.BLACK + fmtstr % {'id':'#','content':'Task','due':'Due','priority':'Priority'}

        if len(self.activetasks) == 0:
            print "There are no active tasks. Use the 'Add' command to to one."
        else:
            c = 0
            for t in self.activetasks:
                numlines = int(len(t.content) / (clen))+1
                col1 = c
                col2 = ""
                col3 = time.strftime("%H:%M:%S %d/%m/%Y", time.localtime(t.duedate))
                col4 = t.priority
                start = 0
                for i in range(numlines):

                    end = start+clen
                    if end < len(t.content):
                        while end>0:
                            if t.content[end].isspace():
                                break
                            end-=1
                        if end==0:
                            end = start+clen
                    col2 = (t.content[start:end]).strip()
                    start = end
                    print self.priorityStyles[t.priority] + fmtstr % {'id':col1 , "content": col2, 'due':col3,'priority':col4}
                    col1 = col3 = col4 = ""
                c+=1

        print ""


    def toJSON(self):
        return {
            'name' : self.name, 
            'active' : [t.toJSON() for t in self.activetasks], 
            'completed' : [t.toJSON() for t in self.completedtasks]
        }