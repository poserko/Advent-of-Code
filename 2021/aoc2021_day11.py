# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 17:30:51 2021

@author: Maruša Pungartnik
"""

import os
import numpy as np
import threading 

os.chdir(r'C:\Users\Maruša Pungartnik\Desktop\Žiga')

data=[]
with open('AoC.txt') as aoc:
    line=aoc.readline()
    while line:
        full = [x for x in line.strip('\n')]
        number = [int(x) for x in full]
        data.append(number)
        line=aoc.readline()


R = len(data) # index
C = len(data[0]) #elements in each list
 
ans = 0
def flash(r,c):
    global ans
    ans += 1
    data[r][c] = -1
    for dr in [-1,0,1]:
        for dc in [-1,0,1]:
            rr = r+dr
            cc = c+dc
            
            if 0<=rr<R and 0<=cc<C and data[rr][cc]!=-1:
                data[rr][cc] += 1
                if data[rr][cc] >= 10:
                    flash(rr,cc)

for t in range(100):
    
    for r in range(R):
            for c in range(C):
                data[r][c] += 1
    for r in range(R):
        for c in range(C):
            if data[r][c] == 10:
                flash(r,c)
    
    for r in range(R):
        for c in range(C):
            if data[r][c] == -1:
                data[r][c] = 0
                
print(f'Part 1 solution: {ans}')


# part 2 - comment the whole part 1 code!!!
G = data
R = len(G)
C = len(G[0])

ans = 0
def flash(r,c):
    global ans
    ans += 1
    G[r][c] = -1
    for dr in [-1,0,1]:
        for dc in [-1,0,1]:
            rr = r+dr
            cc = c+dc
            if 0<=rr<R and 0<=cc<C and G[rr][cc]!=-1:
                G[rr][cc] += 1
                if G[rr][cc] >= 10:
                    flash(rr,cc)

t = 0
while True:
    t += 1
    for r in range(R):
        for c in range(C):
            G[r][c] += 1
    for r in range(R):
        for c in range(C):
            if G[r][c] == 10:
                flash(r,c)
    done = True
    for r in range(R):
        for c in range(C):
            if G[r][c] == -1:
                G[r][c] = 0
            else:
                done = False # not all flashed at once
    if t == 100:
        print(ans)
    if done:
        print(f'Part 2 solution: {t}')
        break
