from sklearn.datasets import make_blobs

from sklearn.model_selection import train_test_split

x, labels = make_blobs(n_samples=1000, n_features=2,
                       centers=[[0, 0], [1, 1], [1, 3]],
                       cluster_std=[0.4, 0.2, 0.2])

x_train, x_test = train_test_split(x)

from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=3)

kmeans.fit(x_train)

kmeans.cluster_centers_.round(2)

import matplotlib.pylab as plt

label_pred = kmeans.predict(x_test)

set(kmeans.labels_)

'*'}

for k, marker in label_marker.items():
    x_test_k = x_test[label_pred==k]
    plt.scatter(x_test_k[:, 0], x_test_k[:, 1], marker=marker, color='k')

plt.show()

