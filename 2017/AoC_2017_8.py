# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 18:00:43 2022

@author: zkoritnik
"""

FILE = 'aoc_2017_8'
with open(f"C:/Users/zkoritnik/AoC/2017/{FILE}.txt") as f:
    data = f.readlines()
    data = [i.split() for i in data]

def modify(register, direction, value):
    if direction == 'inc':
        register += value
    elif direction == 'dec':
        register -= value
    else:
        print('Error')
    return register

def changeRegister(register, direction, value, testReg, status, valueCondition):
    if status == '>':
        if testReg > valueCondition:
            register = modify(register, direction, value)
    elif status == '<':
        if testReg < valueCondition:
            register = modify(register, direction, value)
    elif status == '>=':
        if testReg >= valueCondition:
            register = modify(register, direction, value)
    elif status == '<=':
        if testReg <= valueCondition:
            register = modify(register, direction, value)
    elif status == '==':
        if testReg == valueCondition:
            register = modify(register, direction, value)
    elif status == '!=':
        if testReg != valueCondition:
            register = modify(register, direction, value)
    else:
        print('False condition')
    return register

dictiReg = {}
highest = set()

for i in data:
    if i[0] not in dictiReg:
        dictiReg[i[0]] = 0
    if i[4] not in dictiReg:
        dictiReg[i[4]] = 0
    dictiReg[i[0]] = changeRegister(dictiReg[i[0]], i[1], int(i[2]), dictiReg[i[4]], i[5], int(i[6]))
    highest.add(dictiReg[i[0]])
print(f'Solution for Part 1: {max(dictiReg.values())}')
print(f'Solution for Part 2: {max(highest)}')
