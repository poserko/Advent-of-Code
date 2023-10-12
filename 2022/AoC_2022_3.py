# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 18:00:43 2022

@author: zkoritnik
"""

file = 'aoc_2022_3'
with open(f"C:/Users/zkoritnik/AoC/2022/{file}.txt") as f:
    data = f.readlines()
    data = [i.split() for i in data]
    data = [list(j) for i in data for j in i]

lower = list(map(chr, range(97, 123)))
prior_lower = [i for i in range(1, 27)]

upper = [i.upper() for i in list(map(chr, range(97, 123)))]
prior_upper = [i for i in range(27, 53)]

low = {lower[i]: prior_lower[i] for i in range(len(lower))}
upp = {upper[i]: prior_upper[i] for i in range(len(upper))}

def split_list(lst):
    half = len(lst)//2
    return lst[:half], lst[half:]

both = []
for line in data:
    a, b = split_list(line)
    n = list(set(a).intersection(b))
    both.append(n)

c = 0
for b in both:
    if b[0].islower():
        c += low[b[0]]
    else:
        c += upp[b[0]]
print(f'Solution for Part 1: {c}')

compartment  = []
for line in range(0, len(data), 3):
    inner = []
    for i in data[line:line+3]:
        inner.append(i)
    compartment.append(list(set(inner[0]).intersection(inner[1], inner[2])))

count = 0
for b in compartment:
    if b[0].islower():
        count += low[b[0]]
    else:
        count += upp[b[0]]
print(f'Solution for Part 2: {count}')
