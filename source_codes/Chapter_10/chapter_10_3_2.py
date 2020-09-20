mul_index = pd.MultiIndex.from_arrays([df.dt, df.Country])

ser_temp = pd.Series(df['AverageTemperature'].values, index=mul_index)

ser_temp.tail()

