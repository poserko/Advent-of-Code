# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 15:51:23 2021

@author: Maruša Pungartnik
"""

import os
import numpy as np
os.chdir(r'C:\Users\Maruša Pungartnik\Desktop\Žiga')

with open('AoC.txt') as aoc:
    template = aoc.readline()
    template = template.strip('\n')
    data = [i for i in aoc.readlines() if i != '']
    data = data[1:]
    data = [i.split('\n')[0] for i in data]
    data= [i.split('->') for i in data]

rules = {}

for i,v in enumerate(data):
    for ii,vv in enumerate(data):
        if i == ii:
            rules[v[0].strip(' ')] = vv[1].strip(' ')

#Part 1

for step in range(10):
    nex = template[0]
    for index in range(len(template)-1):
        start = template[index:index+2]
        nex += rules.get(start)
        nex += start[1]       
    template = nex

most = max(template, key=template.count)
least = min(template, key = template.count)

m=0
l=0
for i in template:
    if i == most:
        m+=1
    elif i == least:
        l+=1
print(f'Solution Part 1: {m-l}')


#Part 2

for step in range(40):
    nex = template[0]
    for index in range(len(template)-1):
        start = template[index:index+2]
        nex += rules.get(start)
        nex += start[1]       
    template = nex

most = max(template, key=template.count)
least = min(template, key = template.count)

m=0
l=0
for i in template:
    if i == most:
        m+=1
    elif i == least:
        l+=1
print(f'Solution Part 2: {m-l}')



        
        




    
    

        
