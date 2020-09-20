import numpy as np

import pandas as pd

ser_x = pd.Series([0, 1, 2], index=['a', 'b', 'c'])

ser_y = pd.Series([2, 3, 4], index=['b', 'c', 'd'])

ser_x + ser_y

ser_x.index | ser_y.index

ser_x.reindex(ser_x.index | ser_y.index)

ser_y.reindex(ser_x.index | ser_y.index)

np.NaN + 0.0

ser_x.add(ser_y, fill_value=0.0)

df_x = pd.DataFrame(np.random.randint(0, 10, (4, 4)),
                    columns = ['c1', 'c2', 'c3', 'c4'])

df_y = pd.DataFrame(np.random.randint(0, 10, (3, 3)),
                    columns = ['c4', 'c1', 'c2'])

df_x + df_y

mean_v = df_y.stack().mean()

df_x.add(df_y, fill_value=mean_v)

