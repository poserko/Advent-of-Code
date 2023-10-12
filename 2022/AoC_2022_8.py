# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 18:00:43 2022

@author: zkoritnik
"""

file = 'aoc_2022_8'
with open(f"C:/Users/zkoritnik/AoC/2022/{file}.txt") as f:
    data = f.readlines()
    data = [i.split() for i in data]
    arr = [list(map(int, str(a))) for i in data for a in i]

visible = (len(arr[0]) - 2)  * 2 + (2 * len(arr))

d = {}
for i in range(1,len(arr)-1):
    for j in range(1,len(arr[i])-1):
        element = arr[i][j]

        is_larger_than_all_above = True
        is_larger_than_all_below = True
        is_larger_than_all_left = True
        is_larger_than_all_right = True
        for k in range(i):
            above_element = arr[k][j]
            # Check if the element is larger than the element above it
            if element <= above_element:
                # The element is not larger than all elements above it, so we can stop the loop
                is_larger_than_all_above = False
                break
        if is_larger_than_all_above:
            d[(i,j, element)] = 1

        for k in range(i + 1, len(arr)):
            below_element = arr[k][j]
            if element <= below_element:
                is_larger_than_all_below = False
                break
        # If the element is larger than all the elements below it, increment the counter
        if is_larger_than_all_below:
            d[(i,j, element)] = 1

        for k in range(j):
            left_element = arr[i][k]
            # Check if the element is larger than the element to the left of it
            if element <= left_element:
                # The element is not larger than all elements to the left of it, so we can stop the loop
                is_larger_than_all_left = False
                break
        # If the element is larger than all the elements to the left of it, increment the counter
        if is_larger_than_all_left:
            d[(i,j, element)] = 1

        for k in range(j + 1, len(arr[i])):
            right_element = arr[i][k]
             # Check if the element is larger than the element to the right of it
            if element <= right_element:
        #         # The element is not larger than all elements to the right of it, so we can stop the loop
                is_larger_than_all_right = False
                break

        if is_larger_than_all_right:
            d[(i,j, element)] = 1

print(f'Solution Part 1: {visible + len(d)}')


up = {}
down = {}
left = {}
right = {}
for i in range(1,len(arr)-1):
    for j in range(1,len(arr[i])-1):
        element = arr[i][j]

        for k in reversed(range(i)):
            above_element = arr[k][j]
            if above_element < element:
                if (i, j, element) not in up:
                    up[(i,j, element)] = 1
                else:
                    up[(i,j, element)] += 1
            elif above_element >= element:
                if (i, j, element) not in up:
                    up[(i,j, element)] = 1
                else:
                    up[(i,j, element)] += 1
                break

        for k in range(i + 1, len(arr)):
            below_element = arr[k][j]
            if below_element < element:
                if (i, j, element) not in down:
                    down[(i,j, element)] = 1
                else:
                    down[(i,j, element)] += 1
            elif below_element >= element:
                if (i, j, element) not in down:
                    down[(i,j, element)] = 1
                else:
                    down[(i,j, element)] += 1
                break

        for k in reversed(range(j)):
            left_element = arr[i][k]
            if left_element < element:
                if (i, j, element) not in left:
                    left[(i,j, element)] = 1
                else:
                    left[(i,j, element)] += 1
            elif left_element >= element:
                if (i, j, element) not in left:
                    left[(i,j, element)] = 1
                else:
                    left[(i,j, element)] += 1
                break

        for k in range(j + 1, len(arr[i])):
            right_element = arr[i][k]
            if right_element < element:
                if (i, j, element) not in right:
                    right[(i,j, element)] = 1
                else:
                    right[(i,j, element)] += 1
            elif right_element >= element:
                if (i, j, element) not in right:
                    right[(i,j, element)] = 1
                else:
                    right[(i,j, element)] += 1
                break

s = set()
for i in range(1, len(arr)-1):
    for j in range(1,len(arr[i])-1):
        prod = up[i,j,arr[i][j]] * down[i,j,arr[i][j]] * left [i,j,arr[i][j]] * right[i,j,arr[i][j]]
        s.add(prod)

print(f'Solution Part 2: {max(s)}')
