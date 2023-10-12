# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 18:00:43 2022

@author: zkoritnik
"""

file = 'aoc_2017_1'
with open(f"C:/Users/zkoritnik/AoC/{file}.txt") as f:
    data = f.readline()

total = 0
l = len(data)
half = len(data) // 2
data += data
for i in range(l):
    if data[i] == data[i+1]:
        total += int(data[i])
print(f'Solution for Part 1: {total}')

t = 0
for i in range(l):
    # print(d[i], d[i+h])
    if data[i] == data[i+half]:
        t += int(data[i])
print(f'Solution for Part 2: {t}')
