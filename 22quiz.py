#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build a multiple choice quiz

Created on Sat Dec 28 22:10:29 2024

@author: luzi
"""
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
        
question_prompts = [
    "What color are apples\n(a) Read/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
    ]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")    
    ]

def run_test(questions):
    score = 0
    for q in questions:
        answer = input(q.prompt)
        if answer == q.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)