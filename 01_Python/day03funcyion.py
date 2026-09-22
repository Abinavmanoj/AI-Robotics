def check_obstacle(distance):
    print("obstacle distance =", distance)

    if distance < 30:
        print(" stop.")

    elif 30 <= distance <= 70:
        print(" move slowly.")

    else:
        print(" move fast.")

check_obstacle(20)
check_obstacle(50)
check_obstacle(100)