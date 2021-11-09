# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 01:51:17 2021

@author: Haadi
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import math as mt

# Monte Carlo function which returns approximations of pi
def mainonte(n):
        x = np.random.uniform(0,1,n)
        y = np.random.uniform(0,1,n)
        
        mask = [x**2+y**2<1]
        xsub = x[mask]
        ysub = y[mask]
        pi = (4*len(xsub))/n
        
        return pi

# initializing figure and axis
fig = plt.figure()
ax = fig.add_axes([0.0,0.0, 0.8, 0.8])
plt.title("$Monte\ Carlo \  Trials$")
plt.xlabel("$n$")
plt.ylabel("$Expected \ Values $")

# initializing an array of pi values and an array of n values ranging from n=10 to n = 1000
mu = np.full((991), mt.pi)
n = np.arange(10 ,1001,1)

# using the above arrays to plot the mu function
plt.plot(n, mu,  label = "$\mu = \pi$")

# initializing and plotting standard deviations using formulae from part (f)
sigma = ((mt.pi*(4-mt.pi))/n)**0.5

plt.plot(n, (mu+2*sigma),  label = "$ = \mu+2\sigma$")
plt.plot(n, (mu-2*sigma), label = "$ = \mu-2\sigma$")

# initializing specific values of n against which to plot the Monte Carlo Simulation trials

n_list = [10, 20, 50, 100, 200, 400, 600, 800, 1000]

for i in n_list:
    for j in range(1,101): #iterator to run each trial 100 times
        plt.scatter(i, monte(i)) 

# change the limits of the Axes to zoom in:
plt.xlim(1,1000) 
plt.ylim( (1.9,4.5) )
plt.legend()




