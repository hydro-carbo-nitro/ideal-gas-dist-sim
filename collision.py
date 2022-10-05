#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

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

    def __init__(self, n, radius):


    def setup_animation(self):
    def init_animation(self):





if __name__ == "__main__":
    nParticles  =   20
    radii       =   1
    sim         =   Simulation(nParticles, radii)
    sim.init_animation()
