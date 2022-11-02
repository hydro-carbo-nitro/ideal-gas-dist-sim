#!/usr/bin/python3 
 
import numpy as np 
import random 
import matplotlib.pyplot as plt 
from matplotlib.patches import Circle
from matplotlib.animation import FuncAnimation 
import random 
  
pi            =    np.pi 
L            =    50 
nParticles    =    50
radii        =    2.0 
 
def init_fig(): 
    fig        =   plt.figure(figsize=(7, 7)) 
    ax        =   fig.add_axes([0.1, 0.1, 0.8, 0.8], frameon=True) 
 
    ax.set_xlim(-L, L) 
    ax.set_ylim(-L, L) 
    ax.set_xticks([]) 
    ax.set_yticks([]) 
 
    return fig, ax
    
def overlap(p_i, p_j): 
    dx    =    p_i['pos'][0] - p_j['pos'][0] 
    dy    =    p_i['pos'][1] - p_j['pos'][1] 
    d    =    p_i['rad'] + p_j['rad'] 
 
    return dx**2 + dy**2 < d**2 
 
 
def init_particles(idx_arr, radii): 
    p_arr = np.zeros(len(idx_arr), dtype=[    ('pos', float,  (2,)), 
                                            ('vel', float,  (2,)), 
                                            ('rad', float), 
                                            ('mass', float)]) 
 
    for idx in idx_arr:     # place {idx}th particle 
        target = 0
        
        p_arr[idx]['rad'] = radii
        p_arr[idx]['mass'] = p_arr[idx]['rad']**2
        p_arr[idx]['pos'] = (L - p_arr[idx]['rad']) * (2*np.random.rand(2) - 1)   #   place particle 
        v = 0.5
        vphi = random.random() * 2*pi 
        p_arr[idx]['vel'][0] = v * np.cos(vphi) 
        p_arr[idx]['vel'][1] = v * np.sin(vphi)
 
        while(target < idx):    # compare with {target}th particle
            print(f"{idx}, {target}, {overlap(p_arr[idx], p_arr[target])}")
            if overlap(p_arr[idx], p_arr[target]): 
                p_arr[idx]['pos']   =   (L - p_arr[idx]['rad']) * (2*np.random.rand(2) - 1)   #   replace particle 
                target  =   0   #   compare again from first 
            else:
                target += 1
 
    return p_arr 
 
def draw_circles(idx_arr, p_arr, ax): 
    #    draw circle 
    circles = []
    for idx in idx_arr: 
        circle = Circle(xy = p_arr[idx]['pos'], radius=p_arr[idx]['rad'], fill=False, color='r')
        circles.append(circle)
        ax.add_patch(circle)
    return circles
 
 
fig, ax = init_fig() 
setIdx = np.array(list(x for x in range(nParticles))) 
p = init_particles(setIdx, radii) 
c = draw_circles(setIdx, p, ax) 
 
def update(dt):         
    for idx in setIdx:
        #    ########################################################################################## 
        #    bouncing wih wall 
        #    ########################################################################################## 
        if p[idx]['pos'][0] > L - p[idx]['rad']:
            p[idx]['vel'][0] *= -1.0
            p[idx]['pos'][0] = L - p[idx]['rad']

        if p[idx]['pos'][1] > L - p[idx]['rad']:
            p[idx]['vel'][1] *= -1.0
            p[idx]['pos'][1] = L - p[idx]['rad']

        if p[idx]['pos'][0] < p[idx]['rad'] - L:
            p[idx]['vel'][0] *= -1.0
            p[idx]['pos'][0] = p[idx]['rad'] - L

        if p[idx]['pos'][1] < p[idx]['rad'] - L:
            p[idx]['vel'][1] *= -1.0
            p[idx]['pos'][1] = p[idx]['rad'] - L
 
        #    ########################################################################################## 
        #    collision 
        #    ########################################################################################## 
        for target in range(idx):
            if overlap(p[idx], p[target]): 
                print(f"{idx}, {target}") 
                m1, m2    =    p[idx]['mass'], p[target]['mass'] 
                M = m1 + m2 
                r1, r2    =    p[idx]['pos'], p[target]['pos'] 
                d        =    np.linalg.norm(r1 - r2)**2 
                v1, v2    =    p[idx]['vel'], p[target]['vel'] 
                u1        =    v1 - 2*m2 / M * np.dot(v1-v2, r1-r2) / d * (r1 - r2) 
                u2        =    v2 - 2*m1 / M * np.dot(v2-v1, r2-r1) / d * (r2 - r1) 
                 
                p[idx]['vel']        =    u1 
                p[target]['vel']    =    u2 
    for idx in setIdx: 
        p[idx]['pos']    +=  p[idx]['vel'] 
        c[idx].center    +=  p[idx]['vel']
         
    return c 
 
animation       =   FuncAnimation(fig, update, interval=20) 
plt.show() 
