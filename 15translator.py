#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build a translator

Created on Sat Dec 28 20:35:47 2024

@author: luzi
"""
# change all vowels into g

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else: 
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))