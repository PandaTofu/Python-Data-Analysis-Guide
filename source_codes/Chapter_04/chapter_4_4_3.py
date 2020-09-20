import numpy as np

arr1 = np.arange(10)

arr1

np.delete(arr1, 4)

arr1

np.delete(arr1, [4, 8])

np.delete(arr1, slice(0, 9, 2))

arr2 = np.array([[0, 1, 2], [3, 4, 5],
                 [6, 7, 8], [9, 10, 11]])

np.delete(arr2, 0, axis=0)

np.delete(arr2, 0, axis=1)

np.delete(arr2, [1, 3], axis=0)

np.delete(arr2, [1, 2], axis=1)

np.delete(arr2, slice(0, None, 2), axis=0)

np.delete(arr2, [3, 4, 5])

