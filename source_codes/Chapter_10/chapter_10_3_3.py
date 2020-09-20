df = ser_temp.unstack()

df.tail()

df['2000']

df['2000']

df = df['1900':'2000']

df.index

df.to_csv('datasets/Prepared_GlobalLandTemperaturesByCountry.csv')

pd.read_csv(
    'datasets/Prepared_GlobalLandTemperaturesByCountry.csv',
    index_col=[1]).iloc[:5, :5]

