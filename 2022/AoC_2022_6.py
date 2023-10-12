# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 18:00:43 2022

@author: zkoritnik
"""

file = 'aoc_2022_6'
with open(f"C:/Users/zkoritnik/AoC/2022/{file}.txt") as f:
    data = f.readline()

d = {}
start = 0
end = 4
c = 0
while sum(d.values()) != 4 and len(d) != 4:
    d = {}
    for i in data[start:end]:
        c+=1
        if i not in d:
            d[i] = 1
        else:
            d[i] = 1
    start += 1
    end += 1
print(f'Solution for Part 1: {end-1}')

d = {}
start = 0
end = 14
c = 0
while sum(d.values()) != 14 and len(d) != 14:
    d = {}
    for i in data[start:end]:
        c+=1
        if i not in d:
            d[i] = 1
        else:
            d[i] = 1
    start += 1
    end += 1
print(f'Solution for Part 2: {end-1}')
