import pandas as pd

ser = pd.Series([0, 1, 2], index=['x', 'y', 'z'])

ser

ser['x']

'y' in ser

ser.keys()

list(ser.items())

ser['v'] = 10

ser

import pandas as pd

ser = pd.Series([0.1, 0.2, 0.3, 0.4, 0.5],
                index = ['a', 'b', 'c', 'd', 'e'])

ser['b':'d']

ser[1:3]

ser[(ser > 0.1) & (ser < 0.5)]

ser[['b', 'e']]

import pandas as pd

ser = pd.Series(['a', 'b', 'c', 'd'], index=[1, 3, 5, 7])

ser

ser[1]

ser[1:3]

ser.loc[1]

ser.loc[1:3]

ser.iloc[1]

ser.iloc[1:3]

