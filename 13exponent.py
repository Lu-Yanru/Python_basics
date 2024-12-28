#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build a exponent function

Created on Sat Dec 28 20:24:09 2024

@author: luzi
"""
# 2 raised to the third power
print(2**3)

def raise_to_power(base_num, power_num):
    result = 1
    for index in range(power_num):
        result = result * base_num
    return result

print(raise_to_power(2, 3))