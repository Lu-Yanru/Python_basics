#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calculator 2

Created on Sat Dec 28 19:23:19 2024

@author: luzi
"""
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter the operator: ")

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("invalid operator")