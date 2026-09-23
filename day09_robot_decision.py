def robot_decision(distance, battery):

    if distance < 20:
        return "stop"

    elif battery < 20:
        return "return to recharge"

    elif distance < 70:
        return "move slow"

    else:
        return "move fast"


distance = [15, 50, 100]
battery = [10, 50, 80]

for d, b in zip(distance, battery):
    print("Robot decision:", robot_decision(d, b))