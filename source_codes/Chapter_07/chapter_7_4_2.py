import pandas as pd

import seaborn

df_pg = seaborn.load_dataset('penguins')

df_pg.pivot_table('body_mass_g', 'species', 'sex')

df_pg.pivot_table(values='bill_depth_mm', index='species')

df_pg.pivot_table(index='species')

df_pg.pivot_table(values=None, index='species')

df_pg.pivot_table(values=['bill_depth_mm', 'bill_length_mm'], columns='sex')

df_pg.pivot_table(columns='island')

flipper_len_mapping = pd.cut(df_pg['flipper_length_mm'], [190, 200, 210, 231])

flipper_len_mapping

df_pg.pivot_table(index=flipper_len_mapping)

island_cond = (df_pg['island'] == 'Biscoe')

island_cond

df_pg.pivot_table(columns=island_cond)

df_pg.pivot_table(values=['bill_depth_mm', 'bill_length_mm'],
                  index=['species', flipper_len_mapping],
                  columns=['sex', island_cond])

