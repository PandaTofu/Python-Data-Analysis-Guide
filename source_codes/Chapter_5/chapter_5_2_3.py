def my_func(x):
    return (x ** 2 + 1)

import numpy as np

my_ufunc = np.frompyfunc(my_func, 1, 1)

type(my_ufunc)

my_ufunc.nin

my_ufunc.nout

x = np.arange(9)

x

my_ufunc(x)

x = np.random.randn(1000)

%timeit my_ufunc(x)

%%timeit
for value in x:
    my_func(x)

def my_binary_func(x, y):
    return (x + y) / 2.0

my_binary_ufunc = np.frompyfunc(my_binary_func, 2, 1)

type(my_binary_ufunc)

my_binary_ufunc.nin

x = np.arange(9)

x

my_binary_ufunc(x, 2)

