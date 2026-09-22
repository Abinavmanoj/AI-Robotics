def check_obstacle(distance):
   if distance < 30:
    return"stop"
   elif 30 <= distance <= 70:
    return"move slow"
   else:
    return"move fast"

decision = check_obstacle(40)
print(decision)