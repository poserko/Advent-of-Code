# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 12:18:05 2021

@author: Maruša Pungartnik
"""

import os
from scipy import ndimage
import numpy as np
from collections import deque 


os.chdir(r'C:\Users\Maruša Pungartnik\Desktop\Žiga')

data=[]
with open('AoC.txt') as aoc:
    line=aoc.readline()
    while line:
        full = [x for x in line.strip('\n')]
        number = [int(x) for x in full]
        data.append(number)
        line=aoc.readline()

for i in data:
    i.insert(0, 10)
    i.insert(len(i), 10) 
    
for i in data:
    lenght = len(i)
     
add = [10] * lenght

data.insert(0, add)
data.insert(len(data), add)

def low(): 
    small = []       
    for item in data:
       
        for index in range(len(data)-1):
            
            for lenght in range(len(item)-1):
                
                if data[index+1][lenght+1] < data[index][lenght+1] and data[index+1][lenght+1] < data[index+1][lenght] and data[index+1][lenght+1] < data[index+2][lenght+1] and data[index+1][lenght+1] < data[index+1][lenght+2]:
                   
                    small.append(data[index+1][lenght+1])
        return small
    
lowest = low()
risk = sum([i+1 for i in lowest])
print(f'Solution for Part 1: {risk}')


####### Part 2 - Floodfill ----- BFS algorithm

data1=[]
with open('AoC.txt') as aoc:
    line=aoc.readline()
    while line:
        full = [x for x in line.strip('\n')]
        number = [int(x) for x in full]
        data1.append(number)
        line=aoc.readline()

rows = len(data1)
colls = len(data1[0])
DR = [-1,0,1,0]
DC = [0,1,0,-1]
basin = []
seen = set()
for index in range(rows):
    for lenght in range(colls):
        if (index, lenght) not in seen and data1[index][lenght] != 9:
            count = 0
            queue = deque()
            queue.append((index, lenght))
            while queue:
                (index, lenght) = queue.popleft()
                if (index, lenght) in seen:
                    continue
                seen.add((index, lenght))
                count += 1
                for l in range(4):
                    rr = index + DR[l]
                    cc = lenght + DC[l]
                    if 0 <= rr < rows and 0 <= cc < colls and data1[rr][cc] != 9:
                        queue.append((rr,cc))
            basin.append(count)           
basin.sort()
print(f'Part 2 solution: {basin[-1] * basin[-2] * basin[-3]}')
                
                
                
                
                
                
            
            
        








