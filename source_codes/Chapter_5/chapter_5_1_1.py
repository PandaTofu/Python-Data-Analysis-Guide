import numpy as np

def get_loop_reciprocal(x):
    out = []
    for value in x:
        if value != 0:
            out.append(1.0 / value)
        else:
            out.append(value)
    return np.array(out)

big_arr = np.random.randn(1000000)

get_loop_reciprocal(big_arr)

%timeit get_loop_reciprocal(big_arr)

np.reciprocal(big_arr)

%timeit np.reciprocal(big_arr)

def get_reciprocal(x):
    if x != 0:
        return 1.0 / x
    else:
        return x

get_reciprocal(big_arr[0])

get_vec_reciprocal = np.vectorize(get_reciprocal)

get_vec_reciprocal(big_arr)

@np.vectorize
def get_vec_reciprocal(x):
    if x != 0:
        return 1.0 / x
    else:
        return x

get_vec_reciprocal(big_arr)

%%timeit
for value in big_arr:
    get_reciprocal(value)

%timeit get_vec_reciprocal(big_arr)

%timeit get_vec_reciprocal(big_arr)

%timeit np.reciprocal(big_arr)

