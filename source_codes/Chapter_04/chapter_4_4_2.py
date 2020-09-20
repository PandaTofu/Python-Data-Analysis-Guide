import numpy as np

arr1 = np.arange(5)

arr1

np.insert(arr1, 3, -7)

arr1_insert = np.insert(arr1, 0, 9)

arr1_insert

arr1

np.insert(arr1, [1, 2], 6)

np.insert(arr1, [1, 2], [6, 7])

arr2 = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])

arr2

np.insert(arr2, 0, 9, axis=0)

np.insert(arr2, 0, [9, 10 , 11], axis=0)

np.insert(arr2, 2, [9, 10 , 11], axis=1)

arr2.shape

np.insert(arr2, 3, 10, axis=1)

np.insert(arr2, [0, 3], 12, axis=0)

arr_add = np.eye(3)

arr_add

np.insert(arr2, [1, 2], arr_add[:2], axis=0)

np.insert(arr2, [0, 1], arr_add[:, :2], axis=1)

np.insert(arr2, [0, 1], [31, 32, 33], axis=0)

arr3 = np.random.rand(3, 4, 4)

arr2_add = np.random.rand(4, 4)

arr3

arr2_add

np.insert(arr3, 0, arr2_add, axis=0)

np.insert(arr2, 3, 99)

np.insert(arr2, slice(0, 3), 99, axis=0)

