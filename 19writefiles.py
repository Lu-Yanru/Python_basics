#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Write a file

Created on Sat Dec 28 21:10:02 2024

@author: luzi
"""
# append to a file
employee_file = open("employees.txt", "a")
employee_file.write("\nToby - Human Resources")
employee_file.close()

# overwrite an entire existing file/creat a new file
employee_file = open("employees1.txt", "w")
employee_file.write("\nToby - Human Resources")
employee_file.close()