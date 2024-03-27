#!/usr/bin/env python3

#Now import shutil. Remember, Python is the general contractor who shows up to the job with a toolbelt containing only the most common tools (modules), unless told otherwise. The import statement is how we're able to remind Python to bring special tools (modules) to the jobsite (our script).

import shutil

#This module provides a portable way of using operating system dependent functionality. Where shutil allows for higher-level file manipulation, os is more targeted at the operating system.

import os

#force the Python program to 'start' in the home user directory, which for us will be /home/student/mycode/. This is made possible by calling, os.chdir(). This will allow the user to run the program from any location on the system, and our script still always start at /home/student/mycode/

os.chdir('/home/student/mycode/')

#Calling shutil.move(source, destination) will move the file or folder at the path source to the path destination and will return a string of the absolute path of the new location. If destination points to a folder, the source file gets moved into destination and keeps its current filename.

shutil.move('raynor.obj', 'ceph_storage/')

#Prompt the user for a new name for the kerrigan.obj file.

xname = input('What is the new name for kerrigan.obj? ')

#Rename the current kerrigan.obj file.

shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)
