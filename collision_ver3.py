#!/usr/bin/python3

import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random
 
resolution      =   120
pi              =   np.pi
angle           =   np.linspace(0, 2*pi, resolution)
L               =   50
nParticles      =   25
radii           =   1.0

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
    p_arr = np.zeros(len(idx_arr), dtype=[('pos', float,  (2,)), ('vel', float,  (2,)), ('rad', float)])

	p_arr['rad'] = radii
	p_arr['pos'][:, 0]	=	(L - p_arr['rad']) * (2 * np.random.rand(len(idx_arr)) - 1)
	p_arr['pos'][:, 1]	=	(L - p_arr['rad']) * (2 * np.random.rand(len(idx_arr)) - 1)
	p_arr['vel'][:, 0]	=	np.random.rand(len(idx_arr)) * 1.0
	p_arr['vel'][:, 1]	=	np.random.rand(len(idx_arr)) * 1.0


#	###################################################################################################
#	repositioning particles which is overlapped
#
#	idx		:	Index of particle. If overlapped, change this one
#	target	:	Index of target particle.
#	judge	:	Is particle not overlapped?
#	###################################################################################################


    idx = 0
    while(idx < len(idx_arr)):	#	search for all index

        judge, target	=	0

        while(target < len(idx_arr)):	#	search for all index

            if idx != target:			#	idx and target must be different

                dx	=	p_arr[idx]['pos'][0] - p_arr[target]['pos'][0]	#	difference of x
                dy	=	p_arr[idx]['pos'][1] - p_arr[target]['pos'][1]	#	difference of y
                d	=	p_arr[idx]['rad'] + p_arr[target]['rad']		#	sum of radius

                if dx**2 + dy**2 <= d**2:								#	if they are overlapped

                    p_arr[idx]['pos'][0]	=	(L - p_arr[idx]['rad']) * (2*random.random() - 1)	#	x
                    p_arr[idx]['pos'][1]	=   (L - p_arr[idx]['rad']) * (2*random.random() - 1)	#	y
                    judge, target			=	0, 0	#	initialize judge and target

                else:
                    judge+=1			#	okay, pass
                    target+=1			#	okay, pass
            else:

                target+=1				#	there is no reason for comparing same particle

            if judge == len(idx_arr)-1:	#	if all particles passed

                idx+=1					#	new particle
                target=0				#	initialize target
                break

    return p_arr

def draw_circles(idx_arr, p_arr):
	#	draw circle
    c_arr		=	np.zeros(len(p_arr), dtype=[    ('x',   float,  (resolution,)),
                                                    ('y',   float,  (resolution,))])
    for idx in idx_arr:
        c_arr[idx]['x']		=	p_arr[idx]['pos'][0] + p_arr[idx]['rad'] * np.cos(angle)
        c_arr[idx]['y']		=	p_arr[idx]['pos'][1] + p_arr[idx]['rad']*np.sin(angle)

    return c_arr


setIdx          =   np.array(list(x for x in range(nParticles)))
p				=   init_particles(setIdx, radii)
c				=   draw_circles(setIdx, p)
fig, ax, line,  =   init_fig()

def update(dt):        
    for idx in setIdx:
        if not (p[idx]['pos'][0] >= -(L - p[idx]['rad']) and p[idx]['pos'][0] <= (L - p[idx]['rad'])): 
            p[idx]['vel'][0] *= -1.0

        if not (p[idx]['pos'][1] >= -(L - p[idx]['rad']) and p[idx]['pos'][1] <= (L - p[idx]['rad'])): 
            p[idx]['vel'][1] *= -1.0

        p[idx]['pos'][0]    +=  p[idx]['vel'][0]
        p[idx]['pos'][1]    +=  p[idx]['vel'][1]
        c[idx]['x']         +=  p[idx]['vel'][0]
        c[idx]['y']         +=  p[idx]['vel'][1]
        
    line.set_data(c['x'], c['y'])
    return line,

animation       =   FuncAnimation(fig, update, interval=1)
plt.show()
