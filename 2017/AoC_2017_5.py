# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 18:00:43 2022

@author: zkoritnik
"""

FILE = 'aoc_2017_5'
with open(f"C:/Users/zkoritnik/AoC/2017/{FILE}.txt") as f:
    data = f.readlines()
    data = [int(i.strip()) for i in data]

# steps = 0
# i = 0
# while 0 <= i < len(data):
#     j = data[i]
#     data[i] += 1
#     i += j
#     steps += 1
# print(f'Solution for Part 1: {steps}')

# s = 0
# i = 0
# while 0 <= i < len(data):
#     j = data[i]
#     data[i] += -1 if j > 2 else 1
#     i += j
#     s += 1
# print(f'Solution for Part 1: {s}')

for c in (lambda _: False, lambda x: x > 2): # narediš loop, kjer uporabiš dve funkciji
    m, s, i = list(data), 0, 0
    while 0 <= i < len(m):
        j = m[i]
        m[i] += -1 if c(j) else 1
        i += j
        s += 1
    print(s)



