sensor_readings = [15, 45, 80, 25, 60, 100, 20]
def analyze_sensors(readings):
    danger_count = 0
    slow_count = 0
    safe_count = 0

    for distance in readings:
        if distance < 30:
            danger_count += 1
        elif distance < 70:
            slow_count += 1
        else:
            safe_count += 1

    return danger_count, slow_count, safe_count
stop, slow, fast = analyze_sensors(sensor_readings)
print("Danger readings:", stop)
print("Slow readings:", slow)
print("Safe readings:", fast)