#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.animation import FuncAnimation


class Particle:
	def __init__(self, x, y, vx, vy, radius):
		self.pos = np.array((x, y))
		self.vel = np.array((vx, vy))
		self.rad = radius
		self.mass = self.rad ** 2


	# Getter and Setter
	@property
	def x(self): return self.pos[0]
	@property
	def y(self): return self.pos[1]
	@property
	def vx(self): return self.vel[0]
	@property
	def vy(self): return self.vel[1]

	@x.setter
	def x(self, value): self.pos[0] = value
	@y.setter
	def y(self, value): self.pos[1] = value
	@vx.setter
	def vx(self, value): self.vel[0] = value
	@vy.setter
	def vy(self, value): self.vel[1] = value


	def DrawCircle(self, ax):
		circle = Circle(xy=self.pos, radius=self.rad, fill=False, color='r')
		ax.add_patch(circle)
		return circle

	def Overlap(self, target): return np.hypot(*(self.pos - target.pos)) < (self.rad + target.rad)

class Simulation:
	ParticleClass = Particle

	def __init__(self, nParticles, L, radii):
		self.L = L
		self.radii = radii
		self.nParticles = nParticles

		self.InitParticles(nParticles)
	
		for p in self.particles:
			print(f"{p.x:.2f}\t{p.y:.2f}\t/ {p.vx:.2f}\t{p.vy:.2f}\t/ {p.rad}")

		self.SetFigure(L)
		anim = FuncAnimation(self.fig, self.update, init_func=self.init, interval=1)
		plt.show()

	def InitParticles(self, nParticles):
		self.particles = []
		for idx in range(nParticles):
			radius = self.radii
			x, y = (self.L - radius) * (2 * np.random.rand(2) - 1)
			v = 0.5
			vphi = 2 * np.pi * np.random.rand()
			vx, vy = v*np.cos(vphi), v*np.sin(vphi)

			particle = self.ParticleClass(x, y, vx, vy, radius)

			target = 0
			while(target < idx):
				if particle.Overlap(self.particles[target]):
					particle.x, particle.y = (self.L - radius) * (2 * np.random.rand(2) - 1)
					target = 0
				else: target += 1

			self.particles.append(particle)

	def SetFigure(self, L):
		self.fig = plt.figure(figsize=(7, 7))
		self.ax = self.fig.add_axes([0.1, 0.1, 0.8, 0.8], frameon=True)

		self.ax.set_xlim(-L, L)
		self.ax.set_ylim(-L, L)
		self.ax.set_xticks([])
		self.ax.set_yticks([])

	def collision(self, p1, p2):
		M = p1.mass + p2.mass
		d = np.linalg.norm(p1.pos - p2.pos)**2
		p1.vel = p1.vel - 2*p2.mass / M * np.dot(p1.vel - p2.vel, p1.pos - p2.pos) / d * (p1.pos - p2.pos)
		p2.vel = p2.vel - 2*p1.mass / M * np.dot(p2.vel - p1.vel, p2.pos - p1.pos) / d * (p2.pos - p1.pos)

	def init(self):
		self.circles = []
		for particle in self.particles:
			self.circles.append(particle.DrawCircle(self.ax))
		return self.circles

	def update(self, dt):
		for i in range(self.nParticles):
			p = self.particles[i]

			# Bouncing on the wall
			if p.x > self.L - p.rad:
				p.x = self.L - p.rad
				p.vx *= -1.0
			if p.x < p.rad - self.L:
				p.x = p.rad - self.L
				p.vx *= -1.0
			if p.y > self.L - p.rad:
				p.y = self.L - p.rad
				p.vy *= -1.0
			if p.y < p.rad - self.L:
				p.y = p.rad - self.L
				p.vy *= -1.0
			
			# Collision
			for j in range(i):
				q = self.particles[j]

				if p.Overlap(q):
					self.collision(p, q)
		
		for i in range(self.nParticles):
			p = self.particles[i]
			c = self.circles[i]
			p.pos += p.vel
			c.center = p.pos

		return self.circles



if __name__=="__main__":
	wow = Simulation(50, 50, 1)
	
