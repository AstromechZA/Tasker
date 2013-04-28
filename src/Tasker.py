# Tasker.py
import argparse
import os
from os import path


if __name__ == '__main__':

    # check if home folder has .tasker folder
    home = path.expanduser("~")
    taskerfolder = path.join(home, ".tasker")
    if not path.exists(taskerfolder):
        print 'Creating Tasker folder at: ' + taskerfolder
        os.makedirs(taskerfolder)


