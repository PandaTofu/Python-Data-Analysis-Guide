import numpy as np

import pandas as pd

list("ABABABABA"),

df.index.name = 'ID'

df

def print_groups(gb):
    for name, group in gb:
        print("---------------------------")

print_groups(df.groupby('i0'))

print_groups(df.groupby(by='i1'))

print_groups(df.groupby(by='ID'))

print_groups(df.groupby(by=['i0', 'i1']))

print_groups(df.groupby(df['c1'] > 0))

print_groups(df.groupby(df.dtypes, axis=1))

'night',

print_groups(df.groupby(mapping, axis=1))

print_groups(df.groupby(level=0))

print_groups(df.groupby(level='ID'))

df.set_index(['i0', 'i1'], append=True, inplace=True)

df

print_groups(df.groupby(level=1))

print_groups(df.groupby(level='i1'))

print_groups(df.groupby(level=['ID', 'i0']))

print_groups(df.groupby(level=[1, 2]))

df.reset_index(['i0', 'i1'], inplace=True)

df

print_groups(df.groupby(by=['i0', 'i1'], level='ID'))

print_groups(df.groupby(by=['i0', 'i1', 'ID']))

