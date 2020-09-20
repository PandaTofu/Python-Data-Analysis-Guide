from sklearn import datasets

dataset = datasets.load_iris()

x = dataset.data

y = dataset.target

from sklearn.decomposition import PCA

pca = PCA(n_components=2).fit(x)

x_proj = pca.transform(x)

import matplotlib.pyplot as plt

set(y)

'*'}

for k, marker in label_marker.items():
    x_k = x_proj[y == k]
    plt.scatter(x_k[:, 0], x_k[:, 1], marker=marker)

plt.show()

plt.cla()

gmm = GaussianMixture(n_components=3, covariance_type='spherical')

gmm.fit(x_proj)

y_pred = gmm.predict(x_proj)

for k, marker in label_marker.items():
    x_k = x_proj[y_pred == k]
    plt.scatter(x_k[:, 0], x_k[:, 1], marker=marker)

plt.show()

plt.cla()

gmm = GaussianMixture(n_components=3, covariance_type='full')

gmm.fit(x_proj)

y_pred = gmm.predict(x_proj)

for k, marker in label_marker.items():
    x_k = x_proj[y_pred == k]
    plt.scatter(x_k[:, 0], x_k[:, 1], marker=marker)

plt.show()

plt.cla()
