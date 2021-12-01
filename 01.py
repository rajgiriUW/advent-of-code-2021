# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 21:00:46 2021

@author: Raj
"""

import numpy as np

base = r'C:/Users/Raj/OneDrive/UW Work/Coding and Signal Processing Work/Python/aoc_2021/'
f = open(base + r'01_input.txt')
data = [int(x) for x in f.read().split('\n')[:-1]]

# Part 1
diff = np.diff(data)
print(sum(diff > 0)) 

# Part 2

# Things I learned; numerical error in fftconvolve prevents "exact" 0
from scipy.signal import oaconvolve

data_conv = oaconvolve(data, np.array([1,1,1]))
diff = np.diff(data_conv[2:-2])
print(sum(diff > 0))

# Manual method
c = 0
for n in range(2, len(data)-1):
    
    s = sum(data[n-2:n+1])
    t = sum(data[n-1:n+2])
    
    if t > s:
        c += 1

# investigating fftconvolve
from scipy.signal import fftconvolve

data_conv_fft = fftconvolve(data, np.array([1,1,1]))
diff_fft = np.round(np.diff(data_conv_fft[2:-2]), 0) # forces numerically close to 0s
print(sum(diff_fft > 0))
