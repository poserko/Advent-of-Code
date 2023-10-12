# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 18:00:43 2022

@author: zkoritnik
"""

FILE = 'aoc_2017_9'
with open(f"C:/Users/zkoritnik/AoC/2017/{FILE}.txt") as f:
    data = f.readline()
    data = list(data)


garbage = False
cancel = False
level = 0
c = 0
g = 0

for i in data:
    if cancel:
        cancel = False
    elif i == '!':
        cancel = True
    elif i == '>':
        garbage = False
    elif garbage:
        g += 1
    elif i == '<':
        garbage = True
    elif i == '{':
        level += 1
    elif i == '}':
        c += level
        level -= 1
print(f'Solution for Part 1: {c}')
print(f'Solution for Part 2: {g}')
