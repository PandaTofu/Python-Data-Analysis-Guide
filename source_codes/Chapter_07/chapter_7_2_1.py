import numpy as np

import pandas as pd

ser = pd.Series(np.random.randn(8))

ser

np.mean(ser), np.std(ser)

np.random.randn(8),

df

np.max(df), np.min(df)

df.apply(np.median)

df.median()

['x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z'],

try:
    df.apply(np.prod)
except Exception as e:
    print(repr(e))

np.prod(df)

df.prod()

np.random.randn(6),

df

np.mean(df, axis=1)

df.mean(axis=1)

df.mean(axis='index')

df.mean(axis='rows')

df.mean(axis='columns')

