#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Try/except

Created on Sat Dec 28 20:44:49 2024

@author: luzi
"""
# catching errors without breaking program

try:
    #value = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("invalid input")