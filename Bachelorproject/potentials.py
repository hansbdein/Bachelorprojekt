# -*- coding: utf-8 -*-
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
from galpy import potential



from galpy.potential import plotRotcurve
plotRotcurve(MWPotential2014,label=r'$\mathrm{MWPotential2014}$',ro=8.,vo=220.) # need to set ro and vo explicitly, because MWPotential2014 has units turned off
plotRotcurve(McMillan17,overplot=True,label=r'$\mathrm{McMillan\, (2017)}$')
