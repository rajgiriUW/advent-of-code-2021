# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 22:49:42 2021

@author: Raj
"""

import numpy as np
import pandas as pd
from collections import deque

base = r'C:/Users/Raj/OneDrive/UW Work/Coding and Signal Processing Work/Python/aoc_2021/'
f = open(base + r'12_input.txt')
data = [x.rstrip() for x in f.readlines()]

# Create graph DataFrame

def setupFrame(data):
    left = []
    right = []
    for d in data:
        _l,_r = d.split('-')
        left.append(_l)
        right.append(_r)
    
    paths = pd.DataFrame(index = np.union1d(left, right), 
                         columns=np.union1d(left, right), 
                         data = 0)
    
    for l, r in zip(left, right):
        
        paths[r].loc[l] = 1
        paths[l].loc[r] = 1
        
        paths[r].visited = False
        paths[l].visited = False
        
        paths[r].visits = 0
        paths[l].visits = 0
    
    return paths

def traverseFrame(paths, current, deq):
    

    global totalPaths
    deq.append(current)
    
    # Only big caves can be multiply visited
    if current != current.upper():
        paths[current].visited = True
    
    if current == 'end':
        #If found the end, append a new row to the list and reset the visited Flag

        totalPaths.append(','.join([x for x in deq]))
        paths[current].visited = False
        
    else:
        for nextStep in paths[current][paths[current] == 1].index.values:
            if paths[nextStep].visited == False:
                traverseFrame(paths, nextStep, deq)
        
    deq.pop()
    if current != current.upper():
        paths[current].visited = False

# Part 1
current = 'start'
totalPaths = []
deq = deque()

paths = setupFrame(data)       
traverseFrame(paths, 'start', deq)
print(len(totalPaths))

# Part 2

def checkVisits(paths, node):
    ''' Checks if any other node has been visited twice already'''
    if node == 'start' or node == 'end':
        return False
    
    if paths[node].visits >= 2:
        
        return False
    
    for c in paths.columns:
        
        if c != c.upper(): # only small caves
            if paths[c].visits >= 2 and c != node:
                
                return False
        
    return True

def traverseFramePart2(paths, current, deq):

    global totalPaths
    deq.append(current)
    
    # Only big caves can be multiply visited
    if current != current.upper():
        
        paths[current].visits += 1
        paths[current].visited = True
        
    if current == 'end':
        #If found the end, append a new row to the list and reset the visited Flag

        totalPaths.append(','.join([x for x in deq]))
        paths[current].visits = 0
        paths[current].visited = False
        
    else:
        for nextStep in paths[current][paths[current] == 1].index.values:

            if nextStep != 'start':
                
            # check if unvisited small cave or 
            # if visited but no one else visited twice or 
            # is a big cave
                check = [paths[nextStep].visited == False,
                         checkVisits(paths, nextStep),
                         nextStep == nextStep.upper()]
                if True in check:
                    
                    traverseFramePart2(paths, nextStep, deq)
                    
    deq.pop()
    
    if current != current.upper():
        paths[current].visits -= 1
        
        if paths[current].visits  == 0:
            paths[current].visited = False
    
current = 'start'
totalPaths = []
deq = deque()

paths = setupFrame(data)       
traverseFramePart2(paths, 'start', deq)
print(len(totalPaths))
