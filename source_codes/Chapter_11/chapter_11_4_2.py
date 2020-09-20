df_merged.pivot_table(values='avgTemp', index='dt', columns='Country').iloc[:, :5]

df_merged.pivot_table('avgTemp', index=['dt', 'Region'])

df_merged.pivot_table('avgTemp', index='dt', columns='Region', margins=True)

df_merged.pivot_table('avgTemp', index=['dt'], columns=['Region', zones]).iloc[:, :6]

df_merged.pivot_table(
    values='avgTemp',
    aggfunc='std',
    index='dt',
    columns='Region',
    margins=True)

df_merged.pivot_table(

