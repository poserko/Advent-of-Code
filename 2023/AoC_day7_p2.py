# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 11:33:53 2023

@author: zkoritnik
"""

import itertools
from collections import Counter

with open("C:/Users/zkoritnik/Skripte/AoC/2023/input/aoc_7.txt", 'r') as f:
    deck = [i.strip().split() for i in f.readlines()]


hands_j = {"T": "A", "Q": "C", "K": "D", "A": "E"}

hands = {"T": "A", "J": ".", "Q": "C", "K": "D", "A": "E"}

def fullhouse(string):
    return 3 in {c: string.count(c) for c in set(string)}.values() and 2 in {c: string.count(c) for c in set(string)}.values()

def three_kind(string):
    return 3 in {c: string.count(c) for c in set(string)}.values() and 1 in {c: string.count(c) for c in set(string)}.values()

def has_two_pairs(string):
    return sum(count // 2 for count in Counter(string).values() if count >= 2) == 2

def one_pair(string):
    counts = Counter(string)
    return sum(count == 2 for count in counts.values()) == 1


def all_characters_distinct(string):
    return len(set(string)) == len(string)

def generate_combinations(hand):
    joker_replacements = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']
    combinations = []

    # Find the indices of 'J' in the hand
    j_indices = [i for i, char in enumerate(hand) if char == 'J']

    # Generate all possible combinations by replacing 'J'
    for replacement_combination in itertools.product(joker_replacements, repeat=len(j_indices)):
        current_combination = list(hand)
        for index, replacement in zip(j_indices, replacement_combination):
            current_combination[index] = replacement
        combinations.append(''.join(current_combination))

    return combinations


def calssify(char):
    if all(c == char[0] for c in char):
        return 'Five_kind'
    
    elif any(char.count(c) == 4 for c in set(char)):
        return 'Four_kind'
    
    elif fullhouse(char):
        return 'Full_house'
        
    elif three_kind(char):
        return 'Three_kind'
    
    elif has_two_pairs(char):
        return 'Two_pair'
        
    elif one_pair(char):
        return 'One_pair'

    elif all_characters_distinct(char):
        return 'High_card'

# def find_key(combinations, original_hand):
#     global a
#     a = []
#     for i in combinations:
#         converted_string = ''.join(hands_j.get(char, char) for char in i)
#         a.append((original_hand, i, converted_string)) 
#         return a

def clas(list_of_hands):
    types = {
        'Five_kind': [],
        'Four_kind': [],
        'Full_house': [],
        'Three_kind': [],
        'Two_pair': [],
        'One_pair': [],
        'High_card': []    
        }
    
    for a,b,c in list_of_hands:
        cl = calssify(b)
        types[cl].append(a)
        return types


ranking = {
    'Five_kind': [],
    'Four_kind': [],
    'Full_house': [],
    'Three_kind': [],
    'Two_pair': [],
    'One_pair': [],
    'High_card': []    
    }


last = {}
for char, bid in deck:
    last = {}
    if 'J' in char:

        # print(char)
        
        all_combinations = generate_combinations(char)
        
        a = []
        for i in all_combinations:
            converted_string = ''.join(hands_j.get(char, char) for char in i)
            a.append(((char, bid), i, converted_string))
        
        
        types = {
            'Five_kind': [],
            'Four_kind': [],
            'Full_house': [],
            'Three_kind': [],
            'Two_pair': [],
            'One_pair': [],
            'High_card': []    
            }
        
        for a,b,c in a:
            cl = calssify(b)
            types[cl].append(a)
            
      
        
        names = ['Five_kind', 'Four_kind', 'Full_house', 'Three_kind', 'Two_pair', 'One_pair', 'High_card']
        for name in names:
            if name in types and types.get(name):
                ranking[name].append(types.get(name)[0])
                break
        
    else:
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
        print(i[0][0], rank)
        bid = i[0][1]
        score += (int(bid) * rank)
        
        rank += 1
        
print(f'Part 2: {score}')














