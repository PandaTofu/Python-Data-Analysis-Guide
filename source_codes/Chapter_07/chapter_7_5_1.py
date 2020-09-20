from datetime import datetime

now = datetime.now()

now

now.year, now.month, now.day

dt = datetime(2020, 1, 1)

dt

str_time = "2020-02-14 07:00:00"

datetime.strptime(str_time, "%Y-%m-%d %H:%M:%S")

from datetime import timedelta

dt1 = datetime(2019, 10, 1, 8, 0)

dt2 = datetime(2019, 10, 7, 9, 30)

td = dt2 - dt1

td

td.days, td.seconds

import numpy as np

dt = datetime.now()

dt64 = np.datetime64(dt)

dt64

str(dt64)

print(dt64)

dt64 = np.datetime64('2020-08-20')

dt64

dt_list = ['2020-09-01', '2020-09-02', '2020-09-03']

np.array(dt_list, dtype=np.datetime64)

import pandas as pd

pd.to_datetime(datetime(2020, 1, 1))

pd.to_datetime(np.datetime64('2020-01-01'))

pd.to_datetime('2020-01-01')

dt = pd.to_datetime('2020-01-01 08:15:30')

dt.year, dt.month, dt.day

dt.hour, dt.minute, dt.second

pd.to_datetime('2020-01-02') - pd.to_datetime('2020-01-01')

