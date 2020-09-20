import pandas as pd

pd.MultiIndex.from_tuples([('x', 1), ('x', 2), ('y', 1), ('y', 2)])

pd.MultiIndex.from_arrays([['x', 'x', 'y', 'y'], [1, 2, 1, 2]])

df = pd.DataFrame([['x', 1], ['x', 2], ['y', 1], ['y', 2]])

pd.MultiIndex.from_frame(df)

pd.MultiIndex.from_product([['x', 'y'], [1, 2]])

pd.MultiIndex(levels=[['x', 'y'], [1, 2]],
              codes=[[0, 0, 1, 1], [0, 1, 0, 1]])

ind = pd.MultiIndex.from_product([['x', 'y'], [1, 2]])

ind.names = ['axis', 'ID']

ind

