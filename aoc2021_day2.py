# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 12:14:28 2021

@author: Maruša Pungartnik
"""

import os

os.chdir(r'C:\Users\Maruša Pungartnik\Desktop\Žiga')

with open('AoC.txt') as aoc:
    data=aoc.readlines()
    data=[i.split('\n')[0] for i in data]
    data=[i.split() for i in data]
    
forward = 0
depth = 0

for i in data:
    if i[0] == 'forward':
        forward += int(i[1])
    elif i[0] == 'down':
        depth += int(i[1])
    elif i[0] == 'up':
        depth -= int(i[1])

print(f'Part 1 result: {forward * depth}')


aim = 0
forward = 0
depth = 0

for i in data:
    if i[0] == 'forward':
        forward += int(i[1])
        depth = depth + (aim * int(i[1]))        
    elif i[0] == 'down':
        aim += int(i[1])        
    elif i[0] == 'up':
        aim -= int(i[1])
        
print(f'Part 2 result: {forward * depth}')

    
    
    