# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 12:05:08 2021

@author: Hans
"""

import numpy as np
from galpy import potential
from galpy.orbit import Orbit
from astropy import units as u




R=8.2*u.kpc      #afstand fra centrum
vR=-67.*u.km/u.s   #radiel hastighed
vT=46.*u.km/u.s   #Transversal hastighed
z=0.*u.kpc      #højde
vz=16.*u.km/u.s  #hastighed i z
phi=0.*u.deg    #startvinkel



o= Orbit([R,vR,vT,z,vz,phi])
ts= np.linspace(0.,15.,1001)
o.integrate(ts,potential.MWPotential2014)

o.plot(d1='x',d2='y',zorder=1,
                  label=r'$\mathrm{Full\ 3D}$',
                  xrange=[-10.,10],yrange=[-10.,10.])



o.plot(d1='x',d2='z',zorder=1,
                  label=r'$\mathrm{Full\ 3D}$',
                  xrange=[-10.,10],yrange=[-2.,2.])

o.plot3d()  