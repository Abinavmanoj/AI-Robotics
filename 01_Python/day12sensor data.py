file = open("sensor_data.txt", "r")
data = file.read()
print("Sensor reading:", data)
file.close()