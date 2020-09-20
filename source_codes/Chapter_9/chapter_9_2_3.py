import numpy

from pandas import Series

import matplotlib.pyplot as plt

fig, axes = plt.subplots(2,1)

s = Series(numpy.random.standard_normal(1000))

s.plot(ax=axes[0], kind='hist', bins=50)

s.plot(ax=axes[1], kind='kde')

