#12.11
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from sklearn.ensemble import RandomForestClassifier

iris_dataset = load_iris()

N = 1000
knn_method = []
clf_method = []
rfc_method = []
debug = False

for _ in range(N):
    X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'])

    clf = DecisionTreeClassifier()              #DecisionTreeClassifier METHOD
    clf.fit(X_train, y_train)
    clf_value = clf.score(X_test, y_test)
    clf_method.append(clf_value)

    knn = KNeighborsClassifier(n_neighbors = 1) #KNeighborsClassifier METHOD
    knn.fit(X_train, y_train)
    knn_value = knn.score(X_test, y_test)
    knn_method.append(knn_value)

    rfc = RandomForestClassifier(max_depth=2, random_state=0)   #RandomForestClassifier METHOD
    rfc.fit(X_train, y_train)
    rfc_value = rfc.score(X_test, y_test)
    rfc_method.append(rfc_value)

    if debug == True:
        print("Test set score (clf): {:.2f}".format(clf_value))
        print("Test set score (knn): {:.2f}".format(knn_value))
        print("Test set score (rfc): {:.2f}".format(rfc_value))


print("Test set score (clf) promedy: {:.3f}".format(np.mean(clf_method)))
print("Test set score (knn) promedy: {:.3f}".format(np.mean(knn_method)))
print("Test set score (rfc) promedy: {:.3f}".format(np.mean(rfc_method)))
