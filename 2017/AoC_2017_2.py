# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 18:00:43 2022

@author: zkoritnik
"""

FILE = 'aoc_2017_2'
with open(f"C:/Users/zkoritnik/AoC/2017/{FILE}.txt") as f:
    data = f.readlines()
    data = [i.strip(' ').split() for i in data]

numbers = []
for l in data:
    numbers.append([int(i) for i in l])

total = 0
for l in numbers:
    total += max(l) - min(l)
print(f'Solution for Part 1: {total}')

t = 0
for lists in numbers:
    for ii, num in enumerate(lists):
        for jj, nums in enumerate(lists):
            if ii != jj:
                if num % nums == 0:
                    t += num // nums
print(f'Solution for Part 2: {t}')
