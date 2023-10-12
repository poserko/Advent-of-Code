# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 18:00:43 2022

@author: zkoritnik
"""

file = 'aoc_2022_9'
with open(f"C:/Users/zkoritnik/AoC/2022/{file}.txt") as f:
    data = f.readlines()
    data = [i.split() for i in data]

hx, hy = 0, 0
tx, ty = 0, 0

visited = set()

for line in data:
    if line[0] == 'R':
        for _ in range(1, int(line[1])+1):
            hx += 1
            ty = hy if (abs(hx - tx)**2 + abs(hy - ty)**2)//2 == 2 else ty
            tx = hx - 1 if (abs(hx - tx)**2 + abs(hy - ty)**2)//2 == 2 else tx
            visited.add(tuple([tx, ty]))

    elif line[0] == 'L':
        for _ in range(1, int(line[1])+1):
            hx -= 1
            ty = hy if (abs(hx - tx)**2 + abs(hy - ty)**2)//2 == 2 else ty
            tx = hx + 1 if (abs(hx - tx)**2 + abs(hy - ty)**2)//2 == 2 else tx
            visited.add(tuple([tx, ty]))

    elif line[0] == 'U':
        for _ in range(1, int(line[1])+1):
            hy += 1
            tx = hx if (abs(hx - tx)**2 + abs(hy - ty)**2)//2 == 2 else tx
            ty = hy - 1 if (abs(hx - tx)**2 + abs(hy - ty)**2)//2 == 2 else ty
            visited.add(tuple([tx, ty]))

    else:
        for _ in range(1, int(line[1])+1):
            hy -= 1
            tx = hx if (abs(hx - tx)**2 + abs(hy - ty)**2)//2 == 2 else tx
            ty = hy + 1 if (abs(hx - tx)**2 + abs(hy - ty)**2)//2 == 2 else ty
            visited.add(tuple([tx, ty]))

print(f'Solution Part 1: {len(visited)}')


# rope = [[0,0] for _ in range(4)]


# for i in range(3):

#     for j in reversed(range(2,3)):
#         # print(i,j)
#         rope[i][0] = j
#         # print(rope[i][0])







