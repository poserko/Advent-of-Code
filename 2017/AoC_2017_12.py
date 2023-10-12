# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 15:53:40 2022

@author: zkoritnik
"""

FILE = 'aoc_2017_12'
with open(f"C:/Users/zkoritnik/AoC/2017/{FILE}.txt") as f:
    data = f.readlines()
    data = [i.strip('\n') for i in data]
    data = [i.replace('<->', '').replace(',', '') for i in data]
    data = [i.split() for i in data]
    # data = [int(j) for i in data for j in i]

programs = {}
for d in range(len(data)):
    programs[data[d][0]] = data[d][1:]


connect = programs['0'].copy()
step = 0
while step < len(connect):
    for item in programs[connect[step]]:
        if item not in connect:
            connect += [item]
    step += 1
print(f'Solutiin for Part 1: {len(connect)}')




