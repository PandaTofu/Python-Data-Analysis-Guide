import numpy as np

import pandas as pd

mul_ind = pd.MultiIndex.from_product([['x', 'z', 'y'], [1, 2]])

ser = pd.Series(np.random.rand(6), index=mul_ind)

try:
    ser['x':'y']
except KeyError as e:
    print(e)

ser_sorted = ser.sort_index()

ser_sorted

ser_sorted['x':'y']

mul_ind = pd.MultiIndex.from_tuples([
    ('Zhejiang', 2018), ('Zhejiang', 2019),
    ('Fujian', 2018), ('Fujian', 2019)])

pop_ser = pd.Series([5737, 5850, 3941, 3973], index=mul_ind)

df0 = pop_ser.unstack(level=0)

df0

df1 = pop_ser.unstack(level=1)

df1

df0.stack()

df1.stack()

pop_ser.index.names = ['province', 'year']

pop_ser.name = 'population'

pop_ser_flat = pop_ser.reset_index()

pop_ser_flat

pop_ser_flat.set_index(['province', 'year'])

