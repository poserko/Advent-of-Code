# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 18:00:43 2022

@author: zkoritnik
"""

file = 'aoc_2022_10'
with open(f"C:/Users/zkoritnik/AoC/2022/{file}.txt") as f:
    data = f.readlines()
    data = [i.split() for i in data]

x = 1
l = []
for line in data:
    if line[0] == 'noop':
        l.append(x)
    else:
        l.append(x)
        l.append(x)
        x += int(line[1])

print(sum(((x+1) * y for x, y in list(enumerate(l))[19::40])))

x = 1
l = []
for line in data:
    if line[0] == 'noop':
        l.append(x)
    else:
        l.append(x)
        l.append(x)
        x += int(line[1])

for i in range(0, len(l), 40):
    for j in range(40):
       print('#' if abs(l[i + j] - j) <= 1 else ' ', end='')
    print()
