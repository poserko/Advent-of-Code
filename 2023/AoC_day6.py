# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 10:40:12 2023

@author: zkoritnik
"""

with open("C:/Users/zkoritnik/Skripte/AoC/2023/input/aoc_6.txt", 'r') as f:
    d = [i.strip().split() for i in f.readlines()]

time = list(map(int, d[0][1:]))
distance = list(map(int, d[1][1:]))

new_time = int(''.join(map(str, time)))
new_distance = int(''.join(map(str, distance)))

count = 1
for option, dist in zip(time, distance):
    ref_time = option 
    ref_dist = dist
    c = 0
    for i in range(option+1):
        res = i * (ref_time - i)
        if res > ref_dist:
            c += 1
    count *= c
    
print(f'Part 1: {count}')
 
    
ref_time = new_time 
ref_dist = new_distance
c = 0
for i in range(new_time+1):
    res = i * (ref_time - i)
    if res > ref_dist:
        c += 1
            
print(f'Part 2: {c}')
