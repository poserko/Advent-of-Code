# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 09:34:18 2023

@author: zkoritnik
"""

import concurrent.futures


with open("C:/Users/zkoritnik/Skripte/AoC/2023/input/aoc_5.txt", 'r') as f:
    maps = [i.strip() for i in f.readlines()]

seed = [int(i) for i in maps[0].split(':')[1].strip().split()]
maps = [i for i in maps[1:] if i.strip()]

ranges = [[seed[i], seed[i+1]] for i in range(0, len(seed), 2)]

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
    
# dicti = {k: [] for s in ranges for k in range(s[0], s[0] + s[-1])}
dicti  = {}
for s in ranges:
    print(s)
    for s in range(s[0], s[0] + s[-1]):
        dicti[s] = []
        # print(s)
        for key in key_list:
            pos_maps = set()
            for val in result_dict[key]:
                sid = s if not dicti.get(s) else dicti.get(s)[-1]
                if sid in range(val[1], val[1] + val[-1]):
                    map_num = sid + (val[0] - val[1])
                    dicti[s].append(map_num)
                    pos_maps.add(map_num)
                    break
                
            if not pos_maps:
                dicti[s].append(sid)

res = min([i[-1] for i in dicti.values()])
print(f'Part 2: {res}')
             

# def process_range(single_range):
#     start, length = single_range
#     print(start, length)
#     local_dicti = {}
#     for s in range(start, start + length):
#         # print(s)
#         local_dicti[s] = []
#         for key in key_list:
#             pos_maps = set()
#             for val in result_dict[key]:
#                 sid = s if not local_dicti.get(s) else local_dicti.get(s)[-1]
#                 if sid in range(val[1], val[1] + val[-1]):
#                     map_num = sid + (val[0] - val[1])
#                     local_dicti[s].append(map_num)
#                     pos_maps.add(map_num)
#                     break
#             if not pos_maps:
#                 local_dicti[s].append(sid)
#     return local_dicti
                
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     results = list(executor.map(process_range, ranges))

# print('res obtained')
# dicti = {}
# # Combine the results into the final dicti
# for local_dicti in results:
#     for k, v in local_dicti.items():
#         if k not in dicti:
#             dicti[k] = v
#         else:
#             dicti[k].extend(v)

# res = min([i[-1] for i in dicti.values()])
# print(f'Part 2: {res}')            





