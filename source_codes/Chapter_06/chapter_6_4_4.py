import pandas as pd

employees = ['Mike', 'David', 'Erin']

height = [172, 178, 165]

weight = [130, 120, 100]

height})

weight})

df1

df2

pd.merge(df1, df2)

180}])

135}])

df1

df2

pd.merge(df1, df2)

df1['ID'] = employee_id

df2['ID'] = employee_id

df1

df2

pd.merge(df1, df2, on='ID')

pd.merge(df1, df2, on=['ID', 'name'])

'employee_ID'}, inplace=True)

pd.merge(df1, df2, left_on='ID', right_on='employee_ID')

df3 = df1.set_index('ID')

df4 = df2.set_index('employee_ID')

df3

df4

pd.merge(df3, df4, left_index=True, right_index=True)

pd.merge(df3, df4, left_index=True, right_index=True, suffixes=('_1', '_2'))

170}])

'ID'}, inplace=True)

120}])

df1

df2

pd.merge(df1, df2)

pd.merge(df1, df2, how='outer')

pd.merge(df1, df2, how='left')

pd.merge(df1, df2, how='right')

