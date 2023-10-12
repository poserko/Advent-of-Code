# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 18:00:43 2022

@author: zkoritnik
"""

file = 'aoc_2022_1'
with open(f"C:/Users/zkoritnik/AoC/2022/{file}.txt") as f:
    data = f.read() #importaš txt file kot string...readlines da podatke v list
    data = data.split('\n\n') # split po empty line
    data = [text.replace('\n', ' ') for text in data]
    data = [i.split() for i in data]
    data = [[int(x) for x in lst] for lst in data]

sums = set()
for line in range(len(data)):
    s = sum(data[line])
    sums.add(s)

most = sorted(sums, reverse=True)[0]
print(f'Solution for Part 1: {most}')

top3 = sum(sorted(sums, reverse=True)[:3])
print(f'Solution for Part 1: {top3}')
