import numpy as np

mat = np.matrix(6)

mat

mat.shape

mat = np.matrix((0, 1, 3))

mat

mat.shape

mat = np.matrix([[0, 1], [2, 3]])

mat

mat.shape

arr = np.arange(6).reshape(2, 3)

arr

mat = np.matrix(arr)

mat

mat.shape

mat = np.matrix(np.zeros(3))

mat

mat.shape

mat = np.matrix(np.eye(5))

mat

mat.shape

mat = np.matrix(np.empty((3, 2)))

mat

mat.shape

mat = np.matrix(np.arange(6))

mat

mat.shape

mat = np.matrix(np.random.randn(3, 4))

mat

mat.shape

arr = np.random.randint(1, 10, (3, 3))

mat = np.matrix(arr)

arr

mat

mat * mat

arr * arr

arr = np.arange(6).reshape(3, 2)

mat = np.matrix(arr)

mat

mat.I

arr = np.array([[1, 2+3j], [4+5j, 6]])

mat = np.matrix(arr)

mat

mat.H

arr = np.arange(4).reshape(2, 2)

mat = np.matrix(arr)

mat

mat.A

mat.A.dtype

np.array(mat, dtype=np.float64)

np.asarray(mat, dtype=np.float32)

%timeit arr.T

%timeit mat.T

