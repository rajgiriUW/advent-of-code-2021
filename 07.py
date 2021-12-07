# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 20:48:53 2021

@author: Raj
"""
import numpy as np

base = r'C:/Users/Raj/OneDrive/UW Work/Coding and Signal Processing Work/Python/aoc_2021/'
f = open(base + r'07_input.txt')
crabs = np.array([int(x) for x in f.read().rstrip().split(',')])

# Part 1: could tell by looking at the list that median is the best
print(sum(np.abs(crabs - np.median(crabs))))

# Part 2
def sum_to_end(num):
    return sum(np.arange(num+1))

# The answer is on either side of the mean
mn = int(np.floor(crabs.mean()))
mx = int(np.ceil(crabs.mean()))

fuel = [sum(list(map(sum_to_end, np.abs(crabs - x)))) for x in [mn, mx]]
print(min(fuel))
