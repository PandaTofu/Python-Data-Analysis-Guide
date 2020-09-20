import numpy as np

np.zeros(5)

np.zeros((3, 3))

np.ones(6)

np.ones((3, 5))

arr0 = np.zeros(3)

arr0.dtype

arr1 = np.ones(3)

arr1.dtype

np.zeros(3, dtype=np.int32)

np.ones(3, dtype=np.int16)

np.full(3, 8)

np.full((3, 4), 6)

np.full((3, 4), 6, dtype=np.float32)

arr = np.array([[0, 1, 2], [3, 4, 5]])

arr

np.zeros_like(arr)

np.ones_like(arr)

np.full_like(arr, 6)

np.full(arr.shape, 6)

arr = np.array([[1.1, 2.2], [3.3, 4.4], [5.5, 6.6]])

arr_f = np.full(arr.shape, 8)

arr_fl = np.full_like(arr, 8)

arr.shape, arr.dtype

arr_f.shape, arr_f.dtype

arr_fl.shape, arr_fl.dtype

arr_fl = np.full_like(arr, 8, dtype=np.int64)

arr_fl.shape, arr_fl.dtype

