obstacle_distance = int(input("Enter obstacle distance =:"))
battery = int(input("Enter battery percentage = :"))

if obstacle_distance < 30:
    print("stop:")
elif battery  < 20:
    print("RETURN TO CHARGER:")
elif 30 <= obstacle_distance <= 70:
    print("move slow:")
elif battery >= 20 and obstacle_distance > 70:
    print("move fast:")



