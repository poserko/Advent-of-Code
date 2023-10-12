# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 18:00:43 2022

@author: zkoritnik
"""
# from collections import Counter

FILE = 'aoc_2017_4'
with open(f"C:/Users/zkoritnik/AoC/2017/{FILE}.txt") as f:
    data = f.readlines()
    data = [i.split() for i in data]

valid = 0
for line in data:
    if len(line) == len(set(line)):
        valid += 1
print(f'Solution for Part 1: {valid}')

v = 0
for p in data:
    if len(p) == len(set(tuple(sorted(w)) for w in p)):
        v += 1
print(f'Solution for Part 2: {v}')
