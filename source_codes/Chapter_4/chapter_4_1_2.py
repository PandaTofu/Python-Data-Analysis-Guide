import numpy as np

arr = np.array([0, 1, 2])

arr.dtype

np.dtype(np.int64)

arr1 = np.array([0, 1, 2], dtype=np.uint8)

arr2 = np.array([0, 1, 2], dtype=np.int16)

arr3 = np.array([0, 1, 2], dtype=np.float32)

arr4 = np.array([0j, 1j, 2j], dtype=np.complex64)

arr1.dtype, arr2.dtype, arr3.dtype, arr4.dtype

arr1.dtype, arr1.itemsize

np.dtype('f16')

arr

arr[0] = 3.888

arr

arr.astype(np.float64)

arr = np.array([1.2, 2.8, 3.9])

arr.astype(np.int64)

arr = np.array(['1.2', '2.8', '3.9'])

arr.dtype

arr.astype(np.float64)

