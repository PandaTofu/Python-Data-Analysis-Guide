import numpy as np

mat = np.random.randint(1, 10, (3, 4))

mat_m = np.matrix(mat)

mat

mat_m

np.dot(mat, mat.T)

np.dot(mat_m, mat_m.T)

mat_m * mat_m.T

mat.dot(mat.T)

np.linalg.multi_dot((mat, mat.T, mat))

np.linalg.matrix_power(mat, 3)

np.linalg.multi_dot((mat, mat, mat))

