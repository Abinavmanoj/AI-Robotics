import numpy as np
from sklearn.neighbors import KNeighborsClassifier
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
model = KNeighborsClassifier(n_neighbors=3)
model.fit(x, y)
prediction = model.predict([[35]])
print("Prediction for distance 35:", prediction[0])