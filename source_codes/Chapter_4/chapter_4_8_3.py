import numpy as np

data = np.random.randint(3, 8, 10)

np.min(data), np.max(data)

data.min(), data.max()

data

np.argmin(data)

np.argmax(data)

data[np.argmin(data)]

data[np.argmax(data)]

data = np.array([[1001, 172], [1002, 176], [1003, 168], [1004, 170], [1005, 165]])

data

data[np.argmin(data[:, -1])]

data[np.argmax(data[:, -1])]

