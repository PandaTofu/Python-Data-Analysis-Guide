from sklearn import preprocessing

import numpy as np

data = np.random.RandomState(616).lognormal(size=(4, 4))

transformer = preprocessing.PowerTransformer(method='box-cox', standardize=False)

data

transformer.fit_transform(data)

