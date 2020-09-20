df_year_gb = df_year.groupby('dt')

df_year_gb.mean().iloc[:, :5]

df_year_gb.agg(['mean', 'std']).iloc[:, :6]

df_year_gb.get_group(pd.Period('2000')).describe().iloc[:, :5]

