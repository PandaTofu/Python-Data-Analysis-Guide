import numpy as np

x = np.arange(9)

x

np.add.reduce(x)

np.sum(x)

x = np.arange(1, 5)

x

np.multiply.reduce(x)

np.prod(x)

x = np.random.randint(1, 10, 6)

x

np.maximum.reduce(x)

np.max(x)

np.minimum.reduce(x)

np.min(x)

x = np.random.randint(1, 10, (3, 3))

x

np.add.reduce(x)

np.add.reduce(x, axis=1)

np.maximum.reduce(x, axis=0)

np.minimum.reduce(x, axis=1)

np.add.reduce(x, axis=None)

x = np.random.randint(1, 10, 9)

x

np.add.accumulate(x)

np.cumsum(x)

np.multiply.accumulate(x)

np.cumprod(x)

x = np.ones(3) * 2

x

np.power.accumulate(x)

x = np.arange(1, 10)

x

np.multiply(x, x)

np.multiply.outer(x, x)

x = np.random.randint(1, 10, 5)

y = np.random.randint(1, 10, 5)

x

y

np.maximum.outer(x, y)

