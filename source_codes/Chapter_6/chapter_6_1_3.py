import pandas as pd

ind = pd.Index([7, 9, 11, 3, 5])

ind

ind[0]

ind[::2]

ind.size, ind.shape, ind.ndim, ind.dtype

ind[0] = 0

ind_a = pd.Index([3, 5, 7, 9, 11])

ind_b = pd.Index([17, 15, 10, 5, 9])

ind_a & ind_b

ind_a | ind_b

ind_a ^ ind_b

ind_a.intersection(ind_b)

ind_a.union(ind_b)

ind_a.symmetric_difference(ind_b)

