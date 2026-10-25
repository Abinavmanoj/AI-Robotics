sensor_readings = [20, 45, 80, 15, 60, 100]
with open("sensor_log.txt", "w") as file:
    for reading in sensor_readings:
        file.write(str(reading) + "\n")
        print("Sensor reading logged:", reading)

