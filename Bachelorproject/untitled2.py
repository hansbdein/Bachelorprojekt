# -*- coding: utf-8 -*-
"""
Created on Mon May 17 19:08:40 2021

@author: Hans
"""
import pandas as pd
import matplotlib.pyplot as plt

import numpy as np
from galpy import potential
from galpy.orbit import Orbit
from astropy import units as u
from galpy.util import bovy_conversion


def set_axes_equal(ax):
    '''Make axes of 3D plot have equal scale so that spheres appear as spheres,
    cubes as cubes, etc..  This is one possible solution to Matplotlib's
    ax.set_aspect('equal') and ax.axis('equal') not working for 3D.

    Input
      ax: a matplotlib axis, e.g., as output from plt.gca().
    '''

    x_limits = ax.get_xlim3d()
    y_limits = ax.get_ylim3d()
    z_limits = ax.get_zlim3d()

    x_range = abs(x_limits[1] - x_limits[0])
    x_middle = np.mean(x_limits)
    y_range = abs(y_limits[1] - y_limits[0])
    y_middle = np.mean(y_limits)
    z_range = abs(z_limits[1] - z_limits[0])
    z_middle = np.mean(z_limits)

    # The plot bounding box is a sphere in the sense of the infinity
    # norm, hence I call half the max range the plot radius.
    plot_radius = 0.5*max([x_range, y_range, z_range])

    ax.set_xlim3d([x_middle - plot_radius, x_middle + plot_radius])
    ax.set_ylim3d([y_middle - plot_radius, y_middle + plot_radius])
    ax.set_zlim3d([z_middle - plot_radius, z_middle + plot_radius])



coords=pd.read_csv("run1/200."+str(10)+".csv", usecols=[1, 2, 3])


xyz = np.array([cord for cord in np.array(coords)[:1000] if np.linalg.norm(cord)<100])

x = xyz[:,0]
y = xyz[:,1]
z = xyz[:,2]


ax = plt.axes(projection='3d')


ax.scatter3D( x,y,z,s=5,marker='*');




coords=pd.read_csv("run1/100."+str(10)+".csv", usecols=[1, 2, 3])
xyz = np.array([cord for cord in np.array(coords)[:1000] if np.linalg.norm(cord)<100])
x = xyz[:,0]
y = xyz[:,1]
z = xyz[:,2]

ax.scatter3D( x,y,z,s=5,marker='*');







coords=pd.read_csv("coordinates.csv", usecols=[1, 2, 3])

xyz = np.array([cord for cord in np.array(coords)[:1000] if np.linalg.norm(cord)<100])

x = xyz[:,0]
y = xyz[:,1]
z = xyz[:,2]

ax.scatter3D( x,y,z,s=5,marker='*');

ax.set_xlim3d([-30, 30])
ax.set_ylim3d([-30, 30])
ax.set_zlim3d([-30, 30])




'''
v=200.*u.km/u.s 

l=20.*u.deg 
b=5.*u.deg 

R=8.*u.kpc      #afstand fra centrum
vR=v*np.cos(l)*np.cos(b)  #radiel hastighed
vT=v*np.sin(l)*np.cos(b)  #Transversal hastighed
z=0.*u.kpc      #højde
vz=v*np.sin(b) #hastighed i z
phi=0.*u.deg    #startvinkel



o= Orbit([[R,vR,vT,z,vz,phi],[1.5*R,vR,vT,z,vz,phi]])
ts= np.linspace(0.,20.,1001)
o.integrate(ts,potential.MWPotential2014)

o.plot(d1='x',d2='y',zorder=1,
                  label=r'$\mathrm{Full\ 3D}$',
                  xrange=[-10.,10],yrange=[-10.,10.])



o.plot(d1='x',d2='z',zorder=1,
                  label=r'$\mathrm{Full\ 3D}$',
                  xrange=[-10.,10],yrange=[-1.,1.])

o.plot3d()  

'''