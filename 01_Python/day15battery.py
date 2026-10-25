def robot_decision(distance, battery):
    if distance < 20:
        return "stop"
    elif battery < 20:
        return "Battery is low"
    elif distance < 50:
        return "Slow"
    else:
        return "move fast"