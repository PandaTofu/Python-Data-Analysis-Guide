import numpy as np

mat = np.random.randint(1, 10, (3, 3))

mat

q, r = np.linalg.qr(mat)

q

r

np.set_printoptions(suppress=True)

np.dot(q, q.T)

np.dot(q, r)

mat

U,sigma,VT = np.linalg.svd(mat)

U

sigma

V = VT.T

V

np.dot(U, U.T)

np.dot(V, VT)

sigma_m = np.diag(sigma)

sigma_m

np.linalg.multi_dot((U, sigma_m, VT))

mat

