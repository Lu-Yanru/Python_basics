#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Directories

Created on Tue Dec 31 15:32:14 2024

@author: luzi
"""
from pathlib import Path


# absolute path: start from the root of hard drive
# c:\Program Files\Microsoft
# /usr/local/bin

# relative path: a path starting from the current directory
# call a Path object
# if not pass an argument, refers to the current directory
# can pass a string as file or directory as argument
path = Path("emails")
# check if a path exists
print(path.exists())
# create a new directory
path.mkdir()
# remove the directory
path.rmdir()

# find all the files and directories in a given path
path = Path()
# path.glob("search pattern")
# * means everything
# can add extension after .
# can iterate through them to automate sth
for file in path.glob("*.py"):
    print(file)