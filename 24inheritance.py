#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Inheritance

Created on Sat Dec 28 22:33:46 2024

@author: luzi
"""
# define attributes inside of a class
# another class can inherit those attributes

from Chef import Chef
from ChineseChef import ChineseChef

myChef = Chef()
myChef.make_special_dish()

myChineseChef = ChineseChef()
myChineseChef.make_chicken()
myChineseChef.make_special_dish()