import numpy as np

arr_x = np.random.randint(0, 10, (3, 4))

arr_y = np.random.randint(0, 10, 4)

arr_x

arr_y

arr_x - arr_y

import pandas as pd

df_x = pd.DataFrame(arr_x, columns=list('abcd'))

df_y = pd.Series(arr_y, index=list('abcd'))

df_x

df_y

df_x + df_y

df_x.add(df_x['c'], axis=0)

In [20]:

