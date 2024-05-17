# -*- coding: utf-8 -*-
"""


"""

import warnings
warnings.filterwarnings('ignore')
import numpy
from IPython.display import Image
from galpy.util import bovy_plot
bovy_plot.bovy_print(axes_labelsize=17.,text_fontsize=12.,
                     xtick_labelsize=15.,ytick_labelsize=15.)
#%pylab inline
from pylab import *


from galpy import potential
from galpy.util import bovy_plot
figsize(10,6)
# Define each potential
kp= potential.KeplerPotential(amp=1.)
hp= potential.IsochronePotential(normalize=1.,b=1000.)
pp= potential.PlummerPotential(amp=1.,b=1.)
ip= potential.IsochronePotential(amp=1.,b=1.)
# Plot the rotation curve for each
line_kepler= potential.plotRotcurve(kp,Rrange=[0.,10.],\
                label=r'$\mathrm{Point\ mass}$',yrange=[0.,1.5],
                xlabel=r'$r$',ylabel=r'$v_c(r)$')
line_homog= potential.plotRotcurve(hp,Rrange=[0.,10.],\
                label=r'$\mathrm{Homogeneous\ sphere}$',overplot=True)
line_plummer= potential.plotRotcurve(pp,Rrange=[0.,10.],\
                label=r'$\mathrm{Plummer}\,(b=1)$',overplot=True)
line_isochrone= potential.plotRotcurve(ip,Rrange=[0.,10.],\
                label=r'$\mathrm{Isochrone}\,(b=1)$',overplot=True)
legend(handles=[line_kepler[0],line_homog[0],
                line_plummer[0],line_isochrone[0]],
       fontsize=18.,loc='upper right',frameon=False);