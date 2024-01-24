# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 09:11:10 2023

@author: zkoritnik
"""
import numpy as np

with open("C:/Users/zkoritnik/Skripte/AoC/2023/input/aoc_2.txt", 'r') as f:
    data = [i.strip() for i in f.readlines()] 

red = 12
green = 13
blue = 14
def checker(cube, blue, red, green):
    global parts, num
    for ele in cube:
        parts = ele.split(' ')
        num = int(parts[0])

        if 'blue' in ele and num > blue:
            return False
        elif 'red' in ele and num > red:
            return False
        elif 'green' in ele and num > green:
            return False

    return True

d = {}
for line in data:
    res = []
    key = line.split(':')[0]
    values = line.split(':')[1].split(';')
    for line in values:
        items = line.split(', ')
        res.extend(items)
    result = [item.strip() for item in res]

    d[key] = result

fin = []
for k, v in d.items():
    if checker(v, blue, red, green):
        fin.append(k)
c = 0
for i in fin:
    par = i.split(' ')
    num = int(par[1])
    c += num
print(f'Part 1:{c}')

game = {}
for k, v in d.items():
    dic = {'red':0, 'blue': 0, 'green': 0}
    for ele in v:
        parts = ele.split(' ')
        num = int(parts[0])
        word = str(parts[1])
        if word in dic and num > dic[word]:
            dic[word] = num
    game[k] = dic
   
counter = 0            
for k, v in game.items():
    prod = np.prod(list(game[k].values()))
    counter += prod
    
print(f'Part 2:{counter}')


    
    
    
    
    