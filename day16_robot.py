from robot_controller import control_robot

battery = 10
distance = 100
decision = control_robot(distance, battery)
print("Robot decision:", decision)