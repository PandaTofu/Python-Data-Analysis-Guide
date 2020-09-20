import numpy

import matplotlib.pyplot as plt

fig, ax = plt.subplots(1,1)

line1, = ax.plot(numpy.random.randn(30), 'k', label='item-1')

line2, = ax.plot(numpy.random.randn(30), 'k--')

line2.set_label('item-2')

ax.legend()

ax.legend((line1, line2), ('item-1', 'item-2'))

ax.legend(loc='upper right')

ax.legend(loc='best')

