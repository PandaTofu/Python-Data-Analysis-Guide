import numpy as np

arr1 = np.arange(10)

arr1

arr1[:5]

arr1[5:]

arr1[3:7]

arr1[:]

arr1[::2]

arr1[1::2]

arr1[7:0:-1]

arr1[-1:0:-2]

arr2 = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])

arr2

arr2[:2, :2]

arr2[:3, ::2]

arr2[::-1, ::-1]

arr2[:2]

arr2[:2, :]

arr2[slice(0, 2)]

