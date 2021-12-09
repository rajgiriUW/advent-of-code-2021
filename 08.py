# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 21:15:24 2021

@author: Raj
"""
import numpy as np

base = r'C:/Users/Raj/OneDrive/UW Work/Coding and Signal Processing Work/Python/aoc_2021/'
f = open(base + r'08_input.txt')
data = [x.rstrip() for x in f.readlines()]

codes = [d.split('|')[0].rstrip() for d in data]
outputs = [d.split('|')[1].strip() for d in data]

nums = np.zeros(10)
digits = {2:1, 3:7, 4:4, 5:[2,3,5], 6:[0, 6,9], 7:8}
for o in outputs:
    
    vals = o.split(' ')
    digits_to_check = [1,4,7,8]
    for v in vals:
        
        if digits[len(v)] in digits_to_check:
            
            nums[digits[len(v)]] += 1
            
print(sum(nums))

#Part 2
import re

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

sevensegment = {'abcefg':0, 'cf': 1, 'acdeg': 2, 'acdfg':3,'bcdf':4,
                'abdfg':5, 'abdefg':6, 'acf':7, 'abcdefg':8, 'abcdfg':9}

def find_digits(code_array):
    
    digits = {}
    counts = {}

    for l in letters:
        
        counts[l] = len(re.findall(l, code_array))
    
    # Locate the A
    vals = np.array(code_array.split(' '))
    lens = np.array([len(x) for x in vals])
    
    _7 = vals[np.where(lens == 3)[0]]
    _1 = vals[np.where(lens == 2)[0]]
        
    for s in _7[0]:
        
        if s not in _1[0]:
            
            digits[s] = 'a'

    for ct, v in counts.items():
        
        if v == 4:
            
            digits[ct] = 'e'
        
        elif v == 6:
            
            digits[ct] = 'b'
        
        elif v == 9:
            
            digits[ct] = 'f'

        elif v == 8:
            
            if ct not in digits:
                
                digits[ct] = 'c'
                
    for l in np.where(lens == 4)[0]:
        
        for let in vals[l]:
            
            if let not in digits:
                
                digits[let] = 'd'
    
    for l in letters:
        
        if l not in digits:
            
            digits[l] = 'g'
            
    return digits

output_total = 0
for c, o  in zip(codes, outputs):

    digits = find_digits(c)
    
    vals = np.array(c.split(' '))
    

         
    # Replace the output letters
    new_o = []
    for char in o:
        
        if not char.isspace():
            new_o.append(digits[char])
        else:
            new_o.append(' ')
        
    outnums = o.split(' ')
    new_o = ''.join(new_o)
    
    for n, v in enumerate(new_o.split(' ')):
        
        outnums[n] = ''.join(sorted(v))
    
    output_total += 1000*sevensegment[outnums[0]]  \
                    + 100*sevensegment[outnums[1]] \
                    + 10*sevensegment[outnums[2]] \
                    + sevensegment[outnums[3]]
          
            
            
                