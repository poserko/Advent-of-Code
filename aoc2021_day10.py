# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 18:33:24 2021

@author: Maruša Pungartnik
"""

import os
from collections import deque 

os.chdir(r'C:\Users\Maruša Pungartnik\Desktop\Žiga')

with open('AoC.txt') as aoc:
    data = aoc.readlines()
    data = [x.split('\n')[0] for x in data]
    data = [list(i) for i in data]    
    
openpar = ['(','[','{','<']
closedpar = [')',']','}','>']
score = [3,57,1197,25137]

count = 0
stack = []
incomplete = []
for line in data:
    for char in line:
        if char in openpar:
            stack.append(char)     
        elif char in closedpar:
            index = closedpar.index(char)
            if stack[-1] != openpar[index]:
                count += score[index]           
                break
            else:
                del(stack[-1])
                
    incomplete.append(line)
            
                
print(f'Part 1 solution: {count}')

openpar = ['(','[','{','<']
closedpar = [')',']','}','>']
score = [1,2,3,4]

incomplete = []
for line in data:
    stack = []
    corrupt = False
    for char in line:
        if char in openpar:
            stack.append(char)     
        elif char in closedpar:
            index = closedpar.index(char)
            if stack[-1] != openpar[index]:
                count += score[index]   
                corrupt = True
                break
            else:
                del(stack[-1])
    if corrupt == False:
        incomplete.append("".join(stack))
  
points=[]
for i in incomplete:
    total = 0
    for x in i[::-1]: #reverse loop 
        total *=5
        total += score[openpar.index(x)]
    points.append(total)

sort = sorted(points)
middle = len(points)//2

print(f'Part 2 solution: {sort[middle]}')























# =============================================================================
# 
# 
# 
# test = '[({(<(())[]>[[{[]{<()<>>'
# test= [i for i in test]
# 
# nested=[]
# for line in data:
#     d = {'(':0, '[':0, '{':0, '<':0, ')':0, ']':0, '}':0, '>':0}
#     for i in line:
#         if '(' in i:
#             d[i] +=1
#         elif '[' in i:
#             d[i] += 1
#         elif '{' in i:
#             d[i] += 1
#         elif '<' in i:
#             d[i] += 1
#         elif ')' in i:
#             d[i] += 1
#         elif ']' in i:
#             d[i] += 1
#         elif '}' in i:
#             d[i] += 1
#         elif '>' in i:
#             d[i] += 1
#         else:
#             pass
#     nested.append(d)
#     #print(d)
# 
# dife=[]
# raz = []
# chack = [')','}',']','>']
# for i in nested:
#     
#     for l in range(len(i.keys())-4):
#        # print(l)
#         
#         
#         if list(list(i.items())[l])[1] == list(list(i.items())[l+4])[1]:
#             pass
#         else:
#             dif=abs((list(list(i.items())[l])[1]) - (list(list(i.items())[l+4])[1]))
#            # print(list(list(i.items())[l])[0], list(list(i.items())[l+4])[0])
#            # print(f'diff {dif}')
#             dife.append((dif,list(list(i.items())[l+4])[0]))
#             
#             score = 0
#             for items in dife:
#                 if items[1] == ')':
#                     score = score * 5 + 1
#                 elif items[1] == ']':
#                     score = score * 5 + 2
#                 elif items[1] == '}':
#                     score = score * 5 + 3
#                 elif items[1] == '>':
#                     score = score * 5 + 4
#                 print(score)
#                     
# 
# # ): 1 point.
# # ]: 2 points.
# # }: 3 points.
# # >: 4 points
# 
# 
#     
# 
# 
#     
# 
# =============================================================================

        
        
  
            