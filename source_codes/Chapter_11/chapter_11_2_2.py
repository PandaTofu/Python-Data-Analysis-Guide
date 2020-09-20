df.mean()

df.mean(axis='columns')

df.aggregate(['mean', 'std'], axis='columns')

df.agg(['max', 'idxmax']).T

