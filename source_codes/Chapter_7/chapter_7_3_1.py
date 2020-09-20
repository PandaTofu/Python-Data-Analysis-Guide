import numpy as np

import pandas as pd

['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three', 'two'],

df

df.groupby('A')

df.groupby('A').groups

gbs = df.groupby('A').groups

df.loc[gbs['one']]

df.loc[gbs['two']]

df.loc[gbs['three']]

for k, gb in df.groupby('A'):
    print("\ngroup name:", k)
    print(gb)

list(df.groupby('A'))

len(df.groupby('A'))

gb = df.groupby('A')

gb['A']

list(gb['A'])

gb['B']

list(gb['B'])

