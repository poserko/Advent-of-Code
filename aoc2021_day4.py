# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 18:27:28 2021

@author: Maruša Pungartnik
"""

import os

os.chdir(r'C:\Users\Maruša Pungartnik\Desktop\Žiga')

with open('AoC.txt') as aoc:
    drawn = [int(i) for i in aoc.readline().strip('\n').split(',')]
    

    cards = []
    while aoc.readline():
        card = []
        for i in range(5):
            card.extend([int(i) for i in aoc.readline().strip('\n').split(' ') if i != ''])
            if card not in cards:  
                cards.append(card)

new=list(map(list, zip(*[iter([e for sublist in cards for e in sublist])]*5)))

def stop():
    for num in drawn:
        
        for index in range(0, len(new), 5):
                    
            for i in new[index:index+5]:  
                
                for k in range(len(i)):
                    
                    if i[k] == num:
                        i[k] = 100
                        
                        for r in range(len(new)): 
                            
                            if new[r][0] + new[r][1] + new[r][2] + new[r][3] + new[r][4] == 500:
                                return num, new[index:index+5]
                            else:
                                for s in range(0,len(new),5):
                                    for col in range(0,5):
                                        if new[s][col] + new[s+1][col] + new[s+2][col] + new[s+3][col] + new[s+4][col] == 500:                                            
                                            return num, new[index:index+5]
                                        else:
                                            pass                          

result = stop()
number = result[0]
win_card = result[1]

flattened = [val for sublist in win_card for val in sublist]
remain = [i for i in flattened if i != 100]
print(f'Result for part 1: {sum(remain) * number}')

