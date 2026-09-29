sensor_readings = [15, 45, 80, 25, 60, 100, 20]
file = open("sensor_log.txt", "r")
data = file.readlines()
for reading in data:
        print("Sensor reading:", reading.strip())
file.close()