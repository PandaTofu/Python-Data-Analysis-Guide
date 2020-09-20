from sklearn import datasets

dataset = datasets.load_iris()

x = dataset.data

y = dataset.target

x.shape

from sklearn.decomposition import PCA

pca = PCA(n_components=2)

pca.fit(x)

x_proj = pca.transform(x)

import matplotlib.pyplot as plt

set(y)

'*'}

for k, marker in label_marker.items():
    x_k = x_proj[y == k]
    plt.scatter(x_k[:, 0], x_k[:, 1], marker=marker, color='k')

plt.show()

