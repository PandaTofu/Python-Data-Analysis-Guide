import numpy as np

x = np.array([5, 3, -1, -8])

abs(x)

np.abs(x)

y = np.array([1+0j, 0+2j, 3+4j, 4+3j])

abs(y)

np.abs(y)

x

x.dtype

np.abs(x)

np.abs(x).dtype

np.fabs(x)

np.fabs(x).dtype

x = np.random.randint(1, 10, 50)

%timeit np.abs(x)

%timeit np.fabs(x)

