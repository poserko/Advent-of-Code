# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 18:00:43 2022

@author: zkoritnik
"""

data = [5,	1,	10,	0,	1,	7,	13,	14,	3,	12,	8,	10,	7,	12,	0,	6]

s = set()
while tuple(data) not in s:
    s.add(tuple(data))
    m = max(data)
    i = data.index(m)
    data[i] = 0
    for step in range(m):
        data[(step+i+1) % len(data)] += 1
print(f'Solution for Part 1: {len(s)}')

d = data
s = set()
while tuple(d) not in s:
    s.add(tuple(d))
    m = max(d)
    i = d.index(m)
    d[i] = 0
    for step in range(m):
        data[(step+i+1) % len(d)] += 1
print(f'Solution for Part 2: {len(s)}')
