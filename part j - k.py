# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 11:02:49 2021

@author: Haadi
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import math as mt

# Monte Carlo function which returns approximations of pi
def monte(n):
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
plt.xscale('log', basex = 10)
plt.title("$Monte\ Carlo \  Trials$")
plt.xlabel("$n$")
plt.ylabel("$Expected \ Values$")

# initializing an array of pi values and an array of n values ranging from n=10 to n = 1000
mu = np.full((1000), mt.pi)
n = np.linspace(10, 10**8, 1000)

# initializing specific values of n against which to plot the Monte Carlo Simulation trials
n_list = [10, 20, 50, 100, 200, 400, 700, 1200, 3000, 10000, 10**5, 10**6]
avgvalues = [] # empty list to store average values of each Monte Carlo simulation

for i in n_list:
    
    simvalues = [] # empty list to store the values of each Monte Carlo simulation
    for j in range (0,100): # running 100 trials 
         simvalues.append(monte(i))
         
    avgvalues.append(np.average(simvalues[0:100])   ) #storing the average value of the list of simulation values of pi

diffvalues = [] # empty list to store the differences between the average values and pi

for k in avgvalues:
    diffvalues.append(np.pi - k) # assigning the difference between pi and the average value to the array of differences

plt.plot(n_list, diffvalues) # plotting the final list of differences as a function of n
    
# change the limits of the Axes to zoom in:
plt.xlim(1,10**8) 
plt.ylim( (-0.1, 0.1) )

'''
As n tends to infinity, the rate of convergence increases. The gradient of the standard deviation functions in parts (h) and (i) 
tend to zero. Therefore, the greater the value of n, the closer the approximation converges to the value of pi. If we print the difference
values, we can see that the approximation becomes correct to the tenth decimal place for values of $n^10$
'''
print(diffvalues)
