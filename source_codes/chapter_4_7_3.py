import numpy as np

x = np.array([1, 2, 3])

print("x     = ", x)
print("2 ** x = ", 2 ** x)
print("3 ** x = ", 3 ** x)
print("e ** x = ", np.e ** x)

print("x     = ", x)
print("2 ** x = ", np.power(2, x))
print("3 ** x = ", np.power(3, x))
print("e ** x = ", np.power(np.e, x))

print("x     = ", x)
print("2 ** x = ", np.exp(x))
print("e ** x = ", np.exp2(x))

x

np.log(x)

np.log2(x)

np.log10(x)

np.log(x) / np.log(10)

np.log10(x)

