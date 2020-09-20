from sklearn import preprocessing

import numpy as np

data = np.random.randint(1, 10, (4, 4))

data

data_scaled = preprocessing.scale(data)

data_scaled

data_scaled.mean(axis=0).round(2)

data_scaled.std(axis=0).round(2)

x_data = np.random.randint(1, 10, (8, 4))

x_train, x_test = x_data[0:4, :], x_data[4:8, :]

scaler = preprocessing.StandardScaler()

scaler.fit(x_train)

scaler.mean_

scaler.var_

x_train_scaled = scaler.transform(x_train)

x_train_scaled.mean(axis=0)

x_train_scaled.std(axis=0)

scaler.transform(x_test)

