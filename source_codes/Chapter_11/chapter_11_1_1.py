import numpy as np

import pandas as pd

df = pd.read_csv(
    'datasets/Prepared_GlobalLandTemperaturesByCountry.csv',
    index_col=0,
    parse_dates=['dt'],
    date_parser=pd.to_datetime).round(decimals=2)

df.index

