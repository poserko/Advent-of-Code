# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 18:57:38 2023

@author: zkoritnik
"""


with open("C:/Users/zkoritnik/Skripte/AoC/2023/input/aoc_13.txt", 'r') as f:
    inpt = [i.strip().split(',') for i in f.readlines()]

g = [list(j) for i in inpt for j in i]

current_grid = []
grids = []
for i in g:
    if not i:
        if current_grid:
            grids.append(current_grid)
            current_grid = []
    else:
        current_grid.append(i)

if current_grid:
    grids.append(current_grid)

rows = 0
cols = 0

for i, _ in enumerate(grids):
    grid = grids[i]
    grid_cols = list(zip(*grids[i]))
    for i in range(1, len(grid)):
        upper_half = grid[:i][::-1]
        lower_half = grid[i:]
        
        above = upper_half[:len(lower_half)]
        below = lower_half[:len(above)]
           
        if above == below:
            rows += i*100

cols = 0
for i, _ in enumerate(grids):
    grid = grids[i]
    grid = list(zip(*grid))
 
    for i in range(1, len(grid)):
        upper_half = grid[:i][::-1]
        lower_half = grid[i:]
        
        above = upper_half[:len(lower_half)]
        below = lower_half[:len(above)]
           
        if above == below:
            cols += i
    
res = cols + rows
print(res)













