#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Guessing game

Created on Sat Dec 28 20:00:15 2024

@author: luzi
"""
secret_word = "giraffe"
guess = ""
# set limit of guesses
i = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if i < guess_limit:
        guess = input("Guess a word: ")
        i += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You ran out of guesses.")
else:
    print("You guessed the word!")