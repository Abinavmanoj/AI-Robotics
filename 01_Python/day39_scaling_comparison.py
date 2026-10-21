import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

X = np.array([
    [10, 20, 90],
    [15, 20, 85],
    [20, 15, 80],
    [25, 15, 75],
    [30, 10, 70],
    [35, 10, 65],
    [40, 10, 60],
    [45, 20, 55],
    [50, 25, 50],
    [60, 30, 45],
    [70, 35, 40],
    [80, 40, 35],
    [90, 45, 30]
])

y = np.array([
    "STOP", "STOP", "STOP", "STOP",
    "SLOW", "SLOW", "SLOW", "SLOW",
    "FAST", "FAST", "FAST", "FAST", "FAST"
])

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42,
    stratify=y
)

knn_original = KNeighborsClassifier(n_neighbors=3)
knn_original.fit(X_train, y_train)
pred_original = knn_original.predict(X_test)

accuracy_original = accuracy_score(y_test, pred_original)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

knn_scaled = KNeighborsClassifier(n_neighbors=3)
knn_scaled.fit(X_train_scaled, y_train)
pred_scaled = knn_scaled.predict(X_test_scaled)

accuracy_scaled = accuracy_score(y_test, pred_scaled)

print("Actual decisions:", y_test)

print("\nWithout scaling:")
print("Predictions:", pred_original)
print("Accuracy:", accuracy_original * 100, "%")

print("\nWith scaling:")
print("Predictions:", pred_scaled)
print("Accuracy:", accuracy_scaled * 100, "%")