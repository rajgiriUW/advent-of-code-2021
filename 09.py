# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 17:22:03 2021

@author: raj
"""

import numpy as np

base = r'C:/Users/Raj/OneDrive/UW Work/Coding and Signal Processing Work/Python/aoc_2021/'
f = open(base + r'09_input.txt')
data = [x.rstrip() for x in f.readlines()]

volcano = np.zeros([len(data[0]), len(data)])

for n, d in enumerate(data):
    
    arr = np.fromiter(d, dtype='<U100')
    volcano[n,:] = np.array([int(x) for x in arr])
    
# Algorithm is substract 4 shifted arrays, find points where it's negative 4 times.
volc_pad = np.pad(volcano, 1, constant_values=99) ## 99 always greater

lr = volc_pad - np.roll(volc_pad, 1, axis=0)
rl = volc_pad - np.roll(volc_pad, -1, axis=0)
ud = volc_pad - np.roll(volc_pad, 1, axis=1)
du = volc_pad - np.roll(volc_pad, -1, axis=1)

# Find interscetion of ravel (flatten) then unravel
overlap = np.intersect1d(np.where(np.ravel(lr) < 0), np.where(np.ravel(rl) < 0))
overlap = np.intersect1d(overlap, np.where(np.ravel(ud) < 0))
overlap = np.intersect1d(overlap, np.where(np.ravel(du) < 0))

vals = np.unravel_index(overlap, volc_pad.shape)

risk = np.sum(volc_pad[vals] + 1)

print(risk)

# Part 2
# Find the areas of all regions bounded by 9s

mask = np.zeros(volcano.shape)
mask[np.where(volcano == 9)] = 9
mask = np.pad(mask, 1, constant_values = 9)

# Implement a paint bucket per pixel; used Wikipedia for the algorithm...
area = 0

def fill(arr, r, c):
    
    if arr[r,c] == 9:
        
        return
    
    elif arr[r, c] == 1:
        

        return

    elif arr[r, c] == 0:
        
        arr[r, c] = 1
        global area 
        area += 1
        
        fill(arr, r-1, c)
        fill(arr, r+1, c)
        fill(arr, r, c-1)
        fill(arr, r, c+1)
        fill(arr, r, c)
        
        return

areas = []

for r in range(mask.shape[0]):
    
    for c in range(mask.shape[1]):
        
        global area 
        area = 0
        _mask = mask[:]
        fill(_mask, r, c)
        
        areas.append(area)

areas = np.array(areas)
areas = sorted(areas[np.where(areas > 0)]) 

print(np.prod(areas[-3:])) # product of three highest basins

