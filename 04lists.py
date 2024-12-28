#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lists

Created on Sat Dec 28 18:11:19 2024

@author: luzi
"""
# a strucutre to store lists of values
# can be any data type
# represented by []
friends = ["Kevin", "Karen", "Jim", "Oscar", "Tobi"]
lucky_numbers = [4, 8, 15, 16, 23, 42] 

print(friends)
# access individual values with index
print(friends[-2])
# access a range of elements
print(friends[1:])
print(friends[1:3])
# modify elements
friends[1] = "Mike"
print(friends[1])

# list functions
# append another list to a list
friends.extend(lucky_numbers)
print(friends)
# add an element to the end of a list
friends.append("Creed")
print(friends)
# add an element in the middle of a list
friends.insert(1, "Kelly")
print(friends)
# remove elements
friends.remove("Jim")
print(friends)
# remove all elements
friends.clear()
print(friends)
# remove the last item off the list
friends.pop()
print(friends)
# check the index of an element in the list
print(friends.index("Kevin"))
# count similar elements in the list
print(friends.count("Jim"))
# sort the list in acending order
friends.sort()
lucky_numbers.sort()
print(friends, lucky_numbers)
# reverse a list
lucky_numbers.reverse()
print(lucky_numbers)
# make a copy
friends2 = friends.copy()
print(friends2)
