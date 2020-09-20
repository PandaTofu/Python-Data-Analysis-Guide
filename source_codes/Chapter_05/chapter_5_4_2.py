import numpy as np

x1 = np.arange(16)

x1

[x1[2], x1[5], x1[8], x1[9]]

f_index = [2, 5, 8, 9]

x1[f_index]

x1[[0, 3, -1, -3]]

x2 = x1.reshape(4, 4)

x2

row_ind = np.array([0, 1, 3])

col_ind = np.array([3, 0, 2])

x2[row_ind, col_ind]

x2[row_ind][:, col_ind]

new_row_ind = row_ind.reshape(3, 1)

x2[new_row_ind, col_ind]

