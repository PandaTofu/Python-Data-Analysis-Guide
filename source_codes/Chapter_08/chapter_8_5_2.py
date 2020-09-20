import pandas

df = pandas.read_excel('examples/example_6_10.xlsx')

df

df = pandas.read_excel('examples/example_6_10.xlsx', 'Sheet1')

data_file = pandas.ExcelFile('examples/example_6_10.xlsx')

pandas.read_excel(data_file, 'Sheet1')

df = pandas.read_excel('examples/example_6_10.xlsx', 'Sheet1', header=None)

df

from pandas import DataFrame

df = DataFrame([(1,2,3), (4,5,6)], index=['r1','r2'], columns=['c1','c2','c3'])

df.to_excel('pandas_excel_export.xlsx')
