# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 20:45:08 2022

@author: zkoritnik
"""

with open ("C:/Users/zkoritnik/AoC/aoc12_2020txt.txt") as aoc:
    data = [i.strip() for i in aoc.readlines()]


row = 0
col = 0
x, y = 1, 0

for i in data:
    s, v = i[0], int(i[1:])

    if s == 'N':
        row += v
    elif s == 'S':
        row -= v
    elif s == 'E':
        col += v
    elif s == 'W':
        col -= v
    elif s == 'L':
        if v == 90:
            x, y = -y, x
        elif v == 180:
            x, y = -x, -y
        elif v == 270:
            x, y = y, -x
    elif s == 'R':
        if v == 90:
            x, y = y, -x
        elif v == 180:
            x, y = -x, -y
        elif v == 270:
            x, y = -y, x
    elif s == 'F':
        col += x * v
        row += y * v

print(abs(col) +  abs(row))

waypoint_row = 1
waypoint_col = 10
row, col = 0, 0
x, y = 1, 0

for i in data:
    char, value = i[0], int(i[1:])
 #print(char, value)
    if char == 'N':
        waypoint_row += value
    elif char == 'S':
        waypoint_row -= value
    elif char == 'E':
        waypoint_col += value
    elif char == 'W':
        waypoint_col -= value
    elif char == 'R':
        if value == 90:
            waypoint_col, waypoint_row = waypoint_row, -waypoint_col
        elif value == 180:
            waypoint_col = -waypoint_col
            waypoint_row = -waypoint_row
        elif value == 270:
            waypoint_col, waypoint_row = -waypoint_row, waypoint_col
    elif char == 'L':
        if value == 90:
            waypoint_col, waypoint_row = -waypoint_row, waypoint_col
        elif value == 180:
            waypoint_col = -waypoint_col
            waypoint_row = -waypoint_row
        elif value == 270:
            waypoint_col, waypoint_row = waypoint_row, -waypoint_col
    elif char == 'F':
        row += waypoint_row * value
        col += waypoint_col * value

print(abs(row) + abs(col))

