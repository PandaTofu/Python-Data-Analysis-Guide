import numpy as np

x = np.array([7, 2, 3, 1, 6, 5, 4, 9, 10, 8])

np.partition(x, 3)

np.partition(x, -3)

x2 = x.reshape(2, 5)

x2

np.partition(x2, 2, axis=1)

np.argpartition(x, 3)

x[np.argpartition(x, 3)]

