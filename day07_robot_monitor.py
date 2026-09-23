sensor_readings = [15, 45, 80, 25, 60, 100, 20]
danger_count = 0
slow_count = 0
safe_count = 0

for reading in sensor_readings:
    if reading < 30:
        danger_count += 1
    elif reading < 70:
        slow_count += 1
    else:
        safe_count += 1

print("Danger readings:", danger_count)
print("Slow readings:", slow_count)
print("Safe readings:", safe_count)