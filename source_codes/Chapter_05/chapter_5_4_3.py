import numpy as np

x = np.arange(12).reshape(3, 4)

x

x[1, [3, -2, 0]]

x[1:, [0, 1, 3]]

mask = np.array([True, False, True, False])

x[:2, mask]

row = np.array([0, 2]).reshape(2, 1)

x[row, mask]

