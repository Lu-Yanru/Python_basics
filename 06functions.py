#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Functions

Created on Sat Dec 28 18:43:25 2024

@author: luzi
"""
# a collection of codes that perform a specific task
# keword(def) name_of_function(parameters):
#    code that goes into the function needs to be indented
def sayhi(name, age):
    print("Hello " + name + ", you are " + str(age))
    
# call the function
sayhi("Mike", 35)

# use the return statement to get info back from the function
# cannot put code after the print statement anymore
# return statement breaks out of the function
def cube(num):
    return num*num*num
    
result = cube(3)
print(result)

# positional arguments: order of argument matters, 1st argument = value of 1st parameter etc.
# keyword arguments: position does not matter, parameter_name = value
# when mix, use positional arguments before keyword arguments
sayhi(age = 50, name = "Tom")