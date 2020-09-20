from sklearn import datasets

dataset = datasets.load_iris()

x = dataset.data

y = dataset.target

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y)

from sklearn.svm import SVC

clf = SVC(kernel='linear')

clf.fit(x_train, y_train)

y_predict = clf.predict(x_test)

y_predict

error = y_test - y_predict

(error != 0).sum()

y_test.shape

1 - 1.0/38

