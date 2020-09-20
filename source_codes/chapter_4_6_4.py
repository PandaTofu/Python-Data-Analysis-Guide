import numpy as np

mat = np.random.randn(3, 3)

mat

np.linalg.matrix_rank(mat)

mat[0] = 0

mat

np.linalg.matrix_rank(mat)

mat = np.random.randint(1, 10, (3, 3))

mat

np.linalg.norm(mat)

np.linalg.norm(mat, ord=1)

np.linalg.norm(mat, ord=2)

np.linalg.norm(mat, ord=np.inf)

np.linalg.cond(mat)

np.linalg.cond(mat, p=1)

np.linalg.cond(mat, p=2)

np.linalg.cond(mat, p=np.inf)

mat_I = np.linalg.inv(mat)

np.linalg.norm(mat, ord=1) * np.linalg.norm(mat_I, ord=1)

np.linalg.cond(mat, p=1)

mat = np.arange(4).reshape(2, 2)

mat

np.linalg.det(mat)

np.linalg.det(mat.T)

mat = np.random.randint(1, 10, (3, 3))

mat

np.diag(mat)

np.diag(mat).sum()

np.trace(mat)

mat = np.random.randint(1, 10, (5, 5))

mat

np.linalg.eigvals(mat)

np.linalg.eig(mat)

a, b = np.linalg.eig(mat)

a

b

