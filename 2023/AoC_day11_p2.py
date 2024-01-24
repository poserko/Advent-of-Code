# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 09:17:58 2023

@author: zkoritnik
"""

from itertools import combinations

with open("C:/Users/zkoritnik/Skripte/AoC/2023/input/aoc_11.txt", 'r') as f:
    inpt = [i.strip().split(',') for i in f.readlines()]

grid = [list(j) for i in inpt for j in i]

rows_without_hash = [index for index, row in enumerate(grid) if '#' not in row]
columns_without_hash = [index for index in range(len(grid[0])) if '#' not in [row[index] for row in grid]]

rename = 1
galaxy_coord = {}
for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] == '#':            
            grid[row][col] = rename
            galaxy_coord[rename] = (row, col)
            rename +=1 

empty_rows_coord = []
empty_cols_coord = []
for row, i in enumerate(grid):
    for col, j in enumerate(grid):
        if row in rows_without_hash:
            empty_rows_coord.append((row, col))
        elif col in columns_without_hash:
            empty_cols_coord.append((row, col))
            
pairs = list(combinations(list(range(1, rename)), 2))

def manhattan_distance(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])

expansion = 1000000-1
count = 0
for start, end in pairs:
    start_gal = galaxy_coord.get(start)
    end_gal = galaxy_coord.get(end)
    a = (start_gal[0], end_gal[0])
    b = (start_gal[1], end_gal[1])
    for i in range(min(a), max(a)):
        if i in set(a for a, b in empty_rows_coord):
            count += expansion
    for j in range(min(b), max(b)):
        if j in set(b for a, b in empty_cols_coord):
            count += expansion
    
    distance = manhattan_distance(start_gal, end_gal)
    count += distance

print(f'Part 2: {count}')
