#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Object function

Created on Sat Dec 28 22:26:02 2024

@author: luzi
"""
from Student import Student
# from document import class

student1 = Student("Oscar", "Accounting", 3.1, False)
student2 = Student("Phyllis", "Business", 3.8, False)

print(student1.on_honor_roll())
