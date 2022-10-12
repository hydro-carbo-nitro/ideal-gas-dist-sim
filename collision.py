#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

resolution  =   36
pi          =   np.pi
angle       =   np.linspace(0, 2*pi, resolution)

class Particle:
    # Create particle on 2-d space

    def __init__(self, x_0, y_0, vx_0, vy_0, radius):
        # Initialize the particle's pos, vel, radius

        self.position   =   np.array((x_0, y_0))        # array of position
        self.velocity   =   np.array((vx_0, vy_0))      # array of velocity
        self.radius     =   radius                      # Ideal gas has no volume, but assume there is volume for simulation
        self.mass       =   radius ** 2                 # 2-dimension homogeneous circle



class Simulation:
    # Simulation
    
    ParticleClass = Particle
    
    def __init__(self, nParticles, radii):
        self.set_fig()
        self.init_particles(nParticles, radii)
        self.anim()

    def set_fig(self):
        self.fig     =   plt.figure(figsize=(7,7))
        self.ax      =   self.fig.add_axes([0, 0, 1, 1], frameon=False)       # [Top, Bottom, Width, Height]
        
        self.ax.set_xlim(-10, 10)                                        # x-range -10 ~ 10
        self.ax.set_ylim(-10, 10)                                        # y-range -10 ~ 10
        self.ax.set_xticks([])                                           # what is this?
        self.ax.set_yticks([])                                           # what is this?(2)


    def init_particles(self, nParticles, radii):
        
        self.particles      =   np.zeros(nParticles, dtype=[('position',    float,  (2, )),
                                                            ('velocity',    float,  (2, )),
                                                            ('radius',      float),
                                                            ('circle',      float,  (resolution, resolution))])
        # input the quantities of particle

        for idx, particle in enumerate(self.particles):
            particle['position']    =   [-3 + 6*idx, 0]             # (x, y)
            particle['velocity']    =   [idx, 0]                    # (vx, vy)
            particle['radius']      =   radii
        

    def anim(self):
        animation   =   FuncAnimation(self.fig, self.update, interval=10)
        plt.show()

    def update(self, dt):
        for idx, particle in enumerate(self.particles):
            particle['circle'][0]   =   particle['position'][0] + particle['radius']*np.cos(angle)
            particle['circle'][1]   =   particle['position'][1] + particle['radius']*np.sin(angle)

if __name__ == "__main__":

    nParticles      =   2
    radii           =   0.5
    sim             =   Simulation(nParticles, radii)
