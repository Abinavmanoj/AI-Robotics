import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

x = np.array([
    [10],
    [15],
    [20],
    [30],
    [40],
    [50],
    [70],
    [90]
])
y = np.array([
    "STOP",
    "STOP",
    "STOP",
    "SLOW",
    "SLOW",
    "FAST",
    "FAST",
    "FAST"
])

x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)
print("Testing distance:", x_test.flatten())
print("Actual descisions:", y_test)
print("Predicted decisions:", y_pred)
print("Model Accuracy:", accuracy*100, "%")