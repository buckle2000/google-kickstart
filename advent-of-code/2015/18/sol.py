#!/usr/bin/env python

import sys
fin = sys.argv[1]
lines = open(fin).readlines()

import numpy as np
from scipy.signal import convolve2d

lights = np.zeros((len(lines), len(lines[0].strip())), dtype=bool)

for y, line in enumerate(lines):
    line = line.strip()
    for x, light in enumerate(line):
        if light == '#':
            lights[y, x] = True

print(lights.shape)
f = np.ones((3, 3), dtype=int)
f[1, 1] = 0

def init():
    global lights
    lights[0,0] =True
    lights[0,-1] =True
    lights[-1,-1] =True
    lights[-1,0] =True

init()

def step():
    global lights
    status = convolve2d(lights, f, mode='same')
    lights = (lights & (status == 2)) | (status == 3)
    init()
# step()
# step()
# step()
# step()
# print(lights)

for _ in range(100):
    step()

print(np.sum(lights))
# print(lights)