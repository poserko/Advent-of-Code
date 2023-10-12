# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 18:00:43 2022

@author: zkoritnik
"""
from collections import defaultdict


file = 'aoc_2022_7'
with open(f"C:/Users/zkoritnik/AoC/2022/{file}.txt") as f:
    data = f.readlines()
    data = [i.split() for i in data]

s = defaultdict(int)
path = []
for line in data:
    if line[1] == 'cd':
        if line[2] == '..':
            path.pop()
        else:
            path.append(line[2])
    elif line[1] == 'ls':
        continue
    elif line[0] == 'dir':
        continue
    else:
        sz = int(line[0])
        for i in range(1, len(path)+1):
            s['/'.join(path[:i])] += sz

max_used = 70000000 - 30000000
total_used = s['/']
need_to_free = total_used - max_used

p1 = 0
p2 = 1e9
for k,v in s.items():
    if v <= 100000:
        p1 += v
    if v>=need_to_free:
        p2 = min(p2, v)
print(f'Solution for Part 1: {p1}')
print(f'Solution for Part 2: {p2}')
