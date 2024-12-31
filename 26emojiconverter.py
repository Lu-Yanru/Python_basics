#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Emoji converter

Created on Tue Dec 31 14:32:11 2024

@author: luzi
"""
# a dictionary that translates charaters to emojis
message = input(">")
# split the message where there is a space and return a list
words = message.split(' ')
# print("words")
# define a dictionary of emojis
emojis = {
    ":)": "😀",
    ":(": "😞"
    }
# loop through words
# if an emoji, find in dictionary and convert to emoji
# if not an emoji, keep the same word
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)