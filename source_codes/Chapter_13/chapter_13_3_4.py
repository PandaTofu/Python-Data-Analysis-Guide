from sklearn import datasets

from sklearn.model_selection import train_test_split

dataset = datasets.load_iris()

x = dataset.data

y = dataset.target

x_train, x_test, y_train, y_test = train_test_split(x, y)

from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(max_depth=2, random_state=0)

clf.fit(x_train, y_train)

y_predict = clf.predict(x_test)

from sklearn.metrics import accuracy_score

accuracy_score(y_test, y_predict)

