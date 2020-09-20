import numpy as np

x = np.linspace(0, 5, 6)

cond = np.array([False, True, True, True, True, True])

x, cond

np.prod(x, where=cond)

np.prod(x, where=(x != 0))

x[2] = np.nan

x

np.sum(x, where=~ np.isnan(x))

x = np.random.randint(1, 10, 5).astype(np.float64)

x[-1] = 1000

x

cond = np.array([True, True, True, True, False])

np.max(x, where=cond, initial=-np.inf)

x[-1] = 0.01

x

x, cond

np.min(x, where=cond, initial=np.inf)

np.multiply.reduce(x, axis=0, where=(x!=0))

