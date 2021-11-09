# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 12:08:13 2021

@author: Haadi
"""

#initalizing figure and axis

import numpy as np

#initializing two arrays  x and y with 1000 uniformly distributed random variables between zero and one

x = np.random.uniform(0,1,1000)
y = np.random.uniform(0,1,1000)

#plotting corresponding points (x,y) onto a scatterplot

plt.scatter(x, y)
plt.gca().set_aspect('equal')

#initializing proportion of points that are at a distance less than 1 from the origin and plotting

mask = [x**2+y**2<1]
xsub = x[mask]
ysub = y[mask]
plt.scatter(xsub, ysub)

#The proportions in part (c), we can approximate a value for pi by multiplying our proportion by 4:
    
pi =(float(4*len(xsub)/len(x)))
print(pi)
    
#Repeating this process for any arbitrary number of trials to estimate uncertainty:    

for i in range (0,10,1):
    x = np.random.uniform(0,1,1000)
    y = np.random.uniform(0,1,1000)

    #plt.scatter(x, y)
    #plt.gca().set_aspect('equal')

    mask= [x**2+y**2<1]
    xsub = x[mask]  
    ysub = y[mask]
    #plt.scatter(xsub, ysub,)
    print('Trial Result: %.3f' %(float(4*len(xsub)/len(x))))
    
#The trials come reasonably close to the value of pi
