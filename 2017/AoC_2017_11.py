# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 15:53:40 2022

@author: zkoritnik
"""

FILE = 'aoc_2017_11'
with open(f"C:/Users/zkoritnik/AoC/2017/{FILE}.txt") as f:
    data = f.readline()
    data = data.split(',')

def coordinates(x, y, z):
    steps = sum(list(map(abs, [x,y,z]))) // 2
    return steps

x, y, z = 0, 0, 0
highest = []
for step in data:
    if step == 'n':
        x += 1
        y -= 1
        highest.append(coordinates(x, y, z))
    elif step == 's':
        x -= 1
        y += 1
        highest.append(coordinates(x, y, z))
    elif step == 'ne':
        x += 1
        z -= 1
        highest.append(coordinates(x, y, z))
    elif step == 'sw':
        x -= 1
        z += 1
        highest.append(coordinates(x, y, z))
    elif step == 'se':
        y += 1
        z -= 1
        highest.append(coordinates(x, y, z))
    elif step == 'nw':
        y -= 1
        z += 1
        highest.append(coordinates(x, y, z))

res = coordinates(x, y, z)
print(f'Sloution for Part 1: {res}')
print(f'Sloution for Part 2: {max(highest)}')
