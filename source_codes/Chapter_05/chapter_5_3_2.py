x = 2; y = 3

z = x if x > y else y

z

import numpy as np

x = np.random.randint(1, 10, 10)

y = np.random.randint(1, 10, 10)

x

y

[(a if a > b else b) for a, b in zip(x, y)]

def get_max_element(x, y):
    return x if x > y else y

get_vec_max_element = np.frompyfunc(get_max_element, 2, 1)

get_vec_max_element(x, y)

cond = x > y

cond

np.where(cond, x, y)

np.where(x > y, x, y)

x = np.random.randint(1, 10, (3, 3))

y = np.random.randint(-5, 5, (3, 3))

x

y

np.where(y > 0, (x + y) / 2, (x - y) / 2)

x = np.arange(9).reshape(3, 3)

np.where(x == 0, 1, x * 2)

x = np.random.randint(-5, 5, (3, 3))

x

np.where(x < 0, 0, 1)

