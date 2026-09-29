with open("sensor_data.txt", "r") as file:
    data = file.read()
    print("Sensor reading:", data)