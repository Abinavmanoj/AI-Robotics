while True:
    obstacle_distance = int(input("Enter the obstacle distance: "))
    battery = int(input("Enter the battery percentage: "))
    if obstacle_distance < 30:
        print(" stop.")
        break
    elif battery < 20:
        print("Recharge battery.")
    elif 30 <= obstacle_distance <= 70:
        print("slow.")
    else:
        print("move:")
