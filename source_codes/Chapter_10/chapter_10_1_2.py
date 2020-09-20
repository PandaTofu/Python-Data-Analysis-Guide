import pandas as pd

import numpy as np

cat datasets/GlobalLandTemperaturesByCountry.csv | head -5

df1 = pd.read_csv(
    'datasets/GlobalLandTemperaturesByCountry.csv',
    nrows=300000)

df2 = pd.read_csv(
    'datasets/GlobalLandTemperaturesByCountry.csv',
    nrows=300000,
    skiprows=range(1,299901))

