#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build a calculator

Created on Sat Dec 28 18:00:48 2024

@author: luzi
"""
# practical project
# get input numbers from user
# calculate the input
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
# convert input into a number because by default they are strings
# int() for converting into integer
# float() for floats
result = float(num1) + float(num2)
print(result)
