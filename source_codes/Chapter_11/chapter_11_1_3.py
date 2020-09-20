df.rolling(12).mean().iloc[:, :5]

df.rolling(window=12, min_periods=1).mean().iloc[:, :5]

df.rolling('365D').mean().iloc[:, :5]

df.expanding().mean().iloc[:, :5]

df.China['1990':'2000'].plot()

df.China['1990':'2000'].rolling('365D').mean().plot(linestyle='--')

df.China.rolling(12).mean().plot()

df.China.rolling(120).mean().plot()

