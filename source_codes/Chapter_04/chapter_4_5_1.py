import numpy as np

arr2 = np.random.randint(0, 10, size=(4, 3))

arr2

arr2.shape

arr2.ravel()

arr1 = np.ravel(arr2)

arr1

arr1.shape

arr_rs = np.reshape(arr2, 12)

arr_rs

arr2.shape

arr_rs.shape

arr_rs = np.reshape(arr2, (2, 6))

arr_rs

arr2.shape

arr_rs.shape

arr_rs = np.reshape(arr2, newshape=(2, 2, 3))

arr_rs

arr2.shape

arr_rs.shape

arr2.size

arr_rs.size

np.reshape(arr2, -1)

np.reshape(arr2, newshape=(6, -1))

arr2.reshape((2, 6))

arr2.reshape(2, 6)

arr2.reshape(-1)

arr2.reshape(3, -1)

arr2.reshape(3, 2, -1)

arr2.reshape(3, 4)

arr2.shape

arr2.resize(3, 4)

arr2

arr2.shape

