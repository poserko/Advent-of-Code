# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 17:41:11 2022

@author: zkoritnik
"""

import os

os.chdir(r'C:\Users\zkoritnik\csv')

with open('aoc.txt') as aoc:
    data = aoc.readlines()
    card = int(data[0].strip())
    door = int(data[1].strip())
    
count = 0
x = 1
    
while x != card:
    count += 1
    x = (x * 7) % 20201227
    print(x)
    
print(count)

key = 0

for _ in range(count):
    key = (key * door) % 20201227

print()
