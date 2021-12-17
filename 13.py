# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 18:59:42 2021

@author: raj
"""

import numpy as np

base = r'C:/Users/Raj/OneDrive/UW Work/Coding and Signal Processing Work/Python/aoc_2021/'
f = open(base + r'13_input.txt')
data =f.read().split('\n')[:-1]

folds = []
coords = []
for d in data:
    if 'fold' not in d and any(d):
        
        r, c = d.split(',')
        coords.append((int(r), int(c)))
        
    elif any(d):
        
        folds.append(d)

# Create the grid
def load_grid(coords):
    _coords = np.array(coords)
    coords = (_coords[:,1], _coords[:,0])
    grid = np.zeros([_coords[:,1].max()+1, _coords[:,0].max()+1], dtype='bool')
    grid[coords] = True
    
    return grid

# Part 1 - one fold

grid = load_grid(coords)
def parse_fold(line):
    
    axis, val = line.split('=')
    axis = axis[-1]
    val = int(val)
    
    return axis, val

def fold(grid, line):
    
    axis, val = parse_fold(line)
    
    if axis == 'x': # flip over a vertical line
        
        subgrid = grid[:, val+1:]
        c = subgrid.shape[1]
        grid[:, val-c:val] += np.fliplr(subgrid)
        
        return grid[:, :val]
    
    else: # flip over a horizontal line
        
        subgrid = grid[val+1:, :]
        r = subgrid.shape[0]
        grid[val-r:val, :] += np.flipud(subgrid)
        
        return grid[:val, :]
    
grid = fold(grid, folds[0])

print('Dots = ', len(np.where(grid==True)[0]))

# Part 2 - all folds, find letter
grid = load_grid(coords)

for f in folds:
    grid = fold(grid, f)
    
import matplotlib.pyplot as plt
plt.imshow(grid, 'inferno')