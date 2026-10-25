import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

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
    [90, 45, 30],
    [100, 45, 25],
    [110, 50, 20]
])


y = np.array([
    "STOP", "STOP", "STOP", "STOP",
    "SLOW", "SLOW", "SLOW", "SLOW",
    "FAST", "FAST", "FAST", "FAST",
    "FAST", "FAST", "FAST"
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

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)

print("=== MODEL EVALUATION ===")
print("Actual decisions:   ", y_test)
print("Predicted decisions:", y_pred)
print("Accuracy:", round(accuracy_score(y_test, y_pred) * 100, 2), "%")

print("\nConfusion matrix (STOP, SLOW, FAST):")
print(confusion_matrix(
    y_test, y_pred, labels=["STOP", "SLOW", "FAST"]
))
print("\nClassification report:")
print(classification_report(
    y_test, y_pred,
    labels=["STOP", "SLOW", "FAST"],
    zero_division=0
))
new_robot = np.array([[32, 12, 68]])
new_robot_scaled = scaler.transform(new_robot)
decision = model.predict(new_robot_scaled)[0]

print("\n=== NEW ROBOT PREDICTION ===")
print("Distance: 32 cm")
print("Speed: 12")
print("Battery: 68%")
print("Predicted decision:", decision)
