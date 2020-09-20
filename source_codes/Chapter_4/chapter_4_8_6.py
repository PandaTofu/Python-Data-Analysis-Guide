import numpy as np

x = np.random.randn(12)

x

x.shape

np.sum(x)

x.resize(3, 4)

x

x.shape

np.sum(x)

np.sum(x, axis=0)

np.sum(x, axis=1)

np.mean(x, axis=0)

np.std(x, axis=0)

np.median(x, axis=1)

np.argmin(x, axis=0)

np.argmax(x, axis=0)

np.diag(x[np.argmin(x, axis=0)])

np.min(x, axis=0)

np.diag(x[np.argmax(x, axis=0)])

np.max(x, axis=0)

x = np.random.randn(3, 4, 5)

np.percentile(x, 25, axis=2)

np.percentile(x, 25, axis=(1, 2))

np.percentile(x, 25, axis=(0, 1, 2))

np.percentile(x, 25)

