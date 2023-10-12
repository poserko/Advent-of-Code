# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 18:00:43 2022

@author: zkoritnik
"""

import sys

file = 'aoc_2022_14'
with open(f"C:/Users/zkoritnik/AoC/2022/{file}.txt") as f:
    data = f.readlines()

b = set()
abyss = 0
for line in data:
    x = [list(map(int, p.split(","))) for p in line.strip().split(" -> ")]
    print(x)
    for (x1, y1), (x2, y2) in zip(x, x[1:]):
        x1, x2 = sorted([x1, x2])
        y1, y2 = sorted([y1, y2])
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                b.add(x + y * 1j)
        abyss = max(abyss, y + 1)

# t = 0
# while True:
#     s = 500
#     while True:
#         if s.imag >= abyss:
#             # print(t)
#             sys.exit()
#         if s + 1j not in b:
#             s += 1j
#             continue
#         if s + 1j - 1 not in b:
#             s += 1j - 1
#             continue
#         if s + 1j + 1 not in b:
#             s += 1j + 1
#             continue
#         b.add(s)
#         t += 1
#         break


x = 500
y = 9
c = x + y * 1j
s = 500

