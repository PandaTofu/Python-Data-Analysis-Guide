import numpy as np

arr1_1 = np.arange(6)

arr1_2 = np.arange(4)

arr1_1

arr1_2

np.append(arr1_1, arr1_2)

arr2_1 = np.random.randint(1, 10, (2, 2))

arr2_1

np.append(arr1_1, arr2_1)

arr2_2 = np.random.randint(1, 10, (3, 2))

arr2_1

arr2_2

np.append(arr2_1, arr2_2, axis=0)

arr3_1 = np.random.randint(1, 10, (2, 3, 4))

arr3_2 = np.random.randint(1, 10, (3, 3, 4))

arr3_1

arr3_2

arr3_1.shape

arr3_2.shape

arr3_merged = np.append(arr3_1, arr3_2, axis=0)

arr3_merged

arr3_merged.shape

arr1_3 = np.random.randint(1, 10, 3)

arr1_1

arr1_2

arr1_3

np.concatenate((arr1_1, arr1_2, arr1_3))

arr1_1

arr2_1

arr3_1

np.concatenate([arr1_1, arr2_1, arr3_1], axis=None)

arr2_3 = np.random.randint(1, 10, (2, 5))

arr2_3

arr2_1.shape

arr2_2.shape

arr2_3.shape

np.concatenate([arr2_1, arr2_2])

np.concatenate([arr2_1, arr2_3], axis=1)

