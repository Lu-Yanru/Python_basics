#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Student class

Created on Sat Dec 28 22:27:05 2024

@author: luzi
"""
# define own data type with class
# class name_of_class:
class Student:
    # initialize function: map out what attributes a student should have
    def __init__(self, name, major, gpa, is_on_probation):
        # assgin values
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
        
    # define function for this class
    # give or modify information about obj of this class
    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False