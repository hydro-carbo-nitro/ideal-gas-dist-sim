import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

resolution      =   120
pi              =   np.pi
angle           =   np.linspace(0, 2*pi, resolution)
L               =   5

def init_fig():
    fig     =   plt.figure(figsize=(7, 7))
    ax      =   fig.add_axes([0.1, 0.1, 0.8, 0.8], frameon=True)
    line,   =   plt.plot([], [], 'bo', markersize=1)

    ax.set_xlim(-L, L)
    ax.set_ylim(-L, L)
    ax.set_xticks([])
    ax.set_yticks([])

    return fig, ax, line,
   
def init_particles(idx_arr, radii):
    particles_arr   =   np.zeros(len(idx_arr), dtype=[  ('pos', float,  (2,)),
                                                        ('vel', float,  (2,)),
                                                        ('rad', float)])
    particles_arr['rad']        =   radii
    particles_arr['pos'][:, 0]  =   (L-particles_arr['rad'])*(2*np.random.rand(len(idx_arr)) - 1)
    particles_arr['pos'][:, 1]  =   (L-particles_arr['rad'])*(2*np.random.rand(len(idx_arr)) - 1)
    particles_arr['vel'][:, 0]  =   np.random.rand(len(idx_arr)) * 1.0
    particles_arr['vel'][:, 1]  =   np.random.rand(len(idx_arr)) * 1.0

    idx = 0
    while(idx < len(idx_arr)):
        judge = 0
        target = 0
        while(target < len(idx_arr)):
            print(f"{idx}, {target}")
            if idx != target:
                dx = particles_arr[idx]['pos'][0] - particles_arr[target]['pos'][0]
                dy = particles_arr[idx]['pos'][1] - particles_arr[target]['pos'][1]
                d = particles_arr[idx]['rad'] + particles_arr[target]['rad']
                if dx**2 + dy**2 <= d**2:
                    particles_arr[idx]['pos'][0]  =   (L-particles_arr[idx]['rad'])*(2*random.random() - 1)
                    particles_arr[idx]['pos'][1]  =   (L-particles_arr[idx]['rad'])*(2*random.random() - 1)
                    judge = 0
                    target = 0
                else:
                    judge+=1
                    target+=1
            else:
                target+=1
            if judge == len(idx_arr)-1:
                idx+=1
                target=0
                break

    return particles_arr

def draw_circles(idx_arr, particles_arr):
    circles_arr =   np.zeros(len(particles_arr), dtype=[    ('x',   float,  (resolution,)),
                                                            ('y',   float,  (resolution,))])
    for idx in idx_arr:
        circles_arr[idx]['x']   =   particles_arr[idx]['pos'][0] + particles_arr[idx]['rad']*np.cos(angle)
        circles_arr[idx]['y']   =   particles_arr[idx]['pos'][1] + particles_arr[idx]['rad']*np.sin(angle)

    return circles_arr


nParticles      =   25
radii           =   1.0

setIdx          =   np.array(list(x for x in range(nParticles)))
particles       =   init_particles(setIdx, radii)
circles         =   draw_circles(setIdx, particles)
fig, ax, line,  =   init_fig()

def update(dt):        
    for idx in setIdx:
        if not (particles[idx]['pos'][0] >= -(L - particles[idx]['rad']) and particles[idx]['pos'][0] <= (L - particles[idx]['rad'])): 
            particles[idx]['vel'][0] *= -1.0

        if not (particles[idx]['pos'][1] >= -(L - particles[idx]['rad']) and particles[idx]['pos'][1] <= (L - particles[idx]['rad'])): 
            particles[idx]['vel'][1] *= -1.0

        particles[idx]['pos'][0]    +=  particles[idx]['vel'][0]
        particles[idx]['pos'][1]    +=  particles[idx]['vel'][1]
        circles[idx]['x']           +=  particles[idx]['vel'][0]
        circles[idx]['y']           +=  particles[idx]['vel'][1]
        
    line.set_data(circles['x'], circles['y'])
    return line,

print(particles['vel'])
animation       =   FuncAnimation(fig, update, interval=1)
plt.show()
