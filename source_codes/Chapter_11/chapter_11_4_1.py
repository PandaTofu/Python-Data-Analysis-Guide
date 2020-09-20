import numpy as np

import pandas as pd

df = pd.read_csv(
    'datasets/Prepared_GlobalLandTemperaturesByCountry.csv',
    index_col=0,
    parse_dates=['dt'],
    date_parser=pd.to_datetime).round(decimals=2)

df.columns.name = 'Country'

df_avgTemp = df.to_period('Y').stack().reset_index(name='avgTemp')

df_avgTemp

df_country_region = pd.read_csv(
    'datasets/UNSD_country_data.csv',
    error_bad_lines=False,
    usecols=[3, 8],
    index_col=1,
    header=0,
    names=['Region','Country'])

df_merged = pd.merge(df_avgTemp, df_country_region, on='Country')

df_merged

df_coor = pd.read_csv('datasets/world_coordinates.csv', usecols=[1,2])

df_merged = pd.merge(df_merged, df_coor, on='Country')

df_merged

df_merged.latitude = df_merged.latitude.apply(np.abs)
