# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 19:21:08 2021

@author: Raj
"""

import numpy as np
base = r'C:/Users/Raj/OneDrive/UW Work/Coding and Signal Processing Work/Python/aoc_2021/'
f = open(base + r'17_input.txt')
data = f.read().split('\n')[:-1]

# Parse the data, so clunky
datax = data[0].split('x')[-1].split('y')[0].split('=')[1]
datay = data[0].split('y')[-1].split('=')[1]
xrange = sorted([int(r.split(',')[0]) for r in datax.split('..')])
yrange = sorted([int(x) for x in datay.split('..')])

target_cols = np.arange(xrange[0], xrange[1] + 1)
target_rows = np.arange(yrange[0], yrange[1] + 1)

# Part 1

def step(x, y, vel_x, vel_y, acc_x=-1, acc_y = -1):
    ''' 
    Calculates new position from original x, y

    vel_x and vel_y are velocities in x and y
    acc_x and acc_y are acceleration in x and y
    
    x and y are positions in x and y
    '''
    
    x += vel_x
    y += vel_y
    
    vel_x += acc_x
    vel_x = max(vel_x, 0) # velocity in x is never negative
    
    vel_y += acc_y
    
    return x, y, vel_x, vel_y

def fire_cannon(start_pos, start_vel, target_rows, target_cols, start_acc = [-1, -1]):
    '''
    start_pos : tuple
        Initial position
    start_vel : tuple
        Initial velocity
    target_rows : array or list
        Values defining the target (y direction, rows)
    target_cols : array or list
        Values defining the target (x direction, cols)
    start_acce : typle
        Initial acceleration
        
    Returns
    (x, y) : tuple
        final position
    (vel_x, vel_y) : tuple
        final velocity
    y_max : int
        The apex of the cannon position
    in_target : bool
        Did cannon land in the target
    missed_target : array of bool
        Did cannon miss the target in [missed_x, missed_y]. Should be !in_target 
    positions : list
        List of positions during firing, of size 2 with each containing an arrayu
        positions[0] = x positions, positions[1] = y positions
        Can subsequently graph positions[1] vs positions[0]
    '''
    x, y = start_pos
    vel_x, vel_y = start_vel
    acc_x, acc_y = start_acc
    
    y_max = 0
    in_target = False
    missed_target = False
    positions = [[x],[y]]
    
    while not in_target and not missed_target:
    
        x, y, vel_x, vel_y = step(x, y, vel_x, vel_y, acc_x, acc_y)
        
        if y > y_max:
            
            y_max = y
        
        if x in target_cols and y in target_rows:
            in_target = True
        
        elif x > target_cols[-1] or y < target_rows[0]:
            missed_target = True
        
        positions[0].append(x)
        positions[1].append(y)
        
    return (x,y), (vel_x, vel_y), y_max, in_target, missed_target, positions

def test_velocities(start_pos, vel_x, vel_y, target_rows, target_cols):
    '''
    vel_x and vel_y are ranges
    
    Returns:
        
        y_max : int
            Max y position
        best_vel : tuple
            The ideal velocity
        hits : int
            The total number of times the cannon hits the target
    '''
    y_max = 0
    best_vel = [0, 0]
    hits = 0
    for vx in vel_x:
        
        for vy in vel_y:
            
            _, _, _ymx, in_target, missed_target , _ = fire_cannon(start_pos, (vx, vy), 
                                                                   target_rows, target_cols)
            if in_target:
            
                hits += 1
                if _ymx > y_max:
            
                    y_max = _ymx
                    best_vel = [vx, vy]
                
    return y_max, best_vel, hits

# Part 1 and 2
vel_x = np.arange(0, 500)
vel_y = np.arange(-500, 500)
start_pos = [0, 0]
#start_vel = (6, 9)

y_max, final_vel, hits = test_velocities(start_pos, vel_x, vel_y, target_rows, target_cols)

print('Y max =', y_max)
print('Total hits = ', hits)

#%% Makes a map for fun
import matplotlib.pyplot as plt

xr, yr = np.meshgrid(vel_x, vel_y)
vel_x = np.arange(0, 500)
vel_y = np.arange(-500, 500)
pos_map = np.zeros([len(vel_y), len(vel_x)])
hit_map = np.zeros([len(vel_y), len(vel_x)])
for n, vx in enumerate(vel_x):
    
    for m, vy in enumerate(vel_y):
        
        _, _, _ymx, in_target, missed_target , _ = fire_cannon(start_pos, (vx, vy), 
                                                               target_rows, target_cols)

        if in_target:
            
            hit_map[m,n] = 1
        pos_map[m, n] = _ymx
        
plt.figure()
plt.imshow(hit_map, extent=[vel_x[0], vel_x[-1], vel_y[0], vel_y[-1]])
plt.figure()
plt.imshow(pos_map, extent=[vel_x[0], vel_x[-1], vel_y[0], vel_y[-1]])
