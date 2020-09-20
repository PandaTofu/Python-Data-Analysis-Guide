import pandas as pd

mul_ind = pd.MultiIndex.from_tuples([
    ('Zhejiang', 2018), ('Zhejiang', 2019),
    ('Fujian', 2018), ('Fujian', 2019)])

total_pop = [5737, 5850, 3941, 3973]

city_pop = [3847, 3953, 2534, 2594]

city_pop}, index=mul_ind)

pop_df

pop_df[:2]

pop_df.iloc[:2, :1]

pop_df.loc[:, 'city']

pop_df.loc[('Zhejiang', (2018, 2019)), ('city')]

pop_df.loc[ids['Zhejiang', :], ids['city']]

