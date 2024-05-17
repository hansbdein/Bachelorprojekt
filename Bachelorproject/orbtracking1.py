# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 20:35:26 2021

@author: Hans
"""


from time import time

import matplotlib.pyplot as plt
import numpy as np
from galpy import potential
from galpy.orbit import Orbit
from astropy import units as u
from galpy.util.bovy_conversion import get_physical
from galpy.potential.mwpotentials import MWPotential2014, McMillan17, Irrgang13I

import matplotlib.cbook as cbook

R=7.10/8.21      #afstand fra centrum
vR=-67./233.1  #radiel hastighed
vT=46/233.1 #Transversal hastighed
z=-0.4/8.21      #højde
vz=-16./233.1  #hastighed i z
phi=np.pi    #startvinkel



o= Orbit([R,vR,vT,z,vz,phi])
ts= np.linspace(0.,1.,1001)*0.5/220*8/8.21*233.1*u.Gyr

tiden=time()
#o.integrate(ts,MWPotential2014,method='dop853_c')
o.integrate(ts,McMillan17,method='leapfrog_c')
print(time()-tiden)


'''
kicks=[]

for t in ts:
    kicks.append(
        np.sqrt((potential.vcirc(McMillan17,o.r(t))  -o.vT(t)*233.1)**2
        + (o.vR(t)*233.1)**2
        + (o.vz(t)*233.1)**2
        ))
    
    
plt.figure()
plt.plot(ts,kicks)


plt.xlabel('Time ago in Gyr')
plt.ylabel('Required kick velocity')







o.plot(d1='x',d2='y',zorder=1,
                  label=r'$\mathrm{Full\ 3D}$',
                  xrange=[-10.,10],yrange=[-10.,10.],**get_physical(McMillan17), color='red', linestyle='dashed')

img = plt.imread('Capture.PNG')

plt.imshow(img, zorder=0, extent=[-10, 10, -10, 10])
'''
#plt.show()
'''
o.plot(d1='x',d2='z',zorder=1,
                  label=r'$\mathrm{Full\ 3D}$',
                  xrange=[-10.,10],yrange=[-2.,2.],**get_physical(McMillan17))



o.plot(d1='x',d2='z',zorder=1,
                  label=r'$\mathrm{Full\ 3D}$',
                  xrange=[-10.,10],yrange=[-2.,2.],**get_physical(McMillan17), color='red', linestyle='dashed')

img = plt.imread('Capture2.PNG')

plt.imshow(img, zorder=0, extent=[-10, 10, -2, 2])
'''


#o.plot3d(ro=8.21)  
