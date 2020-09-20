import numpy as np

import pandas as pd

ser = pd.Series([0, np.nan, 2, None])

ser.isnull()

ser[ser.notnull()]

ser.dropna()

df = pd.DataFrame([[0, 1, 2],[3, np.nan, 5], [6, 7, None]])

df

df.dropna()

df.dropna(axis='columns')

df.iloc[:,2] = np.nan

df

df.dropna(axis='columns', how='all')

df.dropna(axis='rows', thresh=2)

ser

ser.fillna(0)

ser.fillna(method='ffill')

ser.fillna(method='bfill')

df

df.fillna(method='ffill')

df.fillna(method='ffill', axis='columns')

