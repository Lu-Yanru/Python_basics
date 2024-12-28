#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Reading files

Created on Sat Dec 28 20:56:03 2024

@author: luzi
"""
# open(path/name_of_file, open_mode("read"/"write"/"append"/"read and write r+"))
employee_file = open("employees.txt", "r")

# get info from file
# check if it is possible to read the file
print(employee_file.readable())
# read all info in the file
print(employee_file.read())
# read lines in the file one at a time starting from the last read line
print(employee_file.readline())
# read each line in the file and put them in a list, can acces specific line with index
print(employee_file.readlines()[1])

for employee in employee_file.readlines():
    print(employee)

# close the file
employee_file.close()
