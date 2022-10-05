#!/usr/bin/python3

import numpy as np
import random

pi = np.pi

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
        self.init_particles(nParticles, radii)

    def init_particles(self, nParticles, radii):
        self.particles = []

        for i in range(nParticles):
            x, y = random.random()*10, random.random()*10
            vx, vy = random.random(), random.random()
            rad = random.random()*radii

            particle = self.ParticleClass(x, y, vx, vy, rad)
            self.particles.append(particle)



if __name__ == "__main__":
    nParticles      =   20
    radii           =   0.1
    sim             =   Simulation(nParticles, radii)

    for i in range(nParticles):
        pos = sim.particles[i].position
        vel = sim.particles[i].velocity
        rad = sim.particles[i].radius
        print(f"Particle {i} : pos{pos}, vel{vel}, rad{rad}")
