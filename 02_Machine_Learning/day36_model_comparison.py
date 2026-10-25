import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
X = np.array([
    [10],
    [15],
    [20],
    [25],
    [30],
    [35],
    [40],
    [45],
    [50],
    [60],
    [70],
    [80],
    [90]
])

y = np.array([ 
    "STOP",
    "STOP",
    "STOP",
    "STOP",
    "SLOW",
    "SLOW",
    "SLOW",
    "SLOW",
    "FAST",
    "FAST",
    "FAST",
    "FAST",
    "FAST"
])
x_train, x_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42,
    stratify=y 
)
knn_model = KNeighborsClassifier(n_neighbors=3)
knn_model.fit(x_train, y_train)
knn_pred = knn_model.predict(x_test)
knn_accuracy = accuracy_score(y_test, knn_pred)
knn_cm = confusion_matrix(
    y_test,
    knn_pred,
    labels=["STOP","SLOW","FAST"]
)
tree_model = DecisionTreeClassifier(
    max_depth=3,   
    random_state=42
)
tree_model.fit(x_train, y_train)
tree_pred = tree_model.predict(x_test)
tree_accuracy = accuracy_score(y_test, tree_pred)
tree_cm = confusion_matrix(
    y_test,
    tree_pred,
    labels=["STOP","SLOW","FAST"]
)
print("testing distace:", x_test.flatten())
print("actual decisions:", y_test)

print("\nknn predictions:", knn_pred)
print("knn accuracy:", knn_accuracy*100, "%")
print("knn confusion matrix:")
print(knn_cm)

print("\nDecision Tree predictions:", tree_pred)
print("Decision Tree accuracy:", tree_accuracy * 100, "%")
print("Decision Tree confusion matrix:")
print(tree_cm)