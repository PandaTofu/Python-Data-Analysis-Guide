import numpy as np

np.array([1, 3, 5])

np.array((1, 3, 5))

arr1 = np.array([1, 3, 5], dtype=np.float64)

arr1.dtype

arr2 = np.array(([1, 3, 5], [2, 4, 6]))

arr2

arr2.ndim

arr2.shape

np.array(([1, 3, 5], [2, 4, 6]))

np.asarray((1, 3, 5))

arr0 = np.array((1, 3, 5))

arr1 = np.array(arr0)

arr2 = np.asarray(arr0)

arr0 is arr1

arr0 is arr2

