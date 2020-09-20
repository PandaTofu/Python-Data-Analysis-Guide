import numpy as np

arr2 = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])

arr2

arr2_copy = arr2.copy()

arr2_copy

arr2_copy[0] = 19

arr2_copy

arr2

row1_copy = arr2[1].copy()

row1_copy

row1_copy[0] = -3

row1_copy

arr2

arr2_subcopy = arr2[0:2].copy()

arr2_subcopy

arr2_subcopy[0] = 11

arr2_subcopy

arr2

