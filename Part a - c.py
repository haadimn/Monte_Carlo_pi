# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 11:31:30 2021

@author: Haadi
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

#initalizing figure and axis

fig = plt.figure()
ax = fig.add_axes([0.0,0.0, 0.8,0.8])
plt.title("$Monte\ Carlo \  Trials$")
plt.xlabel("$x$")
plt.ylabel("$y$")

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

#The number of values in the xsub and ysub array will be equal, hence the proportion of points at a distance less than 1 from the origin is (float(len(xsub)/len(x)))
print('The proportion of points which are at a distance less than 1 from the origin is %.3f' %(float(len(xsub)/len(x))))




 


