#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dictionaries

Created on Sat Dec 28 19:30:41 2024

@author: luzi
"""
# store info in key-value pairs
# access piece of info by refering to its key

# create a dictionary
# name = {key: value}
# keys have to be unique
# keys can be strings or numbers
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "Auguest",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}
print(monthConversions["Nov"])
# can specify default value when key is not found
print(monthConversions.get("Luv", "Not a valid key"))
