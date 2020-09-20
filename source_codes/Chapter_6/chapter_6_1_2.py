import numpy as np

import pandas as pd

arr = np.zeros((3, ), dtype=[('A', 'i4'), ('B', 'f4'), ('C', 'a10')])

arr[:] = [(1, 2, 'x1'), (3, 4, 'x2'), (5, 6, 'x3')]

pd.DataFrame(arr)

pd.DataFrame(arr,
             index=['row1', 'row2', 'row3'],
             columns=['C', 'A', 'B'])

pd.Series([1, 2, 3], index=['r1', 'r2', 'r3']),

df = pd.DataFrame(data)

df

[1., 2., 3., 4.],

pd.DataFrame(d)

[0, 1, 2, 3],

pd.DataFrame(data)

pd.DataFrame(data, index=['r1', 'r2', 'r3', 'r4'], columns=['A', 'C'])

-5}]

pd.DataFrame(data)

4}]

df = pd.DataFrame(data, index = ['row1', 'row2'])

df.index

df.columns

10.20,

area_ser = pd.Series(area_data)

5442,

pop_ser = pd.Series(pop_data)

area_ser, pop_ser

pop_ser})

df

df['area']

