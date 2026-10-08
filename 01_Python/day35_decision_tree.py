import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
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
model = DecisionTreeClassifier(
    max_depth=2,
    random_state=42
)
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)
print("Testing distance:", x_test.flatten())
print("Actual descisions:", y_test)
print("Predicted decisions:", y_pred)
print("Accuracy:", accuracy*100, "%")