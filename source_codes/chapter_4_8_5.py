import numpy as np

data = np.array([True, True, True])

np.all(data)

np.any(data)

data = np.array([True, True, False])

np.all(data)

np.any(data)

data = np.array([False, False, False])

np.all(data)

np.any(data)

data = np.array([-3, -1, 0, 1, 2])

np.all(data)

np.any(data)

np.array(data, dtype=np.bool)

data.all()

data.any()

data = np.array([75, 58, 80, 91])

(data < 60).any()

(data >= 60).all()

