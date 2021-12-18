# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 20:48:37 2021

@author: raj
"""

import numpy as np

base = r'C:/Users/Raj/OneDrive/UW Work/Coding and Signal Processing Work/Python/aoc_2021/'
f = open(base + r'14_input.txt')
data = f.read().split('\n')[:-1]

template = data[0]
result = template
rules = {}
for d in data[2:]:
    r, c = d.split('->')
    r = r.strip()
    c = c.strip()
    rules[r] = c
    #rules[r[::-1]] = c

def apply_step(result, rules):
    
    new_result = []
    for n, ch in enumerate(result[:-1]):
        
        new_result.append(ch)

        if result[n:n+2] in rules:
            new_result.append(rules[result[n:n+2]])
            
    new_result.append(result[-1])
    
    return ''.join(new_result)

def apply_steps(result, rules, steps=1):
    
    for s in range(steps):
        
        result = apply_step(result, rules)
    
    return result

def count_letters(result):
    
    alphas = {}
    for r in result:
        
        if r in alphas:
            alphas[r] += 1
        else:
            alphas[r] = 1
    
    return alphas

# Part 1
steps = 10
new_result = apply_steps(result, rules, steps)
alphas = count_letters(new_result) 
print('Difference from most to least:', max(alphas.values()) - min(alphas.values()))

# Part 2
# Need to count pairs and increment that way, rather than just letters

def create_pairs(rules, start):
    
    pairs = {}
    for r in rules:
        pairs[r] = 0

    _letters = np.union1d(np.unique(np.fromiter(start, '<U100')), 
                         np.unique(np.fromiter(rules.values(), '<U100')))
    letters = {}
    for a in _letters:
        letters[a] = 0
        
    for n, s in enumerate(start[:-1]):
        pairs[start[n:n+2]] += 1
        letters[s] += 1    
        
    letters[start[-1]] += 1

    return pairs, letters

def apply_step_pairs(pairs, letters, rules):
    
    new_pairs = dict(pairs)
    for k, v in pairs.items():
        
        l = k[0]
        r = k[1]
        
        lkey = ''.join([l,rules[k]])
        rkey = ''.join([rules[k], r])
        
        new_pairs[lkey] += v
        new_pairs[rkey] += v
        new_pairs[k] -= v
        
        letters[rules[k]] += v

    return new_pairs, letters

def apply_steps_pairs(pairs, letters, rules, steps=1):
    
    for s in range(steps):

        pairs, letters = apply_step_pairs(pairs, letters, rules)
    
    return pairs, letters

steps = 40
pairs, letters = create_pairs(rules,result)
new_pairs, new_letters = apply_steps_pairs(pairs, letters, rules, steps)
print('Difference from most to least:', max(new_letters.values()) - min(new_letters.values()))
