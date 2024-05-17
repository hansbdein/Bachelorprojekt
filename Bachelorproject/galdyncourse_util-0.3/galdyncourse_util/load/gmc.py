# gmc.py: download, parse, and plot the Miville-Deschênes GMC catalog
import os, os.path
import numpy
from astropy.io import ascii
from matplotlib import pyplot
from galdyncourse_util.load.vizier import vizier
from galdyncourse_util.load import cache
_MIVILLE_VIZIER_NAME= 'J/ApJ/834/57'
def read(verbose=False):
    """
    NAME:
       read
    PURPOSE:
       read the Miville-Deschênes GMC catalog
    INPUT:
       verbose= (False) if True, be verbose
    OUTPUT:
       pandas dataframe      
    HISTORY:
       2017-09-12 - Written - Bovy (UofT)
    """
    # Generate file path and name
    tPath= os.path.join(cache._CACHE_VIZIER_DIR,'cats',
                        *_MIVILLE_VIZIER_NAME.split('/'))
    filePath= os.path.join(tPath,'table1.dat.gz')
    readmePath= os.path.join(tPath,'ReadMe')
    # download the file
    if not os.path.exists(filePath[:-3]):
        vizier(_MIVILLE_VIZIER_NAME,filePath,readmePath,
               catalogname='table1.dat.gz',readmename='ReadMe')
    # Read with astropy, w/o the .gz
    table= ascii.read(filePath[:-3],readme=readmePath,format='cds')
    return table.to_pandas()

def plot_lv(**kwargs):
    """
    NAME:
       plot_lv
    PURPOSE:
       plot the (l,v) diagram for the GMC catalog
    INPUT:
       plotting kwargs
    OUTPUT:
       matplotlib axes object
    HISTORY:
       2017-09-12 - Written - Bovy (UofT)
    """
    data= read()
    data= data[numpy.fabs(data['GLAT']) < 2.]
    s= data['Area']*15.
    s[s>30.]= 30.
    c= 'k'
    out= pyplot.scatter(data['GLON'],data['Vcent'],s=s,c=c,
                        cmap='gist_yarg',alpha=0.1,**kwargs)
    pyplot.xlabel(r'$\mathrm{Galactic\ longitude}\,(\mathrm{deg})$')
    pyplot.ylabel(r'$v_{\mathrm{los}}\,(\mathrm{km\,s}^{-1})$')
    pyplot.xlim(185.,-185.)
    pyplot.ylim(-200.,200.)
    return out
    
