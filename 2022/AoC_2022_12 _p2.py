# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 18:00:43 2022

@author: zkoritnik
"""
from collections import deque

file = 'aoc_2022_12'
with open(f"C:/Users/zkoritnik/AoC/2022/{file}.txt") as f:
    data = f.readlines()
    data = [i.split() for i in data]
    data = [list(j) for i in data for j in i]

for row, i in enumerate(data):
    for col, j in enumerate(data[row]):
        if data[row][col] == 'S':
            data[row][col] = 'a'
        elif data[row][col] == 'E':
            re = row
            ce = col
            data[row][col] = 'z'
        else:
            pass

que = deque()
que.append((0, re, ce))

visited = {(re, ce)}

possible_path = []

while que:
    d, r, c = que.popleft()
    for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
        if nr < 0 or nc < 0 or nr >= len(data) or nc >= len(data[0]):
            continue
        elif (nr, nc) in visited:
            continue
        elif ord(data[nr][nc]) - ord(data[r][c]) < -1:
            continue
        elif data[nr][nc] == 'a':
            # print(d+1)
            possible_path.append(d+1)
            break

        que.append((d+1, nr, nc))
        visited.add((nr, nc))

print(f'Solution for Part 2: {possible_path[0]}')
