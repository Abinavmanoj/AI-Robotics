robot = {
    "name": "Robo1",
    "battery": 80,
    "speed": 20,
    "obstacle_distance": 100,
    "status": "moving"
}
if robot["obstacle_distance"] < 30:
    print("STOP")

elif robot["battery"] < 20:
    print("RETURN TO CHARGER")

elif robot["obstacle_distance"] <= 70:
    print("MOVE SLOW")

else:
    print("MOVE FAST")

