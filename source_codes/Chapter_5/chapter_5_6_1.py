import numpy as np

students = np.array([r"小明", r"小虹", r"刘梅", r"陈露"])

scores = np.array([[93, 88, 67],
                   [94, 67, 53],
                   [58, 43, 85],
                   [43, 64, 97]])

st_dtype = np.dtype([('Name', 'U10'), ('Math', 'i4'), ('English', 'i4'), ('Chemistry', 'i4')])

st_scores = np.empty(4, dtype = st_dtype)

st_scores['Name'] = students

st_scores['Math'] = scores[:, 0]

st_scores['English'] = scores[:, 1]

st_scores['Chemistry'] = scores[:, 2]

print(st_scores)

np.dtype([('Name', 'U10'), ('Math', 'i4'), ('English', 'i4'), ('Chemistry', 'i4')])

["Name", "Math", "English", "Chemistry"],

np.dtype("U10, i4, i4, i4")

