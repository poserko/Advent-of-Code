# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 18:00:43 2022

@author: zkoritnik
"""

file = 'aoc_2022_2'
with open(f"C:/Users/zkoritnik/AoC/2022/{file}.txt") as f:
    data = f.readlines()
    data = [i.strip().split() for i in data]

score = 0
needs = 0
for play in data:
    if play[0] == 'A' and play[1] == 'Y':
        score += 8
        needs += 4
    if play[0] == 'A' and play[1] == 'Z':
        score += 3
        needs += 8
    if play[0] == 'A' and play[1] == 'X':
        score += 4
        needs += 3
    if play[0] == 'B' and play[1] == 'Y':
        score += 5
        needs += 5
    if play[0] == 'B' and play[1] == 'Z':
        score += 9
        needs += 9
    if play[0] == 'B' and play[1] == 'X':
        score += 1
        needs += 1
    if play[0] == 'C' and play[1] == 'Y':
        score += 2
        needs += 6
    if play[0] == 'C' and play[1] == 'Z':
        score += 6
        needs += 7
    if play[0] == 'C' and play[1] == 'X':
        score += 7
        needs += 2

print(f'Solution for Part 1: {score}')
print(f'Solution for Part 2: {needs}')

s = 0
n = 0
for play in data:
    s += {'X':1, 'Y': 2, 'Z': 3}[play[1]]
    s += {('A', 'Y'): 6, ('B', 'Y'): 3, ('C', 'Y'): 0,
          ('A','Z'): 0, ('B', 'Z'): 6, ('C', 'Z'): 3,
          ('A', 'X'): 3, ('B', 'X'): 0, ('C', 'X'): 6}[play[0], play[1]]

    n += {'X':0, 'Y': 3, 'Z': 6}[play[1]]
    n += {('A', 'Y'): 1, ('B', 'Y'): 2, ('C', 'Y'): 3,
          ('A','Z'): 2, ('B', 'Z'): 3, ('C', 'Z'): 1,
          ('A', 'X'): 3, ('B', 'X'): 1, ('C', 'X'): 2}[play[0], play[1]]

print(f'Solution for Part 1 using dict: {s}')
print(f'Solution for Part 2 using dict: {n}')












