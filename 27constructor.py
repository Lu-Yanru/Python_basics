#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Constructor

Created on Tue Dec 31 14:43:54 2024

@author: luzi
"""
class Point:
    # constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # methods
    def move(self):
        print("move")
        
    def draw(self):
        print("draw")


class Person:
    def __init__(self, name):
        self.name = name
    
    def talk(self):
        print(f"Hi I am {self.name}")


# object/intance of the class
#point1 = Point()
# attributes of the object, like variables that belongs to a particular object
#point1.x = 10
#point1.y = 20
#point1.draw()

# a constructor is a function that is called at the time when creating an object
# sets initial values of attributes when creating the object
point = Point(10, 20)
# attribute can be updated later
point.x = 11
print(point.x)

john = Person("John")
john.talk()