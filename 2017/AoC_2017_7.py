# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 18:00:43 2022

@author: zkoritnik
"""
FILE = 'aoc_2017_7'
with open(f"C:/Users/zkoritnik/AoC/2017/{FILE}.txt") as f:
    data = f.readlines()
    data = [i.strip() for i in data]
    data = [i.split('->') for i in data]
    data = [w.split() for i in data for w in i]
    # data = [w.split(',') for i in data for w in i]


one = set()
two = []
for i in data:
    if '(' in i[1]:
        one.add(i[0])
    else:
        two.append(i)

flatList = set([element.rstrip(',') for innerList in two for element in innerList])
r = (one - flatList).pop()
print(f'Result for Part 1: {r}')

















# t = dict((m[0], (int(m[1]), m[3].split(', ') if m[3] else []))
#          for m in [re.match('(\w+) \((\d+)\)( -> ((\w+, )*\w+))?', l).groups()
#                    for l in data])
# n = (set(t) - set(c for n in t for c in t[n][1])).pop()
# # print(n)
# w = lambda n: t[n][0] + sum(w(c) for c in t[n][1])
# b = lambda n: len({w(c) for c in t[n][1]}) == 1
# a = lambda n: sum(w(c) for c in t[n][1]) / len(t[n][1])

# while not b(n):
#     c = sorted(t[n][1], key=lambda c: -abs(w(c)-a(n)))
#     n = ([c for c in t[n][1] if not b(c)] + c)[0]
# print(t[c[0]][0] + w(c[1]) - w(c[0]))

# g = [j.split() for i in data2 for j in i]

# di = {}
# for j in range(len(data)-1):
#     print(data[j])
#     if '(' in data[j][1]:
#         di[data[j][0]] = [int((data[j][1].strip('()')))]
#         # print(data[j][1].strip('()'))
#     if '(' not in data[j+1][1]:
#         # print(data[j][0])
#         di[data[j][0]].append([i.rstrip(',') for i in data[j+1]])

# for k, v in di.items():
#     # print(k)
#     # print('.....')
#     if len(v) > 1:
#         # print(v[1])
#         for j in v[1]:
#             for kk, vv in di.items():
#                 if j == kk:
#                     print(j, vv[0])





# o = {}
# t = []
# for i in data:
#     if '(' in i[1]:
#         o[i[0]] = int(i[1].lstrip('(').rstrip(')'))
#     else:
#         t.append([j.rstrip(',') for j in i])