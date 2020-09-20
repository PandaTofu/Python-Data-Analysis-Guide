import pandas as pd

10.20,

5442,

area_ser = pd.Series(area_data)

pop_ser = pd.Series(pop_data)

pop_ser})

df

df['area'], df['population']

df.area, df.population

df['area'] is df.area

df['population'] is df.population

df.columns = ['area', 'pop']

df

df.pop is df['pop']

df['density'] = df['pop'] / df['area']

df

df.values

df.T

df.values[0, 0]

df.iloc[:4, :]

df.loc[:'Fujian', :'pop']

df.loc[df.density > 300, ['area', 'pop']]

df.iloc[0, 2] = 500.0

df

df.loc['Zhejiang', 'density'] = 533.5

df

