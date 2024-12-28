#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chinese Chef Class

Created on Sat Dec 28 22:37:57 2024

@author: luzi
"""
# inherits from Chef class
from Chef import Chef

class ChineseChef(Chef):
    # overwrite certain function
    def make_special_dish(self):
        print("The chef makes orange chicken.")
    # add new functions
    def make_frid_rice(self):
        print("The chef makes fried rice.")