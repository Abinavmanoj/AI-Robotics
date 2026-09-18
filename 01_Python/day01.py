obstacle_distance = int(input("Enter the obstacle_distance: "))
if obstacle_distance < 30:
    print(" stop.")
elif 30 <= obstacle_distance <= 70:
    print("slow.")
else: 
    print("move.")