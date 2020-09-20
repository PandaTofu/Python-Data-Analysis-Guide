import numpy as np

arr1 = np.array([0, 1, None, 4])

arr1

arr1.sum()

arr2 = np.array([True, False])

arr2.dtype

arr2 = np.array([True, False, np.nan])

arr2.dtype

arr2 = np.array([0, 1, np.nan, 4])

arr2.sum()

np.nansum(arr2)

pd.Series([0, 1, np.nan, None])

ser = pd.Series(np.arange(2), dtype=int)

ser

ser[0] = None

ser

arr1 = np.array(['aa', 'bb', np.nan])

arr1

arr1[2] == 'nan'

arr1[2] is np.nan

ser = pd.Series(['aa', 'bb', np.nan, None])

ser

ser[2] is np.nan

ser[3] is None

