df_pg.pivot_table(values='body_mass_g', index='species', columns='island', aggfunc='std')

df_pg.pivot_table(values='body_mass_g', index='species', columns='island',
                  aggfunc=['mean', 'std'])

df_pg.pivot_table(index='species', columns='island',

df_pg.pivot_table(values='body_mass_g', index='species', columns='sex', margins=True)

df_pg.pivot_table(values='body_mass_g', index='species', columns='sex',
                  margins=True, margins_name='All Groups')

df_pg.pivot_table(values='body_mass_g', index='species',
                  columns='island', aggfunc='count')

df_pg.pivot_table(values='body_mass_g', index='species',
                  columns='island', aggfunc='count', fill_value=0)

flipper_len_mapping = pd.cut(df_pg['flipper_length_mm'], [190, 200, 210, 231, 240])

df_pg.pivot_table(values='body_mass_g', index=flipper_len_mapping)

df_pg.pivot_table(values='body_mass_g', index=flipper_len_mapping, dropna=False)

