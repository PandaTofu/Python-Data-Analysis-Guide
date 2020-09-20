cat datasets/UNSD_country_data.csv | head -5

df_country = pd.read_csv('datasets/UNSD_country_data.csv', error_bad_lines=False)

df = df[df['Country'].isin(df_country['Country or Area'])]

