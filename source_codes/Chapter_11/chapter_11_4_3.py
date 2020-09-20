df_country = pd.read_csv('datasets/UNSD_country_data.csv', error_bad_lines=False)

df_country.columns

df_country.rename(
   columns={

df_country['LDC'].replace(['x'], ['yes'], inplace=True)

pd.crosstab(
   index=df_country['Region'],
   columns=df_country['DevelopedOrDeveloping'],
   margins=True)

pd.crosstab(
   index=[df_country['Region'], df_country['DevelopedOrDeveloping']],
   columns=df_country['LDC'],
   margins=True)

