# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 18:00:43 2022

@author: zkoritnik
"""

file = 'aoc_2022_11'
with open(f"C:/Users/zkoritnik/AoC/2022/{file}.txt") as f:
    data = f.read().strip().split('\n\n')

monkeys = []
for group in data:
    lines = group.splitlines()
    monkey = []
    monkey.append(list(map(int, lines[1].split(': ')[1].split(', '))))
    monkey.append(eval('lambda old:' + lines[2].split('=')[1]))
    for l in lines[3:]:
        monkey.append(int(l.split()[-1]))
    monkeys.append(monkey)


monkey_count = [0] * len(monkeys)


for _ in range(20):
    for indx, items in enumerate(monkeys):
        for i in items[0]:
            worry = items[1](i)
            worry_update = worry // 3
            if worry_update % items[2] == 0:
                monkeys[items[3]][0].append(worry_update)
            else:
                monkeys[items[4]][0].append(worry_update)
        # print(items[0])
        monkey_count[indx] += len(items[0])
        items[0] = []

monkey_count.sort()

res = monkey_count[-1] * monkey_count[-2]
print(f'Solution for Part 1: {res}')




