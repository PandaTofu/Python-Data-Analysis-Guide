df.iloc[:5, :5]

df_year = df.to_period('Y')

df_year.iloc[:5, :5]

df_year.groupby('dt').mean().iloc[:5, :5]

df_year.pivot_table(index=['dt']).iloc[:5, :5]

