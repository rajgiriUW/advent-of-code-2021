# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 09:50:23 2021

@author: Raj
"""

import numpy as np
from collections import deque

base = r'C:/Users/Raj/OneDrive/UW Work/Coding and Signal Processing Work/Python/aoc_2021/'
f = open(base + r'10_input.txt')
data = [x.rstrip() for x in f.readlines()]

scores = {')': 3, 
          ']': 57,
          '}': 1197, 
          '>': 25137}

lefts = ['(', '[', '{', '<']
rights = [')', ']', '}', '>']
pairs = dict(zip(lefts,rights))

totalScore = 0
fixedData = [x for x in data] # For Part 2

for code in data:
    
    deq = deque(code)
    stack = deque()
    
    notFound = True
    while any(deq) and notFound:
        
        char = deq.popleft()
        if char in lefts:
            
            stack.append(char)
        
        elif char in rights:
            
            if char != pairs[stack.pop()]: # not matching most recent left
            
                totalScore += scores[char]
                notFound = False
                fixedData.remove(code)
                
print(totalScore)

#Part 2
completedData = []
totalScore = 0
totalScores = []

scoresPart2 = {')': 1, 
               ']': 2,
               '}': 3, 
               '>': 4}

for code in fixedData:
    
    totalScore = 0
    deq = deque(code)
    stack = deque()
    
    while any(deq):
        
        char = deq.popleft()
        if char in lefts:
            
            stack.append(char)
        
        elif char in rights:
            
            if char == pairs[stack[-1]]: # only pop off stack if matching
                
                stack.pop()

    deq = deque(code)
    while any(stack): # append remaining
    
        totalScore *= 5
        char = pairs[stack.pop()]
        deq.append(char)
        totalScore += scoresPart2[char]
    
    totalScores.append(totalScore)
    st = ''.join(deq)
    completedData.append(st)
    
totalScores = sorted(totalScores)
print(np.median((np.array(totalScores))))
