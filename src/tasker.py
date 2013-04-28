# Tasker.py
import argparse
import os
import sys
import glob
from os import path

from tasklist import TaskList

class Tasker:

    # Open a tasker in the given folder
    def __init__(self, _folder):
        self.folder = _folder
        self.current_list = "default"

    # List all of the tasklists in the folder
    def listLists(self):
        flist = glob.glob(path.join(self.folder, "*.tsk"))
        print flist




if __name__ == '__main__':

    # check if home folder has .tasker folder
    home = path.expanduser("~")
    taskerfolder = path.join(home, ".tasker")
    if not path.exists(taskerfolder):
        # Create it if it does not exist
        print 'Creating Tasker folder at: ' + taskerfolder
        os.makedirs(taskerfolder)

    # Parser argument
    parser = argparse.ArgumentParser()
    parser.add_argument("command", help="The tasklist command you wish to run.")
    parser.add_argument("-l","--list",help="The name of the tasklist you want to work on.")
    parser.usage = "%(prog)s command [options]"

    args = parser.parse_args()

    tasker = Tasker(taskerfolder)
    tasker.listLists()

    #tl = TaskList("default", taskerfolder)
    #tl.addTask("Do something", 12312049, 0)

    print args
