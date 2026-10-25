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
model.fit(x,y)
test_distance = np.array([ 
    [12],
    [25],
    [35],
    [45],
    [60],
    [85]
])
prediction = model.predict(test_distance)
for distance, prediction in zip(test_distance, prediction):
    print("distance", distance[0], "cm", prediction)