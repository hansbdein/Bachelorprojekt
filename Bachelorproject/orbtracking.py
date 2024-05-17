# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 20:35:26 2021

@author: Hans



import numpy as np
from galpy import potential
from galpy.orbit import Orbit
from astropy import units as u


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
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 13:45:14 2021

@author: Hans
"""
import pandas as pd
import matplotlib.pyplot as plt
from time import time
import numpy as np
from galpy import potential
from galpy.orbit import Orbit
from astropy import units as u
from galpy.util import bovy_conversion

def random_three_vector():
    """
    Generates a random 3D unit vector (direction) with a uniform spherical distribution
    Algo from http://stackoverflow.com/questions/5408276/python-uniform-spherical-distribution
    :return:
    """
    phi = np.random.uniform(0,np.pi*2)
    costheta = np.random.uniform(-1,1)

    theta = np.arccos( costheta )
    x = np.sin( theta) * np.cos( phi )
    y = np.sin( theta) * np.sin( phi )
    z = np.cos( theta )
    return (x,y,z)

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

coordinates = pd.read_csv('coordinates.csv', usecols=[1, 2, 3])
xyz = np.array(coordinates)[:1000]
x = np.array(coordinates)[:,0]
y = np.array(coordinates)[:,1]
z = np.array(coordinates)[:,2]


ax = plt.axes(projection='3d')




ax.scatter3D( x,y,z,s=5,marker='*');


set_axes_equal(ax)



def makeorbits(kick, xyzstars, t):
    pot=potential.mwpotentials.McMillan17
    
    v=kick/233.1
    

    
    coordscartesian = np.array([[*i,*random_three_vector()] for i in xyzstars])
    
    
    orbcoords=[[np.sqrt(abs(x**2+y**2))/8.21,vR*v,
                
                potential.vcirc(pot,np.sqrt(abs(x**2+y**2))/8.21)/233.1+vT*v
                
                ,z/8.21,
                vz*v,np.arctan2(x,y)] for x,y,z,vR,vT,vz in coordscartesian]
    
    o= Orbit(orbcoords)
    
    
    ts= np.linspace(0.,1.,1001)*t*u.Gyr
    o.integrate(ts,pot,method='dop853_c')


    return o
#makeorbits(1, xyz, 0.001).plot3d()



tiden=time()
o=makeorbits(100, xyz, 1)
print(time()-tiden)



#o.plot3d(ro=8.21)
'''
o200 = makeorbits(200, xyz, 10)
print('200 done')
o100 = makeorbits(100, xyz, 10)
print('100 done')
o50 = makeorbits(50, xyz, 10)
print('50 done')
o20 = makeorbits(20, xyz, 10)
print('20 done')



def converttoxyz(orb,t):
    return np.array([
              orb.r(t)*np.sin(orb.phi(t)),
              orb.r(t)*np.cos(orb.phi(t)),
              orb.z(t)]).T

    




for t in [1,5,10]:
    pd.DataFrame(converttoxyz(o200,t*u.Gyr),columns=['X','Y','Z']).to_csv("200."+str(t)+".csv")
    pd.DataFrame(converttoxyz(o100,t*u.Gyr),columns=['X','Y','Z']).to_csv("100."+str(t)+".csv")
    pd.DataFrame(converttoxyz(o50,t*u.Gyr),columns=['X','Y','Z']).to_csv("50."+str(t)+".csv")
    pd.DataFrame(converttoxyz(o20,t*u.Gyr),columns=['X','Y','Z']).to_csv("20."+str(t)+".csv")
    
#xyz10100=np.array([o100.r(10*u.Gyr)*np.sin(o100.phi(10*u.Gyr)),o100.r(10*u.Gyr)*np.cos(o100.phi(10*u.Gyr)),o100.z(10*u.Gyr))






o2001.plot(d1='x',d2='y',zorder=1,
                  #label=r'$\mathrm{Full\ 3D}$',
                  xrange=[-30.,30],yrange=[-30.,30.])



o2001.plot(d1='x',d2='z',zorder=1,
                  #label=r'$\mathrm{Full\ 3D}$',
                  xrange=[-30.,30],yrange=[-30.,30.])

o2001.plot3d()  

otest= makeorbits(200, xyz[:10], 0.01)

fig = plt.figure()
plt.hist(o2001.R(1*u.Gyr), bins=30)
plt.xlabel('R in kpc')


makeorbits(200, xyz[:100], 1).plot(d1='x',d2='y',zorder=1,
                  xrange=[-30.,30],yrange=[-30.,30.])

makeorbits(200, xyz, 1)


'''



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