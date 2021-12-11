# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 10:51:32 2021

@author: Raj
"""


import numpy as np

base = r'C:/Users/Raj/OneDrive/UW Work/Coding and Signal Processing Work/Python/aoc_2021/'
f = open(base + r'11_input.txt')
data = [x.rstrip() for x in f.readlines()]

# Create a numpy matrix
octopi = np.zeros([len(data[0]), len(data)])
for n, d in enumerate(data):
    
    arr = np.fromiter(d, dtype='<U100')
    octopi[n,:] = np.array([x for x in arr])
octopi = octopi.astype(int)
    
def flash(octopi):
    '''
    Determines flashes in an octopi array
    
    Algorithm
        * Increment the array
        * Find all > 9
        * Save these pixels to a mask array
        * All adjacent pixels in octopus += 1
        * All octopi array pixels in mask array set to 0 (have flashed)
        * Continue until no octopi pixels > 9
    
    Parameters:
        octopi : numpy.ndArray
            input octopus array of floats or ints
    
    Returns:
        octopi : numpy.ndarray
            Modified octopus array
        totalFlashes : int
            The total times octopi were > 9 
    '''
    
    totalFlashes = 0
    
    octopi = np.pad(octopi, 1, constant_values=-999) # edge effects
    flashedMask = np.zeros(octopi.shape)
    
    # Find all flashes
    octopi += 1
    flashes = np.where(octopi > 9)
    while (any(flashes[0])): 
    
        totalFlashes += len(flashes[0])
        
        for r,c in zip(flashes[0], flashes[1]):
            
            flashedMask[r,c] = 1
            octopi[r-1:r+2, c-1:c+2] += 1
            
        octopi[np.where(flashedMask == 1)] = 0
        flashes = np.where(octopi > 9)

    octopi = octopi[1:-1, 1:-1] # remove padding
    
    return octopi, totalFlashes

def stepFlash(octopi, steps=1):
    '''
    Returns the octopus array after a number of steps
    
    Parameters:
        octopi : numpy.ndArray
            input octopus array of floats or ints
        steps : int or float
            Number of steps to cycle the octopi array
            Will be forced to an int
            
    Returns:
        octopi : numpy.ndArray
            Modified octopus array after "steps" number of steps
        totalFlashes: int
            The total times octopi were > 9 after "steps" number of steps
    '''
    
    totalFlashes = 0
    
    for i in range(int(steps)):
        octopi, _t = flash(octopi)
        totalFlashes += _t
    
    return octopi, totalFlashes

# Part 1
newOctopi, totalFlashes = stepFlash(octopi, steps=100)
print(totalFlashes)


# Part 2
sync = 0

def synced(octopi):
    '''
    Determines when the octopi array is all the same
    
    First checks if the total sum is in the value of 1 to 9 x octopi array size
    
    If it is, double checks the first row is the same in case the sum just 
    happens to equal exactly one of the above.
    
    Parameters:
        octopi : numpy.ndArray
            input octopus array of floats or ints
    Returns
        bool: 
            if all the same value (True), else False
    
    '''
    sums = np.arange(10)*octopi.shape[0]*octopi.shape[1] 
    if np.sum(octopi) in sums:
        
        # Double check first row all the same in unlikely case the sum
        # Exactly matches a square
        if np.all(octopi[0,:] == octopi[0,0]): 
            
            return True
        
    return False

while not synced(octopi):
    
    sync += 1
    octopi, totalFlashes = stepFlash(octopi, steps=1)
    
print(sync)

#%% Animation
import matplotlib.pyplot as plt
import imageio 
import seaborn_image as isns

# matplotlib animation wasn't working
fig, ax = plt.subplots(facecolor='white', figsize=(3,3))
def aniStepFlash(octopi, ax, steps=1, cmap='Spectral_r', 
                 repeatDelay = 3, skip=25, duration=0.2,
                 fname='11_octopi.gif'):
    '''
    Returns the octopus array after a number of steps
    
    Parameters:
        octopi : numpy.ndArray
            input octopus array of floats or ints
        steps : int or float
            Number of steps to cycle the octopi array
            Will be forced to an int
        ax : matplotlib.axes._subplots.AxesSubplot
            handle to the matplotlib Axis object
        cmap : str
            Any matplotlib valid colormap
        repeatDelay : int
            Adds a number of frames at the end to delay the loop
        skip : int
            Number of steps to skip between saved animated frames
        duration : float
            Seconds to wait between frames
        fname : str
            Filename
            
    Returns:
        octopi : numpy.ndArray
            Modified octopus array after "steps" number of steps
        totalFlashes: int
            The total times octopi were > 9 after "steps" number of steps
    
    Returns:
        octopi : numpy.ndarray
            Modified octopus array
        totalFlashes : int
            The total times octopi were > 9 
        ims : list
            The list of all resulting plots per loop, for us in matplotlib.animation
    '''    

    totalFlashes = 0
    skip = int(skip)
    with imageio.get_writer(fname, mode='I', duration=duration) as writer:

        for i in range(int(steps)):
            
            if i % skip == 0:
                ax.set_title('Frame ' + str(i))
                im0 = isns.imshow(ax=ax, data=octopi, 
                                  cmap=cmap, 
                                  vmin=-1, vmax=9) # for visualization
            
                print('Saving frame', i)
                plt.savefig('_temp.png')
                img = imageio.imread('_temp.png')
                writer.append_data(img)
            
            octopi, _t = flash(octopi)
            totalFlashes += _t
    
        #artificially add a repeat delay of 10 frames
        ax.set_title('Frame ' + str(i))
        im0 = isns.imshow(ax=ax, data=octopi, 
                          cmap=cmap, 
                          vmin=-1, vmax=9) # for visualization
        plt.savefig('_temp.png')
        img = imageio.imread('_temp.png')
        print('Saving last frame', i)
        for i in range(int(repeatDelay)):
            writer.append_data(img)        
    
    return octopi, totalFlashes

_, _ = aniStepFlash(octopi, ax=ax, steps=268, cmap='viridis', skip=10, duration=0.5)