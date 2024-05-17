# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 14:38:11 2021

@author: Hans
"""
import numpy 



from galpy import potential
from galpy.orbit import Orbit
def orbit_RvRELz(R,vR,E,Lz,pot=None):
    """Returns Orbit at (R,vR,phi=0,z=0) with given (E,Lz)"""
    return Orbit([R,vR,Lz/R,0.,
                  numpy.sqrt(2.*(E-potential.evaluatePotentials(pot,R,0.)
                                 -(Lz/R)**2./2.-vR**2./2)),0.],ro=8.,vo=220.)
R, E, Lz= 0.8, -1.25, 0.6

levels= numpy.linspace(-1.25,0.,11)
cntrcolors= ['k' for l in levels]
cntrcolors[numpy.arange(len(levels))\
           [numpy.fabs(levels-E) < 0.01][0]]= '#ff7f0e'

vR= 0.
o= orbit_RvRELz(R,vR,E,Lz,pot=potential.MWPotential2014)
ts= numpy.linspace(0.,100.,1001)
o.integrate(ts,potential.MWPotential2014)
#o.animate(); # remove the ; to display the animation




potential.plotPotentials(potential.MWPotential2014,
                         rmin=0.3,rmax=1.05,
                         zmin=-0.3,zmax=0.3,
                         nrs=101,nzs=101,
                         justcontours=True,
                         levels=levels,
                         cntrcolors=cntrcolors,
                         effective=True,
                         Lz=Lz)
o.plot(overplot=True,lw=0.5,use_physical=False)