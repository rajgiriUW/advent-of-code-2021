# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 22:55:12 2021

@author: Raj
"""

import numpy as np

base = r'C:/Users/Raj/OneDrive/UW Work/Coding and Signal Processing Work/Python/aoc_2021/'

def create_cards():
    f = open(base + r'04_input.txt')
    
    data = f.read().split('\n')
    nums = [int(x) for x in data[0].split(',')]
    del data[0:2]
    
    num_cards = data.count('')
    data = np.array_split(data, num_cards)
    
    for n, d in enumerate(data):
        cards = np.zeros([5,5])
        data[n] = np.vstack(data[n])[:-1]
        for m, r in enumerate(data[n]):
            cards[m] = np.fromstring(str(r)[2:-2], dtype=int, sep = ' ')
        data[n] = cards

    return data, nums

data, nums = create_cards()
no_bingo = True
x = 0
while no_bingo:
    
    
    num = nums[x]
    for n in range(len(data)):
        
        if -1 in np.prod(data[n], axis=0) or -1 in np.prod(data[n], axis=1):
        
            result = np.sum(data[n][np.where(data[n] != -1)])
            print(result, result * nums[x-1], n)
            
            no_bingo = False
            
        else:
            
            data[n][np.where(data[n] == num)] = -1
    
    x += 1
    
# Part 2
# Rerun above
boards = []
lastnum = 0
data, nums = create_cards()

for m, num in enumerate(nums):
    
    for n in range(len(data)):
        
        if n not in boards:
        
            if -1 in np.prod(data[n], axis=0) or -1 in np.prod(data[n], axis=1):
            
                boards.append(n)
                lastnum = nums[m-1] #won on previous loop
                
            else:
                
                data[n][np.where(data[n] == num)] = -1
        
n = boards[-1]
result = np.sum(data[n][np.where(data[n] != -1)])
print(result, result * lastnum, n)
