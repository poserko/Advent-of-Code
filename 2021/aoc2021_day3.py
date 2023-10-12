# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 13:47:21 2021

@author: Maruša Pungartnik
"""

import os

os.chdir(r'C:\Users\Maruša Pungartnik\Desktop\Žiga')

with open('AoC.txt') as aoc:
    data=aoc.readlines()
    data=[i.split('\n')[0] for i in data]


gamma=[]
epsilon = [] 
for i in range(len(data[0])):
    one = 0
    zero = 0    
    for k in range(len(data)):       
       if data[k][i] == '0':
           zero += 1
       else:
           one += 1
    if zero > one:
        gamma.append(0)
        epsilon.append(1)
    else:
        gamma.append(1)
        epsilon.append(0) 

gamma_rate=int(''.join(map(str,gamma)),2)
epsilon_rate = int(''.join(map(str,epsilon)),2)

power = gamma_rate * epsilon_rate
print(f'Part 1: {power}')



data2=data.copy()
index = 0

while len(data) > 1:
    one = 0
    zero = 0
    ones = []
    zeros = []
    
    for i in range(len(data)):
        if data[i][index] == '0':
            zero += 1
            zeros.append(data[i])         
        else:
            one += 1
            ones.append(data[i])  
    if zero > one:
        data = zeros
    else:
        data = ones
    
    index += 1
       
oxygen = int(data[0],2)


data=data2
index = 0

while len(data) > 1:
    one = 0
    zero = 0
    ones = []
    zeros = []
    
    for i in range(len(data)):
        if data[i][index] == '0':
            zero += 1
            zeros.append(data[i])     
        else:
            one += 1
            ones.append(data[i])    
    if one < zero:
        data = ones
    else:
        data = zeros
   
    index += 1
       
co2 = int(data[0],2)

print(f'Part 2: {oxygen * co2}')
            








           

        
    
       
        
        
    
    
