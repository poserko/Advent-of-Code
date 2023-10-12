# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 09:09:30 2021

@author: Maruša Pungartnik
"""

import os
os.chdir(r'C:\Users\Maruša Pungartnik\Desktop\Žiga')

with open('AoC.txt') as aoc:
    data = aoc.readlines()
    data = [i.split('\n')[0] for i in data]
    data= [i.split('->') for i in data]

collect={}
for i in range(len(data)):
    
    x1 = int(data[i][0].split(',')[0])
    x2 = int(data[i][1].split(',')[0])
    y1 = int(data[i][0].split(',')[1])
    y2 = int(data[i][1].split(',')[1])
    if x1==x2 or y1==y2:
        for i in range(min(x1,x2),max(x1,x2)+1):
            for j in range(min(y1,y2),max(y1,y2)+1):
                if (i,j) in collect:
                    collect[(i,j)] +=1                    
                else:
                    collect[(i,j)] = 1
                
overlap = []
for key, value in collect.items():
    if value > 1:
        overlap.append(key)
print(f'Part 1 solution: {len(overlap)}')


collect={}
for i in range(len(data)):
    
    x1 = int(data[i][0].split(',')[0])
    x2 = int(data[i][1].split(',')[0])
    y1 = int(data[i][0].split(',')[1])
    y2 = int(data[i][1].split(',')[1])
    if x1==x2 or y1==y2:
        for i in range(min(x1,x2),max(x1,x2)+1):
            for j in range(min(y1,y2),max(y1,y2)+1):
                if (i,j) in collect:
                    collect[(i,j)] +=1                    
                else:
                    collect[(i,j)] = 1
    else:
            
        xinc=1 if x1<x2 else -1
        yinc=1 if y1<y2 else -1
        
        for i,v in enumerate(range(x1,x2+xinc,xinc)):
            for l,j in enumerate(range(y1,y2+yinc,yinc)):
                if i==l:
                    if (v,j) in collect:
                        collect[(v,j)] += 1
                    else:
                        collect[(v,j)] = 1
                
overlap = []
for key, value in collect.items():
    if value > 1:
        overlap.append(key)
print(f'Part 2 solution: {len(overlap)}')

    

  


