def check_obstacle(readings):
        if readings < 20:
            return "stop"
        elif readings < 70:
            return "slow"
        else:
            return "fast"

readings = [20, 45, 80, 15, 60, 100]

for distance in readings:
    check_obstacle(distance)
    print(distance, check_obstacle(distance))
