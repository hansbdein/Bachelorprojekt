# -*- coding: utf-8 -*-


"""
Created on Wed Apr  7 13:50:57 2021

@author: Hans
"""
import numpy 

import matplotlib.pyplot as plt


from galpy import potential
from galpy.orbit import Orbit
E, Lz= -1.25, 0.6
levels= numpy.linspace(-1.25,0.,11)
cntrcolors= ['k' for l in levels]
cntrcolors[numpy.arange(len(levels))\
           [numpy.fabs(levels-E) < 0.01][0]]= '#ff7f0e'

potential.plotPotentials(potential.MWPotential2014,
                         rmin=.01,nrs=101,nzs=101,
                         justcontours=True,
                         levels=levels,
                         cntrcolors=cntrcolors,
                         effective=True,
                         Lz=Lz);





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
#bovy_plot.bovy_text(r'$L_z= %.2f$' % Lz,
#                    top_left=True,size=18.)