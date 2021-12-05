# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 22:02:44 2021

@author: Raj
"""

import numpy as np

base = r'C:/Users/Raj/OneDrive/UW Work/Coding and Signal Processing Work/Python/aoc_2021/'
f = open(base + r'05_input.txt')

import numpy as np

data = [x.rstrip() for x in f.readlines()]

coords = []
coordsfull = [] # considering all coordinates, not just horizontal/vertical lines

#Part 1
for d in data:
    
    start, end = d.split('->')
    c1, r1 = [int(x) for x in start.split(',')]
    c2, r2 = [int(x) for x in end.split(',')]
    
    if c1 == c2 or r1 == r2:
        
        coords.append([(c1, r1), (c2, r2)])
        
    coordsfull.append([(c1, r1), (c2, r2)])
    
sz = np.max(np.array(coords)) + 1 # Find largest dimension
grid = np.zeros([sz, sz])

def fill(start, end, grid):
    ''' Fill in the grid with the points noted by start and end. 
    Start and end are coordinates (2-ple)'''
    
    # Passed in: 1 = rows, 0 = cols by their specification
    s = np.sort([start[1], end[1]])
    e = np.sort([start[0], end[0]])
    
    s[1] += 1
    e[1] += 1
    # +1 bc array indexing not endpoint inclusive
    if np.allclose(s[0], s[1] - 1):
        grid[s[0], e[0]:e[1]] += 1
        
    elif np.allclose(e[0], e[1] - 1):
        grid[s[0]:s[1], e[0]] += 1
        
    else: # diagonal fill on unsorted coordinates
    
        row_inc = 1
        col_inc = 1
        
        if start[1] > end[1]:
            row_inc = -1
        if start[0] > end[0]:
            col_inc = -1
        
        for r, c in zip(range(start[1], end[1] + row_inc, row_inc), 
                        range(start[0], end[0] + col_inc, col_inc)):
            grid[r, c] += 1

for c in coords:
    
    fill(c[0], c[1], grid)
    
print('Multiple hits = ', np.where(grid > 1)[0].shape[0])

# Part 2
grid = np.zeros([sz, sz])

for c in coordsfull:
    
    fill(c[0], c[1], grid)
    
print('Multiple hits = ', np.where(grid > 1)[0].shape[0])
