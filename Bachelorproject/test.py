# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 15:46:22 2021

@author: Hans
"""
from galpy.potential.mwpotentials import MWPotential2014, McMillan17, Irrgang13I
from galpy.orbit import Orbit
from galpy.util.bovy_conversion import get_physical
from astropy import units
times= np.linspace(0.,10.,3001)*units.Gyr
o_mwp14= Orbit(ro=8.,vo=220.) # Need to set these by hand
o_mcm17= Orbit(**get_physical(McMillan17))
o_irrI= Orbit(**get_physical(Irrgang13I))
o_mwp14.integrate(times,MWPotential2014)
o_mcm17.integrate(times,McMillan17)
o_irrI.integrate(times,Irrgang13I)
o_mwp14.plot(lw=0.6)
o_mcm17.plot(overplot=True,lw=0.6)
o_irrI.plot(overplot=True,lw=0.6)