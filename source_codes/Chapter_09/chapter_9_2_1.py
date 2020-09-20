import numpy

from pandas import DataFrame

data = numpy.random.randn(30,3)

df = DataFrame(data.cumsum(0), columns=['g1', 'g2', 'g3'])

ax = df.plot()

fig = ax.get_figure()

fig.savefig('fig9-7.png')

ax = df.plot(yticks=numpy.arange(-4,7))

