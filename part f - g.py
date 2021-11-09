# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 19:03:48 2021

@author: Haadi
"""


import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import math as mt

'''
As n tends to infinity, the value of our approximation comes closer to the value of pi. The number
to the points less than a distance of 1 from the origin form a quarter circle. This proportion of points, which is
the random variable, X, when divided by n gives the proportion of points less than a distance of 1 from the origin. Multiplying
this by 4 gives us the value of pi itself. this is equivilent to runnin a binomial distribution where as the larger the values
of n are, the closer we get to the value of pi. 

Simiarly, the standard deviation is given by the second experssion when the value of mu is input into the population standard 
deviation formula is used.

'''

# initalizing figure and axis
fig = plt.figure()
ax = fig.add_axes([0.0,0.0, 0.8, 0.8])
plt.title("$Monte\ Carlo \  Trials$")
plt.xlabel("$n$")
plt.ylabel("$Expected \ Values$")

# initializing an array of pi values and an array of n values ranging from n=10 to n = 1000
mu = np.full((991), mt.pi)
n = np.arange(10 ,1001,1)

# using the above arrays to plot the mu function
plt.plot(n, mu,  label = "$\mu = \pi$")

# initializing and plotting standard deviations using formulae from part (f)
sigma = ((mt.pi*(4-mt.pi))/n)**0.5

plt.plot(n, (mu+2*sigma),  label = "$ = \mu+2\sigma$")
plt.plot(n, (mu-2*sigma), label = "$ = \mu-2\sigma$")

# change the limits of the Axes to zoom in:
plt.xlim(1,1000) 
plt.ylim( (2,4.5) )
plt.legend()
        

