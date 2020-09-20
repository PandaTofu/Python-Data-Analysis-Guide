from datetime import datetime

import numpy as np

import pandas as pd

timestamps = [datetime(2020, 1, x) for x in np.arange(1, 6)]

ts = pd.Series(np.random.randint(1, 10, 5), index=timestamps)

ts

ts.index

ts.index.dtype

ts.index[0]

pd.DatetimeIndex([datetime(2020, 1, 1), datetime(2020, 1, 2)])

pd.DatetimeIndex([np.datetime64('2020-01-01'), np.datetime64('2020-01-02')])

pd.DatetimeIndex([pd.Timestamp('2020-01-01'), pd.Timestamp('2020-01-02')])

pd.to_datetime(['2020-01-01', '2020-01-01'])

pd.to_datetime(np.array(['2020-01-01', '2020-01-01'], dtype=np.datetime64))

dt_index = pd.date_range('2020-01-01', '2020-01-06', freq='1D')

dt_index

dt_index.year

dt_index.month

dt_index.day

dt_index.weekday

ts = pd.Series(np.random.randn(365),
               index=pd.date_range('2019-01-01', periods=365, freq='D'))

ts

ts.index

pd_index = ts.index.to_period('M')

pd_index

pd_index = ts.index.to_period('Q')

pd_index

pd_index[0]

pd_index[0].start_time, pd_index[0].end_time

pd_index.is_unique

np.unique(pd_index)

ts

ts = ts.to_period('M')

ts

ts_gp = ts.groupby(level=0).mean()

ts_gp

ts_gp.index

ts_gp.index.is_unique

pd_index = pd.period_range('2019-01', '2019-12', freq='4M')

pd_index

pd_index[-1]

pd_index[-1].start_time, pd_index[-1].end_time

pd_index = pd.period_range('2019-01', periods=4, freq='4M')

pd_index

pd_index[-1]

pd_index[-1].start_time, pd_index[-1].end_time

td_index = pd.timedelta_range('1 days', periods=30, freq='2D')

td_index

ts = pd.Series(np.random.randn(30), index=td_index)

ts

td_index[0]

ts = pd.Series(np.random.randn(10),
     index=pd.date_range('2019-06-01', periods=10, freq='3D'))

ts

ts.index.to_perioddelta(freq='M')

dt_index = pd.date_range('2019-06-03', periods=30, freq='2D')

dt_index.to_perioddelta(freq='M')

