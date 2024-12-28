#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
If statements

Created on Sat Dec 28 19:00:36 2024

@author: luzi
"""
# help programes to make decision
# respond to the input that they are given
# execute certain codes when certain conditions are true
# execute other codes when other conditions are true

is_male = False
is_tall = True

# if condition(true/false)
if is_male or is_tall:
    # if condition is true, execute the following code
    print("You are a male or tall or both")
else:
    # if condition is false, execute the following code
    print("You are neither male nor tall")
    

if is_male and is_tall:
    # if condition is true, execute the following code
    print("You are a tall male")
# add another condition
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but are tall")
else:
    # if condition is false, execute the following code
    print("You are not a male and not tall")
    
    

# conditions with comparison operators
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
    
print(max_num(3,4,5))
