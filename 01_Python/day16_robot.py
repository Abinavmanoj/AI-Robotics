from robot_controller import control_robot

battery = int(input("Enter battery level: "))
distance = int(input("Enter distance to obstacle: "))
decision = control_robot(distance, battery)
print("Robot decision:", decision)