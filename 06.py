# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 21:15:15 2021

@author: Raj
"""

import numpy as np
import pandas as pd

def load_fish():
    base = r'C:/Users/Raj/OneDrive/UW Work/Coding and Signal Processing Work/Python/aoc_2021/'
    f = open(base + r'06_input.txt')
    fish = np.array([int(x) for x in f.read().rstrip().split(',')])
    fish_frame = pd.DataFrame(columns=(0,1,2,3,4,5,6,7,8), index = [0])
    for x in range(9):
        fish_frame[x] = len(np.where(fish == x)[0])
    return fish, fish_frame

def grow_in_place(df):
    
    _df = df.copy(deep=True)
    
    for x in range(1,9): # all fish lose a day
        df[x-1] += _df[x]
        df[x] -= _df[x]
    
    df[6] += _df[0] # all 0s become 6s
    df[0] -= _df[0]
    
    df[8] += _df[0] # all 0s become new 8s
    
    return df

days = 80
fish, fish_frame = load_fish()

for d in range(days):
    
    fish = grow_in_place(fish_frame)

print(sum(fish_frame.loc[0]))

# Part 2
days = 256
fish, fish_frame = load_fish()

for d in range(days):
    grow_in_place(fish_frame)
    
print(sum(fish_frame.loc[0]))

# Part 1 old
def grow(num):
    
    num -= 1
    newfish = np.where(num == -1)[0]
    if newfish.any():
        num = np.append(num, 8*np.ones(len(newfish)))
    
    num[np.where(num == -1)] = 6
    
    return num