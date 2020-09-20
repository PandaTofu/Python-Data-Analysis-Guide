import numpy as np

import pandas as pd

['A', 'A', 'B', 'C', 'B', 'B', 'A', 'C', 'B'],

df

df.groupby('c1').mean()

df_gb.describe()

import seaborn

df_iris = seaborn.load_dataset('iris')

df_iris

df_iris.groupby('species').agg(['mean', 'std'])

df_iris_gbs = df_iris.groupby('species')[['petal_length', 'petal_width']]

df_iris_gbs.agg(['max', 'median', 'min']).unstack()

df_iris_gbs = df_iris.groupby([df_iris['petal_length'] > 1.6, 'species'])

'mean'})

