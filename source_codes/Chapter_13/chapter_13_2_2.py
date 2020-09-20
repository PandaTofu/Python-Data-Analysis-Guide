from sklearn import preprocessing

import numpy as np

data = np.random.randint(1, 10, (4, 4))

data

data_normalized = preprocessing.normalize(data, norm='l2')

data_normalized

normalizer = preprocessing.Normalizer(norm='l2')

normalizer.fit(data)

data2 = np.random.randint(1, 10, (1, 4))

normalizer.transform(data2)

