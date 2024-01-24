# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 10:18:44 2023

@author: zkoritnik
"""

with open("C:/Users/zkoritnik/Skripte/AoC/2023/input/aoc_4.txt", 'r') as f:
    cards = [i.strip() for i in f.readlines()]
    
count = 0
track = {}
for key, line in enumerate(cards, start=1):
    wins = set(int(i) for i in line.strip().split(':')[1].split('|')[0].strip().split())
    have= set(int(i) for i in line.split('|')[1].strip().split())
    
    winners = have.intersection(wins)
    if winners:
        count += pow(2, len(winners)-1)

    if key not in track:
        track[key] = 1
    for copy in range(key+1, len(winners)+key+1):
        track[copy] = track.get(copy, 1) + track[key]
        
print(f'Part 1: {count}')
print(f'Part 2: {sum(track.values())}')
