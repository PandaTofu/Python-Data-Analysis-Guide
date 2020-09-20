import numpy as np

import pandas as pd

ts = pd.Series(np.random.randn(90),
               index=pd.date_range('2019-12-01', periods=90, freq='D'))

ts

ts[3]

ts.index[3]

ts[ts.index[3]]

ts['2019-12-03']

ts['12/3/2019']

ts = pd.Series(np.random.randn(8),
               index=pd.period_range('2019-01-01', periods=8, freq='Q'))

ts

ts['2019Q1']

ts = pd.Series(np.random.randn(30),
               index=pd.timedelta_range('3 days', periods=30, freq='6D'))

ts

ts['21 days']

ts['21D']

ts['3W']

ts = pd.Series(np.random.randn(90),
               index=pd.date_range('2019-12-01', periods=90, freq='D'))

ts

ts['2019']

ts['2020-01']

ts['2019-12-10':]

ts['12/29/2019':'1/15/2020']

ts[:'2020-01-03':3]

ts[:'2019-12-30']

