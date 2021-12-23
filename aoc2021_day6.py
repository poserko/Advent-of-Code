# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 21:37:45 2021

@author: Maruša Pungartnik
"""

import os
os.chdir(r'C:\Users\Maruša Pungartnik\Desktop\Žiga')

with open('AoC.txt') as aoc:
    data = aoc.readlines()
    data = [i.split(',') for i in data]
    data = [int(val) for sublist in data for val in sublist]

new = data.copy()
days = 82

for day in range(1,days):
    new_data = []
    fish = []
    for i in new:
        if i == 0:
            fish.append(8)
            i = 6   
        else:
            i-=1
        new_data.append(i)
    new_data.extend(fish)
    new = new_data
print(len(new))


       
    