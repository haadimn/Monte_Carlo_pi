# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 14:35:01 2021

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

#plotting a square around points generated in (a)

currentAxis = plt.gca()
currentAxis.add_patch(Rectangle((0,0), 1,1, fill=None,))

'''
#The region bounded by the square contains 1000 uniformely distributed random points. These points are enclosed by a square of 
area of $r^2$ (which is equal to 1 sqaure unit in this case). Therefore, the scatterplot of (x,y) is an approximation of this area. Similarly, the coordinates which
are a distance of less than one from the origin approximate a quarter circle of area $1/4*\pi*r^2$. When the ratio of the two regions is taken, it results
to $1/4*\pi*r^2/r^2 = \pi/4$. The randomly distributed points approximate this area. 











