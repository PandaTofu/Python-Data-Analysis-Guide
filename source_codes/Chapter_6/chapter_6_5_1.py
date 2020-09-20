import pandas as pd

mul_ind = pd.MultiIndex.from_tuples([
    ('Zhejiang', 2018), ('Zhejiang', 2019),
    ('Fujian', 2018), ('Fujian', 2019)])

mul_ind

pop_ser = pd.Series([5737, 5850, 3941, 3973], index=mul_ind, name='population')

pop_ser

pop_ser[:, 2018]

pop_df = pop_ser.unstack()

pop_df

pop_df.stack()

city_pop}, index=mul_ind)

pop_df

city_pop_ratio = pop_df['city'] / pop_df['total']

city_pop_ratio.unstack()

