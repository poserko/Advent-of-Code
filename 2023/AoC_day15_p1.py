# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 19:48:27 2023

@author: zkoritnik
"""


with open("C:/Users/zkoritnik/Skripte/AoC/2023/input/aoc_15.txt", 'r') as f:
    inpt = f.readline()
 
# l = inpt.split(',')
final = [list(i) for i in inpt.split(',')]


total = 0
for a in final:
    
    h = 0
    for i in a:
        ascii_code = ord(i)
        # print(h)
        # print(ascii_code)
        h += ascii_code
        # print(h)
        multipy = h * 17
        # print(multipy)
        divide = multipy % 256
        # print(divide)
        h = divide
        # print(h)
    
    total += h
    
print(total)
