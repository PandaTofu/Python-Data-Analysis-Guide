import numpy as np

import pandas as pd

data = np.concatenate([np.random.normal(3, 1.5, 6), np.random.normal(11, 0.5, 6)])

ser = pd.Series(data, index=list('AAAAAABBBBBB'))

ser

ser.mean(level=0)

ser.std(level=0)

data1 = np.concatenate([np.random.normal(3, 1.5, 6), np.random.normal(11, 0.5, 6)])

data2 = np.concatenate([np.random.normal(0, 1, 6), np.random.normal(32, 2.5, 6)])

data2}, index=list('AAAAAABBBBBB'))

df

df.mean(level=0)

df.std(level=0)

list("AAAAAABBBBBB"),

df

df.set_index(['i0', 'i1'], inplace=True)

df

df.sum(level=0)

df.sum(level=1)

df.mean(level='i0')

df.std(level='i1')

df.sum(level=[0, 1])

df.prod(level=['i1', 'i0'])

