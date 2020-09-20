import numpy as np

np.random.seed(6)

np.random.seed(178)

np.random.random(5)

np.random.random(3)

np.random.seed(178)

np.random.random(5)

np.random.random(3)

np.random.random()

np.random.random(3)

np.random.random(size=3)

np.random.rand(3, 2)

np.random.rand(3, 2, 2)

np.random.uniform()

np.random.uniform(-0.9)

np.random.uniform(3)

np.random.uniform(2, 3)

np.random.uniform(3, 2)

np.random.uniform(low=2, high=3)

np.random.uniform(2, 3, 4)

np.random.uniform(2, 3, (4, 3))

np.random.uniform(2, 3, size=(4, 3))

np.random.randint(3)

np.random.randint(2, 5)

try:
    np.random.randint(5, 2)
except Exception as e:
    print(repr(e))

np.random.randint(high=5, low=2)

np.random.randint(1, 10, 3)

np.random.randint(1, 10, size=(3, 3))

arr = np.random.randint(1, 10, 3)

arr.dtype

arr = np.random.randint(1, 10, 3, dtype=np.int16)

arr.dtype

np.random.randn()

np.random.randn(6)

np.random.randn(3, 4)

np.random.normal()

np.random.normal(0.5, 2)

np.random.normal(0.5, 2, 6)

np.random.normal(0.5, 2, size=(2, 3))

