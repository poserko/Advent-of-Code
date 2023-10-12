# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 18:00:43 2022

@author: zkoritnik
"""

file = 'aoc_2022_13'
with open(f"C:/Users/zkoritnik/AoC/2022/{file}.txt") as f:
    data = f.read().strip().split('\n\n')
    data = [i.split() for i in data]

for inx, i in enumerate(data):
    for col, c in enumerate(data[inx]):
        data[inx][col] = eval(data[inx][col])


def compare(x, y):
    if type(x) == int and type(y) == int:
        if x - y < 0:
            return -1
        elif x - y == 0:
            return 0
        else:
            return 1

    elif type(x) == list and type(y) == int:
        y = [y]

    elif type(x) == int and type(y) == list:
        x = [x]

    for xx, yy in zip(x, y):
        res = compare(xx, yy)
        if res != 0:
        #     print(res)
            return res


    n = len(x)
    m = len(y)
    if n < m:
        return -2
    elif n == m:
        return 0
    else:
        return 2

c = 0
for inx, (a, b) in enumerate(data):
    if compare(a, b) < 0:
        c += inx + 1

print(f'Solution for Part 1: {c}.')

paket = []
for a, b in data:
    # print(a, b)
    paket.append(a)
    paket.append(b)

paket.append([[2]])
paket.append([[6]])

import functools

paket.sort(key=functools.cmp_to_key(compare))

result = (paket.index([[2]])+1) * (paket.index([[6]])+1)
print(f'Solution for Part 2: {result}')











