import numpy as np

mat = np.random.randint(1, 10, (3, 3))

mat_m = np.matrix(mat)

mat

mat_m

np.linalg.inv(mat)

np.linalg.inv(mat_m)

mat_m.I

mat_I = np.linalg.inv(mat)

np.dot(mat, mat_I)

np.set_printoptions(suppress=True)

np.dot(mat, mat_I)

mat_pinv = np.linalg.pinv(mat)

mat_pinv

np.linalg.multi_dot((mat, mat_pinv, mat))

mat

np.linalg.multi_dot((mat_pinv, mat, mat_pinv))

mat_pinv

mat = np.random.randint(1, 10, (3, 3))

mat_m = np.matrix(mat)

mat

mat_m

mat_m.H

mat_m.T

np.conj(mat)

np.conj(mat_m)

mat.T

mat = np.array([[1, 2+3j], [4, 5+6j]])

mat_m = np.matrix(mat)

mat

mat_m

np.conj(mat)

np.conj(mat_m)

mat_m.H

