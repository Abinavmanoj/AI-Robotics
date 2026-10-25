sensor_readings = [20, 45, 20, 80, 45, 100, 20]
robot = {
    "name": "Robo1",
    "battery": 75
}
print("Sensor readings:", sensor_readings)
unique_readings = set(sensor_readings)
print("Unique sensor readings:", unique_readings)
print("Number of unique readings:", len(unique_readings))
print("Robot name:", robot["name"])
print("Robot battery level:", robot["battery"])
robot["unique_readings"] = len(unique_readings)
print("Unique readings count:", robot["unique_readings"])