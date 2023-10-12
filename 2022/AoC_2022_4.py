# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 18:00:43 2022

@author: zkoritnik
"""

file = 'aoc_2022_4'
with open(f"C:/Users/zkoritnik/AoC/2022/{file}.txt") as f:
    data = f.readlines()
    data = [i.split() for i in data]
    data = [j.split(',') for i in data for j in i]
    data = [list(j.split('-')) for i in data for j in i]

for indx in range(len(data)):
    data[indx] = [i for i in range(int(data[indx][0]), int(data[indx][1])+1)]

contain = 0
share = 0
for i in range(0, len(data), 2):
    if set(data[i]).issubset(data[i+1]) or set(data[i+1]).issubset(data[i]):
        contain += 1
    if set(data[i]).intersection(set(data[i+1])):
        share += 1

print(f'Solution for Part 1: {contain}')
print(f'Solution for Part 2: {share}')
