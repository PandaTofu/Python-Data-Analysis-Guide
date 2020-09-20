import numpy as np

arr = np.array([ 0,  1,  2,  3,  9, 10])

arr1, arr2, arr3 = np.split(arr, 3)

print(arr1, arr2, arr3)

arr1, arr2, arr3 = np.split(arr, [3, 5])

print(arr1, arr2, arr3)

arr = np.arange(16).reshape((4, 4))

arr

arr1, arr2 = np.vsplit(arr, [2])

arr1

arr2

arr3, arr4 = np.hsplit(arr, [2])

arr3

arr4

