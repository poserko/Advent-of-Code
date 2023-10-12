# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 18:00:43 2022

@author: zkoritnik
"""
import numpy as np

lenghts = [88,88,211,106,141,1,78,254,2,111,77,255,90,0,54,205]
data = [i for i in range(256)]

skip = 0
position = 0
for pos in lenghts:
    if position + pos < len(data):
        data[position: position + pos] = data[position: position + pos][::-1]
    else:
        alt_data = data + data
        rev = alt_data[position:position+pos][::-1]
        data[position:] = rev[:len(data) - position]
        data[:position+pos-len(data)] = rev[len(data)-position:]
    position += pos + skip
    position = np.mod(position, len(data))
    skip += 1

res = data[0] * data[1]
print(f'Solution for Part 1: {res}')
