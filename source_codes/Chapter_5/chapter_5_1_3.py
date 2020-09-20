import numpy as np

x1 = np.arange(3)

x2 = np.ones([3, 3])

x1

x1.shape

x2

x2.shape

x1 + x2

x = np.arange(3)

y = x.reshape((3, 1))

x

x.shape

y

y.shape

z = x + y

z

z.shape

x = np.arange(3)

y = np.ones((3, 2))

try:
    x + y
except ValueError as e:
    print(repr(e))

