robot_status = "robot obstacle detected battery low"
if "obstacle" in robot_status:
    print("Obstacle Detected")
if "battery" in robot_status:
    print("Battery information detected.")
if "low" in robot_status:
    print("WARNING: Battery Low")
    print(robot_status.upper())

