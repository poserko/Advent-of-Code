# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 09:34:18 2023

@author: zkoritnik
"""

with open("C:/Users/zkoritnik/Skripte/AoC/2023/input/aoc_5.txt", 'r') as f:
    maps = [i.strip() for i in f.readlines()]

seed = maps[0].split(':')[1].strip().split()
seed = [int(i) for i in seed]
maps = [i for i in maps[1:] if i.strip()]

result_dict = {}
key_list = []
for line in maps:
    if line.endswith(':'):
        key = line.rstrip(':')
        key_list.append(key)
        result_dict[key] = []
    elif key:
        val = list(map(int, line.split()))
        result_dict[key].append(val)
        

dicti = {k: [] for k in seed}
for s in seed:
    for key in key_list:
        maps = set()
        for val in result_dict[key]:
            sid = s if not dicti.get(s) else dicti.get(s)[-1]
            if sid in range(val[1], val[1] + val[-1]):
                map_num = sid + (val[0] - val[1])
                dicti[s].append(map_num)
                maps.add(map_num)
                break
            
        if not maps:
            dicti[s].append(sid)
             
res = min([i[-1] for i in dicti.values()])
print(f'Part 1: {res}')
