import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from  sklearn.preprocessing import StandardScaler
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

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("Original training data:")
print(X_train)

print("\nScaled training data:")
print(np.round(X_train_scaled, 2))

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)

print("\nTesting data:")
print(X_test)

print("\nActual decisions:")
print(y_test)

print("\nPredicted decisions:")
print(y_pred)

print("\nAccuracy:", accuracy * 100, "%")
