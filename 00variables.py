#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Variables and data types

Created on Sat Dec 28 17:10:56 2024

@author: Yanru Lu
"""
# variable: container that stores certain data values

# import more complicated math functions
from math import *

# name of the variable, diff words separated by _ = values
character_name = "John"
character_age = "50"
is_male = False

print("There once was a man names " + character_name + ",")
print("he was " + character_age + " years old.")

# update the values of variable
character_name = "Tom"

print("He really liked the name " + character_name + ",")
print("but he didn't like being "+ character_age + ".")




# data types

# string: plain text
# in quotation marks
# \n create a new line in the string
print("Giraffe\nAcademy")
# \as escape character to print out the next character literally
print("Giraffe\"Academy")
# store string in variable
phrase = "Giraffe Academy"
print(phrase)
# concatenation with +
print(phrase + " is cool.")
# use functions
# convert to lower/upper case
print(phrase.lower())
# check whether lower/upper case
print(phrase.isupper())
# can be combined
print(phrase.upper().isupper())
# check the length of the string
print(len(phrase))
# grab a character from a string, index starting with 0
print(phrase[0])
# where a specific character or string start in the string, gives error if not exist
print(phrase.index("Acad"))
# replace piece of string with another
print(phrase.replace("Giraffe", "Elefant"))

# numbers
# no quotation marks needed
# basic arithmetic
print(3 * (4 + 5))
# store number in varaible
my_num = -5
# convert number into a string, useful when printing number together with string
print(str(my_num) + " my favorite number")
# math functions
# absolute value
print(abs(my_num))
# number1 raised to the power of number2
print(pow(3, 2))
# the max/min
print(max(4, 6))
# round a number up or down at .5
print(round(3.2))
# round down only
print(floor(3.7))
# rounf up only
print(ceil(3.2))
# square root
print(sqrt(36))

# boolean
# true/false