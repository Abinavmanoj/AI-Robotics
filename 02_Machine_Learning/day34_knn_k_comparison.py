import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
x = np.array([
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
    x,
    y,
    test_size=0.3,
    random_state=42,
    stratify=y
)
for k in [1,3,5]:
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    y_test,
    y_pred,
    labels = ["STOP", "SLOW", "FAST"]
    print("k =", k)
    print("predictions:", y_pred)
    print("Actual:", y_test)
    print(" Accuracy:", accuracy*100, "%")
    print("Confusion Matrix:")
    print(cm)
    print("-----------------------------")

