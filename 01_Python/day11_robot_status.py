robot_status = "robot battery low"
if "battery" in robot_status:
    print("WARNING: Battery Low")
if "low" in robot_status:
    print("Battery information detected.")
    print(robot_status.lower())
