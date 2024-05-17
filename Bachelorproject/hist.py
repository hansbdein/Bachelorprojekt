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

coords=pd.read_csv("coordinates.csv", usecols=[1, 2, 3])

xyz = np.array([cord for cord in np.array(coords)[:5000] if np.linalg.norm(cord)<100])

x = xyz[:,0]
y = xyz[:,1]
z = xyz[:,2]

ax.scatter3D( x,y,z,s=5,marker='*');

ax.set_xlim3d([-30, 30])
ax.set_ylim3d([-30, 30])
ax.set_zlim3d([-30, 30])






#galcoords




for tid in ['1','5','10']:
    
    kick='200'
    coords=pd.concat([pd.read_csv("run1/"+kick+"."+tid+".csv", usecols=[1, 2, 3]),
        pd.read_csv("run2/"+kick+"."+tid+".csv", usecols=[1, 2, 3]),
        pd.read_csv("run3/"+kick+"."+tid+".csv", usecols=[1, 2, 3]),   
        pd.read_csv("run4/"+kick+"."+tid+".csv", usecols=[1, 2, 3]),
        pd.read_csv("run5/"+kick+"."+tid+".csv", usecols=[1, 2, 3]),      
        ])
        
    print(len(np.array([cord for cord in np.array(coords)[:5000] if np.linalg.norm(cord)<500])))
    '''
    for kick in ['200','100','50','20']:
        coords=pd.concat([pd.read_csv("run1/"+kick+"."+tid+".csv", usecols=[1, 2, 3]),
        pd.read_csv("run2/"+kick+"."+tid+".csv", usecols=[1, 2, 3]),
        pd.read_csv("run3/"+kick+"."+tid+".csv", usecols=[1, 2, 3]),   
        pd.read_csv("run4/"+kick+"."+tid+".csv", usecols=[1, 2, 3]),
        pd.read_csv("run5/"+kick+"."+tid+".csv", usecols=[1, 2, 3]),      
        ])
        
        
        xyz = np.array([cord for cord in np.array(coords)[:5000] if np.linalg.norm(cord)<100])
        
        x = xyz[:,0]
        y = xyz[:,1]
        z = xyz[:,2]
        
        
        plt.figure('R for kick of '+kick+'km/s after'+tid+'Gyr')
        plt.hist(np.sqrt(x**2+y**2+z**2),bins=40,range=(0,40))
        plt.xlabel('Distance from MW center in kpc')
        plt.ylabel('Number of systems')
        plt.title('Distrubution after random kick of '+kick+' km/s after '+tid+'Gyr')
        plt.savefig('kick_'+kick+'kms_time_R_'+tid+'Gyr',bbox_inches='tight')
        
    
    
    
    
    
    
    
    
    
    for kick in ['200','100','50','20']:
        coords=pd.concat([pd.read_csv("run1/"+kick+"."+tid+".csv", usecols=[1, 2, 3]),
        pd.read_csv("run2/"+kick+"."+tid+".csv", usecols=[1, 2, 3]),
        pd.read_csv("run3/"+kick+"."+tid+".csv", usecols=[1, 2, 3]),   
        pd.read_csv("run4/"+kick+"."+tid+".csv", usecols=[1, 2, 3]),
        pd.read_csv("run5/"+kick+"."+tid+".csv", usecols=[1, 2, 3]),      
        ])
        
        xyz = np.array([cord for cord in np.array(coords)[:5000] if np.linalg.norm(cord)<100])
        
        x = xyz[:,0]
        y = xyz[:,1]
        z = xyz[:,2]
        
        
        plt.figure('z for kick of '+kick+'km/s after'+tid+'Gyr')
        plt.hist(z,bins=100,range=(-10,10))
        plt.xlabel('z position kpc')
        plt.ylabel('Number of systems')
        plt.title('Distrubution after random kick of '+kick+' km/s after '+tid+'Gyr')
        plt.savefig('kick_'+kick+'kms_time_z_'+tid+'Gyr',bbox_inches='tight')
    
    
    








coords=pd.read_csv("coordinates.csv", usecols=[1, 2, 3])

xyz = np.array([cord for cord in np.array(coords)[:5000] if np.linalg.norm(cord)<100])

x = xyz[:,0]
y = xyz[:,1]
z = xyz[:,2]


plt.figure('R for Initial positions')
plt.hist(np.sqrt(x**2+y**2+z**2),bins=40,range=(0,40))
plt.xlabel('Distance from MW center in kpc')
plt.ylabel('Number of systems')
plt.title('Initial distrubution')
plt.savefig('Original_coordinates_R.png',bbox_inches='tight')




z=np.array([cord[2] for cord in np.array(pd.read_csv("coordinates.csv", usecols=[1, 2, 3]))[:5000] 
            if np.linalg.norm(cord)<100])

plt.figure('z for Initial positions')
plt.hist(z,bins=100,range=(-10,10))
plt.xlabel('z position kpc')
plt.ylabel('Number of systems')
plt.title('Initial distrubution')
plt.savefig('Original_coordinates_z.png',bbox_inches='tight')

'''
'''
#allplots

for tid in ['1','5','10']:
    for kick in ['20','50','100','200']:
        coords=pd.read_csv("run1/"+kick+"."+tid+".csv", usecols=[1, 2, 3])
        
        xyz = np.array([cord for cord in np.array(coords)[:1000] if np.linalg.norm(cord)<100])
        
        x = xyz[:,0]
        y = xyz[:,1]
        z = xyz[:,2]
        
        np.histogram(np.sqrt(x**2+y**2+z**2),bins=10,range=(0,20))
        plt.figure('kick of '+kick+'km/s after'+tid+'Gyr')
        plt.hist(np.sqrt(x**2+y**2+z**2),bins=40,range=(0,40))
        plt.xlabel('Distance from sun in kpc')
        plt.ylabel('Number of systems')
        plt.title('Distrubution after random kick of '+kick+' km/s after '+tid+'Gyr')
        plt.savefig('kick_'+kick+'kms_time_'+tid+'Gyr',bbox_inches='tight')




#heliocoords

coords=pd.read_csv("coordinates.csv", usecols=[1, 2, 3])

xyz = np.array([cord for cord in np.array(coords)[:1000] if np.linalg.norm(cord)<100])

x = xyz[:,0]
y = xyz[:,1]
z = xyz[:,2]

np.histogram(np.sqrt((x+8)**2+y**2+z**2),bins=10,range=(0,20))
plt.figure('Initial positions')
plt.hist(np.sqrt((x+8)**2+y**2+z**2),bins=40,range=(0,40))
plt.xlabel('Distance from sun in kpc')
plt.ylabel('Number of systems')
plt.title('Initial distrubution')
plt.savefig('Original_coordinates.png',bbox_inches='tight')




for kick in ['20','50','100','200']:
    coords=pd.read_csv("run1/"+kick+".5.csv", usecols=[1, 2, 3])
    
    xyz = np.array([cord for cord in np.array(coords)[:1000] if np.linalg.norm(cord)<100])
    
    x = xyz[:,0]
    y = xyz[:,1]
    z = xyz[:,2]
    
    np.histogram(np.sqrt((x+8)**2+y**2+z**2),bins=10,range=(0,20))
    plt.figure('kick of '+kick+'km')
    plt.hist(np.sqrt((x+8)**2+y**2+z**2),bins=40,range=(0,40))
    plt.xlabel('Distance from sun in kpc')
    plt.ylabel('Number of systems')
    plt.title('Distrubution after random kick of '+kick+' km/s')
    plt.savefig('kick_'+kick,bbox_inches='tight')







incoords = pd.read_csv('coordinates.csv', usecols=[1, 2, 3])

'''


'''
for t in [1,5,10]:
    pd.DataFrame(converttoxyz(o200,t*u.Gyr),columns=['X','Y','Z']).to_csv("200."+str(t)+".csv")
    pd.DataFrame(converttoxyz(o100,t*u.Gyr),columns=['X','Y','Z']).to_csv("100."+str(t)+".csv")
    pd.DataFrame(converttoxyz(o50,t*u.Gyr),columns=['X','Y','Z']).to_csv("50."+str(t)+".csv")
    pd.DataFrame(converttoxyz(o20,t*u.Gyr),columns=['X','Y','Z']).to_csv("20."+str(t)+".csv")
 

o20=[None,None,None]  
o100=[None,None,None]
o50=[None,None,None] 
o200=[None,None,None]   

 '''  