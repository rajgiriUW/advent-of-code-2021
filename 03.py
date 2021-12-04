# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 12:12:52 2021

@author: raj
"""

base = r'C:/Users/Raj/OneDrive/UW Work/Coding and Signal Processing Work/Python/aoc_2021/'
f = open(base + r'03_input.txt')
data = [d.rstrip() for d in f.readlines()]

import numpy as np

# Create a matrix
img = np.zeros([len(data), len(data[0])])
for m, d in enumerate(data):
    for n, x in enumerate(d):
        img[m, n] = int(x)

rows, cols = img.shape
gamma = [int(sum(img[:,x]) > int(rows/2)) for x in range(cols)]
epsilon = [int(not x) for x in gamma]

gamma_b = int(''.join([str(x) for x in gamma]), 2)
epsilon_b = int(''.join([str(x) for x in epsilon]), 2)

print(gamma_b * epsilon_b)

# Part 2
o2_arr = np.arange(rows)
co2_arr = np.arange(rows)
for x in range(cols):
    
    if len(o2_arr) > 1:
        r, c = img[o2_arr].shape
        val = sum(img[o2_arr, x]) 
        point = int(val >= r/2)
        o2_arr = np.intersect1d(np.where(img[:, x] == point)[0], o2_arr)
    
    if len(co2_arr) > 1:
        r, c = img[co2_arr].shape
        val = sum(img[co2_arr, x]) 
        point = int(val < r/2)
        co2_arr = np.intersect1d(np.where(img[:, x] == point)[0], co2_arr)

o2_b = int(''.join([str(int(x)) for x in img[o2_arr][0]]), 2)
co2_b = int(''.join([str(int(x)) for x in img[co2_arr][0]]), 2)

print(o2_b * co2_b)
        
