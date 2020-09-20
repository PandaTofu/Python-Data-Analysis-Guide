import numpy as np

arr1_1 = np.arange(5)

arr1_1

arr1_1.shape

arr_stack = np.stack([arr1_1, arr1_1, arr1_1])

arr_stack

arr_stack.shape

arr1_2 = np.random.randint(1, 10, 5)

arr1_3 = np.random.randint(1, 10, 5)

arr1_2

arr1_3

arr_stack = np.stack([arr1_1, arr1_2, arr1_3], axis=1)

arr_stack

arr_stack.shape

arr2_1 = np.random.randint(1, 10, (3, 4))

arr2_2 = np.random.randint(1, 10, (3, 4))

arr2_1

arr2_2

arr2_1.shape, arr2_2.shape

arr_stack = np.stack([arr2_1, arr2_2])

arr_stack

arr_stack.shape

arr_stack

arr_merged.shape

np.vstack([arr1_1, arr1_2])

arr1_1_rs = arr1_1.reshape(1, -1)

arr1_2_rs = arr1_2.reshape(1, -1)

arr1_1_rs

arr1_2_rs

np.vstack([arr1_1_rs, arr1_2_rs])

arr2_1

arr2_2

np.vstack([arr2_1, arr2_2])

np.concatenate([arr2_1, arr2_2], axis=0)

np.hstack([arr1_1, arr1_2])

np.hstack([arr2_1, arr2_2])

np.concatenate([arr2_1, arr2_2], axis=1)

arr_stack = np.dstack([arr1_1, arr1_2])

arr_stack

arr_stack.shape

arr2_1.shape

arr2_2.shape

arr_stack = np.dstack([arr2_1, arr2_2])

arr_stack

arr_stack.shape

arr3_1 = np.random.randint(1, 10, (2, 3, 4))

arr3_2 = np.random.randint(1, 10, (2, 3, 3))

arr3_1

arr3_2

arr_stack = np.dstack([arr3_1, arr3_2])

arr_stack

arr3_1.shape

arr3_2.shape

arr_stack.shape

