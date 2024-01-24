# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 09:17:58 2023

@author: zkoritnik
"""

from collections import deque
from itertools import combinations

with open("C:/Users/zkoritnik/Skripte/AoC/2023/input/aoc_11.txt", 'r') as f:
    inpt = [i.strip().split(',') for i in f.readlines()]

grid = [list(j) for i in inpt for j in i]

rows_without_hash = [index for index, row in enumerate(grid) if '#' not in row]
columns_without_hash = [index for index in range(len(grid[0])) if '#' not in [row[index] for row in grid]]

def add_rows(index_rows, matrix):
    index_increment = 0
    for index in index_rows:
        act_index = index_increment + index
        matrix.insert(act_index, ['.' for _ in range(len(matrix[0]))])
        index_increment += 1
    
    return matrix

def add_cols(index_cols, matrix):
    index_increment = 0
    for index in index_cols:
        act_index = index_increment + index
        index_increment += 1

        for row in matrix:
            row.insert(act_index, '.')

    return matrix
        
grid = add_rows(rows_without_hash, grid)
grid = add_cols(columns_without_hash, grid)

rename = 1
for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] == '#':            
            grid[row][col] = rename
            rename +=1 

def get_start_end_index(matrix, start, end):    
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == start:
                rs, cs = row, col
                
            if matrix[row][col] == end:
                re, ce = row, col
                
    return rs, cs, re, ce


pairs = list(combinations(list(range(1, rename)), 2))

counter = 0
solutions = []
for start, end in pairs:
    print(start, end)
    rs, cs, re, ce = get_start_end_index(grid, start, end)    
 

    que = deque()
    que.append((0, rs, cs))
    
    visited = {(rs, cs)}
    
    while que:
        # print(que)
        d, r, c = que.popleft()
        for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]):
                continue
            elif (nr, nc) in visited:
                continue
            elif nr == re and nc == ce:
                solutions.append(d+1)
                break
            que.append((d+1, nr, nc))
            visited.add((nr, nc))
        else:
            continue
        break
    continue
result = sum(solutions)
print(f'Part 1: {result}')
