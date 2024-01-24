# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 20:47:47 2023

@author: zkoritnik
"""


with open("C:/Users/zkoritnik/Skripte/AoC/2023/input/aoc_9.txt", 'r') as f:
    hist = [i.strip().split(',') for i in f.readlines()]

a = [[int(k) for k in j.split()] for i in hist for j in i]

d = {}
for k, v in enumerate(a):
    if k not in d:
        d[k] = []
    d[k].append(list(v))

end = {}
indx = 0 
while indx < len(d):
    for key in [list(d.keys())[indx]]:
        val = d.get(key)[-1]
        if all(i==0 for i in d.get(key)[-1]):
            end[key] = d.get(key)
            indx += 1
            # break
        else:
            lst = val
            r = [b - a for a, b in zip(lst[: -1], lst[1 :])]
            d[key].append(r)
       
new = {}
for k, v in end.items():
    last_elements = [inner_list[-1] for inner_list in v if inner_list]
    new[k] = last_elements

c = 0
for i in new.values():
    c += sum(i)
    
print(c)
    
p2 = {}
for k, v in end.items():
    first_elements = [inner_list[0] for inner_list in v if inner_list]
    p2[k] = first_elements

cc = 0
test = []
for key, v in p2.items():
    # print(v)
    vv = v[::-1]
    for i in range(len(v)-1):
        # print(vv[i])
        st = vv[i+1] - vv[i]
        vv[i+1] = st
        # print(vv)
            
    test.append(vv[-1])
    
print(sum(test))
