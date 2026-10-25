def check_distance(distance):
    if distance < 30:
        return "stop"
    elif distance < 70:
        return "Slow"
    else:
        return "fast"