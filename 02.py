# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 22:57:24 2021

@author: Raj
"""

base = r'C:/Users/Raj/OneDrive/UW Work/Coding and Signal Processing Work/Python/aoc_2021/'
f = open(base + r'02_input.txt')
data = [d.rstrip().split() for d in f.readlines()]
data = [(x[0], int(x[1])) for x in data]

# Part 1
hor = 0
dep = 0

vector = {'up': -1, 'down': 1}
for d, v in data:
    
    if d == 'forward':
        hor += v
    else:
        dep += vector[d]*v
        
print(hor*dep)

# Part 2
aim = 0
hor = 0
dep = 0

vector = {'up': -1, 'down': 1}
for d, v in data:
    
    if d == 'forward':
        hor += v
        dep += aim*v
    else:
        aim += vector[d]*v
        
print(hor*dep)