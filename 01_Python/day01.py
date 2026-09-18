Robot_name ="robo1"
battery = 80 
speed = 20
obstacle_distance = 20

print(Robot_name)
print(str(battery) + "%")
print(str(speed) + "cm/s")
print(str(obstacle_distance) + " cm")

if obstacle_distance >= 100:
    print("no move.")
else:
    print("yes stop.")