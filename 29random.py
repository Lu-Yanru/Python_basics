#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generating random values

Created on Tue Dec 31 15:17:19 2024

@author: luzi
"""
import random


class Dice:
    def roll(self):
        num1 = random.randint(1, 6)
        num2 = random.randint(1, 6)
        result = (num1, num2)
        return result
        # alternative: return num1, num2   python automatically interpret as a tuple


members = ["John", "Mary", "Bob", "Mosh"]
for i in range(3):
    # generate a random value btw 0 and 1
    print(random.random())
    # generate random value in specified range
    print(random.randint(10, 20))
    # randomly pick an item froma list 
    print(random.choice(members))
    
# roll 2 dices
dice = Dice()
print(dice.roll())
