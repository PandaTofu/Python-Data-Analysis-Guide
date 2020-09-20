import numpy

data = numpy.random.randn(15)

import matplotlib.pyplot as plt

plt.plot(data, color='k’)

plt.plot(data, color='#FFFFFF')

plt.plot(data, linestyle='--')

plt.plot(data, marker='x')

plt.plot(data, color='k', marker='x', linestyle='--')

plt.plot(data, ‘kx--’)

