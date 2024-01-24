# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 20:47:47 2023

@author: zkoritnik
"""

from itertools import cycle
import math


with open("C:/Users/zkoritnik/Skripte/AoC/2023/input/aoc_8.txt", 'r') as f:
    d = [i.strip() for i in f.readlines()]
    instruct = list(d[0])*100
    dicti = dict((i.split('=')[0].strip(), i.split('=')[1].strip()) for i in d[2:])

dicti = {k: tuple(v[1:-1].split(', ')) for k, v in dicti.items()}

K = 'AAA'
c = 0
for inst in instruct:
    if inst == 'L':
        key= dicti.get(K)[0]
        K = key
        c += 1
        
    if inst == 'R':
        key= dicti.get(K)[1]
        K = key
        c += 1
        
    if K == 'ZZZ':
        break
        
print(f'Part 1: {c}')


start = [i for i in dicti.keys() if i.endswith('A')]

num = []
for K in start:
    c = 0
    for inst in cycle(instruct):
        if inst == 'L':
            key= dicti.get(K)[0]
            K = key
            c += 1
            
        if inst == 'R':
            key= dicti.get(K)[1]
            K = key
            c += 1
            
        if K.endswith('Z'):
            num.append(c)
            break

result = math.lcm(*num)
      
print(f'Part 2: {result}')


 