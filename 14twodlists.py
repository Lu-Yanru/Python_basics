#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2D lists and nested loop

Created on Sat Dec 28 20:29:21 2024

@author: luzi
"""
# 2d lists, grid-like structure
# lists inside of list
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9], 
    [0]
]
# access elements in the grid grid[row][column]
print(number_grid[0][0])

# nested for loop
# for loop inside to for loop
# parse through a 2d list
for row in number_grid:
    for col in row:
        print(col)