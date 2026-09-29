sensor_reading = 45
file = open("sensor_data.txt", "w")
file.write(str(sensor_reading))
file.close()