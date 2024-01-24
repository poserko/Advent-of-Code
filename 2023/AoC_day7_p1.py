# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 11:33:53 2023

@author: zkoritnik
"""

from collections import Counter

with open("C:/Users/zkoritnik/Skripte/AoC/2023/input/aoc_7.txt", 'r') as f:
    deck = [i.strip().split() for i in f.readlines()]

hands = {"T": "A", "J": "B", "Q": "C", "K": "D", "A": "E"}

def fullhouse(string):
    return 3 in {c: string.count(c) for c in set(string)}.values() and 2 in {c: string.count(c) for c in set(string)}.values()

def three_kind(string):
    return 3 in {c: char.count(c) for c in set(char)}.values() and 1 in {c: char.count(c) for c in set(char)}.values()

def has_two_pairs(string):
    return sum(count // 2 for count in Counter(string).values() if count >= 2) == 2

def one_pair(string):
    counts = Counter(string)
    return sum(count == 2 for count in counts.values()) == 1

def all_characters_distinct(string):
    return len(set(string)) == len(string)

ranking = {
    'Five_kind': [],
    'Four_kind': [],
    'Full_house': [],
    'Three_kind': [],
    'Two_pair': [],
    'One_pair': [],
    'High_card': []    
    }

for char, bid in deck:
    if all(c == char[0] for c in char):
        ranking['Five_kind'].append((char, bid))
    
    elif any(char.count(c) == 4 for c in set(char)):
        ranking['Four_kind'].append((char, bid))
    
    elif fullhouse(char):
        ranking['Full_house'].append((char, bid))
        
    elif three_kind(char):
        ranking['Three_kind'].append((char, bid))
    
    elif has_two_pairs(char):
        ranking['Two_pair'].append((char, bid))
        
    elif one_pair(char):
        ranking['One_pair'].append((char, bid))
        
    elif all_characters_distinct(char):
        ranking['High_card'].append((char, bid))


upd = {}
l = []
for k, v in ranking.items():
    if k not in upd:
        upd[k] = []
    for i in v:
        a = []
        converted_string = ''.join(hands.get(char, char) for char in i[0])
        upd[str(k)].append((i, converted_string))

new = {}
for k, v in upd.items():
    if k not in new:
        new[k] = []
    s = sorted(v, key=lambda x: x[1], reverse=False)
    new[k] = s
        
names = ['Five_kind', 'Four_kind', 'Full_house', 'Three_kind', 'Two_pair', 'One_pair', 'High_card']

score=0
rank = 1
for key in reversed(names):
    for i in new[key]:
        bid = i[0][1]
        score += (int(bid) * rank)
        
        rank += 1
        
print(f'Part 1: {score}')














