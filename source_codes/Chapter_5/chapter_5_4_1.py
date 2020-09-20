import numpy as np

students = np.array([r"小明", r"小虹", r"刘梅", r"陈露"])

scores = np.random.randint(40, 100, (4, 3))

scores

students == r"小明"

scores[students == r"小明"]

scores[scores < 60]

scores[(scores >= 60) & (scores < 90)]

