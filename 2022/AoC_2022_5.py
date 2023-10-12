# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 18:00:43 2022

@author: zkoritnik
"""

file = 'aoc_2022_5'
with open(f"C:/Users/zkoritnik/AoC/2022/{file}.txt") as f:
    data = f.readlines()
    data = [i.split() for i in data]

def dictionary():
    di = {
        1: ['N', 'S','D','C','V','Q','T'],
        2: ['M','F','V'],
        3: ['F','Q','W','D','P','N','H','M'],
        4: ['D','Q','R','T','F'],
        5: ['R','F','M','N','Q','H','V','B'],
        6: ['C','F','G','N','P','W','Q'],
        7: ['W','F','R','L','C','T'],
        8: ['T','Z','N','S'],
        9: ['M','S','D','J','R','Q','H','N']
        }
    return di

crane= dictionary()
for i in range(len(data)):
    for _ in range(int(data[i][1])):
        s = crane[int(data[i][3])].pop()
        crane[int(data[i][-1])].append(s)

ans = []
for k, v in crane.items():
    ans.append(v[-1])
a = ''.join(ans)
print(f'Solution for Part 1: {a}')



crane= dictionary()
for i in range(len(data)):
    items = crane[int(data[i][3])][-int(data[i][1]):]
    mid = []
    for _ in range(len(items)):
        s = crane[int(data[i][3])].pop()
        mid.append(s)
    for it in reversed(mid):
        crane[int(data[i][-1])].append(it)

ans = []
for k, v in crane.items():
    ans.append(v[-1])
b = ''.join(ans)
print(f'Solution for Part 2: {b}')
