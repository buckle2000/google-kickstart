import numpy as np
import sys, re

screen = np.zeros((50, 6), dtype=bool)

for line in sys.stdin:
    if line.startswith("rect"):
        match = re.match(r"rect (\d+)x(\d+)", line)
        a, b = map(int, match.groups())
        screen[0:a, 0:b] = True
    elif line.startswith("rotate row"):
        match = re.match(r"rotate row y=(\d+) by (\d+)", line)
        a, b = map(int, match.groups())
        screen[:, a] = np.roll(screen[:, a], b)
    elif line.startswith("rotate column"):
        match = re.match(r"rotate column x=(\d+) by (\d+)", line)
        a, b = map(int, match.groups())
        screen[a, :] = np.roll(screen[a, :], b)

import matplotlib.pyplot as plt

# I wonder how the author did this
plt.imshow(screen.T)
plt.show()
print(np.sum(screen))