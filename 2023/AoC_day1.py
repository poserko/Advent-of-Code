# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 09:11:10 2023

@author: zkoritnik
"""

with open("C:/Users/zkoritnik/Skripte/AoC/2023/input/aoc_1.txt", 'r') as f:
    data = [i.strip() for i in f.readlines()]

p1 = 0
for word in data:
    num = []
    for char in word:
        if char.isdigit():
            num.append(char)
    p1 += int(num[0] + num[-1])
print(f'Part 1:{p1}')

encode = {'one': '1',
          'two': '2',
          'three': '3',
          'four': '4',
          'five': '5',
          'six': '6',
          'seven': '7',
          'eight': '8',
          'nine': '9'}

fin = []
p2 = 0
for word in data:
    integ = []
    for i, char in enumerate(word):
        if char.isdigit():
            integ.append(char)
        for k, v in encode.items():
            if word[i:].startswith(k):
                integ.append(v)
    p2 += int(integ[0] + integ[-1])
print(f'Part 2:{p2}')
                
