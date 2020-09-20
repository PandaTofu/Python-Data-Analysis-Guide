import numpy as np

arr = np.random.randint(-5, 5, (3, 4))

arr

np.abs(arr)

arr + 1

type(np.abs)

type(np.add)

np.abs.nin

np.sin.nin

np.sqrt.nin

arr = np.array([-5, -3, 0, 9, 7])

np.sign(arr)

arr = np.array([5+2j, -4-3j, 2j, 0j])

np.sign(arr)

arr = np.array([-1.2, 3.3, 5.5, 2.7, -6.9])

np.rint(arr)

np.ceil(arr)

np.floor(arr)

y1, y2 = np.modf(arr)

y1

y2

arr = np.array([1.1, 2.3, np.nan, 4.0])

np.isnan(arr)

arr = np.array([1.1, 2.3, np.nan, 4.0, np.inf])

np.isinf(arr)

arr

np.isfinite(arr)

arr = np.array([True, False, False, True])

np.logical_not(arr)

(~arr)

np.add.nin

np.power.nin

x1 = np.array([1.0, 2.0, 3.0, 4.0])

x2 = np.array([-3.1, 2.8, 0, 6.0])

np.copysign(x1, x2)

x1 = np.array([1.0, 2.0, -3.0, 4.0])

np.copysign(x1, x2)

x1 = np.arange(5)

x2 = np.array([-1, 1, 3, 2, 9])

x1

x2

x1 > x2

np.greater(x1, x2)

x1 >= x2

np.greater_equal(x1, x2)

x1 < x2

np.less(x1, x2)

x1 <= x2

np.less_equal(x1, x2)

x1 == x2

np.equal(x1, x2)

x1 != x2

np.not_equal(x1, x2)

x1

x2

np.maximum(x1, x2)

np.minimum(x1, x2)

x1 = np.array([True, False, False, True, True])

x2 = np.array([True, True, False, False, True])

x1 & x2

np.logical_and(x1, x2)

x1 | x2

np.logical_or(x1, x2)

x1 ^ x2

np.logical_xor(x1, x2)

x = np.arange(6)

x

np.maximum(x, 3)

np.minimum(x, 3)

