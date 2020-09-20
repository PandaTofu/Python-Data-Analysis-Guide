import numpy as np

arr2 = np.random.randint(0, 10, size=(4, 3))

arr2

arr2.T

arr2.shape

arr2.T.shape

arr3 = np.random.randint(1, 10, (3, 4, 5))

arr3

arr3.T

arr3.shape

arr3.T.shape

arr4 = np.random.randint(1, 10, (3, 4, 5, 2))

arr4

arr4.T

arr4.shape

arr4.T.shape

arr2

arr2.swapaxes(0, 1)

arr2.swapaxes(1, 0)

arr3

arr3.shape

arr3.swapaxes(0, 1)

arr3.swapaxes(0, 1).shape

arr3.swapaxes(1, 2)

arr3.swapaxes(1, 2).shape

arr3.swapaxes(0, 2)

arr3.swapaxes(0, 2).shape

arr2.T

arr2.transpose()

arr3.T

arr3.transpose()

arr4.transpose((1, 0, 3, 2))

arr4.transpose((1, 0, 3, 2)).shape

arr4.shape

