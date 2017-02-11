import numpy as np
import matplotlib.pyplot as plt

plt.axis([0, 10, 0, 1])
plt.ion()
x = []
y = []
for i in xrange(10):
    x.append(i)
    y.append(np.random.random())

plt.scatter(x, y)

