import pandas as pd

import seaborn

df_pg = seaborn.load_dataset('penguins')

df_pg.head()

df_pg.tail()

df_pg.groupby('sex').mean()

df_pg.pivot_table(index='sex')

mass_bins = df_pg['body_mass_g'].agg(['min', 'median', 'max'])

mass_bins

mass_mapping = pd.cut(df_pg['body_mass_g'], mass_bins)

mass_mapping

df_pg.groupby(['species', 'sex', mass_mapping]).mean()

'mean'})

df_pg_grouped = df_pg.groupby(['species', 'sex', mass_mapping])

'mean'}).unstack()

df_pg.pivot_table('flipper_length_mm', ['sex', mass_mapping], 'species')

df_pg.pivot_table('flipper_length_mm', mass_mapping, ['species', 'sex'])

