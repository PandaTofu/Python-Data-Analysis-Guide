from sklearn import datasets

from sklearn.model_selection import train_test_split

dataset = datasets.load_boston()

x = dataset.data

y = dataset.target

x_train, x_test, y_train, y_test = train_test_split(x, y)

from sklearn.neighbors import KNeighborsRegressor

KNN_reg = KNeighborsRegressor(n_neighbors=6, weights='uniform')

KNN_reg.fit(x_train, y_train)

y_predict_knn = KNN_reg.predict(x_test)

y_predict_knn[0:10]

from sklearn.neighbors import RadiusNeighborsRegressor

RNN_reg = RadiusNeighborsRegressor(radius=x_train.std())

RNN_reg.fit(x_train, y_train)

y_predict_rnn = RNN_reg.predict(x_test)

y_predict_rnn[0:10]

RNN_reg = RadiusNeighborsRegressor()

RNN_reg.fit(x_train, y_train)

RNN_reg.predict(x_test)

from sklearn.metrics import mean_absolute_error, mean_squared_error

mean_absolute_error(y_test, y_predict_knn)

mean_squared_error(y_test, y_predict_knn)

mean_absolute_error(y_test, y_predict_rnn)

mean_squared_error(y_test, y_predict_rnn)

