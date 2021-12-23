# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 08:51:38 2021

@author: Maruša Pungartnik
"""

import os
os.chdir(r'C:\Users\Maruša Pungartnik\Desktop\Žiga')

with open('AoC.txt') as aoc:
    data = aoc.readlines()
    data = [i.split('|')[1].strip('\n') for i in data]
    data = [words for segments in data for words in segments.split()]

count = 0
check = [2, 4, 3, 7]
for i in data:
    if len(i) in check:
        count +=1 
print(f'Part 1 solution: {count}')
        
