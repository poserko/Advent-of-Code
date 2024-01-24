# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 11:29:24 2023

@author: zkoritnik
"""

import numpy as np

with open("C:/Users/zkoritnik/Skripte/AoC/2023/input/aoc_3.txt", 'r') as f:
    grid = [i.strip().split(' ') for i in f.readlines()]
    gr = [list(j) for i in grid for j in i]

non_digit_coordinates = []
for row_index, row in enumerate(gr):
    for col_index, value in enumerate(row):
        ele = gr[row_index][col_index]
        if ele == '.':
            continue
        if not ele.isdigit():
            non_digit_coordinates.append((row_index, col_index))

position = {}
for row, col in non_digit_coordinates:
    for ai, ac in [(row-1, col), (row+1, col), (row, col-1), (row, col+1), (row-1, col-1), (row+1, col-1), (row+1, col+1), (row-1, col+1)]:
        if 0 <= ai < len(gr) and 0 <= ac < len(gr[0]):
            if gr[ai][ac].isdigit() and (ai, ac) not in position:
                position[(ai, ac)] = gr[ai][ac]
            else:
                continue

unique_coordinates = set()
for coord in position:
    adjacent_found = False
    for existing_coord in unique_coordinates.copy():
        if coord[0] == existing_coord[0] and abs(coord[1] - existing_coord[1]) == 1:
            adjacent_found = True
            break
    if not adjacent_found:
        unique_coordinates.add(coord)

n = []    
for r, c in unique_coordinates:
    num = ""
    for cc in range(c, -1, -1): #left horizontal search
        if gr[r][cc].isdigit():
            num = gr[r][cc] + num
        else:
            break

    for cc in range(c+1, len(gr[r])):
        if gr[r][cc].isdigit():
            num += gr[r][cc]
        else:
            break
    n.append(int(num))

print(f'Part 1: {sum(n)}')    
    
   

#=========================================================================
#=========================================================================


star = []
for row_index, row in enumerate(gr):
    for col_index, value in enumerate(row):
        ele = gr[row_index][col_index]
        if ele == '*':
            star.append((row_index, col_index))
        else:
            continue

position = {}
for row, col in star:
    for ai, ac in [(row-1, col), (row+1, col), (row, col-1), (row, col+1), (row-1, col-1), (row+1, col-1), (row+1, col+1), (row-1, col+1)]:
        if 0 <= ai < len(gr) and 0 <= ac < len(gr[0]):
            if gr[ai][ac].isdigit() and (ai, ac) not in position:
                position[(ai, ac)] = gr[ai][ac]
            else:
                continue

unique_coordinates = set()
for coord in position:
    adjacent_found = False
    for existing_coord in unique_coordinates.copy():
        if coord[0] == existing_coord[0] and abs(coord[1] - existing_coord[1]) == 1:
            adjacent_found = True
            break
    if not adjacent_found:
        unique_coordinates.add(coord)
        
gears = {}
for row, col in star:
    gears[(row, col)] = []
    for ai, ac in [(row-1, col), (row+1, col), (row, col-1), (row, col+1), (row-1, col-1), (row+1, col-1), (row+1, col+1), (row-1, col+1)]:
        if 0 <= ai < len(gr) and 0 <= ac < len(gr[0]):
            if (ai, ac) in unique_coordinates:
                tup = (ai, ac)
                gears[(row, col)].append(tup)
            else:
                continue
            
gears = {key: value for key, value in gears.items() if len(value) == 2}

n = []
fin = {}  
for k, v in gears.items():
    n = []
    for r, c in v:
        
        num = ""
        for cc in range(c, -1, -1): #left horizontal search
            if gr[r][cc].isdigit():
                num = gr[r][cc] + num
            else:
                break
    
        for cc in range(c+1, len(gr[r])):
            if gr[r][cc].isdigit():
                num += gr[r][cc]
            else:
                break
        n.append(int(num))
    fin[k] = n

c = 0
for v in fin.values():
    c += np.prod(v)

print(f'Part 2: {c}')
