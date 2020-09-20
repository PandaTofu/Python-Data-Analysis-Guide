import numpy

from pandas import DataFrame

import matplotlib.pyplot as plt

x = numpy.arange(100)

y1 = numpy.random.uniform(0,1,100)

y2 = numpy.random.standard_normal(100)

y2})

df.plot(ax=ax, kind='scatter', x='x', y='y1', marker='o', label='uniform')

df.plot(ax=ax, kind='scatter', x='x', y='y2', marker='x', label='standard normal')

