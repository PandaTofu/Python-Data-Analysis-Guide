df.isnull().sum()

df.fillna(method='ffill', inplace=True)

df.isnull().sum()

