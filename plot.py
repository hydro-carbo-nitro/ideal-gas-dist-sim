#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("./test.txt")

print(len(data))

plt.hist(data, bins=50)
plt.show()
