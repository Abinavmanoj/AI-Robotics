from day17_validation  import get_distance, get_battery
from robot_controller import control_robot
battery = get_battery()
distance = get_distance()
decision = control_robot(distance, battery)
print("Robot decision:", decision)