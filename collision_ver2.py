#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

resolution      =   120
pi              =   np.pi
angle           =   np.linspace(0, 2*pi, resolution)

def init_fig():
    fig     =   plt.figure(figsize=(7, 7))
    ax      =   fig.add_axes([0.1, 0.1, 0.8, 0.8], frameon=True)
    line,   =   plt.plot([], [], 'bo', markersize=1)

    ax.set_xlim(-15, 15)
    ax.set_ylim(-15, 15)
    ax.set_xticks([])
    ax.set_yticks([])

    return fig, ax, line,
   
def init_particles(idx_arr, radii):
    particles_arr   =   np.zeros(len(idx_arr), dtype=[  ('pos', float,  (2,)),
                                                        ('vel', float,  (2,)),
                                                        ('rad', float)])

    particles_arr['rad']        =   radii
    particles_arr['pos'][:, 0]  =   np.random.rand(len(idx_arr)) * 30.0 - 15.0
    particles_arr['pos'][:, 1]  =   np.random.rand(len(idx_arr)) * 30.0 - 15.0
    particles_arr['vel'][:, 0]  =   np.random.rand(len(idx_arr)) * 0.2
    particles_arr['vel'][:, 1]  =   np.random.rand(len(idx_arr)) * 0.2

    return particles_arr

def draw_circles(idx_arr, particles_arr):
    circles_arr =   np.zeros(len(particles_arr), dtype=[    ('x',   float,  (resolution,)),
                                                            ('y',   float,  (resolution,))])
    for idx in idx_arr:
        circles_arr[idx]['x']   =   particles_arr[idx]['pos'][0] + particles_arr[idx]['rad']*np.cos(angle)
        circles_arr[idx]['y']   =   particles_arr[idx]['pos'][1] + particles_arr[idx]['rad']*np.sin(angle)

    return circles_arr


nParticles      =   5
radii           =   1.0

setIdx          =   np.array(list(x for x in range(nParticles)))
particles       =   init_particles(setIdx, radii)
circles         =   draw_circles(setIdx, particles)
fig, ax, line,  =   init_fig()

def update(dt):        
    for idx in setIdx:
        if not (particles[idx]['pos'][0] >= -(15.0 - particles[idx]['rad']) and particles[idx]['pos'][0] <= (15.0 - particles[idx]['rad'])): 
            particles[idx]['vel'][0] *= -1.0

        if not (particles[idx]['pos'][1] >= -(15.0 - particles[idx]['rad']) and particles[idx]['pos'][1] <= (15.0 - particles[idx]['rad'])): 
            particles[idx]['vel'][1] *= -1.0

        particles[idx]['pos'][0]    +=  particles[idx]['vel'][0]
        particles[idx]['pos'][1]    +=  particles[idx]['vel'][1]
        circles[idx]['x']           +=  particles[idx]['vel'][0]
        circles[idx]['y']           +=  particles[idx]['vel'][1]
        
    line.set_data(circles['x'], circles['y'])
    return line,

print(particles['vel'])
animation       =   FuncAnimation(fig, update, interval=5)
plt.show()

