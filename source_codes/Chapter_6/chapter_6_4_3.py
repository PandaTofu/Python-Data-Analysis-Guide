import pandas as pd

employees = ['Mike', 'David', 'Erin']

df1 = pd.DataFrame([[172, 130], [178, 120], [165, 100]],
                   index = employees,
                   columns=['Height', 'Weight'])

df2 = pd.DataFrame([['M', 30], ['M', 26], ['F', 23]],
                    index = employees,
                    columns=['Gender', 'Age'])

df1

df2

df1.join(df2)

