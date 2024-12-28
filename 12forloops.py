#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
For loops

Created on Sat Dec 28 20:12:55 2024

@author: luzi
"""
# loop over diff collection of items

# for variable(diff value at diff iteration) in collection_to_loop_over
for letter in "Giraffe Academy":
    print(letter)
    
friends = ["Jim", "Karen", "Kevin"]
for friend in friends:
    print(friend)
    
for index in range(3, 10):
    print(index)
    
for index in range(len(friends)):
    print(friends[index])

for index in range(5):
    if index == 0:
        print("first interation")
    else:
        print("Not first")