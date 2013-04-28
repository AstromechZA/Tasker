# Tasker.py
import argparse
import os
import sys
import glob
import time
from datetime import datetime
from os import path

from tasklist import TaskList
from task import Task
import parsedatetime as pdt

def yesno(query):
    while True:
        print query + " (yes/no)"
        ans = raw_input()
        if ans.lower() == 'yes': return True
        if ans.lower() == 'no': return False



def create_new_task():
    print "What is the task:"
    content = raw_input()
    
    cal = pdt.Calendar(pdt.Constants('en_AU', usePyICU=False))
    dt = None
    while True:
        print "When is it due (ENTER to no due date)"
        dd = cal.parse(raw_input())

        dt = datetime.fromtimestamp(time.mktime(dd[0]))

        if yesno("Did you mean '%s'?" % dt.strftime("%H:%M:%S %d/%m/%Y")):
            break

    prio = 2
    while True:
        print "What is its priority? (0 = Lowest, 1 = Low, 2 = Normal, 3 = High, 4 = Highest)"
        i = input()
        if i>=0 and i<=4:
            prio = i
            break

    t = Task(content, time.mktime(dt.timetuple()), prio)
    return t


if __name__ == '__main__':

    # check if home folder has .tasker folder
    home = path.expanduser("~")
    taskerfolder = path.join(home, ".tasker")
    if not path.exists(taskerfolder):
        # Create it if it does not exist
        print 'Creating Tasker folder at: ' + taskerfolder
        os.makedirs(taskerfolder)

    # No arguments, default to list by adding it
    if len(sys.argv) == 1:
        sys.argv.append('list')

    # Get command from args
    cmd = sys.argv[1].lower()

    if cmd == 'list':
        # List tasks
        t = TaskList('default', taskerfolder)
        t.print_list()

    elif cmd == 'add':
        t = TaskList('default', taskerfolder)
        t.add(create_new_task())
        t.save()

        t.print_list()

    elif cmd =='-h' or cmd == '--help':
        # Show usage
        print "Try one of the following:"
        print "  list \t:   List your tasks."
        print "  add  \t:   Add a new task to the list"
    else:
        # Unrecognised command
        print "Unrecognised command: '%s'" % cmd
        print "Try one of the following:"
        print "  list \t:   List your tasks."
        print "  add  \t:   Add a new task to the list"



    print 1