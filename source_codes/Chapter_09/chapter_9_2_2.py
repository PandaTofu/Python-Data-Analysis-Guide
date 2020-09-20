import numpy

from pandas import DataFrame

import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1)

df = DataFrame(
    numpy.random.randint(10, size=(4, 3)),
    index=['r1', 'r2', 'r3', 'r4'],
    columns=['c1', 'c2', 'c3'])

df.plot(kind='bar', ax=ax)

df.plot(kind='barh', ax=ax)

