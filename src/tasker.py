# Tasker.py
import argparse
import os
import sys
import glob
import time
from os import path

from tasklist import TaskList
from task import Task




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
        tsk = Task('Do something', time.time(), 2)
        t.add(tsk)
        t.save()

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