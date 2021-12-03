# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 12:57:37 2021

@author: Maruša Pungartnik
"""

with open('AoC.txt') as aoc:
    data=aoc.readlines()

data = [int((i.split("\n")[0])) for i in data]


count=0
for i in range(len(data)-1):
    
    if data[i+1] > data[i]:
        count+=1
print(count)



sums = [sum(data[i:i+3]) for i in range(len(data))]

part2=0
for i in range(len(sums)-1):
    if sums[i+1] > sums[i]:
        part2+=1
print(part2)
    

    
    