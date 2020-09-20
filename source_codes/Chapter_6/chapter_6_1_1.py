import pandas as pd

ser = pd.Series([0, 1, 2, 3])

ser

import numpy as np

pd.Series(np.random.randn(3))

pd.Series(np.random.randn(3), index=['x1', 'x2', 'x3'])

3})

3},
          index=['x0', 'x2', 'x3', 'x4'])

s1 = pd.Series([0, 1, 2, 3])

s1.values, s1.index

3})

s2.values, s2.index

s1[0]

s2[:-1]

import pandas as pd

ser = pd.Series([18.77, 15.63, 38.33],
                index=['Hebei', 'Shangxi', 'Yunnan'])

ser['Yunnan']

ser['Hebei']

import pandas as pd

10.20,

area_ser = pd.Series(area_dict)

area_ser

area_ser['Zhejiang']

'Shangxi']

