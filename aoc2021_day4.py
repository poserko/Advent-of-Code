# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 18:27:28 2021

@author: Maruša Pungartnik
"""

import os

os.chdir(r'C:\Users\Maruša Pungartnik\Desktop\Žiga')

with open('AoC.txt') as aoc:
    data=aoc.readlines()
    data=[i.split('\n')[0] for i in data]