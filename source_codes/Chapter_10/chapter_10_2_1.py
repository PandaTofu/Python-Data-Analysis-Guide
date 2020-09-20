df.duplicated(subset=['dt', 'Country']).sum()

df.drop_duplicates(subset=['dt', 'Country'], inplace=True)

df.duplicated(subset=['dt', 'Country']).sum()

