import numpy as np

student_data = np.array([
    [202001, 172, 89],
    [202002, 165, 93],
    [202003, 180, 75]])

np.sort(student_data, axis=0)

scores = np.array(student_data[:, 2])

sorted_index = scores.argsort()

sorted_index

student_data[sorted_index, :]

scores = student_data[:, 1]

height = student_data[:, 2]

sorted_index = np.lexsort((height, scores))

student_data[sorted_index, :]

