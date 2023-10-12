# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 20:34:37 2021

@author: Maruša Pungartnik
"""

import os

os.chdir(r'C:\Users\Maruša Pungartnik\Desktop\Žiga')

with open('AoC.txt') as aoc:
    data = aoc.readlines()
    data = [i.split(',') for i in data]
    data = [int(val) for sublist in data for val in sublist]



f = []
for to in range(1, len(data)):
    fuel=0
    for i in data:
        dif = abs(i - to)
        fuel += dif
    f.append(fuel)
print(min(f))


cost = []
for to in range(1, len(data)):
    fuel = 0
    for i in data:
        c = 0
        dif = abs(i - to)
        for d in range(1,dif+1):
            c += d
        fuel += c
    cost.append(fuel)
print(min(cost))

            
        

        
        

