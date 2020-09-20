cat examples/example_6_1.csv

import pandas

data_df = pandas.read_csv('examples/example_6_1.csv')

data_df

cat examples/example_6_4.csv

data_df = pandas.read_table('examples/example_6_4.csv')

data_df

cat examples/example_6_5.csv

pandas.read_csv('examples/example_6_5.csv', sep='\s+')

pandas.read_table('examples/example_6_5.csv', sep='\s+')

cat examples/example_6_6.csv

pandas.read_csv('examples/example_6_6.csv', header=None)

cat examples/example_6_7.csv

pandas.read_csv('examples/example_6_7.csv')

cat examples/example_6_8\.csv

pandas.read_csv('examples/example_6_8.csv', skiprows=[1,3])

cat examples/example_6_9.csv

pandas.read_csv('examples/example_6_9.csv', na_values=['NA', 'NULL'])

from pandas import Series

row_index = ['r1', 'r2', 'r3']

s1 = Series([1, 2, 3], index=row_index)

s1.to_csv('series_export.csv')

cat series_export.csv

from pandas import DataFrame

s2 = Series([4, 5, 6], index=row_index)

s2})

df.to_csv('df_export.csv')

cat df_export.csv

df.to_csv('df_export.csv', sep=';')

cat df_export.csv

df.to_csv('df_export.csv', index=False, header=False)

cat df_export.csv

df['c1']['r3'] = None

df.to_csv('df_export.csv', na_rep='NA')

cat df_export.csv

